# Estructura de un proyecto

Cómo se arma y se ordena cualquier proyecto de Nick, en el repo y en su computador. La usan
`colaboracion-ias` (proyecto nuevo), `auditor-handover` (handover) y `depurador-recursos`
(fichas y memorias). Si una skill dice otra cosa, manda esta plantilla y la skill se corrige.

Parte de la idea viene del archivo de Gemini del 2026-10-24 (arquitecto-proyecto:
alcance en pocas preguntas, carpeta `anterior/` y criterio de cierre).

## 1. En el repo (memoria compartida entre IAs)

```
proyectos/<proyecto>/
  CONTEXTO.md      Estado actual. Lo único que lee un chat nuevo. Se reescribe, no crece.
  BITACORA.md      Quién hizo qué, propuestas y aprobaciones. Solo crece. Copia en Drive.
  HANDOVER.md      Historial completo de decisiones e hitos. Solo se abre si hace falta.
  archivos/
    investigaciones/  Fichas de investigación (depurador-recursos)
    calculos/         Memorias de cálculo y scripts de verificación (calculo-trazable)
    <otros>           Textos largos aprobados, tablas, código que el CONTEXTO apunta
```

- `<proyecto>`: minúsculas con guiones, corto (`horno-vertical`, `detector-particulas-cern`).
- Los archivos pesados (PDF, CAD, Word, imágenes) **no** van al repo: viven en el computador o
  en Drive y el CONTEXTO los apunta con su ruta.
- Cada proyecto aparece en `proyectos/README.md` (índice) con su estado.

## 2. En el computador de Nick (archivos de trabajo)

Raíz: `D:\Personal\Claude\proyectos\<proyecto>\` (mismo nombre que en el repo).

```
<proyecto>\
  fuentes\       Lo que entregan el profesor, el cliente o el libro (enunciados, PDFs, normas). No se edita.
  trabajo\       Scripts, recortes, figuras, borradores. Puede estar desordenado.
  entregables\   Solo la versión vigente de lo que se entrega.
  anterior\      Versiones viejas o descartadas. Nada se borra: se mueve aquí, con aprobación de Nick.
```

- Si un proyecto ya tiene su orden interno (por ejemplo, un script que busca `assets\`), se
  respeta dentro de `trabajo\`; no se rompe un script por ordenar.
- Mover, renombrar o borrar en el computador siempre pide aprobación de Nick con la lista exacta
  (CONTRATO.md, sección 5).
- Lo que llega sin proyecto (descargas, archivos de otras IAs) va a `D:\Personal\Claude\_entrada\`
  hasta que se decida a qué proyecto pertenece.

## 3. Arrancar un proyecto nuevo

1. **Alcance en máximo 5 preguntas**, en un solo mensaje y con opciones: qué se entrega y en qué
   formato, para cuándo, idioma, de dónde salen los datos (enunciado, libro, cliente) y la rúbrica.
   Solo se pregunta lo que falte.
2. Confirmar el nombre `<proyecto>` y revisar que no exista ya con otro nombre (`proyectos/README.md`).
3. Crear en el repo `CONTEXTO.md` mínimo, `BITACORA.md` (plantilla de colaboracion-ias) y su copia
   en Drive (`shared/BITACORA-DRIVE.md`). El HANDOVER lo crea `auditor-handover` la primera vez.
4. Proponer (no crear sin permiso) la carpeta del computador con la estructura del punto 2.
5. Escribir el **criterio de cierre** en el CONTEXTO (punto 4).
6. Agregar la fila al índice `proyectos/README.md`.

## 4. Criterio de cierre (en el CONTEXTO)

Sección fija del CONTEXTO: qué tiene que existir y qué revisión tiene que pasar para decir que
el proyecto está terminado. Ejemplo:

```markdown
## Criterio de cierre
- [ ] entregables\informe.pdf con el ejercicio final (los mismos números que el Excel y el script)
- [ ] Revisión de consistencia sin hallazgos (calculo-trazable, paso de consistencia)
- [ ] Nada viejo en entregables\ (lo viejo en anterior\)
- [ ] Subido a la carpeta del curso — Nick
```

Cuando todo está marcado, el proyecto pasa a `cerrado` en el índice y en `registry/DRIVE.yml`.

## 5. Estados de un proyecto (índice)

`activo` (se trabaja) · `en pausa` (espera algo de alguien) · `cerrado` (entregado; se conserva).
Un proyecto nunca se borra del índice.
