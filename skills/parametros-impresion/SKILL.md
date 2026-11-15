---
name: parametros-impresion
description: "Ajusta y aplica directamente en Bambu Studio (X2D) y Creality Print (K2 Pro) los parámetros de laminado de una pieza de Nick según el material, la geometría en Fusion y sus presets, y mejora con su retroalimentación. Úsala al laminar, preparar placas, o si una impresión salió mal o tardó demasiado."
---

# Parámetros de impresión (con mejora continua)

Nick dice el material y la pieza. Tú lees la geometría en Fusion, eliges impresora, orientación y parámetros partiendo de sus presets, **los aplicas tú mismo en los dos slicers de su PC** (Bambu Studio para la X2D y Creality Print para la K2 Pro, con computer use), laminas y le entregas una tabla clara con tiempos y gramos reales. Después de imprimir, él te da retroalimentación (foto o comentario); tú la conviertes en un ajuste concreto y la anotas en la bitácora. Así cada pieza sale mejor que la anterior.

Español simple y directo con Nick (o en inglés si él escribe en inglés). Listas y tablas, sin advertencias genéricas.

Antes de imprimir algo con carga o para un cliente, pasa por `puerta-fabricacion`. Esta skill decide **cómo** laminar, no **si** la pieza está lista.

## 0. Arranque: lee la bitácora

Antes de proponer nada, lee el doc del proyecto `claude/bitacora-parametros-impresion.md` (herramienta Projects, `project_read`). Ahí están las reglas ya confirmadas con piezas reales. Lo que diga la bitácora manda sobre los valores por defecto de esta skill, porque viene de impresiones de verdad en sus máquinas.

## 1. Lo que hay que saber de cada pieza

Sácalo del diseño en Fusion (conector de Fusion, script de solo lectura) o del STL:
- Tamaño de cada cuerpo (bounding box) y si cabe en la cama.
- Espesor mínimo de pared. Con paredes de ~1,2 mm, el número de bucles casi no importa: Arachne mete 2–3 líneas de todos modos.
- Cuántos compartimentos o islas hay por capa. Muchas islas significan muchos saltos (retracción + Z-hop), y eso es lo que más tiempo se come.
- La cara plana más grande (para apoyarla en la cama), los voladizos de más de 45° y los puentes largos.
- Partes que en la orientación de impresión arrancan en el aire: bisagras y salientes en piezas que se imprimen boca abajo. Si el slicer avisa "floating regions", no se ignora: se corrige el diseño o la orientación.
- Paredes largas y planas (>150 mm): riesgo de ringing o VFA a velocidades altas.

## 2. Las impresoras

| | Bambu Lab X2D | Creality K2 Pro |
|---|---|---|
| Volumen | 256 × 256 × 260 mm (boquilla principal) | 300 × 300 × 300 mm |
| Cama | PEI texturizada | PEI suave |
| Límites | — | 600 mm/s, 20 000 mm/s² |
| Particularidades | Dos boquillas: la pieza va en la principal (M1) y las velocidades se ajustan en la pestaña M1. AMS: revisa qué rollo hay en cada slot. | Con calibración de cama activa, deja libre la esquina inferior izquierda. Flow/PA: una vez por filamento, guardado en el perfil. |

Colores: revisa qué color tiene cargado cada impresora antes de repartir placas. Si Nick pide un color, la pieza va donde esté ese color.

## 3. Los presets de Nick (punto de partida)

Materiales B2B: Elegoo Rapid PLA+ y Elegoo Rapid PET-G.

**Material por defecto: PLA.** Prototipos, maquetas y piezas sin carga real van en PLA aunque tengan engranajes o encajes. PETG solo si Nick lo pide o si la pieza va a tener carga sostenida, calor (>50 °C) o humedad; en ese caso, propónlo y espera su sí antes de laminar.

**Presets que usa hoy en cada slicer:**
- X2D (Bambu Studio): proceso "Rapid Pla +"; filamento "Bambu PLA Basic" (Nick lo usa por comodidad). Pendiente: crear un preset de filamento propio para que siempre sea igual. Hasta entonces, usa "Bambu PLA Basic" y dilo en la entrega.
- K2 Pro (Creality Print): proceso "Rapid Pla +"; filamento "K2 Pro - Rapid PLA+ B2B".

| | X2D PLA+ | X2D PET-G | K2 PLA+ | K2 PET-G |
|---|---|---|---|---|
| Boquilla | 225 / 230 °C | 245 / 250 °C | 225 °C | 250 °C |
| Cama | 60 °C | 75 °C | 60 °C | 75 °C |
| Ventilador pieza | 80–100 % | 20–50 % | 100 % | 40 % |
| Aux / cámara | 70 % | 0 % | — | 0 % |
| Puerta | Abierta | Cerrada | Abierta | Cerrada |
| Paredes | 4 bucles Arachne | 4 Arachne | 4 Arachne | 4 Arachne |
| Capas sup/inf | 5 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| Relleno | Giroide 15 % | Giroide 15 % | Giroide 15 % | Giroide 15 % |
| Vel. ext / int / relleno | 200 / 300 / 270 | 150 / 250 / 250 | 200 / 300 / 270 | 150 / 250 / 250 |
| Primera capa | 40 mm/s | 35 mm/s | 40 mm/s | 35 mm/s |
| Small perimeter threshold | 5 mm | 5 mm | 5 mm | 5 mm |
| Z soporte | 0,20 (concéntrico) | 0,25 | 0,20 | 0,25 |
| Brim | Auto 5 mm, gap 0,1 | Exterior 5 mm, gap 0,1 | Auto 5 mm, gap 0,1 | 5 mm, gap 0 |
| Torre de purga | — | — | Apagada | Apagada |

Reglas de Nick que no se rompen:
- Giroide, nunca rejilla (grid), a altas velocidades: con la rejilla el cabezal choca al cruzar líneas.
- Soportes normales, no de árbol, en bases planas estructurales.
- Orientación: la cara plana más ancha apoyada ("Lay on face"), nada de diagonales.
- Z de soporte 0,25 en PETG: a 0,20 se pega demasiado y rompe la pieza al quitarlo.
- PETG/ABS en la K2: pegamento como capa de sacrificio para no arrancar el PEI suave.
- No subir la altura de capa para ganar tiempo salvo que Nick lo pida.

## 4. Cómo ajustar según la geometría

Piensa qué limita esta pieza en concreto y ajusta eso. Subir velocidades no sirve si el cuello de botella es otro.

- **Muchas paredes cortas o compartimentos** (organizadores, Gridfinity): mandan la aceleración, las esquinas y los saltos. En la K2 funcionó: aceleración de pared exterior 8000, interior 12 000, normal 15 000 y viaje 20 000 mm/s²; viaje a 600 mm/s; jerk exterior/interior 10/12; Z-hop en 0 o solo al cruzar paredes. Las velocidades de pared del preset se dejan igual.
- **Paredes largas y planas**: el riesgo es el ringing o el VFA. Considera bajar la velocidad de pared exterior (150) o su aceleración, sobre todo si la cara es visible.
- **Piezas boca abajo con salientes** (tapas, bisagras): revisa que nada arranque en el aire. Mejor corregir el diseño que poner soportes.
- **Piezas con encajes** (bisagras, pines, tapas): las holguras son del diseño; si hace falta compensar, usa X-Y hole/contour compensation y anótalo.
- **Varias piezas**: reparte entre las dos impresoras para que terminen a tiempos parecidos, respetando colores.

## 5. Aplicar en los dos slicers (siempre)

El trabajo no termina en una tabla: preparas y laminas las placas en las dos máquinas. Solo te saltas este paso si Nick lo pide o si el computador no responde; en ese caso, dilo y entrega la tabla.

**Preparar los archivos**
1. Con el conector de Fusion, exporta un STL por cuerpo a `Documents\<proyecto>_STL` en el PC de Nick (script con `exportManager`, refinamiento alto, sin los componentes `REF_`). Si un componente tiene varios cuerpos, combínalos antes de exportar o se pierden partes.
2. Si cambias el diseño después, re-exporta y usa "Reload from disk" en el slicer para no perder orientación ni posición.

**Acceso al computador**
- Carga la skill `computer-use` y todas las herramientas de computer use en un solo ToolSearch.
- Pide acceso a "Bambu Studio" y "Creality Print 7.2" (resolve y luego request). El acceso caduca tras 30 min sin actividad: si falla, vuelve a pedirlo.
- Nick tiene dos monitores: usa `switch_display` y toma captura para encontrar cada ventana. Al terminar el turno, libera el lock (`computer_release_lock`).

**Flujo en cada slicer**
1. Proyecto nuevo (Bambu: "Create new project"; Creality: File → New Project). Si pregunta por ajustes modificados, transfiérelos; no descartes nada de Nick.
2. Importa con Ctrl+I. En el diálogo de Windows: escribe la ruta de la carpeta y da Enter como acción aparte; luego los nombres entre comillas (`"a.stl" "b.stl"`) y Enter. Al aviso "object with multiple parts", responde **No**.
3. Orienta: "Lay on face" (F) haciendo clic en la cara que va a la cama, o la herramienta Rotar con valores exactos.
4. Organiza: arrange (A) y luego corrige a mano con la herramienta Mover (coordenadas X/Y del centro; la cama tiene el origen abajo a la izquierda). Duplica con Clone (Ctrl+K o clic derecho). En Creality, la placa 2 empieza en X = +360 mm.
5. Proceso: parte **siempre del preset de proceso de Nick** ("Rapid Pla +") en las dos impresoras. Nunca lo cambies por un perfil de fábrica (por ejemplo, "0.20mm Standard @BBL X2D"): esos traen 2 paredes y otros valores, y así las placas quedan distintas sin razón. Sobre ese preset, aplica solo los ajustes de la pieza, pestaña por pestaña (Quality, Strength, Speed, Support, Others/Multifilament). En Bambu, las velocidades van en la pestaña de la boquilla principal (M1).
   - **Misma regla en las dos placas:** si el material es el mismo, las paredes, las capas superior e inferior, el relleno y los soportes también. Si una placa necesita algo distinto por la geometría, anótalo en la tabla de entrega con el porqué.
6. Filamento: confirma el slot y el color. En Creality, el editor está en ⋯ → Edit; guarda como preset de usuario con nombre claro. En Bambu Studio el editor de filamento es difícil de abrir desde la interfaz: si no lo logras, di claramente en la entrega qué valores quedaron de fábrica.
7. Antes de laminar, compara las dos placas: nombre del preset de proceso y de filamento, paredes, relleno, soportes y material. Si algo difiere sin una razón de la pieza, corrígelo.
8. Slice all y lee "All Plates Stats" (tiempo y gramos por placa). Revisa en la vista previa la esquina de calibración de la K2 y cualquier aviso del slicer ("floating regions", fuera de la placa, colisiones).
9. No envíes la impresión ni guardes el proyecto: eso lo decide Nick.

**Cuidados**
- Trabaja en un proyecto nuevo. No metas piezas en un proyecto abierto de Nick ni guardes sus proyectos sin que lo pida.
- No uses "abrir aplicación" para volver a un slicer que ya está abierto, porque abre otra instancia vacía. Busca la ventana existente (otro monitor, o minimiza la de encima). Si hay varias instancias, identifica la tuya por el título del proyecto antes de tocar nada.
- En Creality Print, haz clic dentro del campo antes de escribir números. Si el foco queda en la vista 3D, los dígitos y letras son atajos (1 = vista superior, Z = fuzzy skin, R = rotar, M = mover) y mueven o giran piezas.
- Si una impresora está imprimiendo, no toques su pestaña Device ni el trabajo en curso.
- Cada 2–3 acciones, confirma con una captura o un zoom que el cambio quedó: a veces los campos no aceptan el valor, y la lista de objetos se reordena al mover piezas entre placas.
- Revisa que el perfil de filamento coincida con el rollo real (marca, tipo y color del slot). No dejes valores de fábrica en silencio.

## 6. Entrega

Siempre en este orden:

```
Pieza · material · impresora
| Parámetro | Preset | Esta pieza | Por qué |
(solo lo que cambia respecto al preset)

Placas: placa → piezas → tiempo → gramos → color/slot → preset de proceso → preset de filamento → paredes / relleno
(si las dos placas no tienen el mismo proceso, decir por qué)
Aplicado en Bambu Studio: sí / parcial (qué falta)
Aplicado en Creality Print: sí / parcial (qué falta)
Riesgos a vigilar: 1–3 cosas concretas que mirar en la primera capa o en la pieza
Retroalimentación que necesito: qué mirar o fotografiar cuando termine
```

## 7. Ciclo de mejora (la parte más importante)

Cuando Nick dé retroalimentación de una pieza impresa:

1. **Diagnostica antes de cambiar.** Si es visual, pide una foto de cerca, en ángulo y con luz lateral. Usa esta guía:

| Lo que se ve | Causa probable | Ajuste |
|---|---|---|
| Ondas verticales que salen de una esquina y se apagan | Ringing | Bajar aceleración o velocidad de pared exterior |
| Líneas verticales finas y parejas en toda la pared | VFA | Cambiar velocidad de pared exterior (probar 150 o 250) |
| Bandas horizontales cada pocas capas | Eje Z / temperatura | Revisar el patrón; suele ser mecánico |
| Superficie hinchada, esquinas redondas, gotas | Sobreextrusión | Flow ratio / PA del filamento; perfil correcto |
| Huecos entre líneas, paredes débiles | Subextrusión | Flow, temperatura, humedad del filamento |
| Hilos | Retracción / temperatura / humedad | Secar, bajar 5 °C, ajustar retracción |
| Esquinas levantadas | Warping | Brim, temperatura de cama, cámara, pegamento |
| No encaja / muy flojo | Holgura del diseño o compensación XY | Corregir en Fusion o compensación XY |
| Tardó demasiado | Ver sección 4: qué limita | Aceleración, saltos, reparto de placas |

2. **Cambia una cosa a la vez**, o dos si están claramente ligadas, para saber qué funcionó. Aplícala en el slicer que corresponda y vuelve a laminar.
3. **Anota en la bitácora** (`project_read` y luego `project_write` del doc completo): fecha, pieza, material, impresora, síntoma, ajuste y resultado cuando Nick lo confirme.
4. **Si un ajuste se confirma dos veces**, súbelo a "Reglas aprendidas" de la bitácora. Si contradice un preset de Nick, propónselo; no cambies sus presets por tu cuenta.

La bitácora es la memoria de esta skill: sin ella, cada pieza empieza desde cero.

## Límites

- No valida resistencia ni decide si la pieza está lista para fabricar (eso es `puerta-fabricacion`).
- No diseña la pieza (eso es `diseno-cad-fusion`), aunque puede señalar qué cambiar en el diseño.
- No envía impresiones ni guarda proyectos sin que Nick lo pida. Puede guardar presets de usuario nuevos con nombre claro, pero nunca sobrescribe los de Nick.
- Usa el PC de Nick solo dentro de Fusion, Bambu Studio y Creality Print.