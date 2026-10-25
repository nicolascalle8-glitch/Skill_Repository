# Incertidumbres: guía rápida

Base: *Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008, "GUM").
https://www.bipm.org/en/doi/10.59161/JCGM100-2008E
Si el curso usa otro criterio (por ejemplo, resolución/2 para instrumentos análogos), manda
el del curso: pregúntale a ella cuál usan y anótalo en el CONTEXTO de la materia.

## Tipo A (estadística)
Con n repeticiones x₁…xₙ:
- media x̄
- desviación estándar s = √(Σ(xᵢ − x̄)² / (n − 1))
- incertidumbre de la media u_A = s / √n

## Tipo B (instrumento y otras)
- Distribución rectangular de ancho total a (por ejemplo, resolución digital a = 1 dígito):
  u_B = a / √12  (equivale a (a/2)/√3).
- Instrumento análogo, lectura a media división: depende del criterio del curso.
- Multímetros: especificación del fabricante, típicamente ±(% de lectura + dígitos);
  se trata como rectangular: u_B = semiancho / √3.

## Combinada
u_c = √(u_A² + u_B²)

## Propagación (primer orden, variables no correlacionadas)
Para f(x, y, …): u_f² = (∂f/∂x)² u_x² + (∂f/∂y)² u_y² + …
- Producto/cociente: (u_f/f)² = Σ (n_i u_i / x_i)² para f = Π x_i^{n_i}.
- Si hay correlación, agregar 2 (∂f/∂x)(∂f/∂y) cov(x, y).
- Si f es muy no lineal o u_x es grande comparada con x, comparar con Monte Carlo
  (`scripts/incertidumbre.py --mc`).

## Expandida
U = k · u_c, con k = 2 para ~95 % (si los grados de libertad son suficientes). Decir k.

## Redondeo
- u con 1 cifra significativa (2 si la primera es 1 o 2, o si el curso lo pide).
- El valor se redondea a la misma posición decimal que u.
- Ejemplo: g = 9.7862 ± 0.0347 m/s² → g = 9.79 ± 0.03 m/s².

## Comparación
Discrepancia en sigmas: z = |x − x_ref| / √(u_x² + u_ref²)
- z < 2: compatibles. 2 ≤ z < 3: tensión, discutir. z ≥ 3: incompatibles, buscar error sistemático.
- El error porcentual se puede dar, pero no reemplaza a z.
