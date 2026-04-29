# Roadmap Cross-Reference: TaskFlow Issues vs. People Analytics / HR Tech Norms
**Date:** 2026-04-22
**Input:** multi-source-triangulation-2026-04-22.md + 2026-04-13-feedback-synthesis.md

---

## Q1: Issues That Would Already Be on a Typical People Analytics / HR Tech Roadmap

These are not differentiators — they're table stakes in the HR tech / analytics space. Any PM in that domain would have these in-flight or recently shipped.

### SSO / SAML + RBAC + Audit Logs
In people analytics and HCM (Workday, UKG, Visier, SAP SuccessFactors), enterprise security compliance isn't a feature request — it's an entry ticket. HR data carries salary, performance, and headcount information that triggers legal and security requirements at every enterprise account. SAML SSO and RBAC are scoped in Q1 of any enterprise motion. Audit logs are typically required for SOC 2 Type II and are shipped before enterprise sales, not after.

**TaskFlow gap:** SSO is not on the current roadmap; audit logs are Q3. This is 2–3 years behind the standard in the HR tech space. The fact that this is still open is unusual for a product targeting enterprise contracts.

---

### Custom Fields
Every mature people analytics platform supports custom metadata — custom pay codes, job level taxonomies, team-specific attributes. This is standard because HR data structures vary dramatically by company. Mid-market HR tools (Lattice, Leapsome, Rippling) all ship custom fields before they reach 100 enterprise customers.

**TaskFlow gap:** Custom fields are on the Q2 roadmap. Timing is reasonable, but the request volume (TK-1211 + Survey R14) confirms this was underscoped earlier than it should have been.

---

### Integration Reliability
HR tech products are deeply integration-dependent — HRIS feeds payroll, payroll feeds benefits, benefits feeds finance. Integration monitoring and reliability infrastructure (token refresh, failure alerting, idempotency) are non-negotiable. Silent failures (the Slack "Task created!" bug in TK-1216) would be a P0 in any HR tech environment because downstream data corruption is a compliance risk.

**TaskFlow gap:** No integration health monitoring. Silent failures currently discoverable only by the customer. Standard in HR tech, absent here.

---

### Cross-Project / Portfolio / Executive Dashboard View
In people analytics, this maps directly to headcount dashboards, workforce planning views, and multi-department reporting. Every enterprise analytics product has a portfolio-level summary that managers and executives can read in one view. This is the product's reason for existing at the director+ level.

**TaskFlow gap:** Absent. Users are building this themselves in Google Sheets. In HR tech, the executive dashboard is typically the *entry point*, not a later roadmap item.

---

### Onboarding That Accounts for Non-Technical Personas
Enterprise HR platforms invest heavily in implementation and change management because the personas who need the tool (managers, employees) aren't the ones who bought it (HR ops, IT). Workday, UKG, and BambooHR all have role-specific onboarding paths. The default assumption is that most users are not technical.

**TaskFlow gap:** Onboarding redesign is on the Q2 roadmap. The root cause — designing for PM personas in a product used by marketers, designers, and ops teams — would have been caught earlier in an HR tech environment with rigorous persona research.

---

## Q2: Issues NOT Typically Prioritized in HR Tech — But Should Be Based on This Data

These are the gaps that HR tech teams routinely defer, often because they feel like engineering concerns or low-probability events.

### Notification System Overhaul (Opt-In vs. Opt-Out)
HR tech platforms accumulate notification types over time and rely on users to turn them off. Almost none have rebuilt the system from opt-out to opt-in. The result is the same as TaskFlow: users stop trusting email from the tool and miss important alerts. This is a chronic problem in Workday and SAP SuccessFactors — managers miss approval requests because they've muted everything.

**Why it's deprioritized:** Feels like a settings page, not a feature. Product teams don't see the downstream impact (missed tasks, degraded engagement) because it's invisible in the data. DAU looks normal; quality of engagement has collapsed.

**Why it should be higher:** Rachel's Gmail filter means she misses @mentions and deadlines. The notification channel is broken as a communication medium. In HR tech, this would mean missed performance review deadlines, skipped approval workflows, and compliance gaps. The fix is relatively low effort (backend bug + UX philosophy change) relative to the damage it's doing.

---

### Data Recovery / Soft Delete
HR tech teams prioritize data governance at the system level (retention policies, GDPR deletion workflows) but consistently underinvest in user-error recovery. Accidental deletion of records by admins is a known gap in most HR platforms — and when it happens, it requires database team intervention, exactly like TK-1207.

**Why it's deprioritized:** Low frequency, high effort to discover (customers don't always report it — they may just recreate data). Engineering teams treat backup restoration as sufficient.

**Why it should be higher:** In HR tech, deleting a compensation review cycle or performance period is equivalent to losing 3 months of project work. The effort to build soft delete with a 30-day recovery window is small (TK-1207 agent note already called this out as a critical backlog item). The cost of not having it is a database escalation and a damaged customer relationship every time it happens.

---

### Billing Accuracy (Repeat Offenders)
Billing accuracy issues (TK-1210 — charged for deactivated users 30 days after offboarding) are typically treated as ops tickets, not product problems. HR tech has the same gap: seat-count billing errors from delayed deactivation are common and rarely fixed at the root cause. Credits are issued, FAQs are updated, and the bug resurfaces.

**Why it's deprioritized:** Each incident gets resolved individually. No one runs a pattern analysis until the second or third recurrence.

**Why it should be higher:** Repeated billing errors erode trust in a way that's invisible to satisfaction surveys (customers ticket and move on) but accumulates toward churn. TK-1210 explicitly notes a prior fix (TK-1089) failed — this is a second occurrence. In HR tech, billing disputes during renewal conversations are disproportionately damaging.

---

## Q3: Top 3 by RICE Framework

### Methodology Notes
Standard RICE: **(Reach × Impact × Confidence) / Effort**

- **Reach:** % of customer base meaningfully impacted per quarter
- **Impact:** 3 = massive (churn risk, revenue directly at stake), 2 = high (adoption/engagement degradation), 1 = medium (QOL improvement), 0.5 = low
- **Confidence:** 0–1, based on source agreement (High = 0.9, Medium = 0.7, Low = 0.5)
- **Effort:** Estimated person-weeks

**Important limitation:** Standard RICE is count-weighted. In B2B, enterprise accounts are 15% of customers but often 40%+ of revenue. Where enterprise is the primary segment for a finding, I've noted a revenue-adjusted reach alongside the raw count.

---

### Rank 1: Notification System Overhaul
**RICE Score: 18.0**

| Factor | Value | Reasoning |
|---|---|---|
| Reach | 60% | All daily users across segments; notification volume affects everyone |
| Impact | 2 | High — degraded engagement, missed task signals, broken communication channel |
| Confidence | 0.9 | All 3 sources; confirmed backend bug + UX philosophy problem |
| Effort | 6 person-weeks | Backend fix (2 wks) + opt-in UX redesign (4 wks) |

**RICE = (60 × 2 × 0.9) / 6 = 18.0**

**Why it scores highest:** Broadest reach of any issue (every segment, daily surface area), reasonable effort, and high evidence confidence. The backend bug means this isn't just a preference — it's a broken feature. Fixing it also recovers the notification channel as a reliable engagement mechanism, which has secondary adoption benefits.

**Risk if deferred:** Users who have muted or filtered TaskFlow email are permanently less engaged. This doesn't show up as a spike in support tickets — it shows up as flat or declining DAU quality over time.

---

### Rank 2: Onboarding Redesign (Persona-Aware, Simplified Path)
**RICE Score: 7.2**

| Factor | Value | Reasoning |
|---|---|---|
| Reach | 80% | Every new customer goes through onboarding; also has remediation potential for existing teams that never adopted properly |
| Impact | 1 | Medium — improves time-to-value and long-term adoption; not an immediate churn trigger for current customers |
| Confidence | 0.9 | All 3 sources; Rachel's team is a live example of the long-tail adoption damage |
| Effort | 10 person-weeks | Copy/UX redesign (6 wks) + persona pathing logic (4 wks) |

**RICE = (80 × 1 × 0.9) / 10 = 7.2**

**Why it scores second:** Wide reach and high confidence offset the medium impact score. The interview adds a dimension the RICE can't fully capture: poor onboarding creates persistent adoption deficits. Rachel's 8/12 passive users 8 months in is a hidden churn signal that won't appear until renewal. If 2/3 of licensed seats aren't actively used, the ROI argument at renewal is weak.

**Risk if deferred:** New hires continue to onboard poorly. Existing low-adoption teams don't improve. The tool's value narrative at QBRs weakens as utilization data disappoints.

---

### Rank 3: SSO (Phase 1 of Enterprise Compliance Package)
**RICE Score: 4.5**

| Factor | Value | Reasoning |
|---|---|---|
| Reach | 20% | Enterprise segment only (count-weighted); revenue-weighted reach ~40% |
| Impact | 3 | Massive — direct renewal blocker, confirmed churn trigger, also unlocks pipeline sales |
| Confidence | 0.9 | Named accounts, specific deadlines, dollar figures attached |
| Effort | 12 person-weeks | SAML implementation + identity provider testing |

**RICE = (20 × 3 × 0.9) / 12 = 4.5**  
**Revenue-adjusted RICE = (40 × 3 × 0.9) / 12 = 9.0**

**Why it scores third despite the clearest revenue risk:** RICE penalizes high-effort items and low-reach segments, which is the right instinct for most prioritization. But SSO is the case where RICE undersells priority. Two named accounts totaling $8,000/mo are at renewal risk by Q2. That's $96,000 ARR — before accounting for pipeline accounts blocked from closing.

**Recommendation:** Score SSO using revenue-adjusted reach and treat it as **tied with onboarding** for #2 depending on the quarter's revenue vs. growth objective. If the goal is retention, SSO is #2. If the goal is new customer activation, onboarding is #2.

**Risk if deferred:** Meridian Corp ($4,200/mo) renewal is April — this quarter. Deferring SSO past Q2 likely means losing the account. Audit logs and RBAC should follow SSO as Phase 2 of the same compliance workstream, not separate roadmap items.

---

## Summary Table

| Issue | RICE Score | Confidence | Revenue Risk | Quarter |
|---|---|---|---|---|
| Notification overhaul | 18.0 | High | Indirect (churn via engagement) | Q2 |
| Onboarding redesign | 7.2 | High | Indirect (adoption/renewal) | Q2–Q3 |
| SSO (Phase 1) | 4.5 (9.0 rev-adj) | High | Direct ($96K ARR at risk) | Q2 (urgent) |
| Cross-project view | 4.1 | Medium | Indirect (flight risk signal) | Q3 |
| Gantt / timeline view | 2.1 | Medium | Mid-market deals | Q3 |
| Soft delete / data recovery | 2.25 | Low | Low frequency, high severity | Q3 |
| Android reliability | 2.7 | Medium | DAU impact | Q3 |

---

*RICE is a directional tool, not a deterministic one. The notification fix and SSO both have strong cases for Q2. The question to leadership is whether the Q2 objective is "protect revenue" (SSO first) or "improve daily product health" (notifications first). Ideally both — they're not the same team.*
