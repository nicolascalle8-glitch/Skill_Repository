# BITÁCORA — Horno vertical (pirólisis de café, práctica GIEM UdeA/EIA)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra. Copia idéntica en Google Drive: Proyectos IA / horno-vertical / Bitácora — horno-vertical.

## En curso
- Claude Opus 5.5 — diseño del motor nuevo (subproyecto A, spec) — desde 2026-11-08 19:33

## Propuestas sin respuesta
- (ninguna)

---

## Entradas

### 2026-11-08 19:33 — Claude Opus 5.5 — PREGUNTA
**Qué:** Datos que faltan para calibrar el modelo con el horno real.
**Archivos:** ninguno.
**Fuentes:** revisión de Max_Power/01_Horno_Vertical/datos/ (Mac de Nick).
**Verificado:** n/a.
**Para Nick:** (1) ¿"Café grano" del FTIR es el mismo residuo de tinto del reporte GIEM 28ago2604? (2) Masas de la corrida "Pirolizado 1-2": café cargado, biochar obtenido, rampa y T final. (3) Cualquier registro de temperatura de esa corrida. (4) Fuente de la composición celulosa/hemicelulosa/lignina/lípidos (12/35/28/15 %).
**Para la siguiente IA:** no tratar esa composición como dato del GIEM: el reporte no la trae.

### 2026-11-08 19:33 — Claude Opus 5.5 — HECHO
**Qué:** Se abre el proyecto. Modelo traído al Mac, corrida medida, barrido en paralelo probado, datos revisados y plan aprobado por Nick (A motor nuevo → B calibración térmica → C app Streamlit).
**Archivos:** proyectos/horno-vertical/CONTEXTO.md, BITACORA.md; en el Mac: Max_Power/01_Horno_Vertical/modelos/PyrolysisReactorCoffee/ (copia del repo, commit ddb0a63) y modelos/barrido_paralelo.py.
**Fuentes:** repo nicolascalle8-glitch/PyrolysisReactorCoffee (docs/EVALUACION_CINETICAS.md); reporte GIEM 28ago2604 (7-sep-2026); FTIR muestras 013/014/015 (4-sep-2026).
**Verificado:** caso base (10 °C/min, 500 °C, 30 min, 8 % humedad) corrido en la VM del Mac: 25 s, biochar 24.93 %, bio-oil 38.94 %, gas 20.23 %, agua 15.90 %, balance 100.000 % (igual al informe). Barrido demo 4 casos con 4 procesos: x3.1.
**Para Nick:** nada (el plan ya lo aprobó en el chat).
**Para la siguiente IA:** la shell de Claude en el Mac es una VM Linux de 4 núcleos y ~3 GB; las corridas grandes van en la Terminal de macOS. El GIEM solo reporta humedad 61.2 % bh, cenizas 2.31 % bs, pérdida por calcinación 650 °C 97.7 % bs, CO 49.4 % bs, N 0.418 % bs, C/N 118.2.
