# General stability and a positive detection certificate

Reproducibility materials for the manuscript **Finite-Observation Topological Resolution Bounds for Near-Resonant Projective Quantum Dynamics**.

## Contents
- `code/persistence_core.py`: projective quantum states, Fubini–Study distances and standalone Vietoris–Rips H1 reduction over F2.
- `code/reference_certificate.py`: 12 × 12 phase-grid reference, observation schedule and persistence calculations.
- `results/positive_certificate.json`: numerical certificate and parameters.
- Additional CSV and figures are reproducible by executing the scripts.
- Manuscript code/data link: https://github.com/divinelybless/General-Stability-and-a-Positive-Detection-Certificate

## Reproduce
Install Python 3 with numpy, scipy and matplotlib; at the repository root run:
```bash
python code/reference_certificate.py
```
This recreates CSV outputs and PDF/PNG figures under `results/` and `figures/`.

The symbolic parameter `sqrt(2)-2` is irrational, but computed in floating point. The numerical certificate is not an interval-arithmetic proof; no archival DOI is claimed.

## Declarations
The authors declare no competing interests. AI assistance was used for grammatical restructuring and writing computer code. The authors are responsible for the scientific content, code verification and conclusions.
