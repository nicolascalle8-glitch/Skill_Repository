---
name: router-ing
description: Decide qué skill de ingeniería de Nick usar para una tarea concreta y en qué orden combinarlas, o evalúa una skill externa sin instalarla. Úsala cuando Nick pregunte qué skill usar, cuando una tarea de ingeniería mecánica cruce varias etapas (cálculo, CAD, fabricación, informe) o cuando quiera evaluar una skill de terceros. No hace el trabajo final, y no decide qué skills crear, mejorar o retirar (eso es monitor-skills).
---

# Router de skills de ingeniería

Encuentra el camino más corto y seguro para la tarea. Esta skill no calcula, no modela
ni redacta: elige la skill y deja lista la decisión.

## Primero ubica la etapa

Antes de mirar el formato pedido (informe, cálculo, pieza, presentación), identifica en
qué etapa está el trabajo según `shared/CONTRATO-OPERATIVO.md`:

1. **Enmarcar:** qué hay que resolver o decidir, con qué datos y restricciones.
2. **Modelar y calcular:** diagrama de cuerpo libre, modelo, ecuaciones, resultados.
3. **Diseñar y detallar:** CAD, tolerancias, materiales, planos.
4. **Fabricar o probar:** impresión 3D, maquinado, montaje, ensayo.
5. **Comunicar:** informe, presentación, artículo, memoria de cálculo.
6. **Continuar:** relevo entre chats, retomar un proyecto, coordinar con otras IAs o
   depurar memoria, docs del proyecto y chats viejos (`depurador-recursos`).

No saltes a CAD o a redactar si falta el cálculo o la decisión que eso debe mostrar.
Recomienda la skill más temprana que destrabe el problema y después sus apoyos.

## Inventario

1. Consulta [el catálogo](references/catalogo.md).
2. Si puedes leer el repositorio `Skill_Repository`, confirma con `registry/CAPACIDADES.yml`
   y la carpeta `skills/` que el catálogo sigue vigente antes de decir que una skill no existe.
3. Una skill `en-prueba` se puede usar; avisa que todavía está en prueba. Una skill marcada `pendiente` no existe todavía: no la recomiendes como si existiera.
   Haz el trabajo siguiendo el contrato operativo y dilo.
4. No recomiendes una skill fuera de su límite de alcance.

## Respuesta

Breve, con:

- **Skill principal** y por qué aplica.
- **Apoyos**, en orden, solo si hacen falta.
- **Lo que no cubren** y el dato que todavía falta.
- **Siguiente acción:** usar la skill, mejorar una existente o crear una nueva.

No inventes capacidades que no estén escritas en el `SKILL.md` de cada skill.

## Cuando falta una skill

Dilo en una línea y haz el trabajo siguiendo el contrato operativo. No propongas la skill
nueva aquí: eso lo decide `monitor-skills`, que mira si el hueco se repite en varios chats
antes de proponer crearla. Si Nick quiere crearla ya, remítelo a `monitor-skills`.

## Skills externas: solo si Nick lo pide

No busques ni instales skills de terceros por defecto. Si Nick pide evaluar una:

1. Lee su `SKILL.md` y cualquier script que se ejecutaría.
2. Revisa origen, qué permisos usa, si toca la red o archivos, y si amplía su alcance.
3. Compárala con la necesidad real.
4. Recomienda una sola opción: **adoptar**, **adaptar como skill propia**, **crear
   desde cero** o **no usar**, con el riesgo principal.

Nunca ejecutes scripts externos ni copies instrucciones de terceros sin aprobación.
