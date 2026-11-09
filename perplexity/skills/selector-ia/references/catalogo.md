# Catálogo de modelos y herramientas

**Última revisión: 2026-10-24** (Claude Opus 5.5). Si pasó más de 30 días, verificar en la web antes de usar.

Solo datos sacados de páginas oficiales o, cuando no había, de guías recientes (marcado).
Los límites exactos de uso casi nunca son públicos: no se inventan.

---

## Claude (Anthropic)

| Modelo | Para qué | Nivel por defecto |
|---|---|---|
| **Fable 5.1** | Lo más potente abierto al público. Razonamiento muy exigente, trabajo de horas, documentos finales grandes. | alto |
| **Opus 5.5** | Recomendado por defecto para casi todo: trabajo largo con herramientas, código grande, documentos, análisis. | medio |
| **Sonnet 5.5** | Rápido y capaz para el día a día: código, análisis de datos, redacción. | alto |
| **Haiku 5.5** | Lo más rápido y barato: tareas simples y repetitivas, clasificar, extraer. | medio |

- Niveles de esfuerzo (API): low, medium, high, xhigh, max. Subir el esfuerzo suele servir más que cambiar de modelo. Si Opus 5.5 en un nivel alto no alcanza, se pasa a Fable 5.1.
- Patrón útil: planear con un modelo fuerte y ejecutar con uno más liviano.
- **Planes en claude.ai:**
  - Free: Sonnet y Haiku.
  - Pro (USD 20/mes): Opus, Sonnet y Haiku, más Claude Code y Research. **Fable solo con créditos de uso pagados aparte.**
  - Max (desde USD 100/mes): Fable incluido hasta el 50 % del límite semanal.
- Mythos 5.1 = mismas capacidades que Fable, solo para organizaciones verificadas. No aplica a Nick.

Fuentes: [Models overview](https://platform.claude.com/docs/en/models/overview), [Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model), [Fable en tu plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan), [Precios](https://claude.com/pricing).

## Gemini (Google)

| Modelo (selector de la app) | Para qué |
|---|---|
| **Gemini 4 Argon** | Su modelo de punta para tareas complejas. Desde el 2026-10-13 en AI Pro y Ultra. |
| **Pro** (3.1 Pro según la página de planes) | Tareas difíciles; algunas funciones (videos, imágenes por capas) van atadas a Pro. |
| **3.6 Flash** | Rápido, para todo el mundo. Rutina y Canvas para prototipos. |

- **Google AI Pro (USD 19,99/mes):** Argon, Pro y Flash; 4 veces el uso del plan gratis; Deep Research; ventana de 1 millón de tokens; Jules con más límite; 5 TB de almacenamiento.
- Los límites de la app se renuevan cada 5 horas hasta llegar a un tope semanal. Se pueden comprar créditos.
- Desde el 2026-09-30 las **Skills** reemplazan a los Gems.
- Su punto fuerte para Nick: está metido en Google Docs, Drive y Gmail, tiene contexto largo y Deep Research.
- Deep Think: no aparece en la página del plan Pro → [Por validar].

Fuentes: [Planes Google AI](https://gemini.google/subscriptions/), [Notas de versión](https://gemini.google/release-notes/), [Droid Life, cambio en AI Plus](https://www.droid-life.com/2026/10/15/your-gemini-pro-cost-is-going-up-considerably/).

## Cursor (ahora parte de The X Subscription, xAI)

- Planes nuevos:
  - Plus: USD 8/mes.
  - Premium: USD 30/mes, 4 veces el uso de Plus.
  - Super: USD 100/mes.
  - Ultra: USD 200/mes.
- El uso se comparte entre Cursor y Grok.
- **Modelos propios:** Grok 4.7 (el más fuerte, tareas largas y difíciles), Grok 4.6, Grok 4.5 y Composer 2.5 (rápido y barato, código interactivo).
- **Modelos de terceros** (Claude Opus, Claude Fable 5, GPT-5.6 Sol, Gemini Pro): solo en Premium o más, o en planes viejos (Pro, Pro+, Ultra). Se cobran a precio de API desde el crédito prepagado.
- **Plus** no incluye Auto, agentes en la nube ni modelos de terceros.
- **Auto** (modo Cost en planes individuales) escoge el modelo y cobra como modelo de Cursor.
- Los planes viejos (Pro USD 20, etc.) siguen funcionando igual para quien ya los tenía.
- Para Nick: código dentro de un repo o carpeta, editar varios archivos, autocompletar.

Fuentes: [Precios y planes](https://cursor.com/help/account-and-billing/pricing), [Modelos disponibles](https://cursor.com/help/models-and-usage/available-models), [Anuncio de Cursor](https://x.com/cursor_ai/status/2109783879490191502).

## GitHub Copilot

- **Pro (USD 10/mes):** 1.500 créditos de IA al mes, con "una selección de modelos".
- **Pro+ (USD 39/mes):** 7.000 créditos y modelos premium.
- **Max (USD 100/mes):** 20.000 créditos.
- **Student:** gratis para estudiantes verificados, solo con selección automática de modelo → Nick podría calificar, [Por validar].
- Modelos disponibles (según el plan):
  - Claude: Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1.
  - Gemini: 4 Argon, 3.8 Flash.
  - GPT: 6.1 Sol y otros.
  - Grok: 4.7.
  - Otros: Kimi K3, MAI-Code.
- Configurar el razonamiento o usar el contexto de 1 millón **gasta más créditos**. GitHub recomienda dejarlo en lo normal por defecto.
- Incluye Copilot CLI, modo agente y agente en la nube (convierte un issue en un pull request).
- Para Nick: código en repos de GitHub, el agente que trabaja solo sobre un issue.

Fuentes: [Planes de Copilot](https://docs.github.com/en/copilot/get-started/plans), [Modelos soportados](https://docs.github.com/en/copilot/reference/ai-models/supported-models).

## Perplexity (ver mis-planes.md)

- **Free:** búsquedas básicas casi sin límite, unas 3 Pro Searches al día y muy poca investigación profunda.
- **Pro (USD 20/mes):** más búsquedas avanzadas y modelos de terceros.
- Sirve para buscar datos con fuente rápido. Guía de terceros, actualizada a 2026-06.
- **Perplexity Computer** (donde corre esta skill): agente con búsqueda web, código, el repo
  de GitHub de Nick, Google Drive, automatizaciones y, a veces, su Mac. Plan y límites de
  Nick → [Por validar]; verificar en perplexity.ai antes de dar detalles del plan.

Fuente: [eesel.ai, precios de Perplexity](https://www.eesel.ai/blog/perplexity-pricing).

## Grok (xAI)

- Va incluido en The X Subscription junto con Cursor.
- Sirve para lo que pasa en X/Twitter, opiniones del momento y cripto.
- Si Nick tiene un plan de Cursor nuevo, ya tiene Grok → [Por validar].
