# CEO Morning Update

Posted in the CEO Slack channel at 9:00 am. Reads in under 60 seconds.

## Rules

- Blockers go first, each with the fix and who owns it.
- One line per client when things are fine. Batch detail only when something is blocked.
- Status dot per client:
  - 🟢 On track
  - 🟡 At risk: behind pace, or something has sat 36h+ in one status
  - 🔴 Blocked: needs action today
- Monday covers Fri to Mon. Other days cover the last 24h.

## Template (paste into Slack)

```
*Morning Update · [Day, Mon DD]*
🔴 [#] blocked · 🟡 [#] at risk · 🟢 [#] on track

*Blockers to clear today*
🔴 *[Client]*: [what is stuck] ([status], [#]h). Fix: [action] · Owner: [name] · Client told: [yes / today]
🟡 *[Client]*: [what is at risk]. Fix: [action] · Owner: [name]

*Strategy Engine* · briefs this week / 10 · produced by client
🟢 Atolea · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 Madam Muse · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 Tulas · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 Carbinox · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 LuxFord Tech · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 Longwell & Co · [#]/10 · [#] produced · Next: [#] briefs [day]
🟢 Napper · [#]/10 · [#] produced · Next: [#] briefs [day]

*Done-For-You · Earthling Co* 🟢
Brief [#] · Edit [#] · Review [#] · Ready to Launch [#] · Launched [#]
Ready to Launch this week: [#] · Next: [what moves, by when]

*Production · Ivy Food Scanning App* 🟢
Brief [#] · Edit [#] · Review [#] · Ready to Launch [#] · Launched [#]
Ready to Launch this week: [#] · Next: [what moves, by when]

*Wins* (optional, 1 line)
[Client]: [result or milestone]
```

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
🔴 *Earthling Co*: 3 edits waiting on client notes (Edit Feedback, 40h). Fix: ask for notes in #eathlingco-client by 12pm · Owner: Oli · Client told: today
🟡 *Tulas*: 6/10 briefs, 4 due Fri. Fix: Lil to prioritize Tulas today · Owner: Lil

*Strategy Engine* · briefs this week / 10 · produced by client
🟢 Atolea · 10/10 · 7 produced · Next: Sprint 10 kickoff Mon
🟡 Tulas · 6/10 · 3 produced · Next: 4 briefs Fri
...

*Done-For-You · Earthling Co* 🔴
Brief 2 · Edit 5 · Review 3 · Ready to Launch 4 · Launched 6
Ready to Launch this week: 4 · Next: 5 edits into review Fri
```
