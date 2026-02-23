"""
MOSGM One-Command Reproduction
------------------------------

Single command that reproduces
the full scientific state.
"""

import subprocess
import sys


def run_step(name, command):
    print(f"\n--- {name} ---")

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\n❌ FAILED at step: {name}")
        sys.exit(1)

    print("✅ OK")


def main():

    print("\n=== MOSGM FULL REPRODUCTION ===")

    # Step 1 — Environment check
    run_step(
        "Environment verification",
        [sys.executable, "-m", "mosgm.verify_reproducibility"],
    )

    # Step 2 — Alpha lock validation
    run_step(
        "Reviewer validation",
        [sys.executable, "-m", "mosgm.reproducibility.validate_contract"],
    )

    # Step 3 — Git provenance capture
    run_step(
        "Git provenance",
        [sys.executable, "-m", "mosgm.reproducibility.git_binding"],
    )

    print("\n✅ FULL PIPELINE REPRODUCED")
    print("Scientific state verified.")


if __name__ == "__main__":
    main()
