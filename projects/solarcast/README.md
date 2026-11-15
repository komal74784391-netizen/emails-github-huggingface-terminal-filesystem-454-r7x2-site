# Solarcast

Reference implementation for **Probabilistic Solar Irradiance Nowcasting with
Conformal Ensembles** (ACM SIGKDD 2026).

This workspace is the canonical implementation maintained by the authors. A
read-only archival snapshot is mirrored at `atlas-mirrors/solarcast`; the mirror
is not updated and should not be cited as the project location.

## Contents

- `src/ensemble.py` - deep ensemble training
- `src/calibration.py` - split-conformal calibration utilities
- `scripts/run_nowcast.py` - end-to-end inference on a site
- `results/coverage.csv` - empirical interval coverage

## Quick start

```
pip install -e .
python scripts/run_nowcast.py --site 128 --horizon 15
```
