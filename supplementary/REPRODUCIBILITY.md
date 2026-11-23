# Supplementary reproducibility notes

**Model.** Three energy levels `(0, 1, sqrt(2))`, or detuning `alpha=sqrt(2)-2` relative to `(0,1,2)`; initial populations `(1/3,1/3,1/3)`.

**Reference and sampling.** A 12-by-12 phase grid gives 144 reference rays Q. Candidate times are 0,0.1,...,100. For each reference ray select its closest observed candidate in Fubini–Study distance; retain distinct selected times and call their ray set X.

**Stability budget.** The finite-set Hausdorff discrepancy `h=d_H(Q,X)` bounds Vietoris–Rips diagram bottleneck distance by `2h`. Reference H1 persistence lifetime greater than `4h` forces a matching non-diagonal observed bar.

**Recorded values.** h=0.10122093528134704; two reference lifetimes each 0.7088107626207171; positive survival margin=0.3039270214953289; observation horizon T=100.

**Limitations.** This is a finite-reference certificate, not a model-free topological reconstruction or experimental finite-shot guarantee. Numerical code uses floating-point arithmetic. Irrationality is a statement about the symbolic detuning, not floating-point values. No DOI is claimed.

**Run.** `python code/reference_certificate.py` recreates all data tables and PDF/PNG persistence figures in `results/` and `figures/`.
