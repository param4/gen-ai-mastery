"""Pull closed pydantic issues that carry exactly one type label into evals/data/issues.jsonl."""
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

import httpx

load_dotenv()
REPO = "pydantic/pydantic"
TYPE_LABELS = {"bug V2", "feature request", "question", "documentation"}
OUT = Path(__file__).parent / "data" / "issues.jsonl"


def main(target: int = 400) -> None:
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    print("Token found; using authenticated requests (rate limit 5000/hour)..." if "Authorization" in headers else "No token found, using unauthenticated requests (rate limit 60/hour)...")
    rows = []
    count = target // len(TYPE_LABELS)
    for label in sorted(TYPE_LABELS):
        fetched = fetch_issues_with_exactly_one_type_label(count, headers, label)
        print(f"{label}: {len(fetched)}")
        rows.extend(fetched)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"wrote {len(rows)} issues -> {OUT}")


def fetch_issues_with_exactly_one_type_label(target: int, headers: dict, label: str) -> list:
    rows, page = [], 1
    with httpx.Client(headers=headers, timeout=30) as client:
        while len(rows) < target and page <= 30:
            resp = client.get(
                f"https://api.github.com/repos/{REPO}/issues",
                params={"state": "closed", "per_page": 100, "page": page, "sort": "created", "direction": "desc", "labels": label},
            )
            resp.raise_for_status()
            batch = resp.json()
            if not batch:
                break
            for issue in batch:
                if "pull_request" in issue:
                    continue
                labels = [lbl["name"] for lbl in issue["labels"]]
                types = TYPE_LABELS.intersection(labels)
                if len(types) != 1:
                    continue
                rows.append({
                    "number": issue["number"],
                    "title": issue["title"],
                    "body": (issue["body"] or "")[:4000],
                    "type": types.pop(),
                    # type label stripped so it can't leak into classifier input
                    "labels": [lbl for lbl in labels if lbl not in TYPE_LABELS],
                    "created_at": issue["created_at"],
                    "state_reason": issue.get("state_reason"),
                })
                if len(rows) >= target:
                    break
            page += 1
    return rows

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 400)
