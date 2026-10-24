# Catálogo de skills

La fuente de verdad es la carpeta `skills/` y `registry/CAPACIDADES.yml`. Este catálogo
es un índice para elegir rápido; confírmalo cuando el entorno lo permita.

| Skill | Etapa | Uso principal | Límite importante | Estado |
|---|---|---|---|---|
| `router-ing` | todas | Elegir skill para una tarea y combinarlas; evaluar skills externas. | No hace el trabajo final; no decide qué skills crear. | activa |
| `monitor-skills` | todas | Revisar el conjunto de skills: cuál sobra, cuál actualizar o mejorar y cuál crear según el uso real. Revisión semanal. | No elige skill para una tarea; no borra skills. | en-prueba |
| `auditor-handover` | continuar | Auditar si un chat o proyecto perdió calidad y armar el relevo (CONTEXTO + HANDOVER). | No reemplaza las fuentes del proyecto. | activa |
| `colaboracion-ias` | continuar | Coordinar a Claude con Gemini, Cursor, Copilot, Grok y Perplexity por la bitácora del proyecto (GitHub + Google Drive). | No toma decisiones por Nick; solo deja propuestas. | en-prueba |
| `depurador-recursos` | continuar | Limpiar memoria de Claude, docs del proyecto y chats viejos para gastar menos tokens, guardando antes cálculos e investigaciones en el repo. | No borra chats ni archivos subidos (da la lista); no hace handovers. | en-prueba |
| `selector-ia` | todas | Decidir qué IA, modelo y nivel de razonamiento usar para una tarea, cuidando límites. | No hace la tarea; no inventa límites de uso. | en-prueba |
| `panel-asesores` | por definir | Panel de asesores de ingeniería mecánica (profesores, ingenieros de industria y expertos) que evalúa proyectos de Nick con rúbricas, le dice cuándo se equivoca y lo guía para analizar, planear, ejecutar y presentar. | Ver su SKILL.md. | en-prueba |
| `presentaciones-universidad` | por definir | Arma presentaciones para entregas y sustentaciones de la universidad de Nick. | Ver su SKILL.md. | en-prueba |
| `marco-problema-ing` | enmarcar | Convertir un enunciado o encargo en ficha: objetivo, datos, incógnitas, restricciones, criterio de aceptación. | No calcula ni diseña. | pendiente |
| `calculo-trazable` | calcular | Memorias de cálculo de elementos de máquinas (engranajes, ejes, rodamientos, uniones, resortes) con fuentes, unidades y verificación en Python. | No da por válido un resultado sin supuestos explícitos ni sustituye una norma completa. | pendiente |
| `sistemas-termicos` | calcular | Balances de energía, ciclos e intercambiadores con propiedades citadas. | No inventa propiedades; no reemplaza un software de simulación. | pendiente |
| `ingenieria-inversa-cad` | diseñar | Pasar de una pieza física a un modelo CAD (Fusion 360): medición, incertidumbre, intención de diseño, tolerancias. | No certifica que la copia funcione igual que el original. | pendiente |
| `puerta-fabricacion` | fabricar | Revisión antes de imprimir, maquinar o entregar: material, tolerancias, DFM, parámetros de impresión. Resultado: pasa / bloqueado / prueba limitada. | No aprueba por apariencia del modelo. | pendiente |
| `entregables-ing` | comunicar | Estructura de informes, presentaciones, artículos y memorias de cálculo de la universidad. | No inventa referencias ni resultados. | pendiente |
| `voz-nick` | comunicar | Que los textos que presento como míos suenen a mí, con un perfil sacado de mis textos reales y revisión automática. | No cambia datos ni conclusiones técnicas; no es para la voz de clientes. | en-prueba |

## Rutas típicas

- **Ejercicio de diseño de máquinas:** `marco-problema-ing` → `calculo-trazable` → (`entregables-ing` + `voz-nick` si se entrega).
- **Pieza para imprimir o fabricar:** `marco-problema-ing` → `calculo-trazable` (si hay carga) → `puerta-fabricacion`.
- **Copiar una pieza existente:** `ingenieria-inversa-cad` → `calculo-trazable` (si cambia material o carga) → `puerta-fabricacion`.
- **Presentación o informe:** `entregables-ing` → `voz-nick`.
- **Chat largo que empieza a fallar:** `auditor-handover`.
- **Memoria, proyecto o chats cargados / ahorrar tokens:** `depurador-recursos` → (`auditor-handover` para los chats que haya que guardar antes de borrar).
- **Investigación terminada (research, M&A, sector):** `depurador-recursos` (ficha de investigación) y cerrar el chat.
- **Pasarle o recibir trabajo de otra IA:** `colaboracion-ias`.
- **¿Me sobra o me falta alguna skill? / revisar mis skills:** `monitor-skills`.
- **No sé dónde hacer esto / qué modelo usar:** `selector-ia` → (`colaboracion-ias` si va a otra IA).

## Huecos que no se crean todavía

- `simulacion-fea`: crear solo si `calculo-trazable` no alcanza para un caso real que necesite revisar resultados de elementos finitos.
- `seleccion-materiales`: crear solo si la selección de material se repite en varios proyectos y no cabe dentro de `puerta-fabricacion`.
