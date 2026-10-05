"""U-238 s-wave resonances (ENDF/B-VII.1) vs Riemann zeros: nearest-neighbour spacing test."""
import numpy as np, pathlib
from scipy.stats import ks_2samp
from common import unfold_zeros, unfold_linear, spacings, report
D = pathlib.Path(__file__).resolve().parent.parent / "data"
E = np.loadtxt(D / "u238_swave_endf_b_vii1.csv", delimiter=",", comments="#", skiprows=2, usecols=0)
E = np.sort(E[(E > 0) & (E <= 2.0e4)])
u, Dmean = unfold_linear(E)
print(f"U-238 s-wave levels 0-20 keV: {len(E)}, mean spacing D = {Dmean:.2f} eV")
a = spacings(u)
b = spacings(unfold_zeros(np.loadtxt(D / "zeta_zeros_first2000.txt")[:len(E)]))
report("U-238", a); report("zeros", b)
print("two-sample KS U-238 vs zeros:", ks_2samp(a, b))
