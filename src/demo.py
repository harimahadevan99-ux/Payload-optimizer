from simulate import trips
from core import analyze

for k, v in analyze(trips(), 100.0).items():
    print(f"{k}: {v}")
