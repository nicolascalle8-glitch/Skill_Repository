---
name: simulacion-fisica
description: 'Ayuda a la estudiante de Física de la EIA (novia de Nick) a simular y resolver problemas de física con Python: EDOs (osciladores, órbitas, péndulos, circuitos), sistemas acoplados y modos normales, métodos numéricos, Schrödinger 1D, Monte Carlo, gráficas y animaciones, siempre validando con conservación, convergencia y casos analíticos. Úsala cuando ella pida "simular", "hacer en Python", un notebook, métodos numéricos, integrar una ecuación, graficar una solución, animar, o cuando un ejercicio no tenga solución analítica, aunque no nombre la skill. No es para ajustar datos de laboratorio (informe-laboratorio) ni para el código de ingeniería de Nick.'
---

# Simulación y Python para física

Que la simulación sea física correcta, no solo código que corre. Una gráfica bonita no
prueba nada: cada simulación se valida antes de sacar conclusiones.
Sigue `shared/CONTRATO-OPERATIVO.md`, sección 5.

## Antes de empezar

- ¿Qué sistema, qué ecuaciones y qué pregunta física se quiere responder con la simulación?
- ¿Dónde lo corre ella? (Jupyter/Colab, VS Code, Spyder). ¿Qué tanto Python sabe?
  Ajusta el nivel del código: claro y comentado antes que corto.
- ¿Es entrega? Entonces el código tiene que ser de ella: explica cada bloque y no uses
  trucos que no pueda defender.

## Cómo se hace

1. **Modelo en papel primero.** Ecuaciones, variables, parámetros con unidades, condiciones
   iniciales y de frontera. Si viene de un Lagrangiano o Hamiltoniano, deriva las
   ecuaciones de movimiento (con sympy si son largas) y muéstralas.
2. **Adimensionar** cuando las escalas sean muy distintas (cuántica, astrofísica); di las
   escalas usadas.
3. **Elegir el método** (ver `references/metodos.md`): Verlet/leapfrog para sistemas
   conservativos de tiempo largo, `solve_ivp` (RK45, o Radau/BDF si es rígido) para lo
   general, diferencias finitas o matrices para Schrödinger/PDEs.
4. **Partir de la plantilla** `scripts/plantilla_ode.py`: ya trae integradores, energía,
   convergencia y comparación analítica. Para un sistema nuevo se copia un caso y se
   cambian `acel`, `energia` y parámetros.
5. **Validar** (obligatorio, en este orden):
   - Caso con solución analítica (límite lineal, ángulo pequeño, acoplamiento cero…).
   - Cantidades conservadas: energía, momento, momento angular, norma de ψ.
   - Convergencia: repetir con dt/2 (o rtol menor) y ver que el resultado no cambia.
   - Unidades y órdenes de magnitud de los resultados.
6. **Responder la pregunta física**: qué muestra la simulación, en qué régimen vale y qué
   no se puede concluir.

## Gráficas y animaciones

- Ejes con magnitud y unidad; una idea por figura.
- Espacio de fases, energía vs. tiempo y espectro (FFT) suelen decir más que x(t).
- Animaciones con `matplotlib.animation` → GIF o MP4 solo si se piden; la gráfica estática va siempre.

## Salida

- Script o notebook que corre de principio a fin, con comentarios en español.
- Gráficas.
- Resumen corto: modelo, método, validación (con números) y conclusión física.

## Verificación

- [ ] Corrió completo en el workspace antes de entregarlo.
- [ ] Validación con números: deriva de energía, error vs. analítica, convergencia.
- [ ] Parámetros con unidades y fuente si son datos reales.
- [ ] Semilla fija si hay números aleatorios.

## Límites

- Ajuste de datos medidos → `informe-laboratorio`.
- Si el problema tiene solución analítica razonable y la piden en el parcial, primero
  `ejercicios-fisica`; la simulación solo como comprobación.
- Simulaciones grandes (PDEs 3D, dinámica molecular, HPC): decirlo y proponer
  herramienta (FEniCS, LAMMPS, QuTiP…) en vez de forzar numpy.
