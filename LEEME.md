# onda — Tu playlist renovada

Un reproductor estático para GitHub Pages, con degradados, buscador, favoritos, reproducción aleatoria, repetición, control de volumen y diseño adaptable a móviles. No necesita PHP, una base de datos, fuentes externas ni librerías descargadas desde internet.

## Subir a tu repositorio desde Windows

El paquete incluye **SUBIR_A_GITHUB.bat**, configurado para **https://github.com/YottoMtnz/ondaplayer**.

1. Descomprimí todo el ZIP en una carpeta.
2. Poné tus canciones en esa carpeta, junto a `index.html` y al BAT.
3. Hacé doble clic en `SUBIR_A_GITHUB.bat`. Requiere Git para Windows; si falta, te muestra dónde instalarlo.
4. Si Git solicita acceso, iniciá sesión en la ventana oficial de GitHub.
5. Cuando diga **SUBIDA COMPLETADA**, activá GitHub Actions como origen de Pages según las instrucciones de abajo.

La carpeta `.github` y el generador se suben conservando sus rutas. El BAT respeta la rama predeterminada existente; si el repositorio está vacío, inicia `main`. Conserva los archivos que ya existen en el repositorio y no estaban en tu carpeta local. Para quitar una canción publicada, borrala en GitHub.

Solo sube los archivos del reproductor enumerados en el BAT y los audios sueltos. Los errores se muestran y la ventana permanece abierta. La identidad de Git que ya tengas configurada se conserva; si falta, usa `YottoMtnz` y su dirección de commits `noreply` únicamente en la copia temporal.

## Si solo querés cambiar la apariencia

1. Reemplazá tu `index.html` por el nuevo `index.html`.
2. Dejá los audios en la misma carpeta, con sus nombres exactos.
3. Si no hay un `playlist.json`, la página utiliza las **52 canciones originales** que ya estaban en tu archivo. Si usás el JSON incluido, contiene esa misma lista.

El archivo adjunto se llamaba `index(4).html`; en GitHub el archivo de inicio debe llamarse **index.html**. No se adjuntan las canciones: solo recibí tu HTML.

## Lista automática al agregar o quitar canciones — recomendado

GitHub Pages es estático: el navegador no puede recorrer la carpeta del servidor ni escribir un JSON en el repositorio. El paquete resuelve eso con **GitHub Actions**, que prepara la lista antes de publicar.

1. Descomprimí el ZIP. Copiá su contenido a la raíz de tu repositorio, donde están `index.html` y las canciones.
2. Incluí `tools/generate_playlist.py` y **`.github/workflows/onda-pages.yml`**, conservando esas rutas. Si subís archivos con la web de GitHub y no aparece la carpeta `.github`, usá **Add file → Create new file**, escribí esa ruta completa y pegá el contenido del archivo del ZIP.
3. En tu repositorio abrí **Settings → Pages → Build and deployment → Source** y elegí **GitHub Actions**.
4. En **Actions**, abrí **Publicar onda y actualizar canciones** y ejecutá **Run workflow** sobre la rama predeterminada. También se ejecuta al guardar cambios en esa rama.
5. Esperá a que el proceso termine en verde y abrí tu URL habitual de GitHub Pages.

A partir de ahí, subí, renombrá o eliminá canciones **junto a index.html**. Al guardar los cambios, se detectan los archivos actuales, se genera `playlist.json` y se publica la nueva colección. No necesitás editar nombres dentro del código ni añadir un token.

**Dónde se guarda el JSON:** se genera dentro de la versión publicada, accesible en `playlist.json` junto a la página. La acción no crea un commit ni modifica el JSON del repositorio. Esto evita pedir permisos de escritura al código; la página sí recibe la lista actualizada. Podés descargar el JSON publicado desde el menú de tres puntos.

**Si tu página está dentro de `docs/`:** colocá allí `index.html`, `playlist.json`, `tools/` y los audios; conservá `.github/workflows/onda-pages.yml` en la raíz del repositorio y cambiá `SITE_DIR: .` por `SITE_DIR: docs` en ese archivo.

**Si ya existe otra acción que publica esa misma página:** integrá el paso de generación en ella o reemplazá ese flujo por el incluido, para que dos acciones no publiquen versiones diferentes. El flujo incluido publica este reproductor, los audios de su carpeta, el JSON y, si existen, `CNAME` y `robots.txt`. Está preparado para esta página independiente.

## Qué detecta

- Audios sueltos: MP3, M4A, OGG, OGA, WAV, FLAC, AAC, OPUS y WEBM, con extensión en mayúsculas o minúsculas. Que un formato se reproduzca depende del navegador y del códec del archivo; MP3 es una opción ampliamente compatible.
- No explora subcarpetas, no indexa enlaces simbólicos ni incluye documentos, scripts o imágenes.
- Respeta el nombre real del archivo, incluidos espacios, tildes, `#`, `%` y otros símbolos. La página codifica correctamente las rutas.
- Separa artista y canción cuando el nombre usa `Artista - Canción`. Conserva las etiquetas originales cuando ya existen.
- Al eliminar todos los audios se publica una lista vacía: no reaparecen las canciones antiguas como si siguieran disponibles.
- Rechaza punteros de Git LFS que no contienen el audio real, mostrando el nombre que requiere atención en el registro de Actions.

## Uso del reproductor

- **Reproducir** inicia las canciones visibles; **Dejate sorprender** inicia esa selección en orden aleatorio.
- Tocá una canción para escucharla. Si ya está seleccionada y cargada, el botón alterna reproducir/pausar.
- Los corazones guardan favoritas en el navegador actual. No se comparten entre dispositivos.
- Repetición alterna: colección completa → una canción → desactivada. La colección se repite por defecto, como en tu reproductor original.
- Anterior vuelve al inicio si pasaron más de tres segundos; al tocarlo de nuevo pasa a la canción anterior.
- **Actualizar colección** vuelve a leer el JSON publicado. No sube archivos ni fuerza una publicación de GitHub.
- **Abrir música** o arrastrar audios permite reproducir archivos de tu dispositivo sin subirlos. Esa selección dura hasta recargar la página.
- El menú de tres puntos permite importar/exportar JSON. Exportar guarda nombres y etiquetas; **no incluye los audios ni escribe en GitHub**.
- Espacio reproduce/pausa; flechas izquierda/derecha retroceden/avanzan 5 segundos, cuando no estás escribiendo o usando un control.
- La música empieza solo después de tocar reproducir. Si un archivo falla, el reproductor lo señala e intenta seguir con otro de la cola. Si todos fallan, se detiene.

## Generación manual opcional

Con Python 3.9 o posterior instalado, desde la carpeta de la página:

```bash
python tools/generate_playlist.py
```

Esto genera `playlist.json` junto a `index.html`. Subí ambos y los audios mediante tu método habitual. Para una vista local con lectura del JSON, ejecutá `python -m http.server 8000` y abrí `http://localhost:8000`.

Si abrís el HTML con doble clic, el navegador puede impedir leer el JSON vecino. El diseño y la lista incorporada siguen funcionando; usá **Abrir música** o **Importar lista JSON** para elegir los archivos explícitamente.

## Fuentes técnicas

- [Qué es GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Publicar con un flujo de GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Archivos seleccionados desde el navegador — MDN](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications)

La automatización está preparada en los archivos; no se ha instalado ni ejecutado en tu repositorio porque no compartiste su dirección ni acceso a él.
