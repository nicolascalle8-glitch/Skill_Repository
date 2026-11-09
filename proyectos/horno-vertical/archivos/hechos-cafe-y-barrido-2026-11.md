# Hechos del café, del caso base y del barrido (movidos del CONTEXTO el 2026-11-09)

Se sacaron del CONTEXTO para dejarlo en ~1.500 palabras. No cambió ningún valor.

- Caso base (10 °C/min, 500 °C, 30 min, 8 % de humedad): biochar 24.22 / bio-oil 39.60 / gas 20.31 / agua 15.88 % de la carga. Tarda 1.4 s en el M4.
- Barrido de 30 casos (T_final 400–600, rampa 5–20, humedad 8–15 %): biochar 20.3–25.8 %. La T final es lo que más pesa. La humedad solo diluye (en base seca el biochar no cambia). La rampa casi no pesa (< 0.5 pp), y eso es propiedad del régimen `lecho_fijo`: hay que contrastarlo con una corrida real. Archivo: `resultados/barrido_20261108_2148.csv`.
- Datos del GIEM (28ago2604) [Dato]: humedad 61.2 % bh, cenizas 2.31 % bs, pérdida por calcinación a 650 °C 97.7 % bs, CO 49.4 % bs, N 0.418 % bs, C/N 118.2.
- FTIR (Café grano, Pirolizado 1-2, Pirolizado sedimento): solo cualitativo.
- Composición en base seca:
  - celulosa 12.4 y lignina 23.9 % [Dato, Ballesteros et al. 2014, Tabla 1]
  - hemicelulosa 35 [Supuesto]
  - lípidos 15 [Por validar]
  - otros 11.39 [Calculado]
- Densidad aparente 380 kg/m³ [Por validar]; Guendouz 2023 da 387.
