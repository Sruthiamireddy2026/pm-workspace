# Transcript: User Research — Marketing Operations Manager
**Date:** 2026-02-20  
**Source file:** week-1/sample-data/user-interview-transcript.md  
**Participant:** Rachel Torres, Marketing Operations Manager — GreenPath Studios (45 employees, Series A)  
**Length/depth:** 32 minutes, ~1,100 words — good depth; covers friction, workarounds, competitive context, and AI features

---

## Synthesis

Rachel's core problem is that TaskFlow is a task-level tool she's trying to use as a portfolio management tool — and the gap forces her to maintain a parallel Google Sheet she calls "The Real Dashboard." She's an active, technically proficient user who has compensated for the product's weaknesses rather than churning, which means the problems she surfaces are real and load-bearing. The Slack integration is the retention anchor; without it, the switching math would change. Her churn trigger is explicit and time-bound: if she still needs the Google Sheet in a year, she'll evaluate switching. What would surprise a reader: only 4 of 12 team members use TaskFlow actively — Rachel is manually syncing the rest, meaning the adoption problem is much larger than usage stats alone would show.

---

## Pain Points

- **No cross-project view** `High`: "There's no single view that shows me 'here's everything due this week across all projects.' I end up keeping a parallel Google Sheet." — Direct churn trigger stated; active workaround consuming ~1 hr/week.
- **Notification system broken** `High`: "I turned off 'task assignment' notifications and I still get emails when someone assigns me a task." Settings don't work; she's now blind to all TaskFlow emails via Gmail filter.
- **PM-centric onboarding terminology** `Medium`: "The onboarding assumes everyone knows PM terminology — 'epics,' 'sprints,' 'story points.' My team is marketers and designers." Active pain but not cited as churn risk; she workarounded it.
- **Low team adoption / Rachel as human sync engine** `Medium`: 8 of 12 team members treat TaskFlow as read-only; Rachel manually updates status after every standup. Structural account fragility, not immediate churn signal.
- **AI outputs lack context-awareness** `Low`: Generic descriptions require manual editing every time; useful enough that she keeps using it.

---

## Feature Requests / Asks

- **Portfolio / cross-project operational dashboard** `High`: Direct — "A dashboard that shows me: across all my projects, what's due this week, what's overdue, and where there's a blocker. Grouped by project. With the ability to click into any task and update it right there." Explicit churn condition attached.
- **Notification system defaults flipped (opt-in, not opt-out)** `High`: Direct — "The current system tries to notify you about everything and then asks you to turn things off, which is backwards. It should start quiet and let me turn things on." Wants only: new assignment, owned task overdue, @mentions.
- **Simplified role-appropriate onboarding** `Medium`: Direct — "If the official onboarding was 'here's how to see your tasks and mark things done, you're done' instead of 'here's every feature we have,' my new hires could be productive in a day instead of a month." Hiring 2 people soon; pain is imminent.

---

## Good to Have Features

- **Context-aware AI descriptions** `Low`: "If the AI knew that 'GTM launch' means a specific process at our company, or that 'Tier 1 campaign' means it needs VP approval, the output would be much more useful." — Uses AI features already; edits output as a habit. No urgency, no churn signal.

---

## Workarounds

- **"The Real Dashboard" (Google Sheet)** `High`: Manually maintained spreadsheet — one row per project, columns for name/owner/status/next deadline/blockers — updated every Monday and Wednesday. Implies gap in: cross-project operational view. Direct churn trigger if not resolved.
- **Gmail filter archiving all TaskFlow emails** `High`: Created because notification settings don't function reliably. Implies gap in: notification system reliability. Side effect: she misses genuinely important notifications.
- **Custom onboarding Google Doc** `Medium`: Rachel wrote her own team-facing onboarding guide because the official flow uses PM terminology. Implies gap in: non-PM persona onboarding. Workaround works but doesn't scale (hiring more people).
- **Manual standup-to-TaskFlow sync** `Medium`: Rachel updates tasks in TaskFlow after every standup (~20 min) because 8/12 team members won't. Implies gap in: ease of use / adoption for non-power users.

---

## Positive Signals

- **Slack integration** `High`: "Being able to create tasks from Slack messages saves my team probably 2 hours a week. That's our killer feature." — Primary stated reason for not switching. Loss of this would likely trigger immediate evaluation.
- **Speed and cleanliness** `Medium`: "When TaskFlow works, it's clean and fast. Monday.com and Asana feel bloated to me." — Perception-level differentiator; holds weight in switching calculus.
- **AI task summary feature** `Low`: "The summary feature is surprisingly helpful for my Monday reviews." — Uses it regularly; not a retention driver but an emerging positive signal for AI investment.

---

## Deal Breakers

- **Cross-project view still missing in ~1 year** `High`: "If I still need my Google Sheet a year from now, I'll seriously evaluate switching. The whole point of buying a project management tool is to not maintain a parallel system." — Condition: ~Q1 2027, time-based.

---

## Competitive Signals

- **Monday.com** `High`: "Monday.com has a 'my work' view." — Mentioned unprompted while describing the cross-project gap. Has evaluated switching; held back by migration cost only.
- **Asana** `Medium`: "Asana has portfolios." — Also evaluated; rejected as "bloated." Lower threat than Monday.com given her perception, but migration cost is doing the retention work, not satisfaction.

---

## Objections / Risks

- **Migration cost as a decaying barrier** `High`: "Moving 200+ projects and re-training 12 people is a project in itself." — Currently the primary reason she stays, but she has a stated time-bound churn trigger. If cross-project view isn't addressed, this barrier weakens.
- **Shallow team adoption / single point of failure** `High`: 8 of 12 users passive. If Rachel leaves GreenPath, the account likely churns — no institutional adoption holding it.
- **Notification workaround creates invisible disengagement** `Medium`: Gmail filter means Rachel isn't reliably seeing TaskFlow emails. She may be missing real updates and not know it — a silent satisfaction eroder.

---

## Decisions & Commitments

- `Low` Sarah (PM, TaskFlow): Acknowledged AI context-awareness feedback as "great feedback" — no commitment made, no follow-up action stated.

---

## Open Questions

- `High` Does TaskFlow have account-level visibility into write-active vs. read-only users? Rachel's account may look healthy on MAU while being structurally fragile.
- `High` Is the notification settings bug (opt-out not functioning) a known issue or specific to Rachel's account?
- `Medium` What is the actual migration cost/effort if Monday.com or Asana offered a migration concierge — would that change Rachel's calculus?
- `Low` Are there other marketing ops / non-PM personas on TaskFlow hitting the same onboarding friction?

---

## Action Items

- [ ] `High` Sarah: Investigate notification settings bug — "task assignment off" not suppressing assignment emails. Confirm if known issue or Rachel-specific.
- [ ] `High` Sarah: Escalate cross-project / portfolio view to roadmap prioritization; Rachel is a canary for a likely common mid-market pain with a stated churn clock.
- [ ] `Medium` Sarah: Evaluate onboarding flow redesign for non-PM personas (marketers, designers, ops teams).
- [ ] `Low` Sarah: Flag AI context-awareness (team-specific terminology) as a product enhancement for the AI features team.

---

## Top Quotes

> "I end up keeping a parallel Google Sheet that I update manually. It's dumb but it's the only way I can see across everything." — Marketing Ops Manager

> "I turned off 'task assignment' notifications and I still get emails when someone assigns me a task. At this point I've created a Gmail filter that archives everything from TaskFlow. Which means I miss important things too." — Marketing Ops Manager

> "The current system tries to notify you about everything and then asks you to turn things off, which is backwards. It should start quiet and let me turn things on." — Marketing Ops Manager

> "If I still need my Google Sheet a year from now, I'll seriously evaluate switching. The whole point of buying a project management tool is to not maintain a parallel system." — Marketing Ops Manager

> "The Slack integration is genuinely great. Being able to create tasks from Slack messages saves my team probably 2 hours a week. That's our killer feature." — Marketing Ops Manager

---

## Signal / Noise Notes

- **"Monday.com and Asana feel bloated"** `Low`: Treat as perception, not a feature-level evaluation. Rachel hasn't used either in a real work context. Don't let this suppress a deeper competitive analysis.
- **"About 3 weeks before people stopped asking me basic questions"** `Low`: One data point on onboarding time-to-productivity. Marketers/designers at a 45-person Series A aren't representative of all non-PM segments — could vary significantly.
- **"I'm technical-ish"** `Low`: Rachel's 25-minute individual onboarding time is likely a floor, not typical for her segment. Weight her solo friction as best-case for this persona.
