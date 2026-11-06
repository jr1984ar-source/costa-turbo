# Costa Turbo · archivos de trabajo

Todo lo necesario para seguir trabajando en el juego. La web que se juega es `../index.html`; esta carpeta no la cambia.

**Para seguir desde otro ordenador, empieza por `TRASPASO.md`.**

- `costa-turbo.html` — el juego, versión original de la que sale todo.
- `rebuild.js` — genera `../index.html` y `costa-turbo-movil.html` desde `costa-turbo.html` (`node dev/rebuild.js`). Después hay que subir la versión de caché en `../sw.js`.
- `costa-turbo-movil.html` — el juego en un solo archivo, para descargar.
- `versiones/` — copia de cada versión publicada.
- `herramientas/` — scripts de cambios (`patch_*.py`), pruebas automáticas con Playwright (`t*.js`) y generadores de iconos y portadas.
- `iconos/` — icono grande (1024 px) y vista previa.
- `pruebas-sonido/` — páginas para escuchar la válvula de descarga y los escapes, y el script que genera los audios.
- `otros/` — Alerta Galáctica (el primer juego) y los bocetos de las motos.
