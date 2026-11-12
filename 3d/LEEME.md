# Costa Turbo 3D (en desarrollo, separado del juego)

- `shots.html`: escena 3D de la playa (Three.js). `imagenes/`: capturas.
- `src/`: mundo, agua, arena, efectos (estela, salpicaduras).
- `blender/`: scripts que modelan la moto y el piloto y aligeran modelos.
- `models/`: motos 3D (GLB) y modelos aligerados.
- `fetch_ph.py` / `fetch_sf.py`: descargan texturas (Poly Haven) y modelos (Sketchfab). Créditos en `assets/sketchfab/CREDITOS.json`.

Probar en local: `npm i three@0.170.0` y `python -m http.server 8765`, abrir `http://localhost:8765/shots.html?shot=B`.

Modelos de Sketchfab (no están en GitHub por tamaño): `python fetch_sf.py` con los nombres=uid que hay en `assets/sketchfab/CREDITOS.json`. Lee el token de `Escritorio\Api token.txt` o de la variable `SKETCHFAB_TOKEN`.
- `play.html`: pantalla jugable en 3D (mover: flechas/WASD, Shift turbo, Espacio derrape, P pausa; botones táctiles y mando).
