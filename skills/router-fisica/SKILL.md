---
name: router-fisica
description: Decide qué skill de física usar y en qué orden cuando una tarea de la estudiante de Física de la EIA (novia de Nick) cruza varias etapas (teoría, laboratorio, simulación, informe, exposición), o cuando ella pregunte "¿con qué hago esto?" o "¿qué skill uso?". No hace el trabajo final. No es el router de ingeniería de Nick (router-ing).
---

# Router de skills de física

Encuentra el camino más corto para la tarea. Esta skill no resuelve ni redacta: elige.

## Primero ubica la etapa

1. **Entender / resolver**: teoría, ejercicios, talleres, parciales → `ejercicios-fisica`.
2. **Medir**: datos de laboratorio, incertidumbres, ajustes → `informe-laboratorio`.
3. **Simular**: Python, métodos numéricos, notebooks → `simulacion-fisica`.
4. **Comunicar**: artículos, exposiciones, ensayos, trabajo de grado → `articulos-exposiciones`;
   texto que ella firma → `voz-propia`.
5. **Evaluar o decidir**: revisar antes de entregar, preparar sustentación → `panel-asesores-fisica`.

No saltes a redactar si falta el cálculo o el análisis que el texto debe mostrar.

## Inventario

1. Consulta [el catálogo](references/catalogo.md).
2. Si puedes leer el repo, confirma con `registry/CAPACIDADES.yml`.
3. `en-prueba` se puede usar (avisa). `pendiente` o `hueco` no existe todavía: haz el
   trabajo siguiendo `shared/CONTRATO-OPERATIVO.md` y dilo.

## Respuesta

Corta:
- **Skill principal** y por qué.
- **Apoyos** en orden, solo si hacen falta.
- **Lo que falta** (dato, rúbrica, archivo).
- **Siguiente acción.**

## Combinaciones típicas

- Informe con simulación de comparación: `informe-laboratorio` → `simulacion-fisica` →
  `voz-propia` → `panel-asesores-fisica`.
- Exposición de un paper con modelo propio: `articulos-exposiciones` (ficha) →
  `ejercicios-fisica` (derivar ecuaciones) → `simulacion-fisica` → `articulos-exposiciones` (slides).
- Parcial: `ejercicios-fisica` (modo D) → `panel-asesores-fisica` solo si quiere simulacro con jurado.
