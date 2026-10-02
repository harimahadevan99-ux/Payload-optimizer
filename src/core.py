def fuel_per_trip(p, rated, base_l=20.0, k_l_per_t=0.12, overload_pen=0.5):
    over = max(0.0, p - rated * 1.10)
    return base_l + k_l_per_t * p + overload_pen * over


def fuel_per_tonne(p, rated):
    return fuel_per_trip(p, rated) / p


def optimal_payload(rated):
    best = min((fuel_per_tonne(rated * f / 100, rated), rated * f / 100) for f in range(50, 131))
    return best[1]


def analyze(trips, rated):
    target = optimal_payload(rated)
    target_lpt = fuel_per_tonne(target, rated)
    n = len(trips)
    under = sum(1 for p in trips if p < 0.9 * rated)
    over = sum(1 for p in trips if p > 1.1 * rated)
    actual_fuel = sum(fuel_per_trip(p, rated) for p in trips)
    ideal_fuel = sum(p * target_lpt for p in trips)
    return {
        "target_payload_t": round(target, 1),
        "mean_payload_t": round(sum(trips) / n, 1),
        "under_pct": round(100 * under / n, 1),
        "over_pct": round(100 * over / n, 1),
        "l_per_t": round(actual_fuel / sum(trips), 3),
        "extra_fuel_l": round(actual_fuel - ideal_fuel, 1),
    }
