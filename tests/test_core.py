import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import unittest
from simulate import trips
from core import optimal_payload, analyze


class T(unittest.TestCase):
    def test_optimum_near_overload_limit(self):
        self.assertAlmostEqual(optimal_payload(100.0), 110.0, delta=1.0)

    def test_underloading_costs_fuel(self):
        r = analyze(trips(), 100.0)
        self.assertGreater(r["extra_fuel_l"], 0)


if __name__ == "__main__":
    unittest.main()
