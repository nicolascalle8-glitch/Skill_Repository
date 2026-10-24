# Contrato operativo (ingeniería)

Reglas técnicas que toda skill de ingeniería de este repositorio debe respetar. Si una
skill choca con este contrato, manda el contrato y la skill se corrige.

Este contrato complementa a `CONTRATO.md` (raíz), que dice cómo trabaja cualquier IA con
Nick y cómo se coordinan entre ellas. Este dice cómo se hace el trabajo técnico.

Basado en el método del repositorio `twolucky-capabilities` de Luisa (etiquetas de
evidencia, enmarcar antes de producir, puertas de revisión, router con límites).

## 1. Separar lo que se sabe de lo que se supone

Todo número, propiedad o afirmación técnica lleva una etiqueta:

| Etiqueta | Qué significa |
|---|---|
| **[Dato]** | Viene del enunciado, del cliente o del plano. |
| **[Medido]** | Lo medí yo o alguien con un instrumento. Lleva instrumento y resolución. |
| **[Norma]** | Sale de una norma, tabla o libro. Lleva la fuente (ej. Shigley 10.ª ed., tabla 14-2; AGMA 2001-D04). |
| **[Supuesto]** | Lo asumimos para poder avanzar. Lleva el porqué. |
| **[Calculado]** | Resultado de una ecuación a partir de lo anterior. |
| **[Por validar]** | Algo que puede cambiar el resultado y aún no se ha comprobado. |
| **[Decisión]** | Lo decidí yo (o el profesor o el cliente). Una propuesta de una IA no es decisión hasta que yo la acepte. |

No se inventan propiedades de materiales, factores de norma, coeficientes ni
referencias. Si falta el dato, se dice qué falta, cuánto afecta y se propone un valor
marcado como [Supuesto] o se pide.

## 2. Unidades y cálculo

- Se trabaja en SI. Si el dato viene en otro sistema, se convierte una vez y se muestra la conversión.
- Toda ecuación dice de dónde sale (libro, edición, número de ecuación) o se deriva ahí mismo.
- Cuando hay números, se verifica el cálculo ejecutándolo (Python) y no solo a mano.
- Antes de dar un resultado se revisa: orden de magnitud, unidades finales y, si se puede, un caso conocido o un segundo método.
- Los resultados se redondean al final, no a mitad del cálculo.

## 3. Secuencia de trabajo

No se salta una etapa sin decirlo:

`problema → requisitos y datos → concepto o modelo → cálculo → CAD y detalle → puerta de fabricación → fabricación o prueba → aprendizaje`

Para un ejercicio de clase la secuencia se acorta (problema → datos → modelo → cálculo →
verificación), pero el resultado igual queda trazable.

## 4. Nada está "listo" porque se vea terminado

Un modelo bonito, un cálculo que da un número o una simulación con colores no prueban
que la pieza funcione. Antes de fabricar, imprimir o entregar se pasa por una revisión
con resultado explícito: **pasa**, **bloqueado** (con el motivo) o **prueba limitada**
(con el riesgo aceptado por mí).

## 5. Seguridad

Si una pieza soporta carga, presión, temperatura o tiene que ver con personas (frenos,
soportes, recipientes, elementos giratorios), se dice el factor de seguridad, el modo
de falla revisado y lo que no se revisó. Nunca se presenta como seguro algo que solo se
calculó con supuestos sin validar.

## 6. Entregables académicos

- El trabajo es mío: la IA ayuda a entender, calcular, revisar y redactar, pero yo tengo que poder explicarlo todo.
- Los textos que presento como míos van en español simple y directo (ver `voz-nick`).
- Solo se citan fuentes reales que se puedan verificar.

## 7. Cada archivo sirve para algo

No se crea un documento solo para dejar registro. Todo archivo tiene un destino (entrega,
fabricación, decisión, estudio) y un estado: borrador, vigente o histórico.

## 8. Continuidad entre chats y entre IAs

- Cuando un chat se vuelve largo o empieza a fallar, se usa `auditor-handover`.
- Cuando trabaja más de una IA en el mismo proyecto, se usa `colaboracion-ias` y la bitácora del proyecto.
- El relevo debe dejar: la pregunta o decisión en curso, las fuentes y su estado, hechos y supuestos, lo decidido, lo pendiente con su siguiente paso y lo que no se debe cambiar.
