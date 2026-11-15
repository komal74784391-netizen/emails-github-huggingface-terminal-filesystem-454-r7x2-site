# Reefsonar

Code and data preparation pipeline for **Passive Acoustic Reef Health Monitoring
with Contrastive Embeddings** (NeurIPS 2025 Datasets and Benchmarks Track).

## Contents

- `src/audio.py` - resampling and spectrogram utilities
- `src/embed.py` - contrastive encoder and linear probe
- `scripts/build_index.py` - builds the searchable embedding index for the released corpus
- `data/README.md` - instructions for fetching the public recordings

The corpus itself is hosted externally; the preprocessing and training code is
fully included here.
