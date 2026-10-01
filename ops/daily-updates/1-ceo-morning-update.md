# CEO Morning Update

Posted in #ops-team at 9:00 am. Reads in under 60 seconds.

## Rules

- No batch or creative IDs (like B012 or TOK05). Use counts only.
- SMART: every line has a number, and every next step has an owner or a date.
- Add a link to each client's current ClickUp sprint (and delivery tracker for DFY and Production).
- Blockers go first, each with the fix and who owns it.
- One line per client when things are fine. Batch detail only when something is blocked.
- Status dot per client:
  - 🟢 On track
  - 🟡 At risk: behind pace, or something has sat 36h+ in one status
  - 🔴 Blocked: needs action today
- Monday covers Fri to Mon. Other days cover the last 24h.

## Template (paste into Slack)

```
*Ops Update · [Day, Mon DD]:* 🔴 [#] blockers · 🟡 [#] at risk

*Blockers to clear today*
🔴 *[Client]:* [what is stuck, with counts]. Fix: [action] by [time] · Owner: [name] · [Client Pipeline link]
🟡 *[Client]:* [what is at risk]. Owner: [name] · [Client Pipeline link]

*Strategy Engine*
🟢 *[Client] ·* [one short update with a count or date]

*Done-For-You*
🟢 *[Client] ·* [one short update]

*Production*
🟢 *[Client] ·* [one short update]
```

Every blocker gets its pipeline link (Notion pipeline for SE clients, ClickUp sprint for DFY and Production). Clients listed under Blockers are left out of the engine sections. Engine lines are updates only, one line each.

## Status buckets (keeps DFY and Production to one line)

| Bucket | ClickUp statuses |
|---|---|
| Brief | Briefing, Brief Review |
| Edit | Ready to Edit, Editing |
| Review | Edit Review, Edit Feedback |
| Ready to Launch | Approved Prep Files, Ready to Launch |
| Launched | Launched |

## Blocker types to flag

Waiting on client feedback · creator footage late · editor capacity · brief not approved · missing assets · anything 36h+ in one status.

## Example

```
*Morning Update · Thu, Sep 25*
🔴 1 blocked · 🟡 1 at risk · 🟢 7 on track

*Blockers to clear today*
🔴 *Earthling Co*: 3 edits waiting on client notes (Edit Feedback, 40h). Fix: ask for notes by 12pm · Owner: Oli · Client told: today
🟡 *Tulas*: 6/10 briefs, 4 due Fri. Fix: Lil to prioritize Tulas today · Owner: Lil

*Strategy Engine* · briefs this week / 10 · produced by client
🟢 Atolea · 10/10 · 7 produced · Next: Sprint 10 kickoff Mon
🟡 Tulas · 6/10 · 3 produced · Next: 4 briefs Fri
...

*Done-For-You · Earthling Co* 🔴
Brief 2 · Edit 5 · Review 3 · Ready to Launch 4 · Launched 6
Ready to Launch this week: 4 · Next: 5 edits into review Fri
```
