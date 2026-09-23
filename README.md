<div align="center">

# 〰️ Onda Music

### Tu música, a tu manera.

Un reproductor web de música personal, ligero y moderno, pensado para escuchar tu colección desde cualquier navegador y publicarla fácilmente con GitHub Pages.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-222?logo=github)](https://yottomtnz.github.io/ondaplayer/)
![HTML5](https://img.shields.io/badge/HTML5-Audio-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=111)
![Responsive](https://img.shields.io/badge/UI-Responsive-C1ADFF)

**[▶ Abrir Onda Music](https://yottomtnz.github.io/ondaplayer/)**

</div>

---

## 🎧 ¿Qué es Onda?

**Onda Music** es un reproductor de audio web diseñado alrededor de una idea sencilla: tener una colección musical personal, bonita y cómoda de usar, sin depender de una interfaz pesada.

Funciona directamente en el navegador y combina una biblioteca musical con controles completos de reproducción, herramientas de organización, soporte para archivos locales y publicación automática con GitHub Pages.

---

## ✨ Funciones principales

- 🎵 Reproducción de audio directamente desde el navegador.
- 🔎 Búsqueda instantánea por canción o artista.
- ❤️ Favoritos guardados en el navegador.
- 🔀 Reproducción aleatoria.
- 🔁 Repetición de canción o de colección.
- ⏮️⏯️⏭️ Controles completos de reproducción.
- 🔊 Volumen, silencio y barra de progreso.
- 📚 Colección con ordenación y filtros.
- 🎶 Vista de **Reproduciendo ahora** y próxima canción.
- 🖱️ Arrastrar y soltar archivos de audio sobre la página.
- 📂 Abrir música directamente desde el dispositivo.
- 📥 Importar listas en formato JSON.
- 📤 Exportar la colección actual como `playlist.json`.
- ⌨️ Atajos de teclado para reproducción y búsqueda rápida.
- 📱 Diseño adaptable para escritorio, tablet y móvil.
- 🎛️ Integración con **Media Session API** cuando el navegador la soporta.
- 🧠 Recuperación ante audios no disponibles: Onda puede continuar con la siguiente canción.
- 💾 Persistencia local de favoritos, volumen, repetición, aleatorio y última canción.

---

## 🌐 Colección publicada automáticamente

El repositorio incluye un flujo de **GitHub Actions** que prepara y publica Onda en GitHub Pages.

Cada actualización de la rama principal puede:

1. revisar los archivos de audio reales;
2. generar una colección nueva;
3. crear `playlist.json`;
4. actualizar la lista integrada de respaldo;
5. publicar la página mediante GitHub Pages.

Así, la colección pública se construye a partir de los audios que realmente existen en el repositorio.

---

## 🎼 Formatos reconocidos por el generador

`MP3` · `M4A` · `OGG` · `OGA` · `WAV` · `FLAC` · `AAC` · `OPUS` · `WEBM`

> La reproducción final de cada formato también depende de las capacidades del navegador utilizado.

---

## 🗂️ Playlist JSON

Onda puede trabajar con una lista generada automáticamente o con una lista JSON importada.

Cada pista puede incluir información como:

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

El proyecto incluye una página dedicada a canciones compartidas.

Cuando alguien recibe un enlace compatible:

- Onda intenta abrir la canción en la aplicación Android;
- si la app no está instalada, la página ofrece una ruta de descarga;
- el título y el artista compartidos pueden mostrarse antes de abrir la aplicación.

Este flujo mantiene separada la experiencia web de la integración con la app móvil.

---

## 🛠️ Estructura principal

| Archivo / carpeta | Función |
|---|---|
| `index.html` | Reproductor web principal |
| `playlist.json` | Colección musical generada |
| `onda-share.html` | Página para enlaces compartidos |
| `tools/generate_playlist.py` | Generador de la colección |
| `.github/workflows/onda-pages.yml` | Publicación automática en GitHub Pages |

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

Los controles multimedia del sistema también pueden funcionar en navegadores compatibles con Media Session.

---

## 🔒 Privacidad

Onda funciona principalmente del lado del navegador.

Las preferencias de reproducción y favoritos se guardan localmente. Los archivos que abras manualmente desde tu dispositivo se utilizan durante la sesión del navegador y no se suben automáticamente al repositorio.

---

## 👤 Autor

**Fraudy Martinez Madruga**

Proyecto personal creado y mantenido como parte del ecosistema Onda.

---

<div align="center">

### 〰️ Onda Music

**Pon tu música. Dale play. Sigue la onda.**

**[▶ Abrir reproductor](https://yottomtnz.github.io/ondaplayer/)**

© 2026 Fraudy Martinez Madruga

</div>
