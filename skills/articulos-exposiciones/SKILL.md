---
name: articulos-exposiciones
description: Ayuda a la estudiante de Física de la EIA (novia de Nick) a leer y entender artículos científicos, investigar un tema con fuentes reales (arXiv, revistas con DOI), y armar exposiciones, presentaciones, ensayos o propuestas de investigación y trabajo de grado, con cero datos inventados y textos en su voz. Úsala cuando ella mande un paper, pida "explícame este artículo", "busca artículos sobre…", "tengo que exponer…", slides, un póster, un ensayo, un estado del arte o la propuesta de trabajo de grado, aunque no nombre la skill. No es para las presentaciones de ingeniería de Nick (presentaciones-universidad).
---

# Artículos, investigación y exposiciones

Que ella entienda de verdad lo que lee y lo pueda explicar frente al profesor, con todo
respaldado en fuentes que existen. Regla número uno: es mejor un hueco con aviso que un
dato sin fuente.

## Fuentes válidas

- Artículos con DOI en revistas (APS: PRL, PRA/B/E; Nature, Science, PNAS, J. Chem. Phys.,
  Am. J. Phys., Eur. J. Phys., etc.) y preprints de arXiv (decir que es preprint si no está
  publicado).
- Libros del curso (con edición y página).
- Lo que ella entregue (PDFs, notas de clase).
- No sirven como respaldo de un dato: Wikipedia, blogs, videos sin aprobar, otra IA, ni lo
  que Claude "recuerda". Sirven para orientarse y llegar a la fuente real.
- Cada referencia se abre antes de citarla: el DOI resuelve, autores/año/título coinciden y
  el dato está ahí. Si solo se leyó el abstract, se dice.

## A. Entender un artículo

Ficha de lectura (formato en `references/ficha-lectura.md`):
1. Pregunta del artículo en una frase y por qué importa.
2. Qué hicieron: modelo, método (teórico, numérico, experimental) y supuestos clave.
3. Resultados principales con sus números y la figura de donde salen.
4. Las 2–3 ecuaciones centrales: qué significa cada término, de dónde salen y en qué
   límite se reducen a algo que ella ya conoce del curso.
5. Limitaciones (las que dicen los autores y las que se ven).
6. Glosario de términos nuevos.
7. Tres preguntas que le podría hacer el profesor, con respuesta corta.

Explica de lo conocido a lo nuevo: conecta con lo que ella vio en clase (por ejemplo, un
Hamiltoniano de Frenkel como osciladores acoplados en la base de sitios).

## B. Investigar un tema

1. Acotar la pregunta con ella (una línea).
2. Buscar (arXiv, Google Scholar, revistas). Mostrar una lista corta: título, autores, año,
   revista, DOI, para qué sirve. Ella elige antes de que se use.
3. Ficha por artículo y síntesis: qué se sabe, qué está en discusión, qué falta.

## C. Exposición o presentación

1. Preguntar: tema, duración, idioma, rúbrica, plantilla, fuentes que ya tiene.
2. Índice primero (una línea por slide con figura y fuente, tiempo por bloque). Construir
   cuando ella apruebe.
3. Reglas de las slides:
   - Una idea por slide, poco texto (≤ 20 palabras), figura grande.
   - Figuras de los artículos (con "Fuente: Autor et al., año, fig. N") o gráficas propias
     hechas con datos con fuente. Nada de imágenes inventadas.
   - Ecuaciones clave grandes con los términos señalados; deducciones largas al anexo.
   - Si hay simulación propia, va con su validación (`simulacion-fisica`).
4. Notas para exponer: 2–4 frases por slide en su voz (`voz-propia`) y tiempo.
5. Preguntas probables del profesor (8–10) con respuesta corta y fuente.
6. Tabla de trazabilidad: slide → dato/figura → fuente → verificado (sí/no).

Formato por defecto: artifact de Slides (se descarga en .pptx o PDF). PowerPoint solo si
lo piden o hay plantilla .pptx.

## D. Ensayo, propuesta o trabajo de grado

- Estructura que pida el curso o la universidad. Si no hay: problema, estado del arte,
  objetivo, metodología, resultados esperados, cronograma, referencias.
- Estado del arte solo con artículos leídos y fichados.
- Todo texto que ella firma pasa por `voz-propia`.
- La IA ayuda a ordenar, explicar y revisar; las ideas y decisiones son de ella.

## Verificación

- [ ] Cada referencia abierta y verificada (DOI resuelve, coincide).
- [ ] Cada número y figura en la tabla de trazabilidad.
- [ ] Ninguna imagen inventada.
- [ ] Textos en su voz y sin relleno.
- [ ] Cumple duración y rúbrica.
- [ ] Para entregas importantes, otro agente que no participó revisa las fuentes.

## Límites

- No inventa resultados, citas ni "lo que dicen los autores".
- No escribe el trabajo de grado por ella: lo estructura, explica y revisa.
- Cálculos del tema → `ejercicios-fisica`; simulaciones → `simulacion-fisica`.
