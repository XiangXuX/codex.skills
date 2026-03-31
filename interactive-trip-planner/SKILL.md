---
name: interactive-trip-planner
description: Use this skill when the user wants help planning a trip through iterative discussion, comparing destination or routing options, narrowing tradeoffs, and then generating a polished HTML and PDF itinerary report. Trigger when the user provides an origin, trip length, transport preferences, destination ideas, budget, or asks for a travel planning workflow rather than a one-shot answer.
---

# Interactive Trip Planner

This skill turns open-ended travel requests into a structured planning workflow with three phases:

1. Explore: clarify constraints and propose 2-4 plausible trip directions.
2. Converge: help the user make tradeoffs and lock a final trip brief.
3. Deliver: research bookable options and generate an HTML/PDF report.

## What To Do

When this skill triggers:

1. Build a concise trip brief from the user's current inputs.
2. If the brief is incomplete, ask only the next highest-value questions.
3. In the explore phase, propose options, not a single fixed itinerary.
4. In the converge phase, explicitly identify what is fixed, flexible, and excluded.
5. Only after the brief is stable should you research transport, lodging, activities, and pricing.
6. Produce a structured final recommendation and generate a report if the user wants a deliverable.

## Required Planning Discipline

- Optimize for real executability, not maximal coverage.
- Prefer fewer questions with higher decision value.
- Call out date conflicts, transport infeasibility, or overload early.
- Distinguish between inspiration, recommendation, and confirmed bookable options.
- For time-sensitive facts such as prices, schedules, policies, and availability, verify with browsing.

## Phase Guide

### 1. Explore

Use this phase when the user is still deciding where or how to travel.

Collect only what is necessary:
- Origin
- Approximate dates or trip length
- People count
- Budget sensitivity
- Transport preference
- Hard must-haves
- Hard no-go items
- Pace preference

Then propose 2-4 directions using the framework in [references/questioning_framework.md](references/questioning_framework.md).

### 2. Converge

Use this phase when the user starts choosing among options.

Summarize the brief in plain language:
- Fixed
- Preferred
- Flexible
- Excluded

Then apply routing and budget rules from:
- [references/routing_rules.md](references/routing_rules.md)
- [references/budget_rules.md](references/budget_rules.md)

### 3. Deliver

Once the brief is stable:

1. Research bookable transport and lodging.
2. Compare options using the source policy in [references/source_policy.md](references/source_policy.md).
3. Structure the result using [references/report_spec.md](references/report_spec.md).
4. If generating a deliverable, use:
   - [scripts/init_trip_brief.py](scripts/init_trip_brief.py)
   - [scripts/build_report.py](scripts/build_report.py)
   - [scripts/render_pdf.ps1](scripts/render_pdf.ps1)

## When To Read References

- Read [references/workflow.md](references/workflow.md) when shaping the conversation flow.
- Read [references/questioning_framework.md](references/questioning_framework.md) when deciding what to ask next.
- Read [references/source_policy.md](references/source_policy.md) before researching current prices or schedules.
- Read [references/report_spec.md](references/report_spec.md) before assembling the final deliverable.

## Output Standard

Default final deliverable:
- One recommended plan
- One backup plan
- Clear assumptions
- Budget summary
- Transport and lodging comparisons
- Day-by-day itinerary
- Source links

If the user asks for a report, generate HTML first and then render PDF.
