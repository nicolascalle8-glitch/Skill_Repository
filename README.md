# Skill_Repository

Repositorio privado de Nick para skills de Claude y handovers de proyectos.

## Estructura

```
CONTRATO.md        Reglas de Nick para TODAS las IAs (solo Nick lo cambia)
AGENTS.md          Entrada para Cursor, Copilot, Codex → apunta al contrato
GEMINI.md          Entrada para Gemini → apunta al contrato
CLAUDE.md          Entrada para Claude → apunta al contrato
.github/copilot-instructions.md, .cursor/rules/contrato.mdc  (lo mismo)
skills/            Skills de Claude (una carpeta por skill)
  auditor-handover/  Audita la saturación de un chat y arma handovers
  colaboracion-ias/  Coordina a Claude con las otras IAs (bitácora, propuestas)
proyectos/<proyecto>/
  CONTEXTO.md      Estado actual. Lo primero que lee cualquier IA (corto, se reescribe)
  BITACORA.md      Quién hizo qué, propuestas y aprobaciones (solo crece)
  HANDOVER.md      Trazabilidad completa, con historial que nunca se borra
  archivos/        Código y textos largos que el CONTEXTO apunta
```

## Cómo se usa

1. En el chat que está fallando, escribe algo como: "audita este chat" o "haz el handover".
2. La skill pregunta el alcance y el proyecto, da un reporte con puntaje y semáforo, y pregunta si arma el handover.
3. Si dices que sí, actualiza el HANDOVER, reescribe el CONTEXTO y te da el mensaje para pegar en el chat nuevo (con el CONTEXTO incluido). El chat nuevo lee solo el CONTEXTO, sin releer el chat viejo.

## Trabajar con varias IAs

- **Cursor / Copilot / Gemini CLI**: abre este repo en la herramienta. Leen solas su archivo de entrada y siguen el contrato.
- **Grok / Perplexity / Gemini web**: pídele a Claude "prepara el mensaje para <IA> sobre <proyecto>". Lo pegas allá; la respuesta trae su entrada de bitácora y se la pegas a Claude para que la suba.
- **Aprobar**: dile a Claude "apruebo la propuesta de <IA> sobre <tema>" y queda marcado en la bitácora.

## Instalar la skill en Claude

Las skills se instalan en Claude con su archivo `.skill` (botón "Save skill"). Este repo es el respaldo y el historial de versiones.
