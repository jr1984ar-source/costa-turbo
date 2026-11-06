# Traspaso: seguir con Costa Turbo desde el PC

Guía para la sesión que continúa el trabajo hecho en la nube (hasta la **versión 113**, noviembre de 2026).

## Dónde está todo
- **Juego publicado:** https://jr1984ar-source.github.io/costa-turbo/ (GitHub Pages desde la rama `main`).
- **Fuente del juego:** `dev/costa-turbo.html`. Es un solo archivo; todos los cambios se hacen ahí.
- **Versiones publicadas:** `dev/versiones/costa-turbo.vNNN-publicado.html`.
- **Herramientas y pruebas:** `dev/herramientas/` (scripts `patch_vNNN.py` de cada versión, pruebas `t*.js`, generadores).
- **Mapa del lago (Modo libre):** `dev/herramientas/costa_real/`.

## Cómo se hace una versión nueva
1. Cambiar `dev/costa-turbo.html` y subir `const APP_VER=` en 1.
2. Pruebas, desde la carpeta `dev/` (necesita Node.js; la primera vez `npm i playwright` y `npx playwright install chromium`):
   - `node herramientas/mkwrap_test.js` crea `ct-wrapped2.html`, una copia con accesos para las pruebas.
   - `node herramientas/t107.js` juega las 23 pantallas (unos 10 min). Tiene que salir 23 veces `"err":null` y `errs []`.
   - Pruebas del Modo libre: `t200` gasolina y paradas · `t203` zonas y animales · `t204` retos · `t205` paseos · `t210` carrera de recta · `t212` mando · `t213` pasar partida.
   - Algunas pruebas usan `ct-wrapped.html`: se crea con `node herramientas/mkwrap.js`.
3. Publicar, desde la raíz del repositorio:
   - `node dev/rebuild.js` genera `index.html`, `sw.js` y `dev/costa-turbo-movil.html`.
   - Copiar `dev/costa-turbo.html` a `dev/versiones/costa-turbo.vNNN-publicado.html`.
   - Commit en español «Versión NNN: …» con la lista de cambios, y push a `main`. GitHub Pages lo publica en 1 o 2 minutos.

## Mapa del lago (Modo libre)
- `costa_real/gen_lake3.py` lee `realmap3.json` (la costa real) y `marina.py`, y crea `realmap5.json` y `lake_vis5.png` (vista de control). Se ejecuta desde esa carpeta con Python 3, numpy, opencv-python, pillow y scipy. Tarda unos 2 minutos.
- El resultado se mete en el juego cambiando la línea `const RMAP={...};const RCOR=...;const RSPOTS=...;const RZONE=...;` (ver `patch_v108.py`). Las rutas de los `patch_*.py` son de la nube: hay que adaptarlas.
- Valores del mapa (PNG gris, valor × 25): 0 agua, 1 roca, 2 arena, 3 jardín, 4 urbano, 7 bosque, 8 espigón, 9 pantalán, 10 amarres con barcos.

## Reglas de JRAR (importante)
- Hablar en español, breve y con el resultado primero; 🔴 delante de los avisos importantes.
- **No programar sin avisar y esperar su OK.** En los fallos: causa + propuesta.
- Los textos del juego se quedan como están; los que están en inglés siguen en inglés (JJ'S SPORTS LOUNGE, BAR JJ'S, TOP 10, STAGE, Slalom…).
- El BAR JJ va siempre en la costa de la izquierda.
- Probar antes de decir que algo funciona, y mandar capturas de cada cambio.
- Subir solo a `main` de este repositorio, sin pull requests.

## Hecho en las últimas versiones (100–113)
Lago cerrado del Modo libre con islas, calas, faro, islita y premios escondidos (casco dorado) · lado derecho con costa real girada · puerto de Portals con barcos · gasolina, gasolineras y paradas en bares y Piri-Piri · zonas profunda, tropical y pueblo con animales · retos de carrera y paseos de chicas (cambian de sitio en cada partida) · carrera de recta con turbo · pegatinas, dorsal y logo en la pintura · válvula STAGE 3 nueva y volúmenes · mando de Xbox/PlayStation y OCULTAR CONTROLES · pasar la partida a otro aparato.

## Ideas que se ofrecieron y no se han hecho
Día y noche en el lago · combos de trucos · repetición a cámara lenta de los saltos · locutor.
