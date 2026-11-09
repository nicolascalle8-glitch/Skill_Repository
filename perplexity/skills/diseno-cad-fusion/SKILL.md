---
name: diseno-cad-fusion
description: "Diseña desde cero piezas y prototipos de Nick en Fusion 360 con un script de la API de Fusion en Python: enmarca, define parámetros, modela por componentes, revisa movimiento e imprimibilidad y exporta STL. Úsala cuando Nick pida modelar, diseñar o prototipar algo en Fusion. No copia piezas físicas (ingenieria-inversa-cad) ni aprueba imprimir (puerta-fabricacion)."
---

# Diseño CAD en Fusion 360

Para piezas y prototipos nuevos que Nick quiere ver, presentar o imprimir. No es para copiar una pieza física (eso es `ingenieria-inversa-cad`) ni para calcular cargas (`calculo-trazable`). Antes de imprimir, siempre pasa por `puerta-fabricacion`.

Español simple y directo con Nick. Nada de datos inventados: lo que no se sabe es un parámetro marcado "por calibrar".

## 1. Enmarcar (antes de escribir el script)

En un solo mensaje, pregunta a Nick solo lo que falte:
- **Para qué es:** mostrar (maqueta), probar el mecanismo o usar de verdad. Cambia el nivel de detalle.
- **Plazo:** si es para mañana, se diseña lo mínimo que se imprime en una noche.
- **Qué se imprime y qué se compra:** piezas comerciales (frascos, tornillos, rodamientos, ejes). Lo que toque alimentos o piel en uso real no se imprime: se compra certificado.
- **Impresora y cama:** Nick tiene Bambu Lab X2D, Prusa MK3S+ y QIDI X-Pro; confirma cuál y su volumen.
- **Material:** PLA para maquetas rápidas, PETG si hay esfuerzo, humedad o calor moderado.

## 2. Concepto

Propón máximo dos conceptos en texto corto (cómo funciona, piezas, qué se compra) y deja que Nick elija. Para mecanismos, explica el movimiento en una frase (ej. "la manivela gira un rotor de 6 cámaras; cada sexto de vuelta suelta una porción").

## 3. Parámetros de usuario

Todo lo que define el tamaño va en Parámetros de usuario de Fusion (el script los crea con `userParameters.add`), con nombre, unidad y comentario. Ponlos también en un bloque al inicio del script para que Nick los vea y los cambie:
- Medidas de piezas compradas: medidas por Nick, o "por calibrar".
- Holguras de impresión: valor de partida 0,3 mm por lado para ajuste libre y 0,1 mm para ajuste a presión. Son un supuesto; se confirman con una probeta de tolerancias.
- Volúmenes o capacidades que dependen del producto real (ej. volumen de una porción): se miden, no se suponen. Se deja la instrucción de cómo medirlo.

## 4. Modelar

- Diseño nuevo, nunca sobre un archivo de Nick sin permiso. Nombre: `<proyecto>_v1`.
- Un componente por pieza física; bocetos totalmente definidos con los parámetros.
- Uniones (joints) para lo que se mueve, y revisar que gire o deslice sin interferir.
- Pensar la impresión mientras se modela: base plana, voladizos de 45° o menos, chaflanes en vez de redondeos abajo, paredes de al menos 2 perímetros.
- Piezas que no caben en la cama: partir con encajes o tornillos, o bajar la escala si es maqueta (y decirlo).

## 5. Revisar

- Analizar interferencias y mover las uniones.
- Tamaño de cada pieza contra la cama de la impresora elegida.
- Lista de compras (piezas comerciales) y lista de piezas a imprimir con orientación sugerida.

## 6. Entregar

- STL o 3MF por pieza, con nombre claro, en la carpeta del proyecto (el script los exporta al correrlo en Fusion).
- Capturas del ensamble (vista general, explosionada si ayuda) para presentar; el script puede guardarlas con `viewport.saveAsImageFile`, o Nick las toma y las comparte.
- Tabla corta: pieza, material, orientación, tiempo estimado (del slicer, no adivinado), qué falta calibrar.
- Luego `puerta-fabricacion`.

## Herramientas

En Perplexity no hay conector de Fusion: no se puede leer ni tocar un diseño abierto. Todo se hace con un script de la API de Fusion en Python.

1. Escribe el script: carpeta `<proyecto>_v1/` con `<proyecto>_v1.py` y su función `run(context)`. Crea un diseño nuevo, los Parámetros de usuario, un componente por pieza, las uniones y la exportación de STL o 3MF. Comenta en español qué arma cada bloque.
2. Revisa que no tenga errores de sintaxis (`python3 -m py_compile`); el módulo `adsk` solo existe dentro de Fusion, así que no se puede probar completo aquí. Dilo.
3. Entrega:
   - **Si el Mac de Nick está conectado:** guarda la carpeta del script en su computador, en la carpeta del proyecto (pregunta a Nick cuál si no se sabe).
   - **Si no:** comparte el archivo con Nick.
4. Explica cómo correrlo: en Fusion, Utilidades → Complementos → Scripts y complementos → "+" → script desde mi computador, elegir la carpeta y Ejecutar.
5. Si Fusion da un error, pide a Nick el mensaje completo y corrige el script; no adivines qué pasó.

## Límites

- No valida resistencia; si hay carga real, `calculo-trazable` primero.
- No aprueba imprimir: eso es `puerta-fabricacion`.
- No inventa medidas de piezas compradas ni propiedades de materiales.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.
