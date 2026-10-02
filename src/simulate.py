import random


def trips(n=400, rated=100.0, mean_frac=0.93, sd_frac=0.12, seed=2):
    rnd = random.Random(seed)
    return [max(30.0, rnd.gauss(mean_frac * rated, sd_frac * rated)) for _ in range(n)]
