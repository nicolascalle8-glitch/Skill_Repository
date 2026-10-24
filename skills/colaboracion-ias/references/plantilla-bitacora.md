# Plantilla de BITACORA.md

## Reglas

- Las entradas nuevas van **arriba** (debajo de las secciones fijas), la más reciente primero.
- Ninguna entrada se borra ni se edita después. Si algo estaba mal, se agrega una entrada nueva que lo corrige.
- Única excepción: debajo de una PROPUESTA se agrega la línea de aprobación o rechazo de Nick.
- **En curso** y **Propuestas sin respuesta** sí se editan: son el tablero del momento.
- Cada IA firma con su nombre real.

## Tipos de entrada

- **HECHO**: trabajo terminado que no necesitaba aprobación.
- **PROPUESTA**: algo que necesita el visto bueno de Nick antes de quedar firme o ejecutarse.
- **PREGUNTA**: algo que hay que resolver; a Nick o a otra IA.
- **REVISIÓN**: revisión del trabajo de otra IA (qué sirve, qué está mal, con prueba).

---

```markdown
# BITÁCORA — <Nombre del proyecto>

Reglas: CONTRATO.md (raíz). Entradas nuevas arriba. Nada se borra.

## En curso
<!-- una línea por tarea abierta: IA — qué — desde AAAA-MM-DD HH:MM -->
- (nada)

## Propuestas sin respuesta
<!-- enlace corto a cada PROPUESTA que espera a Nick -->
- (ninguna)

---

## Entradas

### AAAA-MM-DD HH:MM — <IA y modelo> — <HECHO | PROPUESTA | PREGUNTA | REVISIÓN>
**Qué:** una o dos líneas.
**Archivos:** rutas que tocaste (o "ninguno").
**Fuentes:** de dónde salen los datos.
**Verificado:** cómo lo comprobaste (o "no verificado" y por qué).
**Para Nick:** lo que tiene que decidir o revisar (o "nada").
**Para la siguiente IA:** lo que tiene que saber.
```

Ejemplo de aprobación debajo de una propuesta:

```
✅ Aprobado por Nick — 2026-10-25 09:10
```

```
❌ Rechazado por Nick — 2026-10-25 09:10 — prefiere usar los datos del libro
```
