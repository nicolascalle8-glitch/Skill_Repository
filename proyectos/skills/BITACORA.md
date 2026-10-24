# BITÁCORA — Skills (Skill_Repository)

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.
Copia en Google Drive: Proyectos IA / skills / Bitácora — skills (https://docs.google.com/document/d/18QtRuv0MvYGrumv7YzqNIKsTefi9423Fgm904UdUWeI/edit)

## En curso
- (nada)

## Propuestas sin respuesta
- 2026-10-24 17:41 — Claude — Cambiar la regla "todo en SI" del contrato operativo a "SI por defecto, salvo que el libro o el enunciado use otro sistema".

---

## Entradas

### 2026-10-24 17:55 — Claude Opus 5.5 — HECHO
**Qué:** Se crea la skill selector-ia (qué IA, modelo y nivel usar) con catálogo de modelos revisado el 2026-10-24. Se monta la copia de las bitácoras en Google Drive: carpeta Proyectos IA con una subcarpeta y un Doc de bitácora por proyecto (engranajes-helicoidales y skills). colaboracion-ias, auditor-handover y selector-ia ahora escriben en GitHub y en Drive.
**Archivos:** skills/selector-ia/, shared/BITACORA-DRIVE.md, shared/scripts/entrada_drive.py, registry/DRIVE.yml, registry/CAPACIDADES.yml, skills/colaboracion-ias/SKILL.md, skills/auditor-handover/SKILL.md, CONTRATO.md (v0.1.1), GEMINI.md, README.md
**Fuentes:** Docs de Anthropic, gemini.google, cursor.com y docs.github.com (links en skills/selector-ia/references/catalogo.md).
**Verificado:** Las 4 skills pasan quick_validate; los YAML cargan; esta entrada se agregó a Drive con entrada_drive.py y se revisó leyendo el Doc.
**Para Nick:** Confirmar qué plan de Claude tienes, si es Cursor o Copilot (y qué plan), y si Gemini es Pro o Ultra. Decir qué otros proyectos quieres con carpeta en Drive.
**Para la siguiente IA:** Los ids de Drive están en registry/DRIVE.yml. Toda entrada va idéntica a GitHub y a Drive (shared/BITACORA-DRIVE.md).

### 2026-10-24 17:41 — Claude Opus 5.5 — HECHO
**Qué:** Se sube el esqueleto de skills de ingeniería basado en twolucky-capabilities (repo de Luisa): contrato operativo, plantilla de skill, router-ing y registro de capacidades. Se corrige el encabezado de colaboracion-ias, que no pasaba la validación.
**Archivos:** shared/CONTRATO-OPERATIVO.md, shared/PLANTILLA-SKILL.md, skills/router-ing/, registry/CAPACIDADES.yml, CONTRATO.md, README.md, skills/colaboracion-ias/SKILL.md
**Fuentes:** chat "Repositorio de skills de mi mentora" (2026-10-24).
**Verificado:** CAPACIDADES.yml carga como YAML; router-ing y colaboracion-ias pasan quick_validate.
**Para Nick:** Instalar router-ing.skill y la versión corregida de colaboracion-ias.skill. Decidir la regla de unidades (ver propuesta).
**Para la siguiente IA:** Las skills nuevas se escriben con shared/PLANTILLA-SKILL.md y se registran en CAPACIDADES.yml y en el catálogo del router en el mismo commit.

### 2026-10-24 17:41 — Claude Opus 5.5 — PROPUESTA
**Qué:** Cambiar en shared/CONTRATO-OPERATIVO.md la regla "Se trabaja en SI" por "SI por defecto, salvo que el libro o el enunciado use otro sistema". El proyecto de engranajes se trabajó en unidades inglesas porque Mott viene así.
**Archivos:** ninguno todavía.
**Fuentes:** CONTEXTO de engranajes-helicoidales ("Presentación en Claude Slides, unidades inglesas").
**Verificado:** n/a.
**Para Nick:** aprobar o rechazar.
**Para la siguiente IA:** no cambiar la regla hasta que Nick decida.

### 2026-10-24 17:29 — Claude Opus 5.5 — HECHO
**Qué:** Se crea el contrato de trabajo para todas las IAs (v0.1, borrador), la skill colaboracion-ias y los archivos de entrada para Cursor, Copilot, Gemini y Claude.
**Archivos:** CONTRATO.md, AGENTS.md, GEMINI.md, CLAUDE.md, .github/copilot-instructions.md, .cursor/rules/contrato.mdc, skills/colaboracion-ias/
**Fuentes:** pedido de Nick en el chat del 2026-10-24.
**Verificado:** commit 91ffcec en main.
**Para Nick:** completar las líneas [COMPLETAR NICK] del contrato.
**Para la siguiente IA:** leer CONTRATO.md antes de cualquier cosa.
