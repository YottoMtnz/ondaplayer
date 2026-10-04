<h1 align="center">〰️ Onda Music</h1>
<p align="center"><em>Tu música, a tu manera.</em></p>
<p align="center"><em>Your music, your way.</em></p>

<p align="center">
  <a href="https://yottomtnz.github.io/ondaplayer/"><img src="https://img.shields.io/badge/GitHub%20Pages-online-7c3aed?style=flat-square&logo=github&logoColor=white" alt="Demo en vivo"></a>
  <img src="https://img.shields.io/badge/HTML5-Audio-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5 Audio">
  <img src="https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript vanilla">
  <img src="https://img.shields.io/badge/UI-Responsive-C1ADFF?style=flat-square" alt="Responsive">
  <img src="https://img.shields.io/badge/Privacidad-100%25%20local-8ff0c8?style=flat-square" alt="Privacidad: todo local">
</p>

---

## Sobre Onda Music

**Onda Music** es un reproductor web de música personal, ligero y moderno, creado por **Fraudy Martinez Madruga**. Escucha tu colección desde cualquier navegador y publícala fácilmente con GitHub Pages — sin cuentas, sin servidores, sin complicaciones.

**EN** — *Onda Music is a lightweight, modern personal web music player. Listen to your collection from any browser and publish it easily with GitHub Pages — no accounts, no servers, no fuss.*

---

## ✨ Características

<table>
<tr>
<td width="50%" valign="top">

### 🎵 Reproducción completa
Controles de reproducción, volumen, silencio y barra de progreso. Repetición de canción o de colección, y modo aleatorio.

</td>
<td width="50%" valign="top">

### 🔎 Búsqueda y organización
Búsqueda instantánea por canción o artista, ordenación, filtros y vista de **Reproduciendo ahora** con la próxima canción.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ❤️ Favoritos
Marca tus canciones favoritas. Se guardan en el navegador junto con tu volumen, repetición, aleatorio y última canción.

</td>
<td width="50%" valign="top">

### 🖱️ Arrastra y suelta
Suelta archivos de audio sobre la página o ábrelos desde tu dispositivo con el botón **Abrir música**.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🗂️ Playlists JSON
Importa listas en formato JSON y exporta tu colección actual como `playlist.json`.

</td>
<td width="50%" valign="top">

### ⌨️ Atajos de teclado
`Espacio` para reproducir/pausar, `←` `→` para saltar 5 segundos, y búsqueda rápida desde el teclado.

</td>
</tr>
</table>

> ### 🎛️ Media Session API
> Integración con los controles multimedia del sistema cuando el navegador la soporta: cambia de canción desde el teclado, los auriculares o la pantalla de bloqueo.
>
> ### 🧠 Recuperación inteligente
> Si un audio no está disponible, Onda continúa automáticamente con la siguiente canción en lugar de detenerse.

---

## 🌐 Publicación automática

El repositorio incluye un flujo de **GitHub Actions** que prepara y publica Onda en GitHub Pages.

Cada actualización de la rama principal puede:

1. revisar los archivos de audio reales;
2. generar una colección nueva;
3. crear `playlist.json`;
4. actualizar la lista integrada de respaldo;
5. publicar la página mediante GitHub Pages.

Así, la colección pública se construye a partir de los audios que realmente existen en el repositorio.

<p align="center">
  <a href="https://yottomtnz.github.io/ondaplayer/"><img src="https://img.shields.io/badge/Abrir-Onda%20Music-7c3aed?style=for-the-badge&logo=github&logoColor=white" alt="Abrir Onda Music"></a>
</p>

---

## 🎼 Formatos reconocidos

`MP3` · `M4A` · `OGG` · `OGA` · `WAV` · `FLAC` · `AAC` · `OPUS` · `WEBM`

> La reproducción final de cada formato también depende de las capacidades del navegador utilizado.

---

## 🗂️ Playlist JSON

Onda puede trabajar con una lista generada automáticamente o con una lista JSON importada. Cada pista puede incluir:

```json
{
  "file": "cancion.mp3",
  "title": "Nombre de la canción",
  "artist": "Artista"
}
```

Si no se proporcionan todos los datos, el generador intenta crear una presentación útil a partir del nombre del archivo.

---

## 📱 Enlaces compartidos y Android

El proyecto incluye `onda-share.html`, una página dedicada a canciones compartidas. Cuando alguien recibe un enlace compatible:

- Onda intenta abrir la canción en la aplicación Android;
- si la app no está instalada, la página ofrece una ruta de descarga;
- el título y el artista compartidos pueden mostrarse antes de abrir la aplicación.

---

## ⌨️ Controles útiles

| Acción | Control |
|---|---|
| Reproducir / pausar | `Espacio` |
| Retroceder 5 segundos | `←` |
| Avanzar 5 segundos | `→` |
| Abrir archivos | Botón **Abrir música** o arrastrar archivos |
| Buscar | Campo de búsqueda |
| Favoritos | Botón ❤️ de cada pista |

---

## 🔒 Privacidad

Onda funciona principalmente del lado del navegador. Las preferencias de reproducción y los favoritos se guardan localmente. Los archivos que abras manualmente desde tu dispositivo se usan durante la sesión y no se suben automáticamente al repositorio.

---

## 🛠️ Estructura del proyecto

| Archivo / carpeta | Función |
|---|---|
| `index.html` | Reproductor web principal |
| `playlist.json` | Colección musical generada |
| `onda-share.html` | Página para enlaces compartidos |
| `tools/generate_playlist.py` | Generador de la colección |
| `.github/workflows/onda-pages.yml` | Publicación automática en GitHub Pages |
| `VERIFICACION.md` | Registro de comprobaciones de la entrega |

---

## 👤 Autor

**Onda Music fue creado por Fraudy Martinez Madruga.**

Copyright © 2026 Fraudy Martinez Madruga. Proyecto personal creado y mantenido como parte del ecosistema Onda.

---

## 🔗 Enlaces

- 🌐 **Reproductor:** https://yottomtnz.github.io/ondaplayer/
- 💻 **Repositorio:** https://github.com/YottoMtnz/ondaplayer

---

<p align="center">
  <strong>〰️ Onda Music</strong><br>
  <em>Pon tu música. Dale play. Sigue la onda.</em>
</p>
