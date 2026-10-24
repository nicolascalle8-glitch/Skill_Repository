# Skill_Repository

Repositorio privado de Nick para skills de Claude, el contrato con las IAs y la memoria de cada proyecto.

El método viene del repositorio `twolucky-capabilities` de Luisa (contrato compartido, router con catálogo, puertas de revisión y registro de huecos), adaptado a ingeniería mecánica.

## Estructura

```
CONTRATO.md        Reglas de Nick para TODAS las IAs (solo Nick lo cambia)
AGENTS.md          Entrada para Cursor, Copilot, Codex → apunta al contrato
GEMINI.md          Entrada para Gemini → apunta al contrato
CLAUDE.md          Entrada para Claude → apunta al contrato
.github/copilot-instructions.md, .cursor/rules/contrato.mdc  (lo mismo)
shared/
  CONTRATO-OPERATIVO.md  Reglas técnicas de ingeniería (etiquetas, unidades, puertas)
  PLANTILLA-SKILL.md     Formato para crear una skill nueva
registry/CAPACIDADES.yml Qué skills están activas, pendientes o son huecos
skills/            Skills de Claude (una carpeta por skill)
  router-ing/        Elige qué skill usar para una tarea
  monitor-skills/    Revisa todas las skills: qué sobra, actualizar, mejorar o crear
  voz-nick/          Hace que los textos que presento como míos suenen a mí
  auditor-handover/  Audita la saturación de un chat y arma handovers
  colaboracion-ias/  Coordina a Claude con las otras IAs (bitácora, propuestas)
  selector-ia/       Dice qué IA, modelo y nivel usar para cada tarea
  depurador-recursos/ Limpia memoria, docs del proyecto y chats viejos sin perder datos
shared/BITACORA-DRIVE.md   Cómo se copia la bitácora a Google Drive
registry/DRIVE.yml         Ids de carpetas y bitácoras en Drive (carpeta "Proyectos IA")
proyectos/<proyecto>/
  CONTEXTO.md      Estado actual. Lo primero que lee cualquier IA (corto, se reescribe)
  BITACORA.md      Quién hizo qué, propuestas y aprobaciones (solo crece). Copia en Drive.
  HANDOVER.md      Trazabilidad completa, con historial que nunca se borra
  archivos/        Código y textos largos que el CONTEXTO apunta
    investigaciones/ Fichas de investigación (las arma depurador-recursos)
    calculos/        Memorias de cálculo
```

## Cómo se usa

1. En el chat que está fallando, escribe algo como: "audita este chat" o "haz el handover".
2. La skill pregunta el alcance y el proyecto, da un reporte con puntaje y semáforo, y pregunta si arma el handover.
3. Si dices que sí, actualiza el HANDOVER, reescribe el CONTEXTO y te da el mensaje para pegar en el chat nuevo (con el CONTEXTO incluido). El chat nuevo lee solo el CONTEXTO, sin releer el chat viejo.

## Trabajar con varias IAs

- **Cursor / Copilot / Gemini CLI**: abre este repo en la herramienta. Leen solas su archivo de entrada y siguen el contrato.
- **Grok / Perplexity / Gemini web**: pídele a Claude "prepara el mensaje para <IA> sobre <proyecto>". Lo pegas allá; la respuesta trae su entrada de bitácora y se la pegas a Claude para que la suba.
- **Aprobar**: dile a Claude "apruebo la propuesta de <IA> sobre <tema>" y queda marcado en la bitácora.

## Crear una skill nueva

1. Pedirle a Claude la skill (el `monitor-skills` revisa que no exista ya o que no quepa en otra).
2. Escribirla con `shared/PLANTILLA-SKILL.md`.
3. Probarla con un caso real antes de marcarla activa.
4. En el mismo commit: actualizar `registry/CAPACIDADES.yml` y `skills/router-ing/references/catalogo.md`.

## Instalar la skill en Claude

Las skills se instalan en Claude con su archivo `.skill` (botón "Save skill"). Este repo es el respaldo y el historial de versiones.
