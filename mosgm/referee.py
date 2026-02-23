"""
MOSGM Referee Simulation Mode
-----------------------------

Simulates skeptical peer review tests.
"""

import numpy as np
import subprocess
import sys


def test_random_stability():
    print("\n[Referee Test] Random stability")

    np.random.seed(42)
    a = np.random.normal(size=5)

    np.random.seed(42)
    b = np.random.normal(size=5)

    if np.allclose(a, b):
        print("PASS: deterministic behaviour")
        return True

    print("FAIL: randomness unstable")
    return False


def test_reproduction_pipeline():
    print("\n[Referee Test] Full reproduction")

    result = subprocess.run(
        [sys.executable, "-m", "mosgm.reproduce"]
    )

    return result.returncode == 0


def main():

    print("\n=== MOSGM REFEREE SIMULATION ===")

    results = []

    results.append(test_random_stability())
    results.append(test_reproduction_pipeline())

    if all(results):
        print("\n✅ REFEREE ACCEPTANCE LIKELY")
    else:
        print("\n❌ REFEREE REJECTION RISK")


if __name__ == "__main__":
    main()
