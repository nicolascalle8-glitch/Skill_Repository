# Criterios de depuración

## 1. Tipos de contenido

| Tipo | Ejemplos | Cómo se depura |
|---|---|---|
| **Técnico** | cálculos, diseño, CAD, fabricación, impresión 3D, cursos | Se conserva el dato exacto con su etiqueta; el procedimiento largo va a una memoria de cálculo en el repo |
| **Investigación** | deep research, papers, análisis de empresas o sectores, M&A | Se vuelve una ficha de investigación en el repo |
| **Proyecto o negocio** | clientes, webs, oportunidades, entrevistas | Estado actual + decisiones; lo cerrado queda en una línea con fecha |
| **Personal o preferencias** | perfil, gustos, forma de trabajar | Se une lo repetido; casi nunca se borra |

Lo técnico se marca además con su etapa del router (1 Enmarcar, 2 Modelar y calcular,
3 Diseñar y detallar, 4 Fabricar o probar, 5 Comunicar, 6 Continuar) y su estado del
contrato operativo (borrador, vigente, histórico).

## 2. Qué se conserva siempre (exacto)

- Datos de entrada y supuestos de un cálculo, con su etiqueta ([Dato], [Medido], [Supuesto]…).
- Resultados con unidades, en el sistema en que estén. No se convierten ni se redondean al depurar.
- Normas y tablas con edición y número (ej. AGMA 2001-D04; Shigley 10.ª ed., tabla 14-2).
- Materiales y propiedades usadas, factores de seguridad y modo de falla revisado.
- Versiones de modelos CAD, tolerancias, parámetros de fabricación o impresión.
- Resultados de puertas de fabricación: pasa / bloqueado / prueba limitada, con su motivo.
- Decisiones de Nick ([Decisión]) con fecha.
- En investigación: pregunta, conclusión, cifras con fuente y fecha del dato, links.

## 3. Qué se puede quitar

- Explicaciones repetidas y teoría que está en el libro (queda la referencia).
- Borradores descartados y alternativas que Nick no eligió (si importan para la
  trazabilidad, ya están en HANDOVER o BITACORA).
- Idas y vueltas de la conversación, saludos, confirmaciones.
- Estados intermedios ("estoy en el paso 3") de tareas terminadas.

## 4. Señales de vencido

| Tipo de dato | Vence |
|---|---|
| Precios, valuaciones, múltiplos, tasas, datos de mercado, noticias de una empresa | ~3 meses |
| Estados financieros | cuando sale el siguiente periodo |
| Normas | cuando sale otra edición |
| Planes y límites de herramientas de IA | ~1 mes (los revisa `selector-ia`) |
| Teoría, ecuaciones, métodos de diseño | no vence |
| Entregas, exámenes, entrevistas | después de la fecha |

Lo vencido no se borra si tiene valor histórico: se marca `VENCIDA <fecha>` (fichas) o pasa a
estado histórico (archivos). En memoria, un pendiente cerrado se resume en una línea con fecha.

## 5. Memoria de Claude: problemas típicos

- **Duplicado**: mismo hecho en dos archivos, o copia del proyecto que repite uno de la cuenta.
- **Vencido o cerrado**: ver tabla 4.
- **Inflado**: frases que dicen lo mismo, historiales largos, archivo cerca del límite.
- **Descripción mala**: larga, vaga o que ya no corresponde. Se carga en cada chat.
- **Dato largo en memoria**: tablas, cálculos o reportes → al repo, con puntero.
- **Mal ubicado**: un dato en el archivo de otro tema.

## 6. Docs del proyecto: problemas típicos

- PDF completo de norma, catálogo o libro cuando solo se usan 2–3 tablas.
- Reporte de investigación largo que nadie vuelve a leer completo.
- Varias versiones del mismo informe, presentación o cálculo.
- Instrucciones del proyecto largas o con reglas repetidas del contrato.
- Docs que ya resume un `CONTEXTO.md`.

## 7. Ideas para hábitos (escoger solo las que apliquen)

- Un chat por tema y por etapa: calcular en un chat y redactar el informe en otro que
  arranque con la memoria de cálculo, no con todo el chat del cálculo.
- Cálculos repetidos en un script de Python o una hoja, no rehechos a mano en el chat.
- Normas y catálogos: subir solo las tablas que se usan.
- Investigaciones: al terminar, ficha de investigación y cerrar el chat.
- Pedir cambios puntuales ("corrige el paso 3") en vez de "rehazlo todo".
- Chat largo que empieza a fallar: `auditor-handover`.
- Procedimiento que se repite en varios chats: `router-ing` para volverlo skill.
- Correr esta skill una vez al mes o al cerrar un semestre o un proyecto.
