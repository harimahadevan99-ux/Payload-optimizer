# PayloadOptimizer - load target and fuel per tonne

**Idea 6/10 - category: Productivity**

## Problem
Under-loaded trips waste fuel per tonne; overloaded trips accelerate wear and break safety limits. The sweet spot is a payload target around 100-110% of rating.

## What this prototype does
Models fuel per trip as a fixed part plus a payload-dependent part with an overload penalty, finds the optimal payload and quantifies fuel and tonnes lost across real trip distributions.

## KPIs
- Fuel per tonne (L/t)
- Share of under- and overloaded trips
- Extra fuel vs target payload (L)

## Quick start
```bash
python src/demo.py                      # run the demo on synthetic data
python -m unittest discover -s tests -v # run the tests
jupyter notebook notebooks/             # optional: interactive demo
```
Core code is pure Python 3.9+ without dependencies (see `requirements.txt` for optional extras).

## Data
Replace simulate.py with onboard payload-weighing data (for example truck payload meter exports).
All numbers in `src/simulate.py` and `data/sample_data.json` are synthetic and only for demonstration; calibrate against real machine data before drawing conclusions.

## Roadmap
- [ ] Per-loader pass-count coaching
- [ ] Material density by pit zone
- [ ] Tyre wear (TKPH) constraint
- [ ] Link to loader bucket weighing

## Repository structure
| Path | Purpose |
|---|---|
| `src/core.py` | Algorithm / business logic |
| `src/simulate.py` | Synthetic data generator |
| `src/demo.py` | Runnable example |
| `tests/` | Unit tests |
| `data/` | Sample data (put real exports in `data/raw/`) |
| `models_artifacts/` | Trained models and calibration files (empty for now) |
| `notebooks/` | Jupyter demo notebook |
| `.github/workflows/ci.yml` | GitHub Actions: tests + demo on every push |
| `requirements.txt` | Optional dependencies |
| `LICENSE` | MIT |

## Extend with AI
Open the repo in GitHub Codespaces or Claude Code / Copilot and try prompts such as:
- "Read src/core.py and add a CSV loader for telematics exports with column mapping."
- "Add a Streamlit dashboard that visualises the demo output."
- "Write more unit tests for edge cases and sensor dropouts."

## Licence
MIT
