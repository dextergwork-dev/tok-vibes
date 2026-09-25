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

Claude reads from this list. Update it when a sprint rolls over.

| Client | Service | Client contact | ClickUp sprint list | Notion pipeline | Client channel | Strategy channel | Editing channel |
|---|---|---|---|---|---|---|---|
| Atolea | SE | n/a | Sprint 9 (9/7 to 10/4) | [link](https://app.notion.com/p/atolea-jewelry/2f4cdc5947bc804b822fc9fb18ce88ea?v=2f4cdc5947bc81158396000c6e6b4df2) | none, skip client update | #strategy-atolea-lil | n/a |
| Madam Muse | SE | Ronan | Sprint 3 (9/21 to 10/18) | [link](https://app.notion.com/p/3a50be0b949f80238d38d1e645494e12?v=3a50be0b949f8090be73000cf147f8bd) | #madammuse-client | #madammuse-strategy-areeb | n/a |
| Tulas | SE | Nicolas | Sprint 4 (9/7 to 10/11) | [link](https://app.notion.com/p/105e60ba02f3826e8539810516b39a08?v=fa1e60ba02f382399e54081c9ebeb87e) | #tulas-client | #tulas-strategy-lil | n/a |
| Carbinox | SE | n/a | Sprint 21 (10/19 to 11/15) | none, ClickUp only | none, skip client update | #strategy-carbinox-areeb, #strategy-carbinox-lil | #editors-carbinox |
| LuxFord Tech | SE | Jordan | Sprint 1 (9/14 to 10/11) | [link](https://app.notion.com/p/Tok-Vibes-Strategy-Engine-3d64214161de80c5a7bcedea3b8f449f) | #luxfordtech-client | #luxfordtech-strategy | n/a |
| Longwell & Co | SE | Saru | Sprint 1 (9/14 to 10/18) | [link](https://app.notion.com/p/3d531bb3a6708004afe5c5bde1844cc8?v=3d531bb3a670802d92b6000cdb9b18d2) | #longwellco-client | #longwellco-strategy | n/a |
| Napper | SE | Marcus | Sprint 1 (9/28 to 10/25) | _add link_ | #napper-client | #napper-strategy | n/a |
| Earthling Co | DFY | Kevin | Sprint 1 (9/21 to 10/18) | n/a | #eathlingco-client | #earthlingco-strategy | #earthlingco-editing |
| Ivy Food Scanning App | Production | Ramzy | Sprint 1 (9/21 to 10/18) | n/a | #ivy-client | #ivy-strategist-kofoshi | #ivy-video-editors |

Client pipelines live in each client's own Notion workspace, so Claude can't read them yet. Until access is sorted, Claude takes brief counts from ClickUp and you add the "produced" numbers in step 4.

## Speed tips

- Keep one ClickUp list per active sprint. When a sprint ends, archive it so Claude reads only the live one.
- Tag blockers in Slack with a 🚧 reaction. Claude can find those in seconds.
- Once this runs smoothly, turn it into a scheduled job: Claude drafts at 8:30 am every day, you just review and post.
