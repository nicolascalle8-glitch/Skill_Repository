# Plantilla del CONTEXTO.md

## Para qué existe

El CONTEXTO.md es lo **único** que la sesión nueva lee al arrancar. Reemplaza releer la sesión vieja y también reemplaza leer el HANDOVER completo, que crece con cada actualización. Si la sesión nueva tiene que leer más para empezar a trabajar, el CONTEXTO está mal hecho.

Piensa en quién lo lee: una sesión (de Perplexity o de otra IA) que no sabe nada del proyecto y tiene que seguir trabajando como si hubiera estado en la sesión, sin preguntarle a Nick lo que ya se dijo.

## Reglas

- **Tope: ~1.500 palabras.** Si te pasas, comprime: quita historia, deja resultados. Lo que no quepa y sea largo va a `archivos/` (ver abajo).
- **Se reescribe completo en cada handover.** No crece. La trazabilidad vive en el HANDOVER.md, no aquí.
- **Solo el estado final**, no cómo se llegó. "Se usa Shopify" sí; "primero pensamos en WordPress, luego…" no (eso va en el historial).
- **Datos exactos, no resúmenes vagos.** Nombres, cifras, precios, medidas, versiones, URLs, rutas de archivos, nombres de variables. Si en la sesión se dijo "COP 2.400.000", aquí va "COP 2.400.000", no "un valor acordado".
- **Lo que tiene que ser literal, va literal**: textos finales aprobados, especificaciones, fórmulas, prompts. Si es corto (< 15 líneas), aquí. Si es largo, en `archivos/`.
- **Mapa de carga bajo demanda**: lista qué archivo abrir para qué tarea, para que la sesión nueva lea solo lo que necesita cuando lo necesita.
- Nada de contraseñas, tokens, números de cuenta ni documentos de identidad.

## Archivos grandes

Código, documentos largos, tablas grandes o textos extensos aprobados se guardan aparte en `proyectos/<proyecto>/archivos/<nombre>` y en el CONTEXTO solo va una línea: qué es, dónde está y cuándo abrirlo. Así no se cargan si la tarea no los necesita. Si un archivo ya vive en otro lado (Drive, Shopify, el computador), solo se apunta ahí, no se copia.

---

```markdown
# CONTEXTO — <Nombre del proyecto>

Actualizado: <AAAA-MM-DD HH:MM> (Bogotá). Lee solo esto para arrancar. El historial completo está en HANDOVER.md y solo se abre si Nick pregunta por algo del pasado.

## En una frase
<Qué es el proyecto y en qué punto va.>

## Tu siguiente tarea
<Lo primero que la sesión nueva tiene que hacer, concreto.>

## Hechos clave (exactos)
- <cifra / nombre / medida / precio / fecha / URL>
- ...

## Decisiones vigentes (no reabrir)
- <decisión> — <por qué en pocas palabras>
- ...

## Restricciones
- <límites de presupuesto, tiempo, técnicos, del cliente, de herramientas>

## Pendientes abiertos
- [ ] <pendiente> — <responsable> — <fecha límite>

## Criterio de cierre
- [ ] <qué archivo tiene que existir / qué revisión tiene que pasar> (ver shared/PLANTILLA-PROYECTO.md, punto 4)

## Preguntas abiertas
- <lo que falta decidir>

## Cómo quiere trabajar Nick aquí
- <formato, tono, lo que no le gusta, lo que tuvo que corregir varias veces>

## Errores que no repetir
- <cosas que salieron mal en la sesión anterior y cómo evitarlas>

## Mapa de archivos (abrir solo cuando la tarea lo pida)
| Archivo | Qué tiene | Abrir cuando |
|---|---|---|
| archivos/<x> | ... | ... |
| HANDOVER.md | trazabilidad, historial de decisiones | Nick pregunte cuándo o por qué cambió algo |

## Glosario
- <término o sigla del proyecto>: <qué significa aquí>
```
