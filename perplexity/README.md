# Skills para Perplexity Computer

Versiones de las skills de Nick adaptadas para Perplexity Computer. Las de Claude siguen en
`skills/` y no se tocan desde aquí: cada IA mantiene su carpeta.

- Mismo propósito, reglas, plantillas y scripts que las de Claude. Cambia lo que depende de
  la plataforma: "chat" → "sesión", repo con `gh`, Drive con `gws`, memoria y Projects de
  Perplexity, automatizaciones, firma `Perplexity Computer (<modelo>)` y commits
  `perplexity(<proyecto>): ...`.
- Todas están guardadas en Perplexity (Mis Skills) con el mismo nombre de carpeta.
- Cada skill termina con "Acceso a las otras skills de Nick": carga de fondo `contexto-nick` y
  `cerebro-nick`, y carga por nombre las skills que nombra (o las lee aquí si no cargan).
- `monitor-skills` (versión Perplexity) sincroniza solo esta carpeta: sus scripts usan
  `perplexity/skills/` y nunca escriben en `skills/`.
- Catálogo del router para Perplexity: `perplexity/skills/router-ing/references/catalogo.md`.
- Registro compartido: `registry/CAPACIDADES.yml` (una capacidad por skill, sirve para las dos
  carpetas).

Las 13: router-ing, monitor-skills, voz-nick, auditor-handover, colaboracion-ias, selector-ia,
depurador-recursos, panel-asesores, presentaciones-universidad, diseno-cad-fusion,
puerta-fabricacion, contexto-nick, cerebro-nick.
