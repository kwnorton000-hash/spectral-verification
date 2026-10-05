"""Pair correlation of the first 400 Riemann zeros vs Montgomery's GUE prediction."""
import numpy as np, pathlib
from common import unfold_zeros, spacings
D = pathlib.Path(__file__).resolve().parent.parent / "data"
z = np.loadtxt(D / "zeta_zeros_first2000.txt")[:400]
u = unfold_zeros(z)
d = np.array([u[j]-u[i] for i in range(len(u)) for j in range(i+1, min(i+40, len(u)))])
h, e = np.histogram(d, bins=np.arange(0, 3.01, 0.25))
c = (e[:-1] + e[1:]) / 2
dens = h / (len(u) * 0.25)
for x, emp in zip(c, dens):
    print(f"x={x:.3f}  empirical {emp:.3f}  GUE {1-(np.sin(np.pi*x)/(np.pi*x))**2:.3f}")
s = spacings(u)
print("P(s<0.25):", round(float(np.mean(s < 0.25)), 4), " Poisson:", round(1-np.exp(-0.25), 4))
print("spacing variance:", round(float(s.var()), 3))
