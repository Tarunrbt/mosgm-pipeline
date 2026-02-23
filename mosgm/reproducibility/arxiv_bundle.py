"""
MOSGM arXiv Submission Bundle Generator
---------------------------------------

Creates a reproducible submission archive.
"""

import tarfile
from pathlib import Path


OUTPUT = "mosgm_arxiv_bundle.tar.gz"

INCLUDE_FILES = [
    "alpha.lock",
    "prediction_contract.json",
    "git_provenance.json",
    "paper_fingerprint.txt",
]


def create_bundle():

    print("\n=== BUILDING ARXIV BUNDLE ===")

    with tarfile.open(OUTPUT, "w:gz") as tar:

        for fname in INCLUDE_FILES:
            path = Path(fname)

            if not path.exists():
                raise RuntimeError(f"Missing file: {fname}")

            tar.add(fname)
            print("Added:", fname)

    print("\n✅ Bundle created:", OUTPUT)


if __name__ == "__main__":
    create_bundle()
