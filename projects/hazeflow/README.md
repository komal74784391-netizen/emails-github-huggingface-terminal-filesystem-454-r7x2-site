# Hazeflow

Reference implementation for **Sparse-Sensor Haze Forecasting over Heterogeneous
Terrain** (IEEE Transactions on Geoscience and Remote Sensing, 2026).

## What is included

- `src/data/loader.py` - sparse-station ingestion and gap-aware normalisation
- `src/models/haze_net.py` - hybrid ConvGRU / transformer forecaster
- `src/train.py` - full training entry point (configs under `configs/`)
- `scripts/evaluate.py` - reproduces the numbers in Table 3
- `results/table3.csv` - released metric values

## Quick start

```
pip install -r requirements.txt
python src/train.py --config configs/haze_48h.yaml
python scripts/evaluate.py --ckpt checkpoints/haze_48h.pt
```

## Citation

```bibtex
@article{miller2026haze,
  title   = {Sparse-Sensor Haze Forecasting over Heterogeneous Terrain},
  author  = {Miller, Ronald and Nadar, Priya and Wroblewski, Tomasz},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  year    = {2026},
  note    = {Under review at IGARSS 2025}
}
```
