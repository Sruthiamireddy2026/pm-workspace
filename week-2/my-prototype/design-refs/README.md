# Design References

## Reference Products

### Linear — clean status lists and information density

**Why referenced:** Linear proves you can surface 20+ actionable items at high density
without visual overwhelm. No decorative chrome, tight rows, color-coded status that reads
in one glance. The target persona (marketing ops managers, program leads) increasingly uses
Linear or works alongside teams that do.

**Specific interaction to lift:** The issue list row — status badge left-anchored
(color-coded: red for blocked, orange/yellow for overdue, blue for in-progress), task title
center-weighted, metadata (assignee, due date) right-aligned. One line per item. Apply this
row pattern to each task in the summary. The visual hierarchy — status → title → metadata —
is the right read order for a team lead scanning for what needs them.

**Also borrow:** The flat list structure that makes item count immediately visible. A team
lead should know "there are 6 things needing attention across 4 projects" within 2 seconds
of the summary loading, before reading a single item.

**What not to copy:** Linear's left-sidebar project tree and breadcrumb navigation — that
is orientation scaffolding for a full app, not needed inside a digest view.

---

### Slack — digest format and weekly summary style

**Why referenced:** Slack's weekly activity digest and app notification surfaces are the
closest existing consumer pattern to what this summary should feel like. They put
action-required items first, group by source, and use bold section headers as anchors.
Most users on the target persona already read Slack daily — leveraging that mental model
reduces cognitive load.

**Specific interaction to lift:** The section-per-source structure: bold project name as
the header, followed by brief bullet items with just enough context to act without clicking.
Each item is one line. Apply to the summary: `## Brand Refresh` as the project header,
then `[BLOCKED] Legal review — Unassigned — due 2026-04-24 — Legal team unresponsive 5 days`
as a bullet. Also borrow Slack's "muted" header treatment for projects with only
due-this-week items (lower urgency than blocked/overdue) — a lighter font weight or muted
color on the project header signals "worth seeing, not on fire."

**What not to copy:** Slack's threaded reply model or inbox-queue UX. The summary is a
point-in-time snapshot — not a conversation thread, not a list of items the user must
triage and clear. Once read, it is done.

---

### Notion — dashboard card layout

**Why referenced:** Notion's home page card treatment and weekly planning templates
establish a "week as a self-contained unit" frame that matches how team leads already think
about their Monday review. The card boundary creates a clean reading context: you open the
summary, you read the card, you close it.

**Specific interaction to lift:** The muted-background card container that holds generated
or structured content, visually separated from editable fields. Use this to distinguish the
AI-generated summary from the inline task edit panel — the user should immediately know
which parts are AI-generated (read the card) vs. editable (open the panel). Also borrow
Notion's week-as-a-card framing: each generated summary is its own card with a header
showing the date range and a "generated on [date]" timestamp. Past summaries are accessible
as previous cards — lightweight history without a separate archive feature.

**What not to copy:** Notion's freeform block editing canvas. The summary is structured
output. Users update tasks via the inline edit panel, not by editing the summary text.

---

### Workday — HR data display patterns

**Why referenced:** The target persona (mid-market ops managers, marketing leads, people
ops) already uses Workday. Workday's "Awaiting Your Action" home panel is the closest
existing product experience to what this summary should feel like — it groups pending items
by category, shows owner and due date inline, and routes to detail without losing context.
Borrowing Workday's visual vocabulary reduces the learning curve for users who already
know the pattern.

**Specific interaction to lift:** The priority grouping — items requiring immediate action
appear first with a red/orange urgency signal, items due this week follow (neutral), items
coming up are muted or absent. Apply this hierarchy within each project group:
blocked → overdue → due this week. Also borrow Workday's compact person-name + task + due
date row format, which packs the three most important facts into one line without
abbreviating any of them.

**What not to copy:** Workday's form-based data entry UI. The reference is the viewing and
action-routing experience, not the editing flows. Workday's input forms are notoriously
slow and form-heavy — the inline task edit panel should be the opposite: 2–3 fields, one
save action, return to summary.

---

## Avoid List

- **Jira's dense metadata rows** — story points, sprint labels, fix versions, components per
  item. Wrong cognitive load for a weekly digest. Users stall at the table instead of
  acting on it.
- **Monday.com's color grid** — reads like a spreadsheet, requires horizontal scrolling,
  implies a configuration burden. This summary must require zero setup.
- **Full Asana portfolio configuration UI** — the "add projects to this portfolio" setup
  screen adds friction before any value is delivered. The summary must generate
  automatically with no user configuration.
- **BI dashboard widget grid** — implies "watch this continuously." The summary is a
  periodic digest, not a live monitoring view. Widgets suggest ongoing observation;
  a card suggests a moment of review.
- **Notification inbox / queue model** — don't make the summary feel like a list of items
  the user must triage and clear. Each generated summary is a snapshot. Once the team lead
  has read it and acted, it is complete.
- **Workday form-based editing** — the viewing patterns are the reference; the editing
  patterns are not. Keep the inline task update panel fast and minimal.

---

## Seeded Data Spec

The prototype must load with this sample data so the feature is testable and demo-ready
without placeholder text.

| Field | Sample value | Notes |
|---|---|---|
| Team lead | Rachel Torres | Primary research persona from interview |
| Active projects | 8 projects | Enough to show grouping value; not so many the view becomes unmanageable |
| Project statuses | 3 on_track, 3 at_risk, 2 blocked | Mix that generates a non-trivial summary with all three label types visible |
| Project names | Q2 Email Campaign, Brand Refresh, GTM Launch — Product A, Event Series Planning, Paid Ads Q2, Customer Newsletter, Sales Enablement Deck, Social Media Audit | Marketing ops naming from Rachel Torres interview — avoids "Project 1" placeholder feel |
| Tasks due this week | 6 tasks across 4 projects | Shows the date-filter logic is doing real work; not all projects surface |
| Overdue tasks | 2 tasks in 2 separate projects | Distributed across projects, not stacked in one |
| Blocked tasks | 3 tasks across 2 projects | One with a written blocker reason; one without (tests the no-blocker-reason display state) |
| Assignees | Marcus Lee, Dana Kim, Priya Nair, Rachel Torres, TBD | Real names for most; TBD on one to show the Unassigned display state |
| Due dates | Mix of past (overdue), current week, and 2+ weeks out | Makes the filtering logic visually demonstrable in the prototype |
