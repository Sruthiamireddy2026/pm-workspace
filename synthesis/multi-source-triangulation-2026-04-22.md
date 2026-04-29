# Multi-Source Research Triangulation
**Date:** 2026-04-22
**Sources:** Support tickets (Feb 2026, n=20), User interview (Rachel Torres, GreenPath Studios, Feb 20), Survey responses (n=25)

---

## Q1: Themes Consistent Across All Three Sources

### 1. Notification system is broken and overwhelming
**Confidence: HIGH** (all 3 sources)

- **Tickets:** TK-1203 — GreenPath Studios; notification toggle saves to frontend but doesn't persist to backend. Customer tried 3 browsers, cleared cache. Receiving 30–40 emails/day.
- **Survey:** Respondent 1 (PM, 150-person tech co) — "The notification system overwhelms my inbox. Better notification controls — let me choose exactly what I get notified about."
- **Interview:** Rachel Torres — "I've created a Gmail filter that archives everything from TaskFlow. Which means I miss important things too." Specifies wanting only 3 notification types; current system is "backwards."

**Signal:** Users aren't just annoyed — they've built workarounds (Gmail filters, ignoring all emails) that create new failure modes. The backend bug is real, but the UX philosophy is also wrong.

---

### 2. Onboarding is too jargon-heavy and assumes PM fluency
**Confidence: HIGH** (all 3 sources)

- **Tickets:** TK-1206 — Designer at LaunchPad Co: "onboarding assumes I know what a 'sprint' and 'backlog' are. I almost gave up during setup."
- **Survey:** Respondent 4 (Operations Manager, healthcare): "Onboarding was terrible — my team almost gave up the first week. Completely redo the onboarding. Assume people don't know PM jargon."
- **Interview:** Rachel Torres — built her own onboarding guide for her team because the official flow didn't work for marketers and designers. Team took 3 weeks to stabilize, 2 months to see value.

**Signal:** The problem isn't just first-run experience — poor onboarding creates lasting adoption gaps. Rachel still has 8/12 team members as passive read-only users 8 months in.

---

## Q2: What Shows Up in Support Tickets But NOT in the Survey

### Billing accuracy errors
- **Ticket:** TK-1210 — Apex Marketing; invoiced for 28 seats, has 24 active users. Happened 2 months in a row despite prior fix (TK-1089). Root cause: system counts deactivated users for 30 days.
- **Why it's absent from survey:** Billing errors are discrete incidents — customers open a ticket and move on. They don't rate their tool poorly in a satisfaction survey over a billing glitch they got credited for. But repeat occurrence signals a trust erosion risk.

### Data loss with no recovery path
- **Ticket:** TK-1207 — NovaTech Industries; team lead accidentally deleted a project containing 3 months of work. No trash, no archive, no undo. Database team recovered from backup manually.
- **Why it's absent from survey:** Catastrophic but infrequent. Survey respondents who experienced this likely churned or haven't had it happen. The absence understates the severity — this is a data safety gap that will recur.

### Integration reliability failures
- **Ticket:** TK-1216 — BrightWave Digital; Slack integration failed silently after a platform update. OAuth token expired, slash command returned success messages while creating nothing.
- **Ticket:** TK-1209 — BrightWave Digital; Google Calendar sync is one-directional.
- **Why absent from survey:** Survey respondents who praise integrations (like Rachel) haven't hit breakage recently. Silent failures are the worst kind — customers think tasks are being created when they aren't.

### API performance degradation
- **Ticket:** TK-1218 — Pinnacle Group; API response times went from ~200ms to 2000ms+ for a customer making 200+ calls/hour. Broke their custom internal tooling.
- **Why absent from survey:** Only affects customers who've built integrations on the API. A small but high-value segment (enterprise, custom workflows). Not surfaced in a general satisfaction survey.

---

## Q3: What the Interview Reveals That Quantitative Data Doesn't

### Users maintain parallel systems as permanent workarounds
Rachel runs "The Real Dashboard" — a Google Sheet she updates twice weekly to get the cross-project view TaskFlow doesn't provide. This is 8 months into using the product. Tickets and surveys surface feature requests; only an interview reveals that users have built permanent alternative infrastructure around the gaps.

### Low team adoption is a hidden churn signal
4 out of 12 of Rachel's team members use TaskFlow actively. The other 8 treat it as read-only. Quantitative data (DAU, logins) would show activity — but wouldn't show that only a minority of licensed seats are generating value. When the renewal conversation comes, the majority of the team hasn't adopted the tool.

### Retention is driven by lock-in, not satisfaction
Rachel explicitly names three retention factors: Slack integration (genuine value), simplicity (preference), and migration cost (8 months of data, 12 people to retrain). The survey and tickets don't capture this. A satisfaction score of 3/5 looks like "at risk" — but the actual churn calculus is "migration cost vs. pain tolerance." The implication: if a competitor reduces migration friction, the retention floor drops.

### The AI feature has untapped potential — and a specific failure mode
Rachel praises the AI task summary feature but describes a clear problem: outputs are generic because the AI has no organizational context. "If the AI knew that 'GTM launch' means a specific process at our company..." Survey respondent 17 hits this too ("AI doesn't know anything about our product context"), but only the interview gives the specific mechanism: the model lacks team-level vocabulary and process definitions, not just general quality issues.

### The onboarding failure compounds over time
Rachel describes a specific trajectory: rough first month, stable at week 3, productive at month 2. The long-tail effect is that habits formed during the learning curve persist — users who never learned to update task status still don't do it 8 months later. Ticket and survey data show onboarding as a first-run problem. The interview shows it's a retention and adoption problem.

---

## Q4: Top 3 Customer Priorities for Leadership

### Priority 1: Fix the notification system end-to-end
**Confidence: HIGH** | Evidence from all 3 sources

The notification bug (backend not persisting settings) combines with a UX philosophy problem (opt-out instead of opt-in). The compounding effect: users who can't fix notifications stop trusting the email channel entirely and miss critical updates.

**Evidence:**
- TK-1203: Known bug in production since before Feb release; fix scheduled for March
- Survey respondent 1: Direct feedback, specific ask for granular controls
- Interview: Rachel has Gmail-filtered all TaskFlow email — she misses @mentions and deadline alerts as a result

**Business impact:** Notification failure breaks the feedback loop between the tool and users. If users stop reading TaskFlow emails, task assignment, deadline reminders, and @mentions all become invisible. This degrades adoption and increases churn risk across all segments.

---

### Priority 2: Unblock enterprise security compliance (SSO + audit logs)
**Confidence: HIGH** | Evidence from 2 source types + named account revenue at risk

This isn't a feature request — it's a renewal blocker for named accounts. Security mandates at enterprise companies aren't negotiable.

**Evidence:**
- TK-1202: Meridian Corp (87 users, $4,200/mo) — SSO required by Q2 or they cannot renew. Currently open, no timeline on roadmap.
- TK-1213: Meridian Corp — audit logs required for SOC 2; flagged as connected to renewal risk
- TK-1208: Pinnacle Group (95 users, $3,800/mo) — RBAC flagged as compliance gap by IT security
- Survey respondents 9 and 16: Two separate enterprise respondents; respondent 16 (VP Engineering, 350-person company, NPS 2) says "SSO. Full stop. Nothing else matters until you have SSO."

**Business impact:** At minimum, one $4,200/mo contract is at direct renewal risk in April. The survey suggests at least 2 additional enterprise accounts are evaluating alternatives. RBAC, SSO, and audit logs are table-stakes for enterprise — the gap is likely blocking expansion sales as well as renewals.

---

### Priority 3: Cross-project portfolio view
**Confidence: MEDIUM** | Evidence from 2 sources (interview + survey)

No support ticket filed directly — customers don't ticket a missing feature the way they ticket a bug. But the workaround behavior (parallel Google Sheets) and survey volume signal this is a widespread, active pain point.

**Evidence:**
- Survey respondent 2 (Marketing Manager, 45-person agency — GreenPath Studios): "No cross-project view — I can't see everything due this week in one place." NPS 6. Would improve: "portfolio or multi-project dashboard view."
- Interview (Rachel Torres, same company): Spends 30 minutes/week manually aggregating across projects. Names it as her #1 improvement request. Cites Monday.com portfolios and Asana's "My Work" view as the benchmark. States she will evaluate switching if she still needs her Google Sheet in a year.
- Survey respondent 25 (PMO Director, 500-person consulting firm): NPS 3, "resource management and capacity planning" — adjacent need at larger scale

**Business impact:** This is a retention signal disguised as a feature request. Rachel is a concrete flight risk with a specific timeline ("a year from now"). The Slack integration is the only thing making her switching cost calculation close — and that's a single feature, not platform depth. Adding portfolio-level views removes the strongest argument to evaluate alternatives.

---

## Confidence Summary

| Finding | Tickets | Survey | Interview | Confidence |
|---|---|---|---|---|
| Notifications broken | ✓ | ✓ | ✓ | High |
| Onboarding jargon | ✓ | ✓ | ✓ | High |
| Enterprise SSO/compliance | ✓ | ✓ | — | High |
| Cross-project view | — | ✓ | ✓ | Medium |
| Gantt/timeline view | ✓ | ✓ | — | Medium |
| Custom fields | ✓ | ✓ | — | Medium |
| Android reliability | ✓ | ✓ | — | Medium |
| AI context/personalization | — | ✓ | ✓ | Medium |
| Billing accuracy | ✓ | — | — | Low |
| Data recovery (soft delete) | ✓ | — | — | Low |
| Integration reliability | ✓ | — | — | Low |
| Bulk task editing | ✓ | ✓ | — | Medium |
| Parallel workaround systems | — | — | ✓ | Low |
| Lock-in vs. satisfaction retention | — | — | ✓ | Low |

---

*Note: "Low confidence" findings from the interview are not unimportant — they represent qualitative depth that surveys and tickets structurally can't capture. Treat them as hypotheses worth validating at scale, not as weak signals.*
