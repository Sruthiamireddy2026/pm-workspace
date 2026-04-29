# Beacon: 2026 Company Vision

**Internal document. Do not distribute externally.**

Last updated: March 2026

---

## Who We Are

Beacon is a project management platform built specifically for product teams. We help PMs, designers, and engineers plan work, track progress, and ship products without drowning in process overhead. We are a Series B company (raised $42M total), 180 employees, roughly 2,400 paying customers.

## Mission

Make it possible for product teams to spend more time building and less time managing the work about the work.

## 2026 Company Goals

1. **Reach $28M ARR by December 2026.** We closed 2025 at $19.5M. Growth needs to come from expansion revenue (upsells to Pro/Enterprise) and net-new mid-market logos. We are not chasing SMB volume this year.

2. **Improve net revenue retention to 115%.** Currently at 108%. The biggest lever here is reducing churn in the first 90 days. Onboarding is still too manual, and teams that don't hit their "aha moment" in the first two weeks tend to drop off.

3. **Launch Beacon AI as a paid add-on by Q3.** AI features are table stakes in our category now. We need a compelling, differentiated AI layer that justifies a price premium. This is not about checking a box. It needs to solve real PM pain points, not just summarize things.

4. **Expand into the European market.** Open a small sales team in London by Q2. Localization (German, French) by Q4. GDPR compliance is already solid, but we need EU data residency to close enterprise deals there.

## Strategic Bets

**Bet 1: AI that actually helps PMs think, not just type faster.**
Most competitors are shipping AI summarization and auto-fill features. We think the real opportunity is in decision support: surfacing risks before they become fires, connecting customer feedback to roadmap items automatically, and flagging when a team's plan doesn't match their actual capacity. This is harder to build, but harder to copy.

**Bet 2: Become the system of record for product decisions.**
Right now, product decisions live in Slack threads, Google Docs, and people's heads. If Beacon can capture the "why" behind prioritization decisions (not just the "what"), we become sticky in a way that task trackers never are. This means investing in our docs and knowledge layer, not just the board view.

**Bet 3: Win the mid-market before enterprise.**
Enterprise sales cycles are 6+ months and require features we don't have yet (SSO/SCIM, audit logs, advanced permissions). Mid-market companies (200 to 2,000 employees) move faster and value the UX advantages we have over legacy tools. We'll build toward enterprise readiness, but mid-market is where the revenue math works this year.

## From the CEO's All-Hands (February 2026)

"We're in a weird spot as a company. We've got real traction, real revenue, and a product that people genuinely like. But we're also in a category where everyone is shipping AI features as fast as they can, and the big players (Atlassian, Monday, Asana) have 10x our engineering headcount. We can't win by doing the same things they do, just slightly better. We have to be opinionated. We have to pick the use cases where we can be genuinely best-in-class and say no to everything else. That's going to feel uncomfortable sometimes. But that focus is our advantage."

"The other thing I want to be honest about: we're not profitable yet, and the board expects us to get to cash-flow positive by mid-2027. That means every initiative we green-light this year needs to have a clear line to revenue or retention. We're past the phase where we can build cool things and figure out the business model later."

## Key Constraints

- **Engineering headcount is capped at 65 for 2026.** We can backfill attrition but no net-new headcount until we hit the Q3 revenue milestone. Current team is 58 engineers.
- **Platform limitations.** Our real-time collaboration infrastructure can't support more than 50 concurrent editors on a single workspace reliably. This blocks some enterprise use cases. Rewriting the collab layer is on the 2026 roadmap but won't land until Q4 at the earliest.
- **Data pipeline.** Our analytics backend is a patchwork of Postgres queries and a Redshift warehouse that's 18 months behind on optimization. Beacon AI features that need fast reads across large datasets will require pipeline investment first.
- **No dedicated ML team yet.** AI features are currently owned by the platform team, who are also responsible for infrastructure. The plan is to hire a small ML team (3 to 4 people) in Q2, but until they ramp, AI work competes directly with reliability work.
- **Brand awareness.** Outside of the product management community on LinkedIn and a few industry podcasts, Beacon doesn't have meaningful brand presence. Marketing budget for 2026 is $2.1M, up from $1.4M last year, but still small relative to competitors.
