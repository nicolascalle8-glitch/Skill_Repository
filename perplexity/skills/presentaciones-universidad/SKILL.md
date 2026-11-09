---
name: presentaciones-universidad
description: "Arma presentaciones para entregas y sustentaciones de la universidad de Nick: cero alucinaciones (todo dato verificado en fuentes indexadas), livianas, con figuras reales de las fuentes y textos que suenen a él. Úsala siempre que Nick pida slides, una presentación, una exposición o una sustentación, aunque no nombre la skill. Para que el panel la evalúe o la ensaye como jurado, usa panel-asesores."
---

# Presentaciones para la universidad

Cuatro reglas que esta skill existe para cumplir, en este orden de prioridad:
0. **Cero alucinaciones**: todo lo que aparece es verídico y sale de fuentes indexadas.
1. **Visuales reales**: fotos y figuras de las fuentes, no imágenes inventadas por la IA.
2. **Slides livianas y llamativas**, fáciles de sustentar.
3. **Que suene a Nick**, no a un robot.

Si algo de lo que vas a entregar rompe alguna, está mal, aunque se vea completo. La regla 0 está por encima de todo: es preferible una slide vacía con un aviso que una slide con un dato no verificado.

## 0. Veracidad: nada sin fuente indexada

**Fuentes válidas**
- Artículos de revistas y congresos indexados (Scopus, Web of Science), encontrados en ScienceDirect, IEEE Xplore, SpringerLink, ASME Digital Collection, Taylor & Francis, Wiley, SAGE, MDPI o similares, siempre con DOI.
- Fuentes que Nick entregue (sus PDFs, libros del curso, normas como ISO, ASTM, AGMA). Se usan citando capítulo, página, tabla o figura exacta.
- Libros técnicos o normas que Nick no entregó: solo si él los aprueba.
- **Videos de YouTube: solo con permiso previo de Nick, video por video.** Antes de usar uno, pedirle aprobación mostrando título, canal, link y para qué se usaría. Si Nick mismo comparte el video, cuenta como aprobado. Al usarlo:
  - Citar canal, título, año, URL y el minuto exacto del dato o la imagen.
  - Perplexity Computer no puede ver el video: solo puede usar lo verificable (transcripción, descripción, o lo que Nick confirme que dice). Si no se puede verificar, Nick confirma el dato antes de que entre.
  - Si el dato del video contradice una fuente indexada, gana la fuente indexada y se le avisa a Nick.

**Fuentes NO válidas como respaldo de un dato**: Wikipedia, blogs, foros, páginas comerciales, videos sin aprobación de Nick, resúmenes de otras IAs y el conocimiento propio de Perplexity Computer "de memoria". Sirven para orientarse y encontrar la fuente real, nunca como cita.

**Cómo trabajar**
- Cada dato, número, ecuación, propiedad de material, afirmación y figura tiene que poder rastrearse a una fuente concreta (autor, año, DOI o libro + página/figura/tabla, o video + minuto).
- Verificar cada referencia abriéndola: el DOI resuelve, el artículo existe, autores, año y título coinciden, y el dato está realmente ahí. Nunca escribir una referencia de memoria.
- Si solo se pudo leer el abstract, solo se usa lo que dice el abstract, y se avisa.
- Si no hay fuente válida para algo: **no se incluye**. Se le dice a Nick en una línea qué no se pudo verificar.
- No completar, redondear ni "suponer valores típicos". Si un dato falta, se marca como faltante.
- Los cálculos propios se hacen con código o Excel a partir de datos con fuente, mostrando de dónde salió cada dato de entrada.

**Tabla de trazabilidad** (se entrega con la presentación): slide → dato o figura → fuente exacta → DOI/página/minuto → verificado (sí/no). Ningún "no" queda en la versión final sin que Nick lo sepa.

Referencias en el formato que pida el curso (IEEE por defecto en ingeniería), con DOI cuando exista.

## 1. Antes de empezar

Preguntar en un solo mensaje solo lo que falte:
- Tema, curso, duración, idioma de slides y de exposición.
- Rúbrica o enunciado (manda sobre la estructura).
- Plantilla o formato exigido (.pptx, PDF).
- **Fuentes**: PDFs, papers, libros, normas, videos, fotos propias, capturas de CAD o del laboratorio.

Si las fuentes no alcanzan, buscar artículos indexados y mostrarle a Nick la lista (título, autores, año, revista, DOI, para qué sirve) antes de usarlos.

Luego mostrar el índice: una línea por slide, qué imagen lleva y de qué fuente sale, y el tiempo por bloque. Construir cuando Nick lo apruebe.

## 2. Visuales: de las fuentes, no de la IA

Nunca ilustraciones, íconos decorativos ni diagramas inventados para rellenar.

- **PDFs**: extraer las imágenes embebidas (`pdfimages -png`) o, si la figura es vectorial, rasterizar la página (`pdftoppm -r 300`) y recortar solo la figura (Pillow). Revisar cada recorte visualmente.
- **Fotos de Nick** (laboratorio, piezas, impresiones 3D, CAD): protagonistas. Recortar y enderezar, sin alterar el contenido.
- **Videos aprobados**: si Nick pasa capturas, usarlas con fuente y minuto.
- **Gráficas**: con matplotlib a partir de datos con fuente, estilo limpio, ejes con unidades, fuente de los datos debajo.
- **Diagramas propios** solo si no existe la figura en las fuentes y explica algo concreto (proceso, diagrama de cuerpo libre). Simples y basados en la fuente.

Cada imagen ajena lleva su fuente abajo ("Fuente: Autor et al., 2021, fig. 4"). Si no hay buena imagen: no inventar; avisar qué foto o figura falta y dejar un marcador claro.

## 3. Slides livianas

- Una idea por slide. La imagen ocupa la mayor parte (60–80 %).
- Máximo ~15–20 palabras por slide. Sin párrafos, sin listas de más de 3 puntos.
- Título corto que dice la idea, no el nombre del tema. Una pregunta también sirve como título (ver sección 5).
- Un número importante va grande, solo.
- Solo ecuaciones clave, grandes, con variables señaladas. Deducciones largas al anexo o al documento escrito.
- Ejemplo resuelto repartido en varias slides (datos → fórmula → resultado → qué significa).
- Lo que no cabe va a las notas o a slides de anexo.

Prueba rápida: si Nick tendría que leer la slide para sustentarla, tiene demasiado texto.

## 4. Que se vea bien

- Respetar la plantilla de la universidad si la hay. Si no: fondo limpio, fuente sans moderna, un color de acento sacado de las fotos, mucho espacio vacío.
- Variar layouts: imagen a pantalla completa con título, imagen + 1 frase, comparación lado a lado, número grande. No repetir "título + viñetas".
- Slides de cambio de sección con una foto fuerte.
- Texto legible desde el fondo del salón (≥ 24 pt). Número de slide visible.

## 5. Que suene a Nick

Todo texto que Nick va a decir o firmar (títulos, frases en slides, notas, respuestas a
preguntas, documento escrito) pasa por la skill `voz-nick`: ahí está su perfil de escritura
y la revisión automática. No repitas aquí sus reglas.

Lo propio de las presentaciones:
- En slides, texto mínimo: una pregunta o una frase corta. Una pregunta sirve como título.
- En notas, su voz completa: primera persona, preguntas que abren cada idea.
- Sonar natural nunca justifica cambiar el sentido técnico de lo que dice la fuente.

## 6. Notas para sustentar

- Por slide: 2–4 frases en la voz de Nick, tiempo aproximado y transición (idealmente una pregunta que abre la siguiente slide).
- Aparte, 8–10 preguntas probables del profesor con respuesta corta y su fuente. Las difíciles tienen slide de anexo.

## 7. Formato

- Por defecto: archivo .pptx hecho con la skill `office` (si hay plantilla .pptx de la universidad, se construye sobre ella). Si piden PDF, se exporta el mismo .pptx a PDF.
- Si hay documento escrito, usa las mismas figuras, números y referencias.

## 8. Revisión antes de entregar

Mirar la presentación slide por slide, renderizando el .pptx a imágenes (skill `office`). Para trabajos importantes, la verificación de fuentes la hace un agente aparte que no participó en hacer la presentación.

- [ ] Cada dato, ecuación y figura está en la tabla de trazabilidad con fuente válida verificada.
- [ ] Todos los DOI resuelven y coinciden con la referencia.
- [ ] Ningún video usado sin aprobación de Nick; todos con minuto citado.
- [ ] Ninguna imagen inventada o decorativa; todas con fuente.
- [ ] Ninguna slide con más de ~20 palabras ni párrafos; layouts variados.
- [ ] Textos y notas pasaron por `voz-nick` (revisión automática sin hallazgos).
- [ ] Números calculados con código/Excel, unidades correctas.
- [ ] Cumple la rúbrica y el tiempo.

Al entregar: comparte con Nick la presentación, las notas, las preguntas y la tabla de trazabilidad, más una línea con lo que falta o no se pudo verificar.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.
