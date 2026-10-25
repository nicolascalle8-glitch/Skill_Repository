#!/usr/bin/env python3
"""Propagación de incertidumbres (GUM, primer orden) con comparación Monte Carlo opcional.

Uso:
  python3 incertidumbre.py "4*pi**2*L/T**2" L=0.500,0.001 T=1.419,0.005
  python3 incertidumbre.py "4*pi**2*L/T**2" L=0.500,0.001 T=1.419,0.005 --mc
  python3 incertidumbre.py "4*pi**2*L/T**2" L=0.500,0.001 T=1.419,0.005 --unidad "m/s^2"

Cada variable va como nombre=valor,incertidumbre_estandar (misma unidad que el valor).
Supone variables no correlacionadas. Con --mc compara contra 10^6 muestras gaussianas.
Requiere: sympy, numpy.
"""
import argparse
import math
import sys

import numpy as np
import sympy as sp


def redondear(valor, u, cifras=None):
    """Redondea u a 1 cifra significativa (2 si empieza en 1 o 2) y el valor a esa posición."""
    if u <= 0 or not math.isfinite(u):
        return f"{valor:g}", "0"
    exp = math.floor(math.log10(u))
    primera = int(u / 10**exp)
    if cifras is None:
        cifras = 2 if primera in (1, 2) else 1
    dec = -(exp - (cifras - 1))
    u_r = round(u, dec)
    # si al redondear sube de orden (p. ej. 0.096 -> 0.1), recalcular
    if u_r >= 10 ** (exp + 1):
        exp += 1
        dec = -(exp - (cifras - 1))
        u_r = round(u, dec)
    v_r = round(valor, dec)
    fmt = f"{{:.{max(dec, 0)}f}}"
    return fmt.format(v_r), fmt.format(u_r)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("expresion", help="Función en sintaxis de Python/sympy, p. ej. '4*pi**2*L/T**2'")
    p.add_argument("variables", nargs="+", help="nombre=valor,u")
    p.add_argument("--mc", action="store_true", help="Comparar con Monte Carlo")
    p.add_argument("--n", type=int, default=1_000_000, help="Muestras Monte Carlo")
    p.add_argument("--unidad", default="", help="Unidad del resultado (solo para mostrar)")
    p.add_argument("--k", type=float, default=None, help="Factor de cobertura para U = k·u")
    a = p.parse_args()

    datos = {}
    for item in a.variables:
        try:
            nombre, resto = item.split("=")
            v, u = resto.split(",")
            datos[nombre.strip()] = (float(v), float(u))
        except ValueError:
            sys.exit(f"Variable mal escrita: '{item}'. Formato: nombre=valor,u")

    simbolos = {n: sp.Symbol(n) for n in datos}
    f = sp.sympify(a.expresion, locals=simbolos)
    libres = {str(s) for s in f.free_symbols}
    faltan = libres - set(datos)
    if faltan:
        sys.exit(f"Faltan valores para: {', '.join(sorted(faltan))}")

    sust = {simbolos[n]: datos[n][0] for n in datos}
    valor = float(f.subs(sust).evalf())

    print(f"f = {sp.simplify(f)}")
    print("\nContribuciones (∂f/∂x · u_x):")
    total2 = 0.0
    filas = []
    for n, (v, u) in datos.items():
        d = float(sp.diff(f, simbolos[n]).subs(sust).evalf())
        c = d * u
        total2 += c**2
        filas.append((n, v, u, d, c))
    for n, v, u, d, c in filas:
        pct = 100 * c**2 / total2 if total2 > 0 else 0
        print(f"  {n:>8} = {v:g} ± {u:g}   ∂f/∂{n} = {d:.6g}   aporte = {abs(c):.3g}  ({pct:.1f} % de u²)")
    u_f = math.sqrt(total2)

    v_s, u_s = redondear(valor, u_f)
    print(f"\nResultado (primer orden): {valor:.6g} ± {u_f:.3g} {a.unidad}")
    print(f"Redondeado:               {v_s} ± {u_s} {a.unidad}")
    if a.k:
        v_k, U_k = redondear(valor, a.k * u_f)
        print(f"Expandida (k={a.k:g}):        {v_k} ± {U_k} {a.unidad}")

    if a.mc:
        rng = np.random.default_rng(12345)
        fnum = sp.lambdify([simbolos[n] for n in datos], f, "numpy")
        muestras = [rng.normal(v, u, a.n) for v, u in datos.values()]
        y = fnum(*muestras)
        y = y[np.isfinite(y)]
        media, s = float(np.mean(y)), float(np.std(y, ddof=1))
        lo, hi = np.percentile(y, [2.5, 97.5])
        print(f"\nMonte Carlo (n={len(y)}, semilla 12345): media {media:.6g}, u {s:.3g}, "
              f"intervalo 95 % [{lo:.6g}, {hi:.6g}]")
        dif = abs(s - u_f) / u_f if u_f else 0
        if dif > 0.1:
            print(f"Aviso: Monte Carlo y primer orden difieren {100*dif:.0f} % en u. "
                  "La función es no lineal en este rango: reporta Monte Carlo y dilo.")
        else:
            print("Primer orden y Monte Carlo coinciden (diferencia < 10 %).")


if __name__ == "__main__":
    main()
