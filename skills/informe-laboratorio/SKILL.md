---
name: informe-laboratorio
description: 'Analiza datos de laboratorio de física y arma el informe de la estudiante de Física de la EIA (novia de Nick): incertidumbres tipo A y B, propagación, ajustes con χ² y residuos, gráficas con barras de error, comparación con el valor teórico y redacción del informe (formato artículo, Word o LaTeX). Úsala cuando ella mande datos medidos, una tabla, una guía de laboratorio, pregunte por incertidumbre, error, ajuste lineal, regresión, gráficas o "tengo que entregar el informe de…", aunque no nombre la skill. No es para ejercicios de lápiz y papel (ejercicios-fisica) ni simulaciones (simulacion-fisica).'
---

# Informes de laboratorio

Convertir sus medidas en un resultado con incertidumbre honesta y un informe que ella
pueda defender. Sigue `shared/CONTRATO-OPERATIVO.md`, sobre todo la sección 4.

## Antes de empezar

Pide en un solo mensaje lo que falte:
- **Guía del laboratorio** o enunciado (objetivo, montaje, qué hay que reportar).
- **Datos crudos** (Excel, CSV, foto de la tabla). Si viene en foto, transcribe y pide que
  confirme antes de calcular.
- **Instrumentos** con su resolución (regla 1 mm, cronómetro 0.01 s, multímetro y su
  especificación). Sin esto no hay incertidumbre tipo B.
- **Formato del informe** (plantilla, artículo IEEE/APS, Word, LaTeX, largo, idioma) y la
  rúbrica si existe.

## Cómo se hace

1. **Datos a archivo.** Pasa los datos a CSV en `proyectos/<materia>/archivos/` con
   columnas, unidades e incertidumbres. Los crudos no se modifican nunca.
2. **Incertidumbres de cada medida** (ver `references/incertidumbres.md`):
   - Tipo A: desviación estándar de la media si hay repeticiones.
   - Tipo B: resolución/√12 (digital, distribución rectangular) o resolución/2·√3 según
     el criterio del curso; especificación del fabricante para multímetros.
   - Combinada: √(uA² + uB²). Di qué criterio usaste.
3. **Magnitudes derivadas**: propaga con `scripts/incertidumbre.py` (derivadas parciales,
   y Monte Carlo para comparar cuando la función es no lineal).
4. **Ajuste** si hay relación entre variables: `scripts/ajuste.py`.
   - Linealiza solo si el curso lo pide; si no, ajusta el modelo no lineal directo.
   - Reporta parámetros ± incertidumbre, χ²/ν y la gráfica de residuos.
   - χ²/ν ≫ 1: modelo o incertidumbres subestimadas. χ²/ν ≪ 1: incertidumbres
     sobreestimadas. Dilo en el análisis, no lo escondas.
5. **Comparar con la teoría**: discrepancia en sigmas, |x − x_ref| / √(u_x² + u_ref²).
   Menor que 2: compatible. Valor de referencia con fuente (CODATA, libro, guía).
6. **Gráficas**: ejes con magnitud y unidad, barras de error, datos como puntos, modelo
   como línea, leyenda solo si hay más de una serie. Exporta PNG a 300 dpi o PDF.
7. **Informe**: estructura en `references/estructura-informe.md`. El texto pasa por
   `voz-propia` (suena a ella, no a IA).

## Datos raros

Si un punto se ve fuera: no se borra. Revisa si hay error de transcripción, de unidad o
de montaje, díselo, y propón (como PROPUESTA) excluirlo con razón física. El informe
reporta el resultado con y sin el punto si ella decide excluirlo.

## Salida

- CSV limpio + script o notebook que reproduce todo el análisis.
- Gráficas (PNG/PDF).
- Tabla de resultados: magnitud, valor ± u, unidad, cómo se obtuvo.
- Informe en el formato pedido (Docs artifact por defecto; .docx o .tex si lo piden).

## Verificación

- [ ] Los scripts corren de principio a fin y reproducen las gráficas.
- [ ] Toda medida y resultado con incertidumbre, bien redondeada.
- [ ] Unidades en tablas, ejes y resultados.
- [ ] Discrepancia con la teoría en sigmas, con la fuente del valor de referencia.
- [ ] Ningún dato crudo modificado o descartado sin su aprobación.
- [ ] El análisis explica las fuentes de error reales del montaje, no una lista genérica.

## Límites

- No inventa datos para "completar" una tabla ni ajusta incertidumbres para que χ² dé bonito.
- Teoría de fondo larga o ejercicio previo al laboratorio → `ejercicios-fisica`.
- Simular el experimento para comparar → `simulacion-fisica`.
