# Catálogo de skills

La fuente de verdad es la carpeta `skills/` y `registry/CAPACIDADES.yml`. Este catálogo
es un índice para elegir rápido; confírmalo cuando el entorno lo permita.

| Skill | Etapa | Uso principal | Límite importante | Estado |
|---|---|---|---|---|
| `router-ing` | todas | Elegir skill, combinarlas o detectar huecos. | No hace el trabajo final. | activa |
| `auditor-handover` | continuar | Auditar si un chat o proyecto perdió calidad y armar el relevo (CONTEXTO + HANDOVER). | No reemplaza las fuentes del proyecto. | activa |
| `colaboracion-ias` | continuar | Coordinar a Claude con Gemini, Cursor, Copilot, Grok y Perplexity por la bitácora del proyecto (GitHub + Google Drive). | No toma decisiones por Nick; solo deja propuestas. | en-prueba |
| `selector-ia` | todas | Decidir qué IA, modelo y nivel de razonamiento usar para una tarea, cuidando límites. | No hace la tarea; no inventa límites de uso. | en-prueba |
| `marco-problema-ing` | enmarcar | Convertir un enunciado o encargo en ficha: objetivo, datos, incógnitas, restricciones, criterio de aceptación. | No calcula ni diseña. | pendiente |
| `calculo-trazable` | calcular | Memorias de cálculo de elementos de máquinas (engranajes, ejes, rodamientos, uniones, resortes) con fuentes, unidades y verificación en Python. | No da por válido un resultado sin supuestos explícitos ni sustituye una norma completa. | pendiente |
| `sistemas-termicos` | calcular | Balances de energía, ciclos e intercambiadores con propiedades citadas. | No inventa propiedades; no reemplaza un software de simulación. | pendiente |
| `ingenieria-inversa-cad` | diseñar | Pasar de una pieza física a un modelo CAD (Fusion 360): medición, incertidumbre, intención de diseño, tolerancias. | No certifica que la copia funcione igual que el original. | pendiente |
| `puerta-fabricacion` | fabricar | Revisión antes de imprimir, maquinar o entregar: material, tolerancias, DFM, parámetros de impresión. Resultado: pasa / bloqueado / prueba limitada. | No aprueba por apariencia del modelo. | pendiente |
| `entregables-ing` | comunicar | Estructura de informes, presentaciones, artículos y memorias de cálculo de la universidad. | No inventa referencias ni resultados. | pendiente |
| `voz-nick` | comunicar | Que los textos que presento como míos suenen a mí: español simple y directo. | No cambia datos ni conclusiones técnicas. | pendiente |

## Rutas típicas

- **Ejercicio de diseño de máquinas:** `marco-problema-ing` → `calculo-trazable` → (`entregables-ing` + `voz-nick` si se entrega).
- **Pieza para imprimir o fabricar:** `marco-problema-ing` → `calculo-trazable` (si hay carga) → `puerta-fabricacion`.
- **Copiar una pieza existente:** `ingenieria-inversa-cad` → `calculo-trazable` (si cambia material o carga) → `puerta-fabricacion`.
- **Presentación o informe:** `entregables-ing` → `voz-nick`.
- **Chat largo que empieza a fallar:** `auditor-handover`.
- **Pasarle o recibir trabajo de otra IA:** `colaboracion-ias`.
- **No sé dónde hacer esto / qué modelo usar:** `selector-ia` → (`colaboracion-ias` si va a otra IA).

## Huecos que no se crean todavía

- `simulacion-fea`: crear solo si `calculo-trazable` no alcanza para un caso real que necesite revisar resultados de elementos finitos.
- `seleccion-materiales`: crear solo si la selección de material se repite en varios proyectos y no cabe dentro de `puerta-fabricacion`.
