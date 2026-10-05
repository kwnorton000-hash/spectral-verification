"""Shared statistics: unfolding, Wigner surmises, Kolmogorov-Smirnov distance."""
import numpy as np

def unfold_zeros(t):
    t = np.asarray(t, float)
    return t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e))

def unfold_linear(E):
    E = np.sort(np.asarray(E, float))
    p = np.polyfit(E, np.arange(1, len(E) + 1), 1)
    return np.polyval(p, E), 1 / p[0]

def spacings(u):
    s = np.diff(u)
    return s / s.mean()

def cdf_poisson(s): return 1 - np.exp(-s)
def cdf_goe(s): return 1 - np.exp(-np.pi * s**2 / 4)
_g = np.linspace(0, 6, 6001)
_cg = np.cumsum(32 / np.pi**2 * _g**2 * np.exp(-4 * _g**2 / np.pi)) * (_g[1] - _g[0])
def cdf_gue(s): return np.interp(s, _g, _cg)

def ks(x, cdf):
    x = np.sort(x); n = len(x); m = np.arange(1, n + 1) / n; c = cdf(x)
    return float(np.max(np.maximum(abs(m - c), abs(m - 1 / n - c))))

def report(name, s):
    crit = 1.36 / np.sqrt(len(s))
    r = {k: ks(s, c) for k, c in [("GOE", cdf_goe), ("GUE", cdf_gue), ("Poisson", cdf_poisson)]}
    verdict = {k: ("fits" if v < crit else "rejected") for k, v in r.items()}
    print(f"{name}: n={len(s)} var={s.var():.3f} P(s<0.25)={np.mean(s<0.25):.4f} crit(5%)={crit:.4f}")
    for k in r: print(f"   KS to {k:8s} {r[k]:.4f}  {verdict[k]}")
    return r
