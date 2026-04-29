# Beacon Customer Feedback Themes

**Source:** 18 customer interviews (Jan-Feb 2026) + 240 support tickets (Q4 2025)
**Synthesis date:** March 2026

---

## Theme 1: "I can't see what's actually at risk until it's too late"

**Frequency:** 14 interviews, 67 support tickets
**Pain level:** High

Teams consistently report that Beacon doesn't surface problems early enough. By the time a PM realizes a project is off track, they've already missed the window to adjust scope or shift resources.

**Sample quotes:**
- "I built a custom dashboard to track risks, but it's all manual. I'm spending two hours a week just updating status fields so my leadership team can see where we stand." (PM, 400-person fintech)
- "We had a launch slip by three weeks because a backend dependency was blocked and nobody flagged it. The information was technically in Beacon, but you'd have to click into five different views to connect the dots." (Director of Product, 800-person healthtech)
- "I wish Beacon would just tell me: here are the three things you should be worried about this week. Instead I have to go hunting." (Senior PM, 200-person edtech)

**Current workaround:** PMs build manual risk registers in Google Sheets or dedicated Notion pages. Some teams run weekly "risk review" meetings where they go ticket by ticket looking for problems.

---

## Theme 2: "Customer feedback lives everywhere except where we make decisions"

**Frequency:** 11 interviews, 42 support tickets
**Pain level:** High

Product teams collect feedback from support tickets, sales calls, user interviews, and NPS surveys, but none of it flows into Beacon where prioritization happens. The gap between "what customers are saying" and "what we're building" is bridged manually, if at all.

**Sample quotes:**
- "We use Productboard for feedback and Beacon for execution. The two systems don't talk to each other at all. So when I'm prioritizing the backlog, I'm going on memory and gut feel about what customers actually want." (PM, 300-person SaaS)
- "Our support team tags tickets with feature requests, but that data just sits in Zendesk. I check it maybe once a quarter when I'm doing planning. By then half of it is outdated." (Group PM, 600-person marketplace)
- "I literally keep a spreadsheet called 'things customers keep asking for' because there's no way to connect that signal to our roadmap inside Beacon." (PM, 150-person developer tools company)

**Current workaround:** Spreadsheets, Productboard, or tagging systems in support tools. One team built a Zapier integration that pushes Zendesk tags into Beacon task descriptions, but called it "fragile and ugly."

---

## Theme 3: "Planning and capacity are a guessing game"

**Frequency:** 10 interviews, 38 support tickets
**Pain level:** High

Teams don't have a reliable way to understand whether their plans are realistic given their actual capacity. Beacon tracks what's planned and what's done, but the gap between "committed work" and "available team hours" is invisible.

**Sample quotes:**
- "Every quarter we commit to a roadmap that we deliver maybe 60% of. And every quarter we act surprised. We don't have a capacity model. We just look at the backlog and make optimistic promises." (VP of Product, 500-person B2B SaaS)
- "I can see that my team has 40 tickets assigned, but I have no idea if that represents two weeks of work or two months. Beacon treats every task the same." (Engineering Manager, 350-person fintech)
- "We started using t-shirt sizing for estimates, but Beacon doesn't do anything useful with that data. It's just a label on a card." (PM, 200-person logistics platform)

**Current workaround:** Teams use spreadsheet-based capacity models, often maintained by a program manager or TPM. Some teams have adopted separate tools like Planview or Tempo for resource planning alongside Beacon.

---

## Theme 4: "Stakeholder updates take way too long to prepare"

**Frequency:** 8 interviews, 51 support tickets
**Pain level:** Medium

PMs spend significant time each week assembling status updates for leadership, pulling data from Beacon into slide decks or documents. The reporting features in Beacon are functional but not flexible enough for executive audiences.

**Sample quotes:**
- "Every Monday I spend about 90 minutes pulling together a status update for my VP. I'm basically copy-pasting from Beacon into a Google Doc and adding context that the tool doesn't capture." (PM, 400-person fintech)
- "The built-in reports are fine for my team, but leadership wants a different view. They want to see themes, not tickets. So I end up rewriting everything." (Director of Product, 700-person enterprise SaaS)
- "I asked my team to start writing better ticket descriptions specifically so I could copy them into status reports. That's backwards, but it's where we are." (Senior PM, 250-person edtech)

**Current workaround:** Manual assembly in Google Slides or Docs. Two companies mentioned building custom Looker dashboards that pull from Beacon's API, but said the API doesn't expose enough context (just status and dates, not narrative updates).

---

## Theme 5: "Cross-team coordination is painful at our size"

**Frequency:** 7 interviews, 29 support tickets
**Pain level:** Medium

As organizations grow past 3 to 4 product teams, coordinating dependencies in Beacon becomes difficult. The tool works well for single-team workflows but doesn't provide good visibility across teams.

**Sample quotes:**
- "We have six product teams and they all use Beacon independently. When Team A needs something from Team B, they send a Slack message. There's no formal dependency tracking." (Head of Product, 500-person B2B SaaS)
- "I tried using Beacon's 'linked tasks' feature for cross-team dependencies, but it's just a hyperlink. There's no timeline view, no blocking/blocked status, nothing that actually helps me manage the dependency." (Program Manager, 400-person healthtech)
- "The bigger we get, the more Beacon feels like it was designed for a single team in a room together. We're five teams across three time zones now." (VP of Engineering, 600-person marketplace)

**Current workaround:** Shared Slack channels for cross-team coordination. Some organizations maintain a separate "program-level" Beacon workspace, but this creates duplicate tickets and sync overhead.

---

## Theme 6: "Onboarding new team members takes too long"

**Frequency:** 5 interviews, 13 support tickets
**Pain level:** Low

When new PMs or engineers join a team, getting them up to speed on the Beacon workspace (how it's configured, what the workflows mean, where to find things) takes longer than expected. Institutional knowledge about "how we use Beacon" lives in people's heads.

**Sample quotes:**
- "Every new PM gets a 45-minute walkthrough of our Beacon setup from me personally. I've done it eight times this year. There's no self-serve way to understand our workflows." (Senior PM, 300-person SaaS)
- "The tool is flexible, which is great, but it means every team uses it differently. When I moved from the Growth team to the Platform team, it felt like learning a new product." (PM, 400-person fintech)

**Current workaround:** Internal wiki pages (usually in Confluence or Notion) documenting team-specific Beacon conventions. One company created a Loom video library, but said it goes stale within a quarter.
