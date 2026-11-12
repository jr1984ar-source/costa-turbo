# RESUMEN PARA SEGUIR — Costa Turbo (12-nov-2026)

## Reglas de JRAR (obligatorias)
- Hablar en español casual, respuestas MUY breves, solo el resultado. 🔴 para avisos importantes.
- No programar ni crear archivos sin avisar y tener su OK (pero ha pedido "dame resultados, no preguntas": avanzar y enseñar resultados).
- Enlaces REALES siempre (URLs clicables), nada de rutas de menú inventadas. Comprobar antes de afirmar.
- Textos del juego: se quedan como están (JJ'S SPORTS LOUNGE, BAR JJ'S, TOP 10, STAGE, Slalom en inglés). El JJ siempre en la costa de la izquierda.
- Push solo a jr1984ar-source/costa-turbo (rama main), sin PRs. No tocar natura-viva-app.
- Commits sin nombre de modelo.

## Juego actual (2D, publicado)
- Jugar: https://jr1984ar-source.github.io/costa-turbo/
- Código: https://github.com/jr1984ar-source/costa-turbo — versión 113. Guía técnica completa: `dev/TRASPASO.md`.
- v112: mando Xbox/PlayStation (X turbo, A derrape, B/RT acelerar, LT freno, START pausa) y "ocultar controles". v113: pasar la partida a otro aparato (código CT1/CT0).

## Costa Turbo 3D (nuevo, separado del juego) — carpeta `3d/`
- Tecnología elegida: web 3D con Three.js 0.170 (mismo enlace en iPhone y PC con mando). Modelos en Blender (paquete Python `bpy` 5.3, Python 3.13: `pip install bpy pillow`).
- `3d/shots.html?shot=A|B|C|D`: escena de playa (A vista dron tipo reel, B vista de juego iPhone con botones, C moto de cerca, D 3 motos). Capturas en `3d/imagenes/`.
- `3d/src/world.js`: relieve de costa, arena con texturas reales (Poly Haven aerial_beach_01, damp_beach_sand_02, aerial_sand), agua con profundidad turquesa, cáusticas, espuma, reflejo del cielo HDRI (kloofendal_43d_clear_puresky; luz de entorno spiaggia_di_mondello). `fx.js`: estela y salpicaduras (también clases Wake/Spray en vivo). `props.js`: hierba, gaviotas, yates, boyas, sombrillas.
- `3d/blender/jetski_model.py`: moto + piloto procedurales (naranja COSTA TURBO, negra RIVA RACING, dorada SEA-DOO) -> `3d/models/jetski_*.glb`. `decimate.py` y `prep.py`: aligerar/orientar modelos descargados.
- Probar en local: `npm i three@0.170.0` + `python -m http.server 8765` y abrir http://localhost:8765/shots.html?shot=B

## Lo que JRAR quiere (prioridad)
1. Calidad máxima, tipo renders de estudio (post de Instagram "Wave Blaster" de classicjetskis: moto Yamaha WaveBlaster azul/amarilla, piloto con casco motocross, gafas, chaleco de 3 hebillas, neopreno, guantes).
2. 🔴 Motos IGUALES a sus fotos reales (en el juego 2D): Yamaha GP roja/blanca, negra/amarilla, negra/gris, blanca; Kawasaki Ultra 310 verde; Sea-Doo RXP-X gris/amarilla; Sea-Doo dorada.
3. 🔴 Palmeras realistas: Phoenix canariensis y Washingtonia. NADA de olivos en la costa. Las palmeras hechas por código le parecieron "extremadamente falsas": usar modelos reales.
4. Piloto realista (cuerpo escaneado con esqueleto + equipo).
5. Después: demo jugable en 3D (física, cámara suave, táctil + teclado + mando igual que el juego).

## Modelos ya elegidos en Sketchfab (gratis, licencia CC Attribution: citar autor)
Descargar con `python 3d/fetch_sf.py nombre=uid ...` (lee el token de `Escritorio\Api token.txt`):
- kawasaki_ultra310=37a2348f02da472d98310fd5621307c6 (XOIAL, 8k caras, la mejor)
- seadoo_gti=d7b3e903d7dc43a694720bd347f4fadf (Sea-Doo GTI SE 130 roja, enviada por JRAR)
- jetski_negra_turquesa=d011473f3ea64da28bdc194013480610 (enviada por JRAR)
- palmera_coco=26e787f2ff2e4c0fb004c3b0210805a3 (enviada por JRAR)
- palmera_datilera=11acf710e6c149daa8d6fb8cdc5d087f (enviada por JRAR)
- washingtonia_a=00bd2ea54eb1405bb056eac3f1e14673 (PlantCatalog Mexican fan palm 8/10)
- washingtonia_b=d63d13e51e1d4925b9eb6b984431762b (andre.arq.89, con falda de hojas secas)
- palmera_canaria=622ffb9dc2904166a1b6f58de6cee854 (PlantCatalog Canary Island date palm 31/40)
- casco_motocross=b8487c414e6641eda2bb4c952d3772f7
- chaleco=8481ac383f5348529d366c99cf86ab8e (azul con hebillas)
- piloto_eric=a46bc9f67aaa415bb4f3241eef900e7f (Renderpeople, escaneado y con esqueleto)
- piloto_b=959e9362c0174bc4a7f065f207524906
- No hay Yamaha GP1800 gratis buena: para Yamaha iguales habría que comprar modelo (CGTrader/TurboSquid) o modelarla.

## Siguiente paso concreto
1. Bajar los modelos (fetch_sf.py), pasarlos por `blender/prep.py` (orientar, escalar: motos ~3.3 m de largo, palmeras por altura; reducir a ~30-60k caras y texturas 1024-2048) -> GLB en `3d/models/`.
2. Meterlos en `shots.html` (cargador GLTF ya existe: `loadSki`), quitar olivos y palmeras procedurales, washingtonias en fila en el paseo, canarias y cocoteros en grupos.
3. Enseñar capturas A/B/C/D y seguir con piloto y demo jugable.
- 🔴 Problema pendiente: en la nube `bpy` fallaba al importar con "InitGoogleLogging() twice" al reiniciar escena; en `prep.py` importar en un proceso por modelo y sin `read_factory_settings`.

## Otros enlaces
- Muestras de música (sintetizador): https://claude.ai/artifact/WpS9UQ8usb2YdgnzLgkz5Z
- Sonido válvula "stu": https://claude.ai/artifact/BGYiZTharPv1dpYnpM1apk
- Juego como Artifact: https://claude.ai/artifact/H9QqYh3cs8zX2B6Fuku9nD
