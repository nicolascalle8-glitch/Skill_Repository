# Qué método usar

| Problema | Método recomendado | Por qué | Validar con |
|---|---|---|---|
| Oscilador, péndulo, órbitas, N cuerpos (conservativo, tiempo largo) | Velocity Verlet / leapfrog | Simpléctico: la energía oscila acotada, no deriva | Energía, momento angular, órbita cerrada |
| EDO general, con fricción o forzada | `solve_ivp` RK45 (rtol 1e-8) | Paso adaptativo, fácil | Caso analítico, bajar rtol |
| EDO rígida (escalas muy distintas, química, circuitos con L y C pequeñas) | `solve_ivp` Radau o BDF | RK45 se vuelve lentísimo o inestable | Comparar dos métodos |
| Caos (Lorenz, péndulo doble) | RK45 con rtol bajo | Sensibilidad a condiciones iniciales | Exponente de Lyapunov, energía (si aplica) |
| Modos normales | `numpy.linalg.eigh` de M⁻¹K | Exacto para sistema lineal | FFT de la simulación temporal |
| Schrödinger 1D estacionario | Diferencias finitas → matriz tridiagonal, `scipy.linalg.eigh_tridiagonal` | Simple y preciso | Pozo infinito, oscilador (E = ħω(n+½)) |
| Schrödinger 1D dependiente del tiempo | Crank–Nicolson o split-operator (FFT) | Conserva la norma | Norma = 1, paquete libre (ensanchamiento analítico) |
| Ecuación de calor / difusión | Diferencias finitas implícitas (Crank–Nicolson) | Estable con dt grande | Solución analítica gaussiana |
| Ecuación de onda | Diferencias finitas centradas | Simple | Condición CFL c·dt/dx ≤ 1, modos estacionarios |
| Laplace / Poisson (electrostática) | Relajación (Jacobi, Gauss-Seidel, SOR) o `scipy.sparse.linalg.spsolve` | Directo | Caso con simetría conocida |
| Integrales | `scipy.integrate.quad` / Simpson | | Integral conocida |
| Raíces / ecuaciones trascendentes | `scipy.optimize.brentq` | Robusto si hay cambio de signo | Graficar la función |
| Sistemas aleatorios (caminatas, Ising) | Monte Carlo / Metropolis con `numpy.random.default_rng(semilla)` | | Límite conocido, error ~ 1/√N |
| Sistemas cuánticos abiertos, dinámica de excitones | QuTiP | Hecho para eso | Casos límite de la teoría |

Referencias de consulta (abrir antes de citar):
- Newman, M. *Computational Physics* (2013).
- Landau, Páez y Bordeianu, *Computational Physics* (Wiley).
- Documentación de SciPy: https://docs.scipy.org/doc/scipy/reference/integrate.html
