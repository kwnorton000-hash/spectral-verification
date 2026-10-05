"""Standard reference case: known-answer control for the test pipeline.

Draws spectra from exactly known ensembles (GOE, GUE random matrices and Poisson)
and runs the same unfolding + KS test. A sound pipeline must label each correctly.
Only the central half of each spectrum is used, unfolded with the semicircle law.
"""
import numpy as np
from common import spacings, report
rng = np.random.default_rng(20261005)
N = 1800

def semicircle_unfold(ev, R):
    x = np.clip(ev / R, -1, 1)
    return N * (0.5 + (x * np.sqrt(1 - x**2) + np.arcsin(x)) / np.pi)

def central(u): k = len(u) // 4; return u[k:-k]

A = rng.normal(size=(N, N)); H = (A + A.T) / 2
report("GOE reference", spacings(central(semicircle_unfold(np.linalg.eigvalsh(H), np.sqrt(2 * N) * np.sqrt(0.5) * np.sqrt(2)))))
B = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); Hc = (B + B.conj().T) / 2
report("GUE reference", spacings(central(semicircle_unfold(np.linalg.eigvalsh(Hc), np.sqrt(4 * N) * np.sqrt(0.5) * np.sqrt(2)))))
report("Poisson reference", spacings(np.sort(rng.uniform(0, N, N))[N//4:-N//4]))
