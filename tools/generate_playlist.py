#!/usr/bin/env python3
"""Build the playlist from actual audio files next to index.html (Python 3.9+)."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

AUDIO_EXTENSIONS = {'.mp3', '.m4a', '.ogg', '.oga', '.wav', '.flac', '.aac', '.opus', '.webm'}
EMBEDDED_PLAYLIST = re.compile(r'(<script\b[^>]*\bid="original-playlist"[^>]*>)(.*?)(</script>)', re.S)


def read_metadata(root: Path) -> dict:
    """Keep display names already supplied by the owner; never trust old paths."""
    known = {}
    html = (root / 'index.html').read_text(encoding='utf-8-sig')
    embedded = EMBEDDED_PLAYLIST.search(html)
    sources = []
    if embedded:
        try:
            sources.append(json.loads(embedded.group(2)))
        except (ValueError, TypeError):
            pass
    if (root / 'playlist.json').is_file():
        try:
            sources.append(json.loads((root / 'playlist.json').read_text(encoding='utf-8-sig')))
        except (ValueError, OSError):
            pass
    for data in sources:
        rows = data if isinstance(data, list) else data.get('tracks', []) if isinstance(data, dict) else []
        for row in rows:
            if isinstance(row, dict) and isinstance(row.get('file'), str):
                known[row['file']] = row
    return known


def display_info(filename: str, previous: dict) -> dict:
    name = previous.get('name')
    if not isinstance(name, str) or not name.strip():
        name = re.sub(r'^\d{1,3}(?:[._]\s*|\s+)', '', Path(filename).stem).replace('_', ' ').strip()
    before, separator, after = name.partition(' - ')
    artist = before.strip() if separator and before.strip() else 'Mi colección'
    title = after.strip() if separator and after.strip() else name
    for field, fallback in [('artist', artist), ('title', title)]:
        value = previous.get(field)
        if isinstance(value, str) and value.strip():
            if field == 'artist':
                artist = value.strip()
            else:
                title = value.strip()
    return {'file': filename, 'name': name, 'title': title, 'artist': artist}


def natural_key(text: str) -> list:
    return [(0, int(part)) if part.isdigit() else (1, part.casefold()) for part in re.split(r'(\d+)', text)]


def atomic_write(path: Path, text: str) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, prefix='.onda-', suffix='.tmp', delete=False) as out:
            temporary = Path(out.name)
            out.write(text)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def build(root: Path, output: Path | None = None) -> dict:
    root = root.resolve()
    if not (root / 'index.html').is_file():
        raise ValueError(f'No se encontró index.html en {root}')
    if output is not None:
        output = output.resolve()
        if output == root or root.is_relative_to(output):
            raise ValueError('La salida debe ser una carpeta diferente, no la raíz ni una carpeta superior.')
        if output.exists() and any(output.iterdir()):
            raise ValueError('La carpeta de salida debe estar vacía para no conservar audios eliminados.')
    known = read_metadata(root)
    files = sorted((file for file in root.iterdir()
                    if file.is_file() and not file.is_symlink()
                    and not file.name.startswith('.') and file.suffix.lower() in AUDIO_EXTENSIONS
                    and not re.search(r'[\\\x00-\x1f\x7f]', file.name)), key=lambda f: natural_key(f.name))
    for file in files:
        with file.open('rb') as audio:
            if audio.read(128).startswith(b'version https://git-lfs.github.com/spec/'):
                raise ValueError(f'{file.name}: es un puntero de Git LFS, no el audio. Se requieren los archivos reales.')
    tracks = [display_info(file.name, known.get(file.name, {})) for file in files]
    manifest = {'version': 1, 'generatedAt': datetime.now(timezone.utc).isoformat(), 'tracks': tracks}
    # A successful scan with no songs MUST clear stale tracks, never keep deleted ones.
    payload = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    destination = output or root
    destination.mkdir(parents=True, exist_ok=True)
    if output:
        # A dedicated site directory publishes only this player and its root-level audio.
        # The output is not removed, so no unrelated source files are deleted.
        html = (root / 'index.html').read_text(encoding='utf-8-sig')
        embedded_json = json.dumps(tracks, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
        html, count = EMBEDDED_PLAYLIST.subn(lambda m: m.group(1) + embedded_json + m.group(3), html, count=1)
        if count != 1:
            raise ValueError('No se encontró la lista de respaldo dentro del index.')
        atomic_write(destination / 'index.html', html)
        for file in files:
            shutil.copy2(file, destination / file.name)
        for extra in ['CNAME', 'robots.txt', 'onda-share.html']:
            source = root / extra
            if source.is_file() and not source.is_symlink():
                shutil.copy2(source, destination / extra)
        atomic_write(destination / '.nojekyll', '')
    atomic_write(destination / 'playlist.json', payload)
    print(f'Colección generada: {len(tracks)} canciones. JSON: {destination / "playlist.json"}')
    if not tracks:
        print('No hay audios junto al index: se ha creado una colección vacía.')
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description='Genera playlist.json con los audios junto a index.html.')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent, help='Carpeta que contiene index.html y los audios.')
    parser.add_argument('--output', type=Path, help='Carpeta dedicada para publicar. Si se omite, solo actualiza playlist.json.')
    args = parser.parse_args()
    try:
        build(args.root, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f'ERROR: {error}\n')


if __name__ == '__main__':
    main()
