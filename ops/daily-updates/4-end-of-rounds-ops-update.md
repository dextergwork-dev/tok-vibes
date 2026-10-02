# End-of-Rounds Ops Update

Posted in #ops-team once the daily rounds are done: client updates, strategist check-ins, editor check-ins, and the internal ops and finance check. It shows where everything stands *now*, after the blockers were worked, not the morning list.

Runs on its own at 9:35am ET on weekdays, or any time you tell Claude "Ops update".

## Step 1: check the rounds are done first

Before pulling any data, Claude checks that Dexter has posted today in:
- every active `-client` channel (client updates)
- every strategy channel (strategist updates)
- every editing channel (editor updates)
- #finance, #billingqueue or the Ops Tasks list (internal check)

If anything is missing, Claude lists the channels still waiting and checks again 30 minutes later, up to 11:30am ET. The report is only built once the rounds are done.

## Step 2: build the update

Claude pulls the live state, saves the update as a draft in #ops-team, and you send it.

## Rules

- Live state only. A blocker that was cleared today goes under *Cleared today*, not *Blockers*.
- Every engine and every active client, one line each when fine.
- Counts, not batch IDs.
- Each open item has an owner and a date.
- Status dot per line: 🟢 on track · 🟡 at risk (behind pace or 36h+ in one status) · 🔴 blocked (needs action today)

## Where Claude pulls from

| Section | Source |
|---|---|
| Strategy Engine, DFY Engine | ClickUp Week tasks in each client sprint (status, due date, Strategist) and the Strategist Delivery Tracker |
| Production Engine | ClickUp Ivy sprint, batch statuses |
| Cleared today | Dexter's Slack messages, emails and ClickUp changes since 8am ET |
| Ops | #ops-team, Ops Tasks list, hiring pipeline |
| Finance | #finance, #billingqueue, Billing Queue tasks, client payment emails |

## Template (paste into Slack)

```
*Ops Update · [Day, Mon DD] · end of rounds*
:white_check_mark: Client, strategist and editor updates sent · :red_circle: [#] blocked · :large_yellow_circle: [#] at risk · :large_green_circle: [#] on track

*Cleared today*
• [Client]: [what was unblocked]

*Still open*
:red_circle: *[Client]*: [what is stuck]. Next: [action] · Owner: [name] · By: [date]

*Strategy Engine* · this week
:large_green_circle: [Client] · W[#] [status] · Next: W[#] due [day] ([strategist])

*DFY Engine*
:large_green_circle: [Client] · W[#] [status] · Next: [what lands, when]

*Production Engine · Ivy*
Brief [#] · Recording [#] · Edit [#] · Review [#] · Ready [#] · Stuck [#]
Next: [what moves, when]

*Internal: Ops*
• [hiring, team changes, systems, SOPs]

*Internal: Finance*
• Client payments: [received / due]
• Team invoices: [# in, # paid, anything to fix]
```
