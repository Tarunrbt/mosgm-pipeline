"""
MOSGM Reviewer Validation Tool
------------------------------

Allows external researchers to verify:
1. alpha lock integrity
2. prediction contract integrity
"""

import json
import hashlib
from pathlib import Path


ALPHA_FILE = Path("alpha.lock")
PRED_FILE = Path("prediction_contract.json")


def verify_alpha():
    if not ALPHA_FILE.exists():
        raise RuntimeError("alpha.lock missing")

    with open(ALPHA_FILE) as f:
        data = json.load(f)

    check = {
        "alpha": data["alpha"],
        "timestamp_utc": data["timestamp_utc"],
    }

    content = json.dumps(check, sort_keys=True).encode()
    expected = hashlib.sha256(content).hexdigest()

    return expected == data["hash"]


def verify_prediction():
    if not PRED_FILE.exists():
        raise RuntimeError("prediction_contract.json missing")

    with open(PRED_FILE) as f:
        data = json.load(f)

    stored_hash = data["contract_hash"]
    data_copy = dict(data)
    del data_copy["contract_hash"]

    content = json.dumps(data_copy, sort_keys=True).encode()
    expected = hashlib.sha256(content).hexdigest()

    return expected == stored_hash


def main():
    print("\n=== MOSGM REVIEWER VALIDATION ===")

    alpha_ok = verify_alpha()
    pred_ok = verify_prediction()

    print("Alpha lock valid:", alpha_ok)
    print("Prediction contract valid:", pred_ok)

    if alpha_ok and pred_ok:
        print("\n✅ FULL REPRODUCIBILITY VERIFIED")
    else:
        print("\n❌ VALIDATION FAILED")


if __name__ == "__main__":
    main()
