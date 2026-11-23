"""Reproduce finite phase-grid reference and positive two-cycle certificate.
The irrational spectral parameter is represented in floating point: this is
a numerical proxy, not exact-arithmetic or interval-arithmetic certification.
"""
from pathlib import Path
import json
import numpy as np
from persistence_core import rays, fsdist, vr_h1

P = Path(__file__).resolve().parents[1]
(P / "results").mkdir(exist_ok=True)
(P / "figures").mkdir(exist_ok=True)
w = np.array([1 / 3] * 3)
M, T, step = 12, 100., 0.1
theta = 2 * np.pi * np.arange(M) / M
a, b = np.meshgrid(theta, theta, indexing="ij")
Q = np.sqrt(w)[None, :] * np.exp(
    -1j * np.column_stack([np.zeros(a.size), a.ravel(), b.ravel()])
)
reference_bars = vr_h1(fsdist(Q))
alpha = float(np.sqrt(2) - 2)
times = np.arange(0, T + step / 2, step)
candidate_rays = rays([0, 1, 2 + alpha], times, w)
pairwise = fsdist(Q, candidate_rays)
chosen = np.unique(np.argmin(pairwise, axis=1))
X = candidate_rays[chosen]
chosen_times = times[chosen]
D = fsdist(Q, X)
hqx = float(np.max(np.min(D, axis=1)))
hxq = float(np.max(np.min(D, axis=0)))
h = max(hqx, hxq)
observed_bars = vr_h1(fsdist(X))
margin = float((reference_bars[1, 1] - reference_bars[1, 0]) - 4 * h)
assert len(reference_bars) >= 2 and margin > 0
summary = {
    "reference_grid_M": M,
    "reference_size": len(Q),
    "candidate_time_step": step,
    "horizon": T,
    "candidate_times": len(times),
    "observed_times": len(X),
    "irrational_parameter_expression": "sqrt(2)-2",
    "float_alpha": alpha,
    "directed_ref_to_observed": hqx,
    "directed_observed_to_ref": hxq,
    "hausdorff_ref_observed": h,
    "bottleneck_bound": 2 * h,
    "reference_first_lifetimes": (reference_bars[:2, 1] - reference_bars[:2, 0]).tolist(),
    "observed_first_lifetimes": (observed_bars[:2, 1] - observed_bars[:2, 0]).tolist(),
    "certified_margin": margin,
    "mesh_bound_to_continuous_closure": float(np.sqrt(2 / 3) * np.pi / M),
    "precision_caveat": "floating-point numerical certificate; exact rank of symbolic sqrt(2)-2 is mathematical",
}
(P / "results" / "positive_certificate.json").write_text(json.dumps(summary, indent=2))
np.savetxt(P / "results" / "selected_times.csv", chosen_times, delimiter=",",
           header="selected_time", comments="")
np.savetxt(P / "results" / "reference_bars_H1.csv", reference_bars,
           delimiter=",", header="birth,death", comments="")
np.savetxt(P / "results" / "observed_bars_H1.csv", observed_bars,
           delimiter=",", header="birth,death", comments="")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6.1, 4))
for bars, label, marker in [
    (reference_bars, "Phase-grid reference", "o"),
    (observed_bars, "Scheduled trajectory", "x"),
]:
    ax.scatter(bars[:, 0], bars[:, 1], s=22, alpha=0.7, label=label, marker=marker)
ax.plot([0, 1.35], [0, 1.35], ls="--", lw=0.8, color="gray")
ax.set(xlabel="Birth (Fubini-Study distance)", ylabel="Death (Fubini-Study distance)",
       title="Persistence transfer (144 points each)")
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
fig.savefig(P / "figures" / "positive_detection.pdf")
fig.savefig(P / "figures" / "positive_detection.png", dpi=180)
print(json.dumps(summary, indent=2))
