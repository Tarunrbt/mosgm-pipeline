"""
MOSGM Alpha Lock System
-----------------------

Freezes calibration parameter alpha.
Predictions cannot run without locked alpha.
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path


LOCKFILE = Path("alpha.lock")


class AlphaLock:

    @staticmethod
    def create(alpha: float):
        data = {
            "alpha": alpha,
            "timestamp_utc": datetime.utcnow().isoformat(),
        }

        content = json.dumps(data, sort_keys=True).encode()
        data["hash"] = hashlib.sha256(content).hexdigest()

        with open(LOCKFILE, "w") as f:
            json.dump(data, f, indent=2)

        print("\n✅ Alpha locked")
        print("α =", alpha)
        print("Hash:", data["hash"][:16], "...")

    @staticmethod
    def load():
        if not LOCKFILE.exists():
            raise RuntimeError(
                "No alpha.lock found. Calibration must be performed first."
            )

        with open(LOCKFILE) as f:
            data = json.load(f)

        # verify integrity
        check = {
            "alpha": data["alpha"],
            "timestamp_utc": data["timestamp_utc"],
        }

        content = json.dumps(check, sort_keys=True).encode()
        expected_hash = hashlib.sha256(content).hexdigest()

        if expected_hash != data["hash"]:
            raise RuntimeError("Alpha lockfile corrupted!")

        return data["alpha"]


if __name__ == "__main__":
    AlphaLock.create(alpha=0.1)
