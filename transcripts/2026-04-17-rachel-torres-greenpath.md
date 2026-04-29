# Transcript: User Research Interview — Marketing Ops Manager, GreenPath Studios
**Date:** 2026-02-20
**Source file:** `week-1/sample-data/user-interview-transcript.md`
**Participant:** Rachel Torres, Marketing Operations Manager — GreenPath Studios (45 employees, Series A)
**Length/depth:** 32 minutes, ~1,100 words, single participant, well-structured

---

## Synthesis
Rachel is a power user keeping the product alive through manual compensating behaviors. She manages 15–20 concurrent projects for a 12-person team, but only 4 of 12 team members actively update the tool — the rest treat it as read-only, leaving Rachel as the de facto human sync layer. Her two biggest pain points (no cross-project view, broken notifications) have both produced active workarounds: a parallel Google Sheet she calls "The Real Dashboard" and a Gmail filter that archives all TaskFlow emails — which she acknowledges also causes her to miss important things. She's not ready to leave — migration cost and the Slack integration anchor her — but she has named a concrete, self-imposed churn trigger: if she still needs her Google Sheet in a year, she'll seriously evaluate switching. That's a specific, time-bounded signal that should be tracked.

---

## Pain Points
- **No cross-project visibility:** "There's no single view that shows me 'here's everything due this week across all projects.' I end up keeping a parallel Google Sheet... It's dumb but it's the only way I can see across everything." Takes 30 minutes every Monday morning just to check project status.
- **Notification system is functionally broken:** Gets 40+ emails/day; turned off "task assignment" notifications but still receives them. Backend bug (confirmed in TK-1203) compounded by a UX model that's opt-out, not opt-in.
- **Low team adoption baked in:** Only 4 of 12 team members actively update TaskFlow. "The rest treat it as read-only." Habits formed in early weeks have calcified — Rachel does the updating for the whole team.
- **Manual standup sync:** Takes notes in Google Docs during the Monday standup, then spends 20 minutes afterward creating tasks, updating statuses, and reassigning in TaskFlow. "I'm basically a human sync engine between the meeting and the tool."
- **Onboarding too complex for non-PM teams:** Setup flow uses PM jargon (epics, sprints, story points) that marketers and designers don't recognize. "I ended up making my own onboarding guide for my team."

---

## Feature Requests / Asks
- **Cross-project portfolio dashboard (high priority):** "A dashboard that shows me: across all my projects, what's due this week, what's overdue, and where there's a blocker. Grouped by project. With the ability to click into any task and update it right there." Stated as her #1 change.
- **Notification opt-in model (high priority):** Start quiet, let users turn things on. Her explicit want: new assignment, overdue items, @mentions only. "The current system tries to notify you about everything and then asks you to turn things off, which is backwards."
- **Simplified, role-aware onboarding (high priority):** Task-first onboarding — "here's how to see your tasks and mark things done" — not a feature tour. Has 2 new hires coming and is dreading the current process.

---

## Good to Have Features
- **Context-aware AI:** "If the AI knew that 'GTM launch' means a specific process at our company, or that 'Tier 1 campaign' means it needs VP approval, the output would be much more useful." Currently uses the AI summary feature and finds it helpful, but always edits the output for team-specific terminology. Not a blocker — she uses the feature anyway.

---

## Workarounds
- **"The Real Dashboard" (Google Sheet):** One row per project; columns for name, owner, status, next deadline, blockers. Updated every Monday and Wednesday. — implies gap in cross-project / portfolio visibility.
- **Custom onboarding guide (Google Doc):** Created by Rachel herself; strips out all advanced features, focuses only on viewing assigned tasks and marking them done. — implies gap in role-appropriate onboarding paths.
- **Gmail filter archiving all TaskFlow emails:** Created because notification volume was unmanageable after settings fixes failed. Side effect: she misses time-sensitive alerts. — implies gap in granular notification controls and backend persistence.
- **Manual post-standup sync (20 min/week):** Notes taken in Google Docs during meeting, then manually entered into TaskFlow. — implies gap in meeting-to-task workflow (possibly a Slack or AI-assist opportunity).

---

## Positive Signals
- **Slack integration:** "Genuinely great... saves my team probably 2 hours a week. That's our killer feature." Mentioned unprompted as the primary reason she hasn't left.
- **AI task summary:** "Surprisingly helpful for my Monday reviews." Uses it regularly despite the generic output issue.
- **Simplicity and speed:** "When TaskFlow works, it's clean and fast. Monday.com and Asana feel bloated to me." Simplicity is a deliberate preference, not a gap.
- **8 months of data / migration cost:** "Moving 200+ projects and re-training 12 people is a project in itself." Currently a retention anchor.

---

## Deal Breakers
- **Cross-project dashboard (or she evaluates switching):** "If I still need my Google Sheet a year from now, I'll seriously evaluate switching. The whole point of buying a project management tool is to not maintain a parallel system." — condition: February 2027. This is a named, time-bounded churn trigger.

---

## Competitive Signals
- **Monday.com:** Mentioned unprompted as having a "my work" view. She has looked at switching. Rejected it as "bloated." — context: came up when explaining why she still uses her Google Sheet workaround; not a hot evaluation.
- **Asana:** Mentioned alongside Monday.com as having "portfolios." Also rejected as bloated. — context: same moment; evaluated and deprioritized due to migration cost and complexity preference.
- **Notable:** She has actively evaluated alternatives and chosen to stay — primarily because of migration cost and Slack integration, not because competitors are worse. If migration cost drops (e.g., an import tool) or Slack integration breaks again, the calculus changes.

---

## Objections / Risks
- **Adoption is a team problem, not just a product problem:** 8 of 12 people are read-only by habit now. Even if the product improves, behavior change at GreenPath will require re-onboarding or a new trigger event (e.g., new hires).
- **Hiring 2 new people soon:** Dreading the onboarding process. This is a near-term risk — bad onboarding of new hires could accelerate her evaluation of switching.

---

## Decisions & Commitments
- None explicitly made during the session.

---

## Open Questions
- Would Rachel beta test a cross-project portfolio view if built? She's a high-quality feedback source given her workaround sophistication.
- Is the low adoption (8/12 read-only) recoverable with product changes, or is it a change management problem that lives at GreenPath?
- Are the 2 incoming hires a trigger to re-evaluate tools before onboarding them into a system she's frustrated with?

---

## Action Items
- [ ] Sarah (TaskFlow PM): Flag Rachel's churn trigger and Feb 2027 timeline to product team — cross-project dashboard is tied to a named renewal risk.
- [ ] Sarah: Confirm TK-1203 (notification settings bug) fix timeline with engineering and follow up with Rachel.
- [ ] Sarah: Consider Rachel as a candidate for portfolio view beta / design research given depth of her workaround.

---

## Top Quotes

> "I end up keeping a parallel Google Sheet that I update manually. It's dumb but it's the only way I can see across everything." — Marketing Ops Manager

> "I'm basically a human sync engine between the meeting and the tool." — Marketing Ops Manager

> "The current system tries to notify you about everything and then asks you to turn things off, which is backwards. It should start quiet and let me turn things on." — Marketing Ops Manager

> "If I still need my Google Sheet a year from now, I'll seriously evaluate switching. The whole point of buying a project management tool is to not maintain a parallel system." — Marketing Ops Manager

> "When TaskFlow works, it's clean and fast. Monday.com and Asana feel bloated to me." — Marketing Ops Manager

---

## Signal / Noise Notes
- **"Monday.com and Asana feel bloated":** Don't over-index on this as a competitive dismissal. She said this in the context of explaining why she *hasn't* switched — it's actually a retention signal. The real competitive risk is that she's already done the evaluation and migration cost is the only thing keeping her.
- **AI context-awareness request:** Genuine product feedback, but low urgency — she uses the feature and finds it helpful. Treat as good-to-have, not a near-term priority driver.
- **Low team adoption (8/12 read-only):** Partly a product problem (onboarding friction), partly a change management problem at GreenPath. Don't attribute all of it to product gaps — some of it is organizational inertia that better onboarding won't fully fix.
