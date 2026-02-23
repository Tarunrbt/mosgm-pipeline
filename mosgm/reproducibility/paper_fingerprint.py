"""
MOSGM Paper Citation Fingerprint
--------------------------------

Creates DOI-grade identity for a scientific result.
"""

import hashlib
from pathlib import Path


FILES = [
    "alpha.lock",
    "prediction_contract.json",
    "git_provenance.json",
]


def compute_fingerprint():

    hasher = hashlib.sha256()

    for fname in FILES:
        path = Path(fname)

        if not path.exists():
            raise RuntimeError(f"Missing required file: {fname}")

        with open(path, "rb") as f:
            hasher.update(f.read())

    return hasher.hexdigest()


def main():

    print("\n=== MOSGM PAPER FINGERPRINT ===")

    fingerprint = compute_fingerprint()

    print("Scientific Fingerprint:")
    print(fingerprint)

    short_id = fingerprint[:16]
    print("\nCitation ID:", short_id)

    with open("paper_fingerprint.txt", "w") as f:
        f.write(fingerprint)

    print("\n✅ Fingerprint saved → paper_fingerprint.txt")


if __name__ == "__main__":
    main()
