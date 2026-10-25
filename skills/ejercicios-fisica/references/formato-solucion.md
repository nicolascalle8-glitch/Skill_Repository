# Formato de solución completa

```markdown
## Problema
(enunciado corto o transcrito)

## Situación física
Qué pasa, en 2–3 frases. Diagrama si ayuda.

## Datos y supuestos
- m = 2.0 kg [Dato]
- g = 9.80665 m/s² [Constante — CODATA/NIST, valor estándar]
- Sin fricción con el aire [Supuesto — v pequeña; deja de valer si v > ~10 m/s]

## Planteamiento
Principio: conservación de la energía mecánica (no hay fuerzas no conservativas).
Ecuación: (1) ½ m v² + m g h = constante

## Desarrollo
Pasos en letras, uno por línea, diciendo qué se hizo.
Resultado simbólico: v = √(2 g h)

## Números
v = √(2 · 9.81 m/s² · 5.0 m) = 9.9 m/s [Calculado]

## Verificación
- Unidades: √(m/s² · m) = m/s ✔
- Caso límite: h → 0 ⇒ v → 0 ✔
- No depende de m: coherente con caída libre ✔

## Qué significa
Una frase de interpretación física.

## Para ti
Una pregunta de control: "¿Qué cambia si la rampa tiene fricción μ?"
```

Notas:
- Ecuaciones en LaTeX (`$...$`) si ella va a pasar la solución a un documento.
- Cifras significativas según los datos del enunciado.
- Si usas Python para verificar, muestra el código corto que corriste.
