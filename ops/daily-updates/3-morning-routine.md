# Morning Routine (about 10 minutes)

Run this with Claude each morning. Claude pulls the data, you review and send.

## Daily steps

1. *8:30 am*: Open Claude and paste:
   > Run the morning update. Today is [day].
2. *Claude pulls* (about 3 min):
   - *ClickUp*: current sprint list per client. Counts by status. Flags anything 36h+ in one status.
   - *Notion*: each Strategy Engine pipeline. Briefs delivered this week vs 10, and how many the client's editors produced.
   - *Slack*: last 24h (Monday: since Friday) in each client's `-client`, `-strategy`, `-editing` channels. Flags anyone waiting on feedback, footage, assets or approval.
3. *Claude drafts* the CEO update from `1-ceo-morning-update.md` and lists anything it wasn't sure about.
4. *You review* (3 to 5 min): fix owners and fixes on blockers.
5. *Claude posts* it to the CEO channel at 9:00 am, or you paste it yourself.
6. *Mon / Wed / Fri only*: say
   > Draft the client updates.

   Claude saves a Slack draft in each `-client` channel using `2-client-update.md`. You open each one, tweak, and hit send.

## Client map

Claude reads from this list. Fill the blanks once and keep it current when a sprint rolls over.

| Client | Service | ClickUp sprint list | Notion pipeline | Client channel | Strategy channel | Editing channel |
|---|---|---|---|---|---|---|
| Atolea | SE | Sprint 9 (9/7 to 10/4) | _add link_ | _not found_ | #strategy-atolea-lil | n/a |
| Madam Muse | SE | Sprint 3 (9/21 to 10/18) | _add link_ | #madammuse-client | #madammuse-strategy-areeb | n/a |
| Tulas | SE | Sprint 4 (9/7 to 10/11) | _add link_ | #tulas-client | #tulas-strategy-lil | n/a |
| Carbinox | SE | _current sprint missing_ (only Sprint 21, 10/19 to 11/15) | _add link_ | _not found_ | #strategy-carbinox-areeb, #strategy-carbinox-lil | #editors-carbinox |
| LuxFord Tech | SE | Sprint 1 (9/14 to 10/11) | _add link_ | #luxfordtech-client | #luxfordtech-strategy | n/a |
| Longwell & Co | SE | Sprint 1 (9/14 to 10/18) | _add link_ | #longwellco-client | #longwellco-strategy | n/a |
| Napper | SE | Sprint 1 (9/28 to 10/25) | _add link_ | #napper-client | #napper-strategy | n/a |
| Earthling Co | DFY | Sprint 1 (9/21 to 10/18) | n/a | #eathlingco-client | #earthlingco-strategy | #earthlingco-editing |
| Ivy Food Scanning App | Production | Sprint 1 (9/21 to 10/18) | n/a | #ivy-client | #ivy-strategist-kofoshi | #ivy-video-editors |

## Speed tips

- Keep one ClickUp list per active sprint. When a sprint ends, archive it so Claude reads only the live one.
- Tag blockers in Slack with a 🚧 reaction. Claude can find those in seconds.
- Once this runs smoothly, turn it into a scheduled job: Claude drafts at 8:30 am every day, you just review and post.
