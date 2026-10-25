#!/usr/bin/env python3
"""Plantilla de simulación de sistemas dinámicos (EDOs) con validación incluida.

Trae dos casos listos que sirven de molde:
  oscilador  -> oscilador armónico simple (tiene solución analítica: sirve para validar)
  acoplados  -> dos masas acopladas por resortes (modos normales; molde del proyecto de
                osciladores acoplados LH2–LH3)

Uso:
  python3 plantilla_ode.py oscilador
  python3 plantilla_ode.py acoplados --metodo verlet --dt 1e-3
  python3 plantilla_ode.py acoplados --metodo rk45 --salida acoplados.png

Métodos:
  rk45   -> scipy.integrate.solve_ivp (paso adaptativo, tolerancias controladas)
  verlet -> velocity Verlet (simpléctico: conserva bien la energía en tiempos largos)

Cada corrida imprime: deriva relativa de energía, prueba de convergencia (dt y dt/2) y, si
existe, el error contra la solución analítica. Para un sistema nuevo copia un caso y cambia
`aceleracion`, `energia` y los parámetros. Requiere: numpy, scipy, matplotlib.
"""
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# ---------------------------------------------------------------- sistemas
# Cada sistema define: parámetros (SI), condiciones iniciales, aceleración a(x, v, t),
# energía E(x, v) y, si existe, solución analítica x(t).

def sistema_oscilador():
    m, k = 1.0, 4.0                # kg, N/m
    w = np.sqrt(k / m)             # rad/s
    x0, v0 = np.array([1.0]), np.array([0.0])   # m, m/s

    def acel(x, v, t):
        return -k / m * x

    def energia(x, v):
        return 0.5 * m * np.sum(v**2, axis=0) + 0.5 * k * np.sum(x**2, axis=0)

    def analitica(t):
        return np.array([x0[0] * np.cos(w * t) + v0[0] / w * np.sin(w * t)])

    return dict(nombre="Oscilador armónico", x0=x0, v0=v0, acel=acel, energia=energia,
                analitica=analitica, T=2 * np.pi / w, etiquetas=["x"])


def sistema_acoplados():
    # pared -k- m1 -kc- m2 -k- pared
    m, k, kc = 1.0, 4.0, 0.5       # kg, N/m, N/m
    x0, v0 = np.array([1.0, 0.0]), np.array([0.0, 0.0])
    w1 = np.sqrt(k / m)                    # modo en fase
    w2 = np.sqrt((k + 2 * kc) / m)         # modo en contrafase

    def acel(x, v, t):
        x1, x2 = x
        return np.array([(-k * x1 - kc * (x1 - x2)) / m,
                         (-k * x2 - kc * (x2 - x1)) / m])

    def energia(x, v):
        x1, x2 = x
        return (0.5 * m * np.sum(v**2, axis=0) + 0.5 * k * (x1**2 + x2**2)
                + 0.5 * kc * (x1 - x2) ** 2)

    def analitica(t):
        # x0 = (1, 0) es la suma de los dos modos con amplitud 1/2
        return np.array([0.5 * (np.cos(w1 * t) + np.cos(w2 * t)),
                         0.5 * (np.cos(w1 * t) - np.cos(w2 * t))])

    T_batido = 2 * np.pi / (w2 - w1)
    return dict(nombre="Osciladores acoplados", x0=x0, v0=v0, acel=acel, energia=energia,
                analitica=analitica, T=T_batido, etiquetas=["x1", "x2"],
                frecuencias=(w1, w2))


SISTEMAS = {"oscilador": sistema_oscilador, "acoplados": sistema_acoplados}


# ---------------------------------------------------------------- integradores

def integrar_verlet(s, t_final, dt):
    n = int(round(t_final / dt))
    t = np.linspace(0, n * dt, n + 1)
    x = np.zeros((len(s["x0"]), n + 1))
    v = np.zeros_like(x)
    x[:, 0], v[:, 0] = s["x0"], s["v0"]
    a = s["acel"](x[:, 0], v[:, 0], 0.0)
    for i in range(n):
        x[:, i + 1] = x[:, i] + v[:, i] * dt + 0.5 * a * dt**2
        a_new = s["acel"](x[:, i + 1], v[:, i], t[i + 1])   # fuerzas sin dependencia de v
        v[:, i + 1] = v[:, i] + 0.5 * (a + a_new) * dt
        a = a_new
    return t, x, v


def integrar_rk45(s, t_final, dt, rtol=1e-9, atol=1e-12):
    d = len(s["x0"])

    def f(t, y):
        x, v = y[:d], y[d:]
        return np.concatenate([v, s["acel"](x, v, t)])

    t_eval = np.arange(0, t_final + dt / 2, dt)
    sol = solve_ivp(f, (0, t_eval[-1]), np.concatenate([s["x0"], s["v0"]]),
                    t_eval=t_eval, rtol=rtol, atol=atol, method="RK45")
    return sol.t, sol.y[:d], sol.y[d:]


INTEGRADORES = {"verlet": integrar_verlet, "rk45": integrar_rk45}


# ---------------------------------------------------------------- validación

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("sistema", choices=SISTEMAS)
    p.add_argument("--metodo", choices=INTEGRADORES, default="verlet")
    p.add_argument("--dt", type=float, default=1e-3, help="paso de tiempo (s)")
    p.add_argument("--periodos", type=float, default=3, help="duración en periodos característicos")
    p.add_argument("--salida", default=None)
    a = p.parse_args()

    s = SISTEMAS[a.sistema]()
    integ = INTEGRADORES[a.metodo]
    t_final = a.periodos * s["T"]

    t, x, v = integ(s, t_final, a.dt)
    E = s["energia"](x, v)
    deriva = np.max(np.abs(E - E[0])) / abs(E[0])
    print(f"{s['nombre']} — método {a.metodo}, dt = {a.dt:g} s, t_final = {t_final:.4g} s")
    print(f"Deriva relativa máxima de energía: {deriva:.2e}")

    if s.get("analitica"):
        err = np.max(np.abs(x - s["analitica"](t)))
        print(f"Error máximo contra solución analítica: {err:.2e} m")

    # convergencia: repetir con dt/2 y comparar posición final
    t2, x2, _ = integ(s, t_final, a.dt / 2)
    dif = np.max(np.abs(x[:, -1] - x2[:, -1]))
    print(f"Convergencia: |x(dt) − x(dt/2)| al final = {dif:.2e} m")
    if s.get("analitica"):
        e1 = np.max(np.abs(x[:, -1] - s["analitica"](t[-1:])[:, 0]))
        e2 = np.max(np.abs(x2[:, -1] - s["analitica"](t2[-1:])[:, 0]))
        if e2 > 0 and a.metodo == "verlet":
            print(f"Orden observado ≈ {np.log2(e1 / e2):.2f} (Verlet debería dar ≈ 2)")

    if "frecuencias" in s:
        # frecuencias por FFT de x1 vs. teoría
        n = len(t)
        from scipy.signal import find_peaks
        ventana = np.hanning(n)
        X = np.abs(np.fft.rfft((x[0] - x[0].mean()) * ventana, n=16 * n))
        fr = np.fft.rfftfreq(16 * n, d=t[1] - t[0]) * 2 * np.pi
        idx, _ = find_peaks(X)
        top = np.sort(fr[idx[np.argsort(X[idx])[-2:]]])
        w1, w2 = s["frecuencias"]
        print(f"Modos normales teóricos: ω1 = {w1:.4f}, ω2 = {w2:.4f} rad/s")
        print(f"Modos por FFT de x1:     ω1 ≈ {top[0]:.4f}, ω2 ≈ {top[1]:.4f} rad/s "
              f"(resolución sin relleno ≈ {2*np.pi/t[-1]:.3f} rad/s; corre más periodos para afinar)")
    if a.metodo == "rk45":
        print("Nota: en rk45 el paso real lo controla rtol/atol, no dt; la prueba de convergencia "
              "se hace bajando rtol, no dt.")

    if a.salida:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5.5), sharex=True)
        for xi, et in zip(x, s["etiquetas"]):
            ax1.plot(t, xi, label=et)
        ax1.set_ylabel("Posición (m)")
        ax1.legend(frameon=False)
        ax2.plot(t, (E - E[0]) / abs(E[0]))
        ax2.set_ylabel("(E − E₀)/E₀")
        ax2.set_xlabel("t (s)")
        fig.tight_layout()
        fig.savefig(a.salida, dpi=200)
        print(f"Gráfica: {a.salida}")


if __name__ == "__main__":
    main()
