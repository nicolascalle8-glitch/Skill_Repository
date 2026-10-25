#!/usr/bin/env python3
"""Ajuste de un modelo a datos con incertidumbres: parámetros ± u, χ²/ν, valor p y residuos.

Uso:
  python3 ajuste.py datos.csv "a*x + b"
  python3 ajuste.py datos.csv "2*pi*sqrt(x/g)" --p0 g=9.8 --x L --y T --uy uT
  python3 ajuste.py datos.csv "A*exp(-x/tau)" --p0 A=1,tau=2 --salida decaimiento.png \
      --xlabel "t (s)" --ylabel "V (V)"

El CSV necesita columnas para x, y y (opcional) la incertidumbre de y. Por defecto se llaman
x, y, uy. Si hay incertidumbre en x (columna ux, --ux), se usa el método de varianza efectiva:
u_ef² = uy² + (df/dx · ux)², iterando.
La variable independiente en el modelo siempre se escribe x. Todo otro símbolo es parámetro.
Sin columna de incertidumbre, se reporta R² y las incertidumbres salen de la dispersión
(no hay χ² con sentido). Requiere: numpy, scipy, sympy, pandas, matplotlib.
"""
import argparse
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp
from scipy import optimize, stats


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv")
    p.add_argument("modelo", help="Expresión en x, p. ej. 'a*x + b'")
    p.add_argument("--x", default="x")
    p.add_argument("--y", default="y")
    p.add_argument("--uy", default="uy")
    p.add_argument("--ux", default=None)
    p.add_argument("--p0", default="", help="Valores iniciales: a=1,b=0")
    p.add_argument("--salida", default="ajuste.png")
    p.add_argument("--xlabel", default="x")
    p.add_argument("--ylabel", default="y")
    a = p.parse_args()

    df = pd.read_csv(a.csv)
    for col in (a.x, a.y):
        if col not in df:
            sys.exit(f"No encuentro la columna '{col}'. Columnas: {list(df.columns)}")
    x = df[a.x].to_numpy(float)
    y = df[a.y].to_numpy(float)
    uy = df[a.uy].to_numpy(float) if a.uy in df else None
    ux = df[a.ux].to_numpy(float) if a.ux and a.ux in df else None

    X = sp.Symbol("x")
    expr = sp.sympify(a.modelo, locals={"x": X})
    params = sorted((s for s in expr.free_symbols if s != X), key=str)
    if not params:
        sys.exit("El modelo no tiene parámetros.")
    f = sp.lambdify([X, *params], expr, "numpy")
    dfdx = sp.lambdify([X, *params], sp.diff(expr, X), "numpy")

    p0 = {str(s): 1.0 for s in params}
    if a.p0:
        for item in a.p0.split(","):
            k, v = item.split("=")
            p0[k.strip()] = float(v)
    p0v = [p0[str(s)] for s in params]

    def modelo(xx, *pp):
        return f(xx, *pp) * np.ones_like(xx)

    con_u = uy is not None
    sigma = uy.copy() if con_u else None
    popt, pcov = optimize.curve_fit(modelo, x, y, p0=p0v, sigma=sigma, absolute_sigma=con_u, maxfev=20000)
    if con_u and ux is not None:
        for _ in range(10):
            sigma = np.sqrt(uy**2 + (dfdx(x, *popt) * ux) ** 2)
            popt, pcov = optimize.curve_fit(modelo, x, y, p0=popt, sigma=sigma, absolute_sigma=True, maxfev=20000)
    perr = np.sqrt(np.diag(pcov))

    res = y - modelo(x, *popt)
    n, k = len(x), len(params)
    nu = n - k
    print(f"Modelo: y = {expr}    (n = {n}, parámetros = {k}, ν = {nu})")
    for s, v, e in zip(params, popt, perr):
        print(f"  {str(s):>6} = {v:.6g} ± {e:.3g}")
    if k > 1:
        corr = pcov / np.outer(perr, perr)
        print("Correlación entre parámetros:")
        for i, si in enumerate(params):
            print("   ", str(si).rjust(6), " ".join(f"{corr[i, j]:+.3f}" for j in range(k)))

    if con_u:
        chi2 = float(np.sum((res / sigma) ** 2))
        pval = float(stats.chi2.sf(chi2, nu)) if nu > 0 else float("nan")
        print(f"χ² = {chi2:.3g}, χ²/ν = {chi2/nu:.3g}, valor p = {pval:.3g}")
        if nu > 0 and chi2 / nu > 3:
            print("Aviso: χ²/ν alto. El modelo no describe bien los datos o las incertidumbres están subestimadas.")
        elif nu > 0 and chi2 / nu < 0.3:
            print("Aviso: χ²/ν muy bajo. Probablemente las incertidumbres están sobreestimadas.")
    else:
        r2 = 1 - np.sum(res**2) / np.sum((y - y.mean()) ** 2)
        print(f"Sin incertidumbres en y: R² = {r2:.5f}. Las u de los parámetros salen de la dispersión.")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 6), sharex=True,
                                   gridspec_kw={"height_ratios": [3, 1]})
    ax1.errorbar(x, y, yerr=uy, xerr=ux, fmt="o", ms=4, capsize=3, color="#1f4e79", label="Datos")
    xs = np.linspace(x.min(), x.max(), 400)
    ax1.plot(xs, modelo(xs, *popt), color="#c0504d", label="Ajuste")
    ax1.set_ylabel(a.ylabel)
    ax1.legend(frameon=False)
    ax2.errorbar(x, res, yerr=sigma, fmt="o", ms=4, capsize=3, color="#1f4e79")
    ax2.axhline(0, color="gray", lw=1)
    ax2.set_xlabel(a.xlabel)
    ax2.set_ylabel("Residuo")
    fig.tight_layout()
    fig.savefig(a.salida, dpi=300)
    print(f"Gráfica: {a.salida}")


if __name__ == "__main__":
    main()
