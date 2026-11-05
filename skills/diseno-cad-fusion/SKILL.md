---
name: diseno-cad-fusion
description: "Diseña desde cero piezas y prototipos de Nick en Fusion 360 (conector de Fusion o script de la API): enmarca, define parámetros, modela por componentes, revisa movimiento e imprimibilidad y exporta STL. Úsala cuando Nick pida modelar, diseñar o prototipar algo en Fusion."
---

# Diseño CAD en Fusion 360

Para piezas y prototipos nuevos que Nick quiere ver, presentar o imprimir. No es para copiar una pieza física (eso es `ingenieria-inversa-cad`) ni para calcular cargas (`calculo-trazable`). Antes de imprimir, siempre pasa por `puerta-fabricacion`.

Español simple y directo con Nick. Nada de datos inventados: lo que no se sabe es un parámetro marcado "por calibrar".

## 1. Enmarcar (antes de abrir Fusion)

En un solo mensaje, pregunta solo lo que falte:
- **Para qué es:** mostrar (maqueta), probar el mecanismo o usar de verdad. Cambia el nivel de detalle.
- **Plazo:** si es para mañana, se diseña lo mínimo que se imprime en una noche.
- **Qué se imprime y qué se compra:** piezas comerciales (frascos, tornillos, rodamientos, ejes). Lo que toque alimentos o piel en uso real no se imprime: se compra certificado.
- **Impresora y cama:** Nick tiene Bambu Lab X2D, Prusa MK3S+ y QIDI X-Pro; confirma cuál y su volumen.
- **Material:** PLA para maquetas rápidas, PETG si hay esfuerzo, humedad o calor moderado.

## 2. Concepto

Propón máximo dos conceptos en texto corto (cómo funciona, piezas, qué se compra) y deja que Nick elija. Para mecanismos, explica el movimiento en una frase (ej. "la manivela gira un rotor de 6 cámaras; cada sexto de vuelta suelta una porción").

## 3. Parámetros de usuario

Todo lo que define el tamaño va en Parámetros de usuario de Fusion, con nombre, unidad y comentario:
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

- STL o 3MF por pieza, con nombre claro, en la carpeta del proyecto.
- Capturas del ensamble (vista general, explosionada si ayuda) para presentar.
- Tabla corta: pieza, material, orientación, tiempo estimado (del slicer, no adivinado), qué falta calibrar.
- Luego `puerta-fabricacion`.

## Herramientas

- **Conector de Fusion** (`mcp__remote-devices__Autodesk_Fusion__*`): necesita Fusion abierto en el computador de Nick y la app de escritorio de Claude conectada. Lee el diseño antes de cambiarlo.
- **Si el conector no está:** escribir un script de la API de Fusion en Python (Utilidades → Scripts y complementos) que arme el modelo con los parámetros, guardarlo en la carpeta del proyecto y explicar cómo correrlo.

## Límites

- No valida resistencia; si hay carga real, `calculo-trazable` primero.
- No aprueba imprimir: eso es `puerta-fabricacion`.
- No inventa medidas de piezas compradas ni propiedades de materiales.