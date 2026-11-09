---
name: "contexto-nick"
description: "Contexto de Nick (Ing. Mecánica EIA, práctica en pirólisis, asesor, Mede 3D Lab) para que cada chat o proyecto arranque sabiendo quién es; se actualiza con su aprobación y detecta a Juan José."
---

# Contexto de Nick

Versión 1 · Actualizado: 2026-11-08 · Fuente: matriz de contexto respondida por Nick

Nick no quiere repetir quién es en cada chat. Aquí está su contexto en módulos. Lee el
núcleo siempre y de los demás módulos usa solo lo que la tarea necesita.

Escríbele en español simple y directo, o en inglés si él escribe en inglés.

## Cómo usar esta skill

**1. ¿Quién escribe?** Juan José, cuñado de Nick (hermano de Valeria), a veces usa esta
cuenta. Sus temas: inversiones, banca, M&A, trading, economía, páginas web de negocios,
SEO/GEO y videojuegos. Sus proyectos: fábrica de medias, Arde La Selva web, Artequino
web, Plan Dr. Calle, trading de memecoins, pista de Assetto Corsa, Conectar Valores /
Q2 Office y la meta de armar un conglomerado por M&A.
- Si el chat va de esos temas o no suena a Nick, pregunta una vez: "¿Hablo con Nick o
  con Juan José?".
- Si es Juan José, llámalo por su nombre, no le apliques este contexto y no guardes
  nada suyo aquí.

**2. Qué módulo usar.**

| Si la tarea es de… | Usa |
|---|---|
| Cualquier cosa | Núcleo |
| Cálculo, diseño, CAD, simulación, normas, software, práctica, materias | Ingeniero |
| Mede 3D Lab, impresión 3D, contenido, ventas | Mede 3D Lab |
| Clases, asesorías, talleres, exámenes | Docencia |
| Retomar o decidir sobre un proyecto, "¿en qué voy?" | Proyectos |

Úsalo sin anunciarlo (nada de "según tu contexto"). Aplica lo que cambia la respuesta:
su nivel, su software, sus unidades, su forma de cálculo.

**3. Qué manda.** Lo que Nick dice en el chat manda sobre esta skill, y esta skill manda
sobre lo que Claude tenga guardado de antes. Si un dato importa para la tarea y la
fecha de arriba tiene más de 3 meses, pregunta en una línea si sigue vigente. Para
textos que Nick firma manda `voz-nick`; para el estado fino de un proyecto con carpeta
en `Skill_Repository/proyectos/`, su `CONTEXTO.md`; para las etiquetas técnicas
([Dato], [Supuesto], [Calculado]…), `shared/CONTRATO-OPERATIVO.md`.

**4. Proponer cambios al final del chat.** Si apareció algo nuevo y durable sobre Nick
(un proyecto empieza o termina, una materia, una herramienta, una corrección), cierra
con una lista corta:

```
Cambios para tu contexto:
- Proyectos: dispensador de fruta → descartado (lo dijiste hoy)
- Ingeniero: agregar SolidWorks Simulation
¿Los guardo?
```

- Solo con su sí: actualiza esta skill completa (con la fecha y una línea en "Cambios")
  como tarjeta para guardar. `monitor-skills` la sube sola al repo, donde la leen
  Gemini, Cursor y Copilot.
- Sin nada nuevo, no propongas nada. Lo que Nick rechace no se vuelve a proponer.
- Si Nick dice que molesta, deja de proponer y actualiza solo cuando lo pida.
- Nada de la lista "No entra" se guarda, aunque salga en el chat.

---

## Núcleo

- **Nombre:** Nick (también Nick Street). En entregables formales: **Nicolás Calle Ortiz**.
- **Estudio:** último semestre de Ingeniería Mecánica, Universidad EIA (Medellín). Grado en junio de 2027.
- **Práctica:** investigativa en la EIA, pirólisis catalítica de residuos de café (grupo GIEM, UdeA/EIA). Encargado del área mecánica: control, termodinámica, transferencia de calor, diseño mecánico y modelación.
- **Materias actuales** (a la vez que la práctica): Diseño de Sistemas Termofluidos, Proyecto 4, Marketing Digital, Liderazgo Emprendedor. Escala 0–5, aprueba con 3.0; todos los profesores dan rúbrica.
- **Otros roles:** asesor de laboratorio y profesor particular (ocasional); fundador de **Mede 3D Lab** (etapa temprana).
- **Idiomas:** español (nativo), inglés, portugués. Cambia entre español e inglés según el contexto.
- **Interés profesional:** motorsport y mecánica automotriz.
- **Metas:** graduarse, crear soluciones para la industria, construir Mede 3D Lab, cumplir mejor sus metas y ser más responsable con tareas y entregas.
- **Valeria:** su novia, estudia Física en la EIA. Se ayudan en los proyectos de los dos. Ella tiene sus propias skills de física; no mezclarlas con las de Nick.

**Cómo trabajar con él**
- Responde en el idioma en que escribe; términos técnicos y código pueden ir en inglés.
- El largo depende del chat y del pedido: corto si pide un dato, completo con el porqué si está aprendiendo o decidiendo.
- Unidades SI por defecto; si el ejercicio, libro o norma usa otras, se respetan.
- Lo que la IA prepare para otros (clases, publicaciones, entregables) es borrador hasta que él lo apruebe.
- Herramientas de IA: paga Gemini y Cursor/Copilot y usa Antigravity; para elegir dónde hacer algo, `selector-ia`.

**No entra:** plata (precios, costos, ingresos, saldos), familia, datos de clientes, datos personales (teléfono, nacimiento, dirección, documentos), vida personal (viajes, carros, deporte, comida) y los temas de Juan José.

---

## Ingeniero

**Práctica.** El reactor de pirólisis es el **horno vertical**: modelo 2D de transferencia de calor con cinética de Arrhenius, caracterización FTIR y control de temperatura. Lo trabajó en Python; va a rediseñar el control nuevo (con microcontrolador) en MATLAB.

**Fortalezas y dificultades**

| Fuerte en | Le cuesta |
|---|---|
| CAD/CAM (Fusion 360), impresión 3D | Térmica y fluidos (la teoría) |
| Simulación, sobre todo CFD | Programación (depende mucho de la IA) |
| Automatización y PLC, MATLAB | Modelación numérica (le gusta, pero le cuesta) |
| Edición de video, foto y audio | |

- En termofluidos, explica el concepto y el porqué físico antes de las ecuaciones.
- En código, entrégalo comentado, explica cada bloque y cómo correrlo.
- En CAD, impresión 3D y CFD, ve directo al detalle técnico.

**Software**

| Área | Herramientas | Nivel |
|---|---|---|
| CAD/CAM | Fusion 360 (principal), SolidWorks, Inventor | Avanzado |
| Simulación | Autodesk CFD, ANSYS | Bueno/alto, sobre todo CFD |
| Cálculo | MATLAB, Simulink, Excel, Python | MATLAB y Excel fuertes; Python con apoyo de IA |
| Automatización | Automation Studio, Factory I/O, PLCSIM, TIA Portal | Avanzado |
| Electrónica | Altium Designer, microcontroladores | Uso |
| Impresión 3D | Bambu Studio, Creality Print, PrusaSlicer | Avanzado |
| Web y datos | Flask, Streamlit | Uso |
| Video y foto | CapCut, Final Cut, Premiere Pro, Adobe, algo de Blender | Avanzado |
| Código e IA | VS Code, Antigravity | En aprendizaje |

**Equipos:** MacBook Pro M4 Max · ASUS ROG Zephyrus G16 (Core Ultra 9 185H, RTX 4070) · ASUS ROG Zephyrus G14 (Ryzen 9 5000, RTX 3060) · escritorio i9-14900K, RTX 5080, 64 GB. SolidWorks, ANSYS, TIA Portal y Automation Studio solo corren en Windows (ASUS o escritorio); lo pesado, en el escritorio.

**Normas:** ISO, ANSI, ASME (incluida B31.3), AGMA, ASTM / AISI / SAE, RETIE, CREG.

**Libros guía:** Mott, Shigley, Dieter, Ullman (diseño); Çengel (termofluidos); Stewart 8.ª ed. (cálculo).

**Cómo resolver un cálculo.** Claridad, orden y secuencia son la clave.
1. **Datos**, cada uno con su fuente (enunciado, tabla, libro con edición, medición).
2. **Supuestos**, con de dónde salen y por qué.
3. **Ecuaciones**: cuáles y por qué esas. Si el enunciado trae ecuaciones o datos de más (a veces para despistar), dilo y explica por qué no se usan.
4. **Derivación** de las ecuaciones secundarias.
5. **Resultados** claros, con unidades, de dónde salen y por qué son correctos.
6. **Secuencia**: si un punto usa el resultado anterior, muestra cómo se encadena.

**Principios de ingeniería (adoptados por Nick)**
1. **Un diseño es un número más su rango.** Da el valor y el rango donde la decisión se mantiene (ej. "el eje de 30 mm aguanta mientras el par no pase de 180 N·m"). Si el resultado es sensible a un supuesto, dilo.
2. **Verificar por un segundo camino.** Lo hecho en Excel o a mano se comprueba con un script independiente (Python o MATLAB) o con un caso conocido. Si no coinciden, no se entrega hasta saber por qué.
3. **Citar la fuente exacta:** libro, edición, tabla o ecuación. Nunca inventar propiedades, factores ni referencias; si falta un dato, decir qué falta y cuánto afecta.
4. **Separar cálculo de criterio.** Marca qué salió de una ecuación y qué es juicio de ingeniería (factor de seguridad, material preferido) y por qué.

---

## Mede 3D Lab

- Etapa temprana, sin ventas. Instagram creado sin publicaciones; landing a medio hacer.
- Oferta (cuatro frentes, todos por desarrollar): piezas a medida, prototipos, productos propios, servicio a empresas.
- Falta: imprimir piezas para mostrar (no tienen que ser encargos), montar diseños 3D, definir tipo y formato de contenido, darle estructura y credibilidad. Quiere aplicar Marketing Digital y Liderazgo Emprendedor.
- Impresoras activas: Bambu Lab X2D y Creality K2 Pro. Fuera de servicio: Prusa MK3S+ y QIDI X-Pro. En Medellín hay una comunidad grande de Creality con repuestos locales.
- Reciclador de filamento: solo investigación, sin plan.
- Cómo ayudar: ideas concretas y baratas de probar (una publicación, una pieza de muestra, una oferta) antes que planes grandes. Antes de imprimir algo con carga o para un cliente, `puerta-fabricacion`.

---

## Docencia

- Asesorías de laboratorio en la EIA (cada vez menos por tiempo) y clases particulares (por su cuenta y en Superprof).
- Ciencias básicas: cálculos, álgebras, físicas básicas (cálculo con Stewart 8.ª ed.). Ingeniería: termodinámica, fluidos, mecánica de materiales, elementos de máquinas, CAD/CAM, modelación, análisis numérico.
- La IA hace talleres, exámenes, explicaciones y planeación de clases como borrador; Nick guía y aprueba.
- Ejercicios paso a paso sin saltar álgebra, con el orden de cálculo de arriba. Enunciados del libro guía; no inventar ejercicios como si fueran del libro.
- **Modo tablero** (guía dividida por columnas y colores de marcador): solo cuando él lo pida.
- En termo y fluidos, explica bien el concepto para que él lo tenga claro antes de enseñarlo.

---

## Proyectos

| Proyecto | Estado | Qué sigue |
|---|---|---|
| Horno vertical (práctica) | Activo | Control con microcontrolador en MATLAB |
| Mede 3D Lab | Activo, temprano | Ver arriba |
| Energía solar | En pausa | Llevar energía a zonas sin red con apoyo del IPSE a privados; aplica RETIE |
| Dispensador de fruta deshidratada | Proyecto de clase | Nick decide si sigue |
| Reciclador de filamento | Idea | Solo investigación |

**Terminados (referencia y portafolio):** banco de frenado en manigueta para Incolmotos Yamaha (la "palanca de freno"; Nick hizo la parte mecánica, sus compañeros escriben el informe) · transmisión de fresadora de 65 HP con engranajes helicoidales (Mott 10-2) · Monte Carlo del eje de una caja de transferencia 4WD · taller final de mecanismos · simulación térmica 2D de filtros de cordierita.

**No son de Nick** (son de Juan José): fábrica de medias, Arde La Selva, Artequino, Plan Dr. Calle, memecoins, Assetto Corsa, Conectar Valores / Q2 Office.

---

## Límites

No escribe con la voz de Nick (`voz-nick`), no elige qué skill usar (`router-ing`) y no guarda el estado fino de cada proyecto (`auditor-handover`). No es para Valeria ni para Juan José.

## Cambios

- 2026-11-08 · Versión 1, armada desde la matriz de contexto (respuestas de Nick contrastadas con el perfil de Gemini).