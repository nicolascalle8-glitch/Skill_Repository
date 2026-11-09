# Mensajes para pasarle trabajo a otra IA

Llena lo que está entre `< >`. Entrégale a Nick el mensaje en un bloque de código, listo para copiar.

## 1. IA con el repositorio abierto (Cursor, Copilot, Gemini CLI, Claude Code o Claude con el repo agregado)

Estas herramientas leen solas `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `.github/copilot-instructions.md` o `.cursor/rules/`, que apuntan al contrato. El mensaje puede ser corto:

```
Proyecto: proyectos/<proyecto>/
Tarea: <qué tiene que hacer, concreto>
Datos que tienes que usar: <fuente o archivo>
No toques: <archivos o decisiones cerradas>
Al terminar: deja tu entrada en BITACORA.md según CONTRATO.md y haz commit "<ia>(<proyecto>): ...".
```

## 2. IA sin acceso al repositorio (Grok, Claude en claude.ai sin el repo, Perplexity en la web sin Computer, Gemini web, otras)

No pueden leer el repo, así que todo va pegado. Usa el resumen del contrato (no el contrato entero) para no gastar espacio, salvo que Nick pida el completo. El CONTEXTO va completo si cabe; si es muy largo, solo lo que la tarea necesita.

```
Vas a trabajar en un proyecto de Nick junto con otras IAs. Sigue estas reglas:

REGLAS (resumen del contrato de Nick)
- Español simple y directo. Respuestas cortas.
- Cero datos inventados: cada número o dato con su fuente (link, libro + página, tabla). Si algo es supuesto, márcalo como supuesto.
- No digas que algo funciona o está bien sin comprobarlo. Di cómo lo comprobaste.
- No reabras las decisiones que aparecen como "Decisiones vigentes".
- Si algo necesita una decisión de Nick, plantéalo como PROPUESTA, no lo des por hecho.
- Nunca pidas ni escribas contraseñas o datos de cuentas.

CONTEXTO DEL PROYECTO
<pegar CONTEXTO.md o la parte que aplica>

TU TAREA
<qué tiene que hacer, concreto>
<qué entregar y en qué formato>

AL TERMINAR
Cierra tu respuesta con este bloque de código, lleno, para que Nick lo pase a la bitácora:

### <AAAA-MM-DD HH:MM> — <tu nombre y modelo> — <HECHO | PROPUESTA | PREGUNTA>
**Qué:**
**Archivos:**
**Fuentes:**
**Verificado:**
**Para Nick:**
**Para la siguiente IA:**
```

## Qué IA para qué (sugerencia, Nick decide)

- **Perplexity Computer** (quien corre esta skill): coordinar, mantener el repo y la bitácora en Drive, buscar datos con fuentes (precios, normas, noticias, empresas).
- **Grok**: lo que pase en X/Twitter, opiniones del momento, cripto.
- **Gemini**: documentos de Google (Docs, Drive), resúmenes largos, segunda opinión.
- **Cursor / Copilot**: código dentro del repositorio o del proyecto.
- **Claude**: revisar el trabajo de los demás, armar entregables, segunda opinión.
