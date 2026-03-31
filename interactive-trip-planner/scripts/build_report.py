import html
import json
import sys
from pathlib import Path


def render_list(items):
    if not items:
        return "<div class='card muted'>鏆傛棤</div>"
    lis = "".join(f"<li>{html.escape(str(item))}</li>" for item in items)
    return f"<div class='list-card'><ul>{lis}</ul></div>"


def render_brief(data):
    parts = []
    brief = data.get("planning_brief", {})
    labels = [("fixed", "鍥哄畾鏉′欢"), ("preferred", "鍋忓ソ"), ("flexible", "鍙皟鏁?), ("excluded", "鎺掗櫎椤?)]
    for key, label in labels:
        parts.append(f"<div class='card'><strong>{label}</strong>{render_list(brief.get(key, []))}</div>")
    return "".join(parts)


def render_options(options):
    if not options:
        return "<div class='card muted'>鏆傛棤鏂规瀵规瘮</div>"
    rows = []
    for opt in options:
        rows.append(
            "<tr>"
            f"<td>{html.escape(opt.get('name', ''))}</td>"
            f"<td>{html.escape(opt.get('strengths', ''))}</td>"
            f"<td>{html.escape(opt.get('tradeoffs', ''))}</td>"
            f"<td>{html.escape(opt.get('verdict', ''))}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr><th>鏂规</th><th>浼樼偣</th><th>浠ｄ环</th><th>缁撹</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def render_itinerary(days):
    if not days:
        return "<div class='card muted'>鏆傛棤姣忔棩琛岀▼</div>"
    cards = []
    for i, day in enumerate(days, start=1):
        title = day.get("title", f"Day {i}")
        body = day.get("body", "")
        cards.append(f"<div class='card'><strong>{html.escape(title)}</strong><p>{html.escape(body)}</p></div>")
    return "".join(cards)


def render_budget(items):
    if not items:
        return "<div class='card muted'>鏆傛棤棰勭畻</div>"
    rows = []
    for item in items:
        rows.append(
            "<tr>"
            f"<td>{html.escape(item.get('name', ''))}</td>"
            f"<td>{html.escape(item.get('value', ''))}</td>"
            f"<td>{html.escape(item.get('note', ''))}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr><th>椤圭洰</th><th>閲戦</th><th>璇存槑</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def render_sources(sources):
    if not sources:
        return "<div class='card muted'>鏆傛棤鏉ユ簮</div>"
    lis = []
    for src in sources:
        label = html.escape(src.get("label", src.get("url", "")))
        url = html.escape(src.get("url", ""))
        lis.append(f"<li><a href='{url}'>{label}</a></li>")
    return f"<div class='card'><ul>{''.join(lis)}</ul></div>"


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: python build_report.py brief.json template.html output.html")
        return 1

    brief_path = Path(sys.argv[1])
    template_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    styles_path = template_path.with_name("styles.css")

    data = json.loads(brief_path.read_text(encoding="utf-8-sig"))
    template = template_path.read_text(encoding="utf-8")
    styles = styles_path.read_text(encoding="utf-8") if styles_path.exists() else ""

    replacements = {
        "{{report_title}}": html.escape(data.get("report_title", "Trip Planning Report")),
        "{{report_subtitle}}": html.escape(data.get("report_subtitle", "")),
        "{{styles_inline}}": styles,
        "{{origin}}": html.escape(data.get("origin", "")),
        "{{dates}}": html.escape(data.get("dates", "")),
        "{{party_size}}": html.escape(data.get("party_size", "")),
        "{{transport_style}}": html.escape(data.get("transport_style", "")),
        "{{recommendation_summary}}": html.escape(data.get("recommendation_summary", "")),
        "{{planning_brief_html}}": render_brief(data),
        "{{options_html}}": render_options(data.get("options", [])),
        "{{itinerary_html}}": render_itinerary(data.get("itinerary_days", [])),
        "{{budget_html}}": render_budget(data.get("budget_items", [])),
        "{{backup_plan_html}}": html.escape(data.get("backup_plan", "")),
        "{{sources_html}}": render_sources(data.get("sources", [])),
    }

    for key, value in replacements.items():
        template = template.replace(key, value)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template, encoding="utf-8")
    print(f"Built report at {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
