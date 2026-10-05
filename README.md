# Spectral Verification — Riemann zeros vs heavy-nucleus resonances

Companion repository to the Verification Ledger at
https://quantumenergyresearch.org/verification — K.W. Norton.

Everything here is meant to be rerun by anyone, including results that count against the proposal.

## Contents

| Path | What it is |
|---|---|
| `data/zeta_zeros_first2000.txt` | First 2000 nontrivial zeros of ζ (A. Odlyzko's published tables) |
| `data/u238_swave_endf_b_vii1.csv` | ²³⁸U s-wave (ℓ=0, J=½⁺) Reich–Moore resonances, ENDF/B-VII.1 (NNDC, Brookhaven), extracted unchanged |
| `scripts/zeros_pair_correlation.py` | Pair correlation of the first 400 zeros vs Montgomery's GUE prediction |
| `scripts/nuclear_test.py` | Nearest-neighbour spacing test: ²³⁸U vs the zeros vs GOE / GUE / Poisson |
| `scripts/reference_case.py` | Known-answer control: GOE, GUE and Poisson spectra must be labelled correctly by the same pipeline |
| `results/*.txt` | Output of each script as committed |

## Run

```
pip install numpy scipy
cd scripts
python reference_case.py          # control first: pipeline must pass
python zeros_pair_correlation.py
python nuclear_test.py
```

## Results (2026-10-05)

- **Control:** the pipeline correctly identifies GOE, GUE and Poisson reference spectra.
- **Zeros:** fit GUE (KS 0.044 < 0.045 critical), reject GOE and Poisson.
- **²³⁸U, 897 levels to 20 keV, D = 22.18 eV:** fit GOE (KS 0.040), reject GUE and Poisson.
- **Direct comparison:** the two spacing distributions differ (two-sample KS 0.138, p ≈ 7 × 10⁻⁸).

Interpretation: both spectra show level repulsion, but of different symmetry class (β=1 vs β=2).
A one-to-one identification of zeros with nuclear levels is not supported by this test.
Any proposed mapping must explicitly account for the GOE–GUE difference.

## Limitations

- Nearest-neighbour spacings only; Δ₃ and number variance not yet tested.
- Evaluated resonance sets miss weak levels and may contain p-wave contamination (uranium variance 0.36 vs GOE 0.29).
- One nucleus only.

## Data provenance

ENDF/B-VII.1 is a public evaluation distributed by the National Nuclear Data Center. Riemann zeros from
Odlyzko, https://www-users.cse.umn.edu/~odlyzko/zeta_tables/. Code is MIT-licensed.
