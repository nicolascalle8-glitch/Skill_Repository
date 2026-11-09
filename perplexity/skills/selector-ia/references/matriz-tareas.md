# Matriz de tareas → herramienta

Punto de partida, no regla fija. Ajustar con `mis-planes.md` y con la dificultad.
"Nivel" = esfuerzo o razonamiento cuando la app deja elegirlo.

| Tipo de tarea | Primera opción | Modelo / nivel de partida | Subir a… si no alcanza |
|---|---|---|---|
| Pregunta rápida, explicación, duda de clase | Claude o Gemini (la que esté abierta) | Sonnet 5.5 o 3.6 Flash · normal | Opus 5.5 / Argon |
| Cálculo de ingeniería con verificación (engranajes, ejes, térmica) | Claude | Opus 5.5 · medio, corriendo Python | Opus 5.5 · alto → Fable 5.1 solo si el plan lo incluye |
| Ejercicio difícil o de examen con razonamiento largo | Claude | Opus 5.5 · alto | Fable 5.1 (ver costo) o segunda opinión con Gemini 4 Argon |
| Trabajo largo de varios pasos (skills, repo, entregables, agentes) | Claude o Perplexity Computer (si ya se está aquí) | Opus 5.5 · medio | Opus 5.5 · alto |
| Investigar con fuentes (empresas, mercado, normas, precios) | Claude Research o Gemini Deep Research | modo de investigación | Cruzar las dos y comparar |
| Dato puntual de hoy con fuente | Perplexity (aquí mismo) o búsqueda web de Claude | búsqueda normal | Pro Search |
| Lo que se dice en X, cripto, memecoins | Grok | por defecto | — |
| Leer o editar Google Docs, Drive, Gmail | Gemini | Argon o Pro | Perplexity Computer o Claude con conector de Google |
| PDF o libro muy largo (resumir, buscar algo) | Gemini (contexto de 1M) | Pro o Argon | Claude Opus 5.5 |
| Código dentro de un repo (editar varios archivos, arreglar errores) | Cursor o Copilot | Auto o el modelo por defecto | Claude Opus 5.5 o Grok 4.7 en el editor |
| Autocompletar mientras escribe código | Cursor o Copilot | Tab / completions | — |
| Tarea de código suelta que puede correr sola (issue → PR) | Copilot cloud agent | por defecto | Claude Code |
| Páginas web de clientes (Shopify, HTML) | Claude | Opus 5.5 · medio | Cursor si ya está en un repo |
| Presentación o documento final | Claude (Slides / Docs) | Opus 5.5 · medio | — |
| Texto corto para mandar como suyo | Claude | Sonnet 5.5 · normal, con su voz | — |
| Tarea repetitiva por lotes (renombrar, extraer, clasificar) | Claude | Haiku 5.5 o Sonnet 5.5 | — |
| Imagen o video | Gemini (Omni, Veo, Flow) | por defecto | — |
| Segunda opinión sobre algo importante | La otra IA que tenga (Gemini ↔ Claude) | su mejor modelo | — |

## Señales para subir de nivel o de modelo
- Ya se equivocó una vez en lo mismo.
- Hay muchos pasos que dependen uno del otro.
- Un error sale caro: entrega con nota, plata de un cliente, una pieza que lleva carga.

## Señales para bajar
- Es la misma tarea repetida muchas veces.
- La respuesta es corta y fácil de revisar.
- Es formato o redacción, no razonamiento.
