# Criterios del monitor

Cada skill queda en una sola casilla. Si dudas entre dos, elige la que pide menos trabajo
y dilo.

## Mantener

Funciona, se usa o es reciente, no choca con otra y sus datos están al día. No se
comenta más allá de una palabra en la tabla.

## Actualizar (la información está vieja o rota; el comportamiento está bien)

- Texto guardado en Perplexity distinto al del repo, o skill en un lado y no en el otro.
- Archivo nombrado que no existe, o skill nombrada que no existe (ni como `pendiente`).
- Catálogo, planes, modelos, precios o normas con fecha de revisión de más de 30 días.
- Falta en `registry/CAPACIDADES.yml` o en el catálogo del router.
- Nombra un procedimiento o archivo que otra skill cambió después.
- Estado `en-prueba` y ya se usó con un caso real que salió bien → pasar a `activa`.

## Mejorar (la skill hace algo mal o le falta algo)

Señales, de más fuerte a más débil:

1. Nick corrigió el resultado de la skill en una sesión (con link).
2. La misma corrección o instrucción extra aparece en 2 o más sesiones donde se usó: eso
   debería estar escrito en la skill.
3. La skill no se disparó cuando debía (Nick tuvo que nombrarla, o el trabajo se hizo sin
   ella) → mejorar la `description`.
4. Se disparó cuando no debía, o choca con otra skill → afinar la `description` de las dos
   y decir cuál gana en cada caso.
5. El `SKILL.md` pasa de ~500 líneas o mete en el cuerpo tablas largas que deberían ir en
   `references/`.

## Fusionar

Dos skills con el mismo disparador **y** la misma salida, o una que siempre se usa justo
después de otra y no tiene sentido sola. Propón cuál absorbe a cuál y qué secciones se
mueven.

## Retirar

Solo con una de estas, y nunca para una skill de menos de 30 días:

- Otra skill (de Nick o integrada de Perplexity) ya hace lo mismo igual o mejor.
- Era para un caso de una sola vez que ya terminó.
- Más de 60 días sin usarse **y** Nick no tiene un proyecto activo donde la vaya a usar
  (mira memoria y bitácoras antes de decirlo).

Retirar no borra: se marca `retirada` en `CAPACIDADES.yml`.

## Crear

Una skill nueva vale la pena cuando el mismo procedimiento de varios pasos:

- aparece en **3 o más** sesiones o entradas de bitácora, o
- aparece en **2** y en alguno Nick tuvo que corregir o volver a explicar lo mismo, o
- coincide con una `pendiente` o un `hueco` de `CAPACIDADES.yml` y ya hay un caso real.

No vale la pena para: una pregunta suelta, algo que Perplexity Computer hace bien sin instrucciones,
algo que cabe en una sección de una skill existente, o un gusto que va mejor en
`CONTRATO.md` o en la memoria o preferencias de Perplexity.

Para cada propuesta de crear, deja un brief corto (como en `shared/PLANTILLA-SKILL.md`):
nombre, problema que resuelve, disparadores con las palabras de Nick, salida, límites,
relación con las skills que ya existen, y el caso real con el que se probaría.

## Cómo ordenar las propuestas

Por ahorro para Nick: cuántas veces le pasa × cuánto le cuesta cada vez (tiempo,
correcciones, riesgo de un error en una entrega). Lo que toca entregas de la universidad o
dinero va antes que lo de comodidad.

## Semáforo del conjunto

- 🟢 Nada urgente: a lo sumo actualizaciones menores.
- 🟡 Hay choques, skills desincronizadas o una propuesta de crear o mejorar con evidencia
  fuerte.
- 🔴 Una skill está dando resultados malos en entregas reales, dos skills se contradicen
  en algo que importa, o lo guardado en Perplexity no es lo que dice el repo en una skill que
  se usa seguido.
