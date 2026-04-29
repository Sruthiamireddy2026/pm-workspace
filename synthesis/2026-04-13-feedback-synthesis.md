# Feedback Synthesis — 2026-04-13

**Source files:**
- `week-1/sample-data/support-tickets.csv` (20 tickets, Feb 3–28 2026)
- `week-1/sample-data/survey-responses.csv` (25 respondents, Feb 1–14 2026)

**Total feedback items reviewed:** 45

---

## Theme 1: Enterprise Security Compliance Gap (SSO + Audit Logs)

- **Frequency:** 4 instances — 2 critical tickets from same $4,200/mo enterprise customer (Meridian Corp), 2 survey respondents at 250–350-person companies
- **Business impact:** Active renewal at risk. Meridian Corp has flagged both SSO (TK-1202) and audit logs (TK-1213) as blockers to contract renewal in Q2. A VP Engineering (350-person company) in the survey states they are "evaluating alternatives." Neither feature is on the near-term roadmap — SSO is not on current roadmap, audit logs are Q3. Timeline vs. renewal date is a collision course.
- **Examples:**
  - "Our security team has mandated that all SaaS tools must support SAML SSO by Q2. Without this, we cannot renew our contract." (TK-1202, Meridian Corp)
  - "No SSO and no audit logs — we can't pass security review... we'll have to switch tools." (Survey R9, Program Manager, 400-person enterprise)
  - "No SSO makes this a non-starter for our security requirements. We're evaluating alternatives." (Survey R16, VP Engineering, 350-person company)
- **Verdict:** Signal — Multiple enterprise customers, clear churn trigger, specific compliance drivers (SOC 2, security mandates). Not a preference — a hard requirement with a deadline.

---

## Theme 2: No Cross-Project Visibility (Portfolio / Resource View)

- **Frequency:** 3 survey respondents, skewing mid-market to enterprise (80–500 employees). Not yet surfacing as support tickets, likely because users work around it.
- **Business impact:** Adoption ceiling for team leads and directors managing multiple projects or people. Users at this level are typically the economic buyers or influencers on renewal decisions. Without a portfolio or resource view, they default to exporting to spreadsheets — reducing DAU and weakening the product's value narrative at QBRs.
- **Examples:**
  - "No cross-project view — I can't see everything due this week in one place." (Survey R2, Marketing Manager, 45-person company)
  - "Reporting is too basic. I can't build custom reports or dashboards. I need to show utilization and velocity to leadership." (Survey R21, Engineering Manager, 200-person company)
  - "No resource management. I can't see who is overloaded or underutilized across projects. We manage 200+ consultants and have zero visibility." (Survey R25, PMO Director, 500-person company)
- **Verdict:** Signal — Consistent across three independent respondents at different company sizes, all describing the same gap from different angles (scheduling, reporting, capacity). Business impact is real: enterprise buyers need this for executive reporting.

---

## Theme 3: Timeline / Gantt View Missing

- **Frequency:** 1 support ticket (TK-1214) + 1 survey respondent (R5) + agent note confirms "top-requested feature in mid-market segment"
- **Business impact:** Adoption blocker for teams doing sequential, dependency-heavy work (design → dev → QA → launch). These teams don't stay on board-only tools past initial evaluation. Directly competitive with Asana and Monday.com, which both have timeline views. Mid-market deal loss risk.
- **Examples:**
  - "We do sequential project work (design > dev > QA > launch) and the board view doesn't show dependencies or timeline. A timeline view would be huge for us." (TK-1214, GreenPath Studios)
  - "Can't do timeline or dependency views." (Survey R5, Product Manager, 200-person SaaS company)
- **Verdict:** Signal — Two independent sources plus internal confirmation it's the top-requested mid-market feature. Competitive gap is clear and well-documented.

---

## Theme 4: Mobile App Unreliability (Android)

- **Frequency:** 1 support ticket (TK-1212) with 2 prior unresolved reports (TK-1056, TK-1098) + 2 survey respondents (R6, R10)
- **Business impact:** Android users are experiencing a degraded product at a recurring rate. This is not a new or isolated bug — three separate tickets over time with no permanent fix. For teams that check tasks on the go, unreliability erodes daily engagement (DAU impact). Risk of app store rating damage if the pattern continues.
- **Examples:**
  - "App crashes 2-3 times per hour on my Samsung Galaxy S24... Still happening. Starting to wonder if Android is a priority for you." (TK-1212, FlowState Labs — references TK-1056, TK-1098)
  - "Mobile app is unreliable on Android." / "Fix the Android app. It crashes constantly." (Survey R6, Designer)
  - "The mobile experience is subpar compared to desktop... My team checks tasks on the go and the app doesn't keep up." (Survey R10, Scrum Master, 100-person company)
- **Verdict:** Signal — Chronic issue with documented repeat reports. Three tickets across time plus two survey respondents. The fact that a customer is questioning platform prioritization is an early churn warning sign.

---

## Theme 5: Notification System Broken and Uncontrollable

- **Frequency:** 1 support ticket (TK-1203) + 1 survey respondent (R1), both daily users
- **Business impact:** Two distinct problems stacked together: a backend bug that makes notification preferences non-functional (settings save but don't persist), and user-reported inbox overwhelm from excessive notifications. The bug workaround requires API access — not viable for most users. Notification fatigue directly reduces DAU quality: users who mute or filter at the inbox level are no longer engaging with task-relevant signals.
- **Examples:**
  - "I went into settings and turned off email notifications for task assignments. I'm still getting them... Getting 30-40 notification emails per day." (TK-1203, GreenPath Studios) — Agent note: known bug, fix scheduled March
  - "The notification system overwhelms my inbox." / "Better notification controls — let me choose exactly what I get notified about." (Survey R1, Project Manager, 150-person company, daily user)
- **Verdict:** Signal — One confirmed bug (backend persistence failure) compounding a UX problem (no granular controls). Together they make notification management functionally broken for power users. High daily-use surface area.

---

## Noise / Not Actioned

- **Dark mode** (TK-1219, Survey R20): Two mentions, but both are cosmetic preferences. No business impact, no churn risk, no adoption blocker. Survey respondent phrases it as "it's 2026" — sentiment, not impact. Deprioritize.
- **Recurring tasks** (TK-1204, Survey R11): Two mentions, both low-urgency. The impact described ("saves me 5–30 minutes/week") is real but marginal and does not affect retention or enterprise sales. Backlog is appropriate.
- **Offline mode** (Survey R13): Single respondent from a niche context (construction job sites). No corroboration in tickets. Weak signal — worth monitoring if the construction/field-work segment grows.
- **Pricing complaints** (Survey R19): One startup respondent, 15-person company. Pricing perception issues in this segment don't generalize to mid-market or enterprise decisions. Noise at this frequency.
- **Collaboration / real-time editing** (Survey R12): One respondent. The described workaround (using Google Docs) suggests low urgency — they've solved it. No corroboration.
- **Accidental data deletion** (TK-1207): Resolved via database recovery. Soft delete with 30-day recovery window is now in critical backlog. Not an open gap — track as in-progress fix, not a theme.

---

## Notes on Data Quality

- Support tickets over-represent bugs relative to survey data because tickets are only submitted when something breaks. Read both sources together to get the full picture.
- Survey sample (n=25) is small. The cross-project visibility theme (Theme 2) appears in 3 of 25 respondents — directionally meaningful but not statistically conclusive. Recommend follow-up interview with 2-3 respondents from that cluster (R21, R25 especially) before scoping work.
- Meridian Corp appears in 3 tickets (TK-1201, TK-1202, TK-1213). Their feedback may be over-represented relative to their actual share of the user base. However, at $4,200/mo with a Q2 renewal in play, their signal should be weighted heavily regardless.
