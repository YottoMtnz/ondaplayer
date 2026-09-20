# Comprobaciones de esta entrega

Fecha: 20 de septiembre de 2026.

## Completadas

- Sintaxis de JavaScript y Python sin errores.
- Estructura HTML: identificadores únicos, controles conectados a elementos existentes y referencias correctas de los iconos.
- Archivo YAML de GitHub Actions válido; trabajos de preparación/publicación conectados y permisos de publicación definidos. La rama predeterminada se detecta sin asumir que se llama main.
- Generador ejecutado con archivos de prueba: detectó seis audios con distintas extensiones, respetó metadatos originales y nombres con espacios, tildes, apóstrofos, #, %, & y signos < >.
- No se incluyeron imágenes, subcarpetas, audios ocultos ni enlaces simbólicos.
- El JSON y la lista incorporada en el HTML publicado coincidieron. Las etiquetas con símbolos HTML se escaparon correctamente.
- Al eliminar los audios, el generador produjo una colección vacía.
- Un archivo que solo contenía un puntero de Git LFS fue rechazado con un error descriptivo.
- Pruebas de lógica con DOM simulado: las 52 canciones originales, búsqueda, favoritas, siguiente/anterior, avance de reproducción, volumen, silencio, aleatorio, repetición y estados vacíos.
- Pruebas de JSON inválido, rutas externas o fuera de carpeta, fallo de carga y almacenamiento del navegador bloqueado: el reproductor conservó su lista de respaldo.
- Una respuesta tardía al cargar el JSON no reemplazó los archivos locales que el usuario acababa de seleccionar.
- Pruebas de cola: avance automático, repetir una canción, detenerse al terminar y detener los intentos cuando todos los audios fallan.

## Límites de la verificación

- El navegador de revisión bloqueó abrir archivos locales. No se realizó inspección visual ni prueba táctil real. El diseño incluye reglas adaptables para escritorio, tablet y móvil, pero esas vistas no se validaron en un navegador real durante esta entrega.
- Las pruebas de controles simularon el elemento de audio. No verifican la decodificación ni el sonido de canciones reales: no se proporcionaron archivos de audio.
- No se ejecutó el flujo en un repositorio de GitHub ni se publicó una página. Las instrucciones para activar el flujo están en LEEME.md.

Antes de dar por validada la publicación, abrí tu URL en computadora y teléfono, reproducí una canción real y probá agregar/quitar un audio para comprobar la actualización de la lista.

## BAT de subida agregado

Se confirmó mediante GitHub que `YottoMtnz/ondaplayer` existe, es público, tiene rama predeterminada `main` y está vacío al preparar este BAT. El BAT apunta a ese destino. Se revisó la sintaxis del bloque PowerShell y el empaquetado con saltos de línea CRLF. No se ejecutó en Windows ni se realizó una subida real con él.
