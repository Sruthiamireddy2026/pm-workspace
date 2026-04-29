# Customer Feedback Themes — People Analytics / HR Tech
**Sources:** feedback-synthesis (2026-04-13), multi-source triangulation (2026-04-22)
**Total feedback items reviewed:** 45 (20 support tickets, 25 survey responses, 1 in-depth interview)

---

## Theme 1: No Unified Cross-Workforce View

**Frequency:** 3 survey respondents + 1 in-depth interview + enterprise support ticket pattern
**Pain Level:** High

### The Problem
HR leaders and operations managers overseeing multiple departments, projects, or workforce
segments have no single view that aggregates status across dimensions. In people analytics
terms: you can see headcount in one place, performance in another, and compensation in a
third — but there is no surface that combines them for a Monday morning review or an
executive briefing. Users describe clicking through each project or report individually,
manually aggregating the information they need, and spending 30+ minutes on a task the
tool should do for them.

The gap is compounded by reporting depth. Individual managers can see their own team data.
Directors and VPs cannot get a cross-functional roll-up without exporting and stitching
files together. The higher the user's organizational scope, the worse the tool works for
them — which is exactly backwards for a product that needs to win with economic buyers.

### Customer Quotes
- *"No cross-project view — I can't see everything due this week in one place."*
  — Survey respondent 2, Marketing Manager, 45-person company (NPS 6)
- *"Reporting is too basic. I can't build custom reports or dashboards. I need to show
  utilization and velocity to leadership."*
  — Survey respondent 21, Engineering Manager, 200-person company
- *"No resource management. I can't see who is overloaded or underutilized across projects.
  We manage 200+ consultants and have zero visibility."*
  — Survey respondent 25, PMO Director, 500-person consulting firm (NPS 3)

### What Teams Do Today
Maintain parallel tracking spreadsheets — typically Google Sheets or Excel — updated
manually on a recurring cadence (Monday and Wednesday being the most common pattern). The
spreadsheet holds the cross-functional roll-up the product doesn't provide: one row per
project or team, columns for owner, status, next deadline, and blockers. These are not
temporary workarounds. Users describe maintaining them for 8+ months with no plan to
stop. The spreadsheet becomes permanent shadow infrastructure alongside the paid product.

---

## Theme 2: Enterprise Security Compliance Is a Renewal Blocker, Not a Feature Request

**Frequency:** 4 instances — 2 critical support tickets from the same named enterprise
account ($4,200/mo), 2 survey respondents at 250–350-person companies
**Pain Level:** High (table stakes for enterprise segment; active churn trigger)

### The Problem
HR data carries salary, performance ratings, headcount plans, and personal information
that triggers legal and security requirements at every enterprise account. SAML SSO and
role-based access control are not feature preferences — they are procurement requirements.
Audit logs are required for SOC 2 Type II and are typically mandated before enterprise
contracts are signed, not added later. In the people analytics space specifically,
security is the first conversation, not the fifth.

The cost of this gap is not just pipeline — it is active renewals. Named enterprise
accounts have attached specific deadlines and dollar figures to the requirement. Security
mandates at enterprise companies are not negotiable and do not move because a vendor asks
for more time.

### Customer Quotes
- *"Our security team has mandated that all SaaS tools must support SAML SSO by Q2.
  Without this, we cannot renew our contract."*
  — TK-1202, Meridian Corp (87 users, $4,200/mo, renewal in April)
- *"No SSO and no audit logs — we can't pass security review... we'll have to switch
  tools."*
  — Survey respondent 9, Program Manager, 400-person enterprise software company (NPS 3)
- *"No SSO makes this a non-starter for our security requirements. We're evaluating
  alternatives."*
  — Survey respondent 16, VP Engineering, 350-person company (NPS 2)

### What Teams Do Today
Short-term: waive the requirement internally and accept the risk, pending vendor delivery.
Medium-term: evaluate alternatives in parallel while staying on the current vendor — the
evaluation is already underway before the renewal conversation. Some accounts submit IT
security exceptions with a documented vendor commitment date; if that date passes, the
exception expires and the tool is off the approved list.

---

## Theme 3: Tools Built for Analysts, Adopted by Everyone Else

**Frequency:** 3 sources (support ticket, survey, in-depth interview)
**Pain Level:** High

### The Problem
HR platforms are purchased by HR ops and IT, but used daily by managers, employees, and
business leaders who don't think in data model terms. Tools that assume PM fluency —
sprints, backlogs, story points, data hierarchies — create steep onboarding curves for
the people who are supposed to benefit from them. The result is not just slow time-to-value
at launch. It is a persistent adoption gap: users who struggle during onboarding settle
into minimal-use habits that persist months later.

In a typical deployment, the team lead or admin becomes the tool's power user and everyone
else becomes read-only. The team lead ends up doing data entry for the whole team —
effectively a human sync engine between meetings and the system. The tool is billing for
seats that are not being used. When the renewal conversation comes, the utilization data
does not support the price.

### Customer Quotes
- *"The onboarding flow assumes I know what a 'sprint' and 'backlog' are. I'm a designer,
  not a PM. I almost gave up during setup."*
  — TK-1206, Designer at LaunchPad Co
- *"Onboarding was terrible — my team almost gave up the first week. Completely redo the
  onboarding. Assume people don't know PM jargon."*
  — Survey respondent 4, Operations Manager, 80-person healthcare company (NPS 4)
- *"I ended up making my own onboarding guide for my team. A Google Doc that says 'here's
  how to see your tasks, here's how to mark something done, ignore everything else for
  now.' That worked better than the official onboarding."*
  — Rachel Torres, Marketing Ops Manager, GreenPath Studios (8 months on platform)

### What Teams Do Today
Team leads build shadow onboarding documentation — their own guides that strip out
technical terminology and reduce the tool to the 2–3 actions non-technical users actually
need. Official onboarding is bypassed or supplemented. Training scopes down to the
minimum viable feature set rather than the product's full capability. Non-technical users
settle into passive read-only use that does not improve over time.

---

## Theme 4: Notification Systems That Cry Wolf

**Frequency:** Confirmed in all 3 source types (support ticket, survey, interview)
**Pain Level:** High

### The Problem
Notification systems default to alerting on everything and rely on users to turn things
off. In practice, users cannot get the settings to work — in this dataset, a confirmed
backend bug means notification preferences save to the front end but do not persist to the
back end. Users receive 30–40 system emails per day regardless of their settings.

The compounding problem is what users do next: they create inbox filters that archive all
emails from the system. This solves the noise problem but creates a new failure mode —
critical signals (task assignments, overdue deadlines, direct @mentions) are now invisible.
The notification channel is broken as a communication medium, which degrades daily
engagement and leads to missed action items.

In HR tech specifically, this failure mode has direct operational consequences: missed
performance review deadlines, approval requests that expire without action, and compliance
workflows that stall because the responsible manager never saw the alert.

### Customer Quotes
- *"I've created a Gmail filter that archives everything from TaskFlow. Which means I miss
  important things too."*
  — Rachel Torres, Marketing Ops Manager (describes wanting notifications only for
  new assignments, overdue items owned by her, and direct @mentions)
- *"The notification system overwhelms my inbox. Better notification controls — let me
  choose exactly what I get notified about."*
  — Survey respondent 1, Project Manager, 150-person technology company (NPS 8, daily user)
- *"I went into settings and turned off email notifications for task assignments. I'm still
  getting them... Getting 30–40 notification emails per day."*
  — TK-1203, GreenPath Studios (confirmed backend bug: toggle saves to frontend state,
  does not persist to backend)

### What Teams Do Today
Email filters that archive all system notifications (creates the missed-signal problem).
Some users check the tool directly twice a day on a manual schedule instead of relying on
push alerts. Power users have set up API-based notification preferences as a workaround —
not viable for non-technical users. The majority simply tolerate the noise and miss
important items.

---

## Theme 5: AI Features Are Useful but Organizationally Blind

**Frequency:** 2 sources (in-depth interview + survey); Medium confidence
**Pain Level:** Medium

### The Problem
AI features in analytics and project management tools produce outputs that are generically
correct but organizationally irrelevant. The model does not know what "GTM launch" means
at a specific company, that "Tier 1 campaign" triggers a VP approval workflow, or that
certain role titles carry specific process obligations. Users spend as much time editing
AI outputs to fit their context as they would have spent writing from scratch.

This is not a quality problem — users in this dataset praise the core AI capability. It
is a context problem: the AI has no organizational memory. Every session starts from zero.
Companies have terminology, hierarchies, and process norms that are not encoded anywhere
the model can access. The result is outputs that require expert editing to be useful,
which limits AI adoption to power users who know what good looks like and have time to
revise.

In people analytics specifically, this gap is acute: workforce data is deeply
organization-specific. Generic headcount insights do not account for the company's span
of control targets, its promotion velocity norms, or its attrition benchmarks. Without
that context, AI recommendations are directionally plausible but not actionable.

### Customer Quotes
- *"The summary feature is surprisingly helpful for my Monday reviews. But I wish I could
  tell it about our team's context. It generates generic descriptions, and I always have
  to edit them to match our terminology."*
  — Rachel Torres, Marketing Ops Manager (specifically: the AI does not know that "GTM
  launch" or "Tier 1 campaign" carry specific process implications at her company)
- *"AI features are surprisingly useful — but AI doesn't know anything about our product
  context. Suggestions are generic."*
  — Survey respondent 17, Product Manager, 120-person SaaS company (NPS 7)

### What Teams Do Today
Manual editing of every AI output before use. Some team leads maintain a separate reference
document with company terminology and process norms that they paste into prompts as context.
Non-technical users avoid AI features entirely because the editing overhead removes the time
benefit. There is no system-level mechanism for encoding organizational context — it is
individual and undocumented.

---

## Theme 6: The Spreadsheet Is Never Going Away

**Frequency:** Interview (primary signal); corroborated by enterprise ticket pattern
**Pain Level:** High (leading churn indicator)

### The Problem
When a product does not provide the views users need, users build permanent infrastructure
outside the product to fill the gap. This is not a workaround — it is the system. Users
maintain parallel tracking spreadsheets for months or years, updating them on a recurring
schedule, and have no plan to stop. The paid product handles task management; the
spreadsheet handles visibility and aggregation.

The churn implication is structural. Retention in this dataset is driven by migration cost
(data history, retraining cost, integration dependencies) rather than product satisfaction.
When a user describes their primary retention factor as "the migration cost is too high,"
the product is one competitor-driven migration-assist offer away from losing the account.
The spreadsheet is the most visible signal that the product is not fulfilling its core
promise — and the user knows it.

In HR tech, the equivalent is pervasive: HR teams export workforce data to Excel for every
non-trivial analysis. Headcount models, attrition forecasts, compensation benchmarks, and
org design scenarios all happen outside the HR platform. The platform is a system of record;
Excel is the system of insight.

### Customer Quotes
- *"I have a Google Sheet called 'The Real Dashboard' and it has one row per project with
  columns for: project name, owner, status, next deadline, and blockers. I update it every
  Monday and Wednesday."*
  — Rachel Torres, Marketing Ops Manager (8 months into using the paid product)
- *"If I still need my Google Sheet a year from now, I'll seriously evaluate switching.
  The whole point of buying a project management tool is to not maintain a parallel
  system."*
  — Rachel Torres (explicit churn trigger with a named timeline)
- *"When I log in, the dashboard spinner runs for 3+ minutes... My team of 12 relies on
  the dashboard view every morning. We've had to start using spreadsheets as a workaround."*
  — TK-1201, Meridian Corp, enterprise account (parallel spreadsheet adopted as a
  response to a product performance failure, not by choice)

### What Teams Do Today
The workaround is the behavior — there is no secondary workaround. The spreadsheet is
maintained indefinitely, updated on a recurring schedule, and treated as the authoritative
source for cross-functional visibility. In some cases the spreadsheet is shared with
leadership as the team's official status view, which further normalizes it and reduces
the perceived need to change.

---

## Summary Table

| Theme | Frequency | Pain Level | Churn Risk |
|---|---|---|---|
| No unified cross-workforce view | High | High | Medium — active flight risk for team leads |
| Enterprise security compliance gap | Medium (concentrated) | Critical | High — named accounts, deadline-driven |
| Tools built for analysts, not users | High | High | Medium — adoption deficit weakens renewal ROI |
| Notification systems that cry wolf | High | High | Medium — degrades daily engagement over time |
| AI features are organizationally blind | Medium | Medium | Low-Medium — limits AI adoption ceiling |
| The spreadsheet is never going away | Low frequency, high signal | High | High — parallel system = explicit churn trigger |
