"""Pull closed pydantic issues that carry exactly one type label into evals/data/issues.jsonl."""
import json
import os
import sys
from pathlib import Path

import httpx

REPO = "pydantic/pydantic"
TYPE_LABELS = {"bug V2", "feature request", "question", "documentation"}
OUT = Path(__file__).parent / "data" / "issues.jsonl"


def main(target: int = 400) -> None:
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    rows, page = [], 1
    with httpx.Client(headers=headers, timeout=30) as client:
        while len(rows) < target and page <= 30:
            resp = client.get(
                f"https://api.github.com/repos/{REPO}/issues",
                params={"state": "closed", "per_page": 100, "page": page, "sort": "created", "direction": "desc"},
            )
            resp.raise_for_status()
            batch = resp.json()
            if not batch:
                break
            for issue in batch:
                if "pull_request" in issue:
                    continue
                labels = [label["name"] for label in issue["labels"]]
                types = TYPE_LABELS.intersection(labels)
                if len(types) != 1:
                    continue
                rows.append({
                    "number": issue["number"],
                    "title": issue["title"],
                    "body": (issue["body"] or "")[:4000],
                    "type": types.pop(),
                    "labels": labels,
                    "created_at": issue["created_at"],
                    "state_reason": issue.get("state_reason"),
                })
            page += 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        for row in rows[:target]:
            f.write(json.dumps(row) + "\n")
    print(f"wrote {min(len(rows), target)} issues -> {OUT}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 400)
