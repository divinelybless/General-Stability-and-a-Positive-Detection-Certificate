# Analytic non-product phase-grid lower bound (revision 2026-11-24)

For the equal-population Fubini–Study phase torus in CP²,
`Phi(a,b)=[(1,e^{-ia},e^{-ib})/sqrt(3)]`, its exact ambient metric satisfies

`sin²(d_FS(Phi(0,0),Phi(a,b)))=(4/9)(sin²(a/2)+sin²(b/2)+sin²((a-b)/2))`.

This metric includes a mixed term at infinitesimal order and is **not** a product metric. Its intrinsic coordinates have `ds²=(2/9)(da²+db²-da db)`.

Let `Q_M` be the M-by-M uniform phase grid, M≥4, with its induced FS metric. Define
- `r_M=acos(sqrt((5+4cos(2pi/M))/9))`
- `r_*=acos(2/3)`

**Two persistent H1 classes:** For `r_M<r<r_*`, every VR_r(Q_M) has two coordinate-loop H1 classes which remain independent under inclusions. Therefore at least two barcode intervals have lifetime ≥`r_*-r_M`.

**Proof sketch:** If a VR edge has FS length below `r_*`, its principal angular difference in either phase coordinate has absolute value below `2pi/3`: maximize the modulus of the three-term overlap over the other phase to get `(1+2cos(|a|/2))/3`. On triangles, the sum of the three principal increments is a multiple of `2pi` of absolute value <`2pi`, hence vanishes. Choosing phase representatives at vertices converts angular increments into integer 1-cocycles, which may be reduced mod 2. The two coordinate grid loops exist for radii >`r_M` and evaluate in the identity matrix on the mod-2 cocycles, so both persist up to `r_*`.

At M=12:
- `r_M=0.2465058555`
- `r_*=0.8410686706`
- guaranteed reference lifetime ≥`0.5945628151`
- observed finite-set Hausdorff distance `h=0.1012209353`
- positive analytic margin ≥`0.5945628151-4h=0.1896790740`
- allowable deterministic per-ray reconstruction error `delta<0.0474197684` from the analytic lower bound.
- using the computed reference lifetime `0.7088107626`, allowable `delta<0.0759817554`.

The numerical reference persistence matching (2 reference bars and 67 observed bars) has a bottleneck-optimal matching cost ~`0.0588071551`: the two long reference bars pair with the two long observed bars, the other observed bars with the diagonal.

These are finite-reference mathematical statements and deterministic error bounds; no interval arithmetic or experimental tomography guarantee is claimed. The full proof and updated matching figure are included in the manuscript revision package associated with this analysis.
