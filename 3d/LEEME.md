# Costa Turbo 3D (separado del juego 2D)

- `play.html`: el juego en 3D (portada, piloto y moto, taller, mapa, 3 pantallas: EL PUERTO, LA CALA y EL MAGO).
- `src/`: mundo, agua y mar de fondo (`world.js`), estela y salpicaduras (`fx.js`), piloto (`rider.js`), juego y menús (`game.js`), sonido (`sound.js`), pintura de la moto (`paint.js`), boyas, gaviotas y sombrillas (`props.js`).
- `models/`: modelos 3D aligerados (GLB). `assets/`: texturas, cielo, música, fotos del taller y de las pantallas.
- `fetch_ph.py` / `fetch_sf.py`: descargan recursos de Poly Haven y Sketchfab. `prep.mjs`: aligera y escala modelos. Créditos en `assets/sketchfab/CREDITOS.json` y en la pantalla CRÉDITOS.

Probar en local: `python -m http.server 8765` y abrir `http://localhost:8765/play.html` (añadir `?mudo=1` para probar sin sonido).

## Versiones

- 1.0.0 (12-nov-2026): JJ'S SPORTS LOUNGE con tienda, gasolina y corazones; escenarios de las tres pantallas con barcos, faro, acantilados e isla; barcos que se mueven; monedas; rampas y saltos; medallas y récords; podio; minimapa y aviso de dirección contraria; semáforo; gaviotas, boyas con cadena, gente en la playa; mar de fondo con olas.
