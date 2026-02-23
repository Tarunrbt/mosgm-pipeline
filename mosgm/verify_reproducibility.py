"""
MOSGM Reproducibility Verification Script
-----------------------------------------

Purpose:
Verify that MOSGM installation and environment
are deterministic and reproducible.
"""

import sys
import platform
import numpy as np


def verify_environment():
    print("\n=== MOSGM ENVIRONMENT CHECK ===")

    print("Python version:", sys.version.split()[0])
    print("Platform:", platform.platform())
    print("NumPy version:", np.__version__)

    # deterministic test
    np.random.seed(42)
    data = np.random.normal(size=5)

    print("\nDeterministic sample:")
    print(data)

    expected = np.array([
        0.49671415,
        -0.1382643,
        0.64768854,
        1.52302986,
        -0.23415337
    ])

    if np.allclose(data, expected):
        print("\n✅ Reproducibility check PASSED")
    else:
        print("\n❌ Reproducibility check FAILED")


if __name__ == "__main__":
    verify_environment()
