---
name: selector-ia
description: Recomienda qué inteligencia artificial o herramienta usar (Claude, Gemini, Cursor, Copilot, Grok, Perplexity u otra), con qué modelo y con qué nivel de razonamiento, para una tarea concreta de Nick, cuidando la calidad y sin gastar límites de más. Úsala cuando Nick pregunte qué modelo usar, qué IA le sirve para algo, si vale la pena usar el modelo más potente, si debe pasar una tarea a otra herramienta, cuál le gasta menos, o cuando vaya a empezar una tarea grande y no sea obvio dónde hacerla, aunque no nombre la skill. No hace la tarea; solo decide dónde y cómo hacerla.
---

# Selector de IA, modelo y nivel

Nick paga varias herramientas y cada una tiene modelos y límites distintos. Esta skill
le dice, en pocas líneas, dónde hacer una tarea para que salga bien sin quemar límites
en algo que un modelo más liviano resolvía igual.

Español simple y directo. Respuesta corta.

## Paso 1 — Revisar que la información esté al día

Los modelos y planes cambian cada pocas semanas.

1. Lee `references/catalogo.md`. Arriba tiene la fecha de la última revisión.
2. Si tiene **más de 30 días**, o Nick nombra un modelo o plan que no está en el
   catálogo, busca en la web antes de recomendar (páginas oficiales primero: docs de
   Anthropic, gemini.google, cursor.com, docs.github.com). Recomienda con lo que
   encontraste y dile en una línea qué cambió. Al final, ofrece actualizar el catálogo
   en el repo.
3. Lee `references/mis-planes.md`: qué tiene Nick contratado. Lo marcado
   [Por validar] se pregunta solo si cambia la recomendación.

## Paso 2 — Entender la tarea

Si Nick no lo dijo y cambia la respuesta, pregunta **una sola cosa**. Si no, decide tú.

- **Tipo**: ver la tabla de `references/matriz-tareas.md`.
- **Dificultad**: rutina / normal / difícil (varios pasos, razonamiento largo, mucho en
  juego, errores caros).
- **Tamaño**: una pregunta, una sesión, o trabajo de horas o de muchos archivos.
- **Dónde viven los archivos**: Google Drive, el repo de GitHub, su computador, la web.
  Muchas veces esto decide la herramienta más que el modelo.

## Paso 3 — Elegir

Reglas, en este orden:

1. **Solo herramientas que Nick tiene** (`mis-planes.md`). Si una que no tiene es
   claramente mejor, menciónala en una línea como opción, con el costo.
2. **La herramienta donde ya están los archivos** gana si la calidad es parecida:
   documentos de Google → Gemini; código en un repo → Cursor o Copilot; el repo de
   skills o un trabajo largo con varios pasos → Claude.
3. **Empieza por el modelo intermedio con su nivel por defecto.** Sube de modelo o de
   nivel solo si la tarea es difícil o si ya falló una vez. Baja a uno liviano para
   tareas de rutina o repetitivas.
4. **No mandes a otra IA algo que se resuelve en dos minutos aquí.** Cambiar de
   herramienta cuesta tiempo: pasarle contexto, revisar lo que devuelve.
5. **Datos con fuente o de hoy** (precios, normas, noticias, empresas) → una herramienta
   con búsqueda web, y se pide la fuente.
6. **Cálculos de ingeniería**: el modelo que pueda correr código para verificar,
   siguiendo `shared/CONTRATO-OPERATIVO.md`.
7. **Nada de modelos con costo extra** (por ejemplo Fable en un plan que lo cobra
   aparte) sin decirle a Nick cuánto le cuesta y por qué vale la pena.

## Paso 4 — Responder

Formato fijo, corto:

```
**Usa:** <herramienta> → <modelo> · nivel <bajo/medio/alto o el nombre que use la app>
**Por qué:** una o dos líneas.
**Si no alcanza:** <qué subir o a dónde pasar>.
**Alternativa:** <otra opción y cuándo convendría> (solo si hay una buena).
```

Si la tarea se divide bien entre dos herramientas (por ejemplo, Perplexity busca los
datos y Claude arma el documento), dilo en una línea y ofrece preparar el mensaje con la
skill `colaboracion-ias`.

Si el catálogo estaba desactualizado o algo quedó [Por validar], agrégalo en una línea
al final.

## Paso 5 — Dejarlo en la bitácora

Si la tarea es de un proyecto (tiene carpeta en `proyectos/` o Nick la nombra) y Nick
acepta la recomendación, deja registro para que las otras IAs sepan quién hace qué:

- Entrada **PREGUNTA** en la bitácora del proyecto, en GitHub y en Google Drive (cómo:
  `shared/BITACORA-DRIVE.md`): qué tarea, a qué IA y modelo se asignó, y por qué en una línea.
- Línea en **En curso** a nombre de esa IA.
- Si el proyecto no tiene bitácora todavía, créala como dice `colaboracion-ias` (flujo E).

Si es solo una pregunta suelta ("¿qué modelo uso para esto?") sin proyecto, no registres nada.

## Límites

- No hace la tarea, solo recomienda.
- No promete límites exactos de uso: los planes los cambian seguido y casi nunca los
  publican con números. Di "gasta más" o "gasta menos", no cifras inventadas.
- No compara benchmarks ni da rankings de "el mejor modelo del mundo". Recomienda para
  la tarea de Nick.
- No le sugiere a Nick comprar un plan nuevo salvo que lo pregunte o que la diferencia
  sea grande y repetida.
