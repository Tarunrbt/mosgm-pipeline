"""
MOSGM Git Commit Binding
------------------------

Binds predictions to exact git commit.
Ensures paper-grade provenance.
"""

import subprocess
import json
from pathlib import Path


OUTPUT = Path("git_provenance.json")


def get_git_commit():
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip()
        return commit
    except Exception:
        return "unknown"


def get_git_branch():
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).decode().strip()
        return branch
    except Exception:
        return "unknown"


def create_provenance():
    data = {
        "git_commit": get_git_commit(),
        "git_branch": get_git_branch(),
    }

    with open(OUTPUT, "w") as f:
        json.dump(data, f, indent=2)

    print("\n✅ Git provenance recorded")
    print("Commit:", data["git_commit"][:12])
    print("Branch:", data["git_branch"])


if __name__ == "__main__":
    create_provenance()
