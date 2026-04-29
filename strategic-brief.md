# Beacon Analytics — Strategic Product Dashboard
**Generated:** April 26, 2026
**Sources:** Competitive Landscape · Customer Feedback (45 items) · Strategy/OKRs FY2026

---

## Section 1 — Customer Pain Radar

| # | Theme | Pain Level | Churn Risk | Frequency | Workaround Signal |
|---|---|---|---|---|---|
| 1 | Enterprise SSO / compliance gap | Critical | **High** | 4 instances — 2 named accounts ($4,200/mo each), 2 survey respondents | Internal IT security exceptions filed; parallel vendor evaluations already underway before renewal |
| 2 | Spreadsheet never goes away | High | **High** | Low frequency, high signal — 1 interview + enterprise ticket pattern | "The Real Dashboard" Google Sheet: updated Mon/Wed, 8+ months running, shared with leadership as official status view |
| 3 | No unified cross-workforce view | High | Medium | 3 survey + 1 interview + enterprise support pattern | Parallel tracking spreadsheets maintained indefinitely — higher the user's org scope, worse the tool works |
| 4 | Notification systems that cry wolf | High | Medium | All 3 source types (confirmed backend bug) | Gmail filters archiving all system emails → critical signals (assignments, @mentions, deadlines) now invisible |
| 5 | Tools built for analysts, not users | High | Medium | 3 sources | Team leads build shadow onboarding docs; non-technical users settle into read-only habits permanently |
| 6 | AI features organizationally blind | Medium | Low–Med | 2 sources | Separate company terminology doc pasted into prompts manually; non-technical users skip AI features entirely |

**Key signal:** Themes 1 and 2 are active churn triggers with named accounts and explicit timelines — not satisfaction gaps. Theme 3 and 6 are structural adoption ceilings that weaken renewal ROI over time.

---

## Section 2 — Competitive Threat Map

| Competitor | What They Just Shipped | Urgency for Beacon | Beacon's Posture |
|---|---|---|---|
| **Dayforce** | AI Workspace + People Analytics Agents (Feb 2026, post $12.3B Thoma Bravo acquisition) | **CRITICAL** — PE-fueled, directly targeting Beacon's mid-market segment, price-aggressive | Defend: Org Context depth + mid-market UX are the only durable advantages. Dayforce can buy features, not context. |
| **Workday** | Sana "superintelligence for work" (GA 2026) + Data Cloud zero-copy sharing | **HIGH** — moving down-market aggressively; Sana takes autonomous action, not just analytics | Hold: Workday requires full HCM suite buy-in. Beacon's wedge is standalone value with faster time-to-insight. |
| **Visier** | MCP for AI Agents (GA April 2026) — positions as governed data infrastructure layer | Medium | Watch: Enterprise-heavy, prices out of Beacon's segment. MCP play raises switching costs for enterprise accounts already on Visier. |
| **Power BI** | Translytical Task Flows (GA 2026) — write data back to source from BI | Medium | Signal, not threat today: directional confirmation that Bet 3 (Insight-to-Action) is where the market is heading. Watch adoption. |
| **Looker / Data Studio** | Rebrand to Data Studio + Conversational Analytics (Fast mode / Thinking mode NL query) | Low–Med | Monitor: GCP-first threat; NL query is now table stakes. Beacon's AI needs org specificity to differentiate from generic NL. |
| **SAP SuccessFactors** | EU Pay Transparency Insights (GA May 2026) | Low | Opportunity signal: compliance-driven analytics wedge. Beacon should have a compliance analytics answer for regulated verticals. |

**The gap no competitor has closed:** AI that knows *your* org. Workday's Sana answers "why is attrition up in engineering" calibrated to 10,000 customers' average. Beacon's Org Context Engine can answer it calibrated to *this company's* IC4s, Seattle vs. Austin dynamics, and last reorg data. This is the 18–24 month window. Dayforce is the clock.

---

## Section 3 — OKR Alignment Matrix

| Customer Pain | Maps to Goal / Bet | Roadmap Status | Gap? |
|---|---|---|---|
| SSO/compliance = renewal blocker | **Goal 3:** SAML SSO GA by May 31 (hard date — 2 June renewals) | On roadmap — **hard deadline** | None. Execution risk only. |
| SSO/compliance = renewal blocker | **Goal 3:** RBAC GA by Q3, Audit Log beta Q3/GA Q4 | On roadmap | None. Sequenced after SSO. |
| AI organizationally blind | **Goal 2:** Org Context Engine beta by Q3 | On roadmap — primary strategic bet | None. KR 2.3: 60% of WAU rate AI outputs as "directly usable" within 60 days. |
| No cross-workforce view | **Bet 3:** Insight-to-Action (write-back to HRIS) | **Q4 — not addressed until H2** | Gap in H1. Customers with this pain have no relief until Q4 at earliest. |
| Tools built for analysts | **Goal 1:** Self-serve onboarding 41% → 70% by Q4, time-to-insight 23 days → 7 days | On roadmap | Medium gap — KR 1.3 target is Q4, pain is active now. |
| Spreadsheet never goes away | **Bet 3:** Insight-to-Action | **Q4 — explicitly named as not solved this year** | Known gap. Strategy doc is honest: "The spreadsheet will still be the default workflow for most customers at end of FY2026." |
| Notification overload | Not named in OKRs | **Not on roadmap** | Confirmed backend bug (toggle saves to frontend, doesn't persist to backend). Active daily engagement degrader. No owner named. |

**Uncovered gap:** Notification bug is not in any Goal or KR. It's a confirmed bug degrading daily engagement across all account types — and there's no roadmap line for it.

---

## Section 4 — Priority Stack

### Priority 1 — Ship SAML SSO by May 31. No slip.
**What:** SAML SSO GA by the hard date in Goal 3 (KR 3.1).
**Why now:** Two named accounts have June renewal conversations. If SSO is not GA before those conversations, both accounts are lost. This is not a roadmap priority — it is an execution dependency with a named dollar value attached.
**OKR:** Goal 3, KR 3.1. Also unlocks $193K in stalled expansion ARR across 23 accounts.
**Competitive defense:** Dayforce will price aggressively to take at-risk accounts. An SSO slip gives them a clean opening. Retain these accounts before the competitive conversation starts.
**Risk if missed:** Two accounts churn in June. Every day of delay is a day Dayforce has to make contact.

---

### Priority 2 — Ship Org Context Engine to beta by Q3. This is the moat.
**What:** Org Context Engine (KR 2.1) — AI outputs that reference company-specific role names, team structures, and named workflows, scoring ≥4.0 on specificity rubric.
**Why now:** Dayforce launched AI Workspace in February. Workday shipped Sana. Both are generic. Neither can solve per-org context at their scale — Beacon can. The 18–24 month window is running. Every quarter of delay is a quarter Dayforce gets to learn mid-market patterns.
**OKR:** Goal 2, KRs 2.1–2.3. Also directly addresses Theme 5 (AI organizationally blind) — moves AI from power-user-only to broadly usable, which drives KR 1.1 (WAU from 34% → 55%).
**Competitive defense:** This is the asymmetric bet the strategy names explicitly. It is also the feature most directly threatened by Dayforce's PE-fueled feature velocity. Ship it before they figure out how to approximate it.
**Risk if missed:** Org Context slips to 2027 H1. NPS stays below 50. Referral flywheel doesn't turn. $32M ARR not achievable without a sales investment Beacon can't make.

---

### Priority 3 — Fix the notification bug. It's a silent engagement killer.
**What:** Resolve the confirmed backend bug where notification preferences save to frontend state but do not persist to backend (TK-1203). Add granular notification controls (new assignments, overdue items, direct @mentions only).
**Why now:** Users are creating Gmail filters that archive *all* system notifications — including critical ones (task assignments, deadlines, @mentions). This is a daily engagement degrader that compounds over time. It is not in any Goal or KR, which means it has no owner and will not get fixed on its own.
**OKR:** Indirect support for Goal 1 (WAU) and KR 1.4 (NPS from 47 → 55). A user archiving all system emails is not an active user. Active users drive NPS.
**Competitive defense:** Not competitive — this is a hygiene fix. But a product that reliably cries wolf trains users to ignore it, and that habit is hard to break even after the bug is fixed. Fix it before it becomes a behavioral norm.
**Risk if missed:** Daily active engagement continues to degrade silently. NPS stays flat. At renewal, utilization data does not support the price.

---

## Quick Reference — What's Not Getting Built This Year (Per Strategy)

Per the constraints section of the Strategy doc — named explicitly as out of scope for FY2026:
- Scheduling module (customers asked; not funded)
- Learning management integration (customers asked; not funded)
- Mobile app (customers asked; not funded)
- Legacy connector architecture rewrite (6–9 month infra project; accepted risk of 1–2 incidents)
- Spreadsheet elimination (Bet 3 is Q4 directional, not a FY2026 completion)

---

*Run `/strategic-brief` to regenerate this dashboard from live Google Drive sources.*
