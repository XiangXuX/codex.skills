import json
import sys
from pathlib import Path


DEFAULT_BRIEF = {
    "report_title": "Trip Planning Report",
    "report_subtitle": "Generated from an interactive travel planning brief.",
    "origin": "",
    "dates": "",
    "party_size": "2 adults",
    "transport_style": "",
    "recommendation_summary": "",
    "planning_brief": {
        "fixed": [],
        "preferred": [],
        "flexible": [],
        "excluded": [],
    },
    "options": [],
    "itinerary_days": [],
    "budget_items": [],
    "backup_plan": "",
    "sources": [],
}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python init_trip_brief.py output.json")
        return 1

    out_path = Path(sys.argv[1])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(DEFAULT_BRIEF, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Initialized trip brief at {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
