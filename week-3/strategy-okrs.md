# FY2026 Vision, Strategy, and OKRs
**Company:** Beacon Analytics
**Prepared by:** Product & Strategy
**Last updated:** April 2026
**Audience:** Leadership team and board

---

## What We Do

Beacon Analytics is a people analytics platform for mid-market companies (250–2,500
employees) that turns workforce data into decisions HR leaders and business managers can
act on — without needing a data science team or a six-month implementation.

We connect to HRIS, ATS, payroll, and performance systems and surface AI-generated
insights on headcount, attrition risk, compensation equity, and workforce planning.
Our differentiation is organizational context: our AI learns how a company names its
roles, structures its teams, and defines its processes — so insights are specific and
actionable, not generic.

We are a Series B company ($22M ARR, 68 employees, raised $38M total). Our primary
competition is Visier (enterprise-heavy, expensive to implement), Workday Analytics
(bundled into HCM suite, inaccessible to non-Workday shops), and Dayforce AI Workspace
(new entrant with PE-fueled velocity that is directly targeting our segment).

---

## Mission

Make every HR leader as analytically capable as the best-resourced teams in their industry
— without requiring them to become data scientists.

---

## The Honest State of Play

We are in a good position and a precarious one simultaneously.

The good: mid-market is underserved. Visier prices out of the segment. Workday requires
buying an entire HCM suite. Neither has cracked the "HR leader who is not a data analyst"
use case. We have product-market fit with the HR director persona — our NPS among that
segment is 47, churn is 8%, and our top accounts expand at 130% NRR.

The precarious: Dayforce just took $12.3B from Thoma Bravo and launched AI Workspace with
people analytics agents in February. Workday shipped Sana — described as "superintelligence
for work" — and is moving down-market aggressively. Two well-capitalized competitors are
converging on our segment simultaneously. They will outspend us on features. We cannot
win that race.

What we can win: time-to-value, organizational specificity, and serving the personas that
enterprise tools structurally underserve. The window is 18–24 months before enterprise
tooling adapts to mid-market sufficiently. We need to use that window to build a moat, not
just grow revenue.

The OKRs below reflect that tension. They are ambitious. Several are in conflict with
each other. That is intentional — the leadership team needs to make real trade-offs this
year, and the OKRs should force those conversations rather than paper over them.

---

## FY2026 Goals and Key Results

### Goal 1: Become the analytics layer HR leaders actually use — not the one IT bought

We define success here as depth of engagement, not breadth of deployment. A customer with
12 monthly active HR leaders is more defensible than a customer with 200 licensed seats
and 14 active users.

**KR 1.1:** Weekly active HR director/VP users as a share of licensed seats reaches 55%
by Q4 (current baseline: 34%). This is the single most important number in the business.
Low weekly active rate is what makes renewals feel optional.

**KR 1.2:** Time-to-first-meaningful-insight drops from 23 days (current, post-sales-hand-off)
to 7 days by Q3. Define "meaningful" as: at least one AI-generated insight rated "relevant
to a decision I made this week" by the user.

**KR 1.3:** 70% of net-new logos complete onboarding without white-glove CS intervention
by Q4 (current: 41%). This is both a capacity constraint and a product quality signal.
If onboarding requires a human, the product is not explaining itself.

**KR 1.4:** NPS among HR director persona reaches 55 by EOY (current: 47). NPS below 50
does not generate the referral flywheel we need to compete without an enterprise sales
motion.

---

### Goal 2: Ship organizational memory before Workday and Dayforce do

This is our asymmetric bet. Large platforms generate generic AI outputs because they cannot
learn an individual company's vocabulary, process norms, and role taxonomies at the model
level. We can, because we are not trying to serve 10,000 companies with one model. The
company that solves "AI that knows your org" in people analytics builds a moat that is
extremely hard to replicate at enterprise scale.

**KR 2.1:** Org Context Engine (working name) ships to beta customers by Q3. Definition of
done: AI outputs for beta accounts reference company-specific role names, team structures,
and named workflows at a rate judges score ≥4.0 on a 5-point specificity rubric (same
eval harness methodology used for product evals).

**KR 2.2:** AI output accuracy in LLM-as-judge evals holds at ≥4.5/5 on factual accuracy
across all test case difficulty levels, including adversarial inputs. We cannot trade
accuracy for specificity. If the Org Context Engine introduces hallucination, it ships
without the context features.

**KR 2.3:** 60% of weekly active HR director users in accounts with Org Context enabled
rate AI outputs as "directly usable without editing" within 60 days of feature launch
(compared to current baseline of 31% who rate outputs as directly usable).

---

### Goal 3: Close the compliance gap before it closes us out of enterprise expansion

We are not primarily an enterprise company. But we have 23 accounts with 500+ employees
where expansion is stalled because we lack SAML SSO, RBAC, or audit logging. At $8,400
average ACV for those accounts, that is $193K in identified expansion ARR that cannot
move until we ship. There are also two accounts up for renewal in Q2 that have explicitly
named security as a condition of renewal.

We have deferred this work for two planning cycles. We cannot defer it again.

**KR 3.1:** SAML SSO ships GA by May 31, 2026. This is a hard date, not a target. Two
named accounts have renewal conversations in June. If SSO is not GA before those
conversations, we lose both accounts.

**KR 3.2:** Role-based access control (viewer, editor, admin, department-scoped) ships
GA by Q3.

**KR 3.3:** Audit log (who accessed what data, when, and what changed) ships to beta by
Q3, GA by Q4. Required for SOC 2 Type II, which is blocked until this ships.

**KR 3.4:** Retain 100% of the 6 accounts that have named security as a blocker in
renewal or expansion conversations. These are known; we are tracking them in Salesforce.
Losing any of them is a failure of execution, not market dynamics.

---

### Goal 4: Grow ARR to $32M without proportional headcount growth

We raised $38M total. We have approximately 22 months of runway at current burn. We need
to reach $32M ARR — the threshold our board has set as the condition for a Series C on
favorable terms — without hiring our way there. We have 68 people today. We plan to end
FY2026 at 74. Every point of ARR growth above $22M has to come from product efficiency
and retention, not headcount.

**KR 4.1:** Net Revenue Retention reaches 118% by EOY (current: 107%). The delta between
107% and 118% is expansion from existing accounts — primarily from unlocking the stalled
enterprise expansion described in Goal 3 and from Org Context driving deeper engagement
in current accounts.

**KR 4.2:** Gross margin improves from 67% to 72% by EOY. Primary lever: reduce the
CS-hours-per-account required for onboarding and QBRs as self-serve improves. Secondary
lever: infrastructure cost optimization as we migrate off the legacy connector architecture.

**KR 4.3:** Average contract value for new logos increases from $18,400 to $24,000 by Q4.
Mechanism: Org Context and compliance features move us out of a pure mid-market price band
and let us compete for the 500–2,500 employee segment on value, not price.

---

## Strategic Bets

### Bet 1: Organizational Memory Is the Moat

Every major competitor is shipping AI features. Workday has Sana. Dayforce has AI
Workspace. Visier has connected their data layer to MCP. What none of them have — and
structurally cannot have at their scale — is an AI that knows *your* company specifically.

When a Workday customer asks "why is attrition up in my engineering org," they get an
answer calibrated to the average of 10,000 Workday customers' engineering orgs. When a
Beacon customer asks the same question, the answer will know that their engineering org
uses "IC4" to mean a senior engineer, that the Seattle office has different attrition
dynamics than Austin, and that the most recent reorg affected two teams whose exit
interview data is already in the system.

This is the bet: invest disproportionately in Org Context Engine — the infrastructure for
encoding and retrieving company-specific vocabulary, org structure, and process norms —
before the large platforms figure out how to do this at scale. The window is 18–24 months.
After that, Workday will have enough data and model budget to close the gap. We need to
be the default choice in mid-market by then, with enough switching cost built in that
context migration is a real barrier.

The risk: we are betting on a technical approach (per-org context storage and retrieval)
that adds infrastructure complexity and potential accuracy risk. If we ship specificity at
the cost of accuracy, we will have built a product that confidently says wrong things. The
eval harness and the accuracy gate in KR 2.2 exist to prevent exactly that failure mode.

---

### Bet 2: Mid-Market-Native, Not Enterprise-Lite

The conventional product strategy in this space is to build for enterprise and adapt down.
Visier is an enterprise product. Workday is an enterprise suite. Even Dayforce, which
historically served mid-market, is now PE-backed and moving upmarket with its AI Workspace.

We are going the other direction. Mid-market HR leaders are not a simplified version of
enterprise HR leaders — they have a different relationship to data (more hands-on, less
delegated to analysts), a different tolerance for implementation timelines (weeks, not
months), and a different set of workflows (they are the analyst and the decision-maker
simultaneously). Building for this persona means starting from their workflow, not from
a feature parity checklist against enterprise tools.

Concretely: this means opinionated defaults instead of infinite configurability, 7-day
onboarding instead of 6-month implementations, and AI-generated summaries that surface
the answer instead of dashboards that require the user to find it. The UX is the product.
If an HR director cannot get a meaningful insight in their first 20 minutes, we have failed
— regardless of what the feature set looks like in a sales demo.

The risk: this positioning is a ceiling as well as a floor. If we optimize for the HR
director persona, we will always struggle with IT buyers, security teams, and procurement
committees who want configurability and control. That tension is real and does not go away.
We are accepting a constraint on our enterprise ceiling in exchange for a stronger
mid-market position.

---

### Bet 3: From Insight to Action in the Same Surface

The current competitive frame in analytics is "show me the data vs. help me understand the
data." The next frame is "understand the data vs. act on it without leaving the tool."
Power BI shipped Translytical Task Flows in 2026 — the ability to write data back to source
systems from a BI report. Workday's Sana takes actions autonomously. The direction of the
market is clear: analytics that do not connect to action will be table stakes, not
differentiation.

For Beacon, this means shipping the ability to take a workforce action — open a req,
initiate a review cycle, flag a compensation outlier for manager review, update a
headcount plan — directly from an insight surface, without switching tools. The insight
and the action live together. The current state (insight in Beacon, action in the HRIS,
documentation in a spreadsheet) is the exact workflow friction we are positioned to
eliminate.

This is a Q4 bet, not a Q2 bet. It requires API write access to HRIS systems we currently
only read from. It requires a trust bar we have not yet established with customers around
AI-initiated actions. And it requires alignment with the HRIS vendors, some of whom will
view this as competitive. We are naming it as a strategic direction now so that
infrastructure and partnership decisions made in H1 are made with H2 in mind.

---

## Key Constraints

### 1. Headcount: 68 People Competing Against Thousands

Workday shipped 460+ features in their 2026 R1 release. We have 12 engineers. We will
never win on feature count and should stop trying. Every roadmap conversation that begins
with "but Visier has X" is a trap. The constraint is real: we can ship 3–4 significant
features per quarter, not 40. This means ruthless prioritization, not just good
prioritization. Something important is not getting built this year. The leadership team
needs to name what that is rather than leaving it as subtext in the backlog.

The practical implication for this OKR set: Goal 2 (Org Context Engine) and Goal 3
(compliance infrastructure) are in direct competition for the same engineering capacity.
They cannot both be fully resourced at the same time. The sequencing decision — SSO in
May, then Org Context in Q3, then RBAC and audit logs in Q3–Q4 — is an intentional
choice, not an accident of planning. If SSO slips, everything behind it slips.

### 2. Legacy Connector Architecture

Our data integration layer was built in 2021 for a world of scheduled batch syncs and
REST API pulls. The market has moved to zero-copy data sharing, live data products, and
event-driven pipelines. Workday Data Cloud, Snowflake, and Databricks all offer patterns
we currently cannot match. Every quarter we do not address this is a quarter we accumulate
more distance from where the market is going.

The constraint is that rewriting the connector layer is a 6–9 month infrastructure project
that produces no user-visible features. It is real work that cannot be deferred indefinitely,
but in a year where we are racing to ship Org Context and compliance features, it will not
get the investment it needs. The risk we are accepting: one or two major connector failures
or performance incidents this year as the legacy architecture strains under load. We are
managing this with monitoring and incident response readiness, not by fixing the root cause.

### 3. Budget: We Are Not Thoma Bravo

Dayforce's PE acquisition gives them a war chest and an aggressive mandate. They will price
aggressively to take share, accelerate feature development, and potentially acquire
companies in adjacent spaces (compensation data, labor market intelligence, skills
taxonomies) that would deepen their analytics capability. We cannot match that on spend.

What we can do: be surgical about where we spend. Our R&D budget is concentrated on Org
Context and compliance — the two bets that are most defensible against a well-funded
competitor. We are not building a scheduling module, a learning management integration, or
a mobile app this year, even though customers have asked for all three. We are investing in
the two things a PE-backed acquirer cannot buy overnight: organizational context depth and
mid-market user trust.

The constraint also applies to GTM. We cannot afford a field sales motion. Our growth
model is product-led, CS-assisted, and referral-fueled. If we cannot improve NPS from 47
to 55 — KR 1.4 — the referral engine does not turn, and we cannot hit $32M ARR without
a sales investment we cannot make.

### 4. Market Compression: Getting Squeezed from Both Directions

Enterprise is coming down. Workday is moving mid-market with Sana. Dayforce, historically
mid-market, is now PE-backed and moving up. AI-native startups with no legacy architecture
are building people analytics features faster than we can. The market that was mid-market's
opportunity two years ago is becoming contested from three directions simultaneously.

The window for building a defensible position is shorter than it was. We are not yet
losing deals to AI-native startups — but we are seeing them appear in competitive RFPs
for the first time this year. The 18–24 month window referenced in Bet 1 is not
conservative; it may be optimistic. Speed of execution is a constraint and a strategy
simultaneously.

### 5. The Spreadsheet Problem Is Also Our Problem

Customer feedback is unambiguous: people analytics tools, including ours, have not
eliminated the spreadsheet. HR leaders export data to Excel for every non-trivial analysis.
Headcount models, attrition scenarios, compensation benchmarks — all happen outside our
platform. We call this a competitor problem in sales calls. It is also a product failure.

The constraint: fixing this requires Bet 3 (action in the insight surface) to be real, not
just directional. And Bet 3 is a Q4 bet. Which means for the first three quarters of this
year, we are shipping features that do not address the root cause of the biggest risk to
our renewal rate. The leadership team should be honest about this rather than messaging
that the roadmap solves it. The spreadsheet will still be the default workflow for most
of our customers at the end of FY2026. Our job this year is to shrink the category of
decisions that require it, not eliminate it.

---

## What Good Looks Like at EOY 2026

If we execute on these OKRs:
- $32M ARR, 118% NRR, 72% gross margin — on the path to a strong Series C
- Org Context Engine in market, with early evidence that AI specificity is driving retention
- SSO and RBAC shipped, 6 at-risk accounts retained, enterprise expansion unlocked
- 55 NPS, self-serve onboarding at 70%, referral flywheel starting to turn

If we do not:
- $26–28M ARR, Series C on less favorable terms or delayed
- Dayforce takes 3–4 accounts from us with price and feature breadth
- We are still building compliance features in Q1 2027 while Org Context slips to 2027 H1
- The spreadsheet is still "The Real Dashboard" for most of our customers

The difference between those two outcomes is not market conditions. It is sequencing,
trade-off discipline, and whether the leadership team holds the line on what we are not
building this year.

---

*This document reflects the strategy as of April 2026. It will be reviewed at the June
board meeting and updated for H2 planning in July.*
