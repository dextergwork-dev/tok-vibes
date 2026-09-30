# Client Playbook

How Claude runs a client from signed to machine running, and day to day after that. Built from the Hommey onboarding. Works for any client: copy `_template.md` to `<client>.md`, fill it in, then use the commands below.

## Client files

[Atolea](atolea.md) · [Carbinox](carbinox.md) · [Earthling Co](earthling-co.md) · [Hommey](hommey.md) · [Ivy](ivy.md) · [Longwell & Co](longwell-co.md) · [LuxFord Tech](luxford-tech.md) · [Madam Muse](madam-muse.md) · [Napper](napper.md) · [Tulas](tulas.md)

[Hommey](hommey.md) is the fully filled example. The others have what we know so far; fill the blanks as you go.

## How to use it

Say one of these in Claude Code. Claude reads `ops/clients/<client>.md` first, then follows the matching section.

| Say | What Claude does |
|---|---|
| "Check [client]" / "Onboard [client]" | Onboarding check: reads email, Slack, ClickUp, then gives status + the onboarding process with what's done and what's left |
| "Update on [client]" | Status update: what moved, waiting on client, your to-dos |
| "Draft the client update for [client]" | Client channel update + strategist note, in our style |
| "Draft an email to [contact] about [topic]" | Email draft for the client thread |
| "Research [client]" | Research doc following the Ads Strategist Dashboard, step by step |
| "Every 8am, update me on [client]" | Sets up the daily brief routine |

Claude drafts. You send. Claude never posts, emails or changes anything unless you say so.

## Where Claude looks

Always check all of these before answering. Use the IDs in the client file.

- *Gmail*: search the client name and domain (spelling variants too, e.g. "Homie" = "Hommey"). Read full threads, not previews.
- *Slack*: `<client>-client`, `<client>-strategy`, `<client>-editing`, plus client mentions in #ops-team and #billingqueue. Open threads with replies.
- *ClickUp*: billing task in Billing Queue, onboarding form response, Ads Strategist Dashboard, sprint list in the Engine space. Read task comments and replies, that's where Oli leaves instructions.
- *Google Drive*: the client folder (brand deck, reviews CSV, performance decks, signed SOW).
- *Onboarding map*: [Client Signed to Machine Running](https://claude.ai/artifact/WBbxJXMwQeibeREtaoWjnB) for the full process.

## 1. Onboarding check

Output, short:

1. *Where things stand*: contract, form, ad account, footage, billing, strategist, client contacts.
2. *Do now*, *Money*, *Once the form is in*, *Once the strategist is picked*, *Sprint + engine setup*: each step marked done or to do.

Rules we follow:

- *Contract*: the client signs the SOW in HoneyBook. If they send a signed PDF instead, Oli countersigns, then we send the fully signed copy back and save it in the client Drive folder.
- *Billing*: Sprint 1 is a one-off QuickBooks invoice. The recurring QuickBooks payment starts on the Sprint 2 Billing Monday (kickoff + 4 weeks), every 4 weeks on Monday. Send invoices to the client's AP email if they give one.
- *Billing Queue comment*: tag @Mary and @Oli with client, product, rate, Billing Monday and contacts.
- *Slack*: invite the client to `<client>-client` with permission to add their own people.
- *Ads Strategist Dashboard*: link the form response at the top ("FORM RESPONSE FROM CLIENT: LINK"), attach the reviews CSV and survey, and keep it inside the client's folder in ClickUp.
- *Sprint template*: rename batches to match the client's weekly volume.

## 2. Status update ("Update on [client]")

Format:

- One line: status (on track / at risk / blocked) and why.
- *Done*, *This week* (table: When · What), *Waiting on the client*, *For you* (numbered, most urgent first, each with who asked and where).
- Offer one next draft at the end.

## 3. Client update + strategist note

Posted Monday, Wednesday, Friday. Follow `ops/daily-updates/2-client-update.md` and the ClickUp page "We Communicate Like Dale Carnegie (Ops)".

*Client channel*

- Open with `hey @channel!` so it reaches everyone.
- Always "we", never "I".
- Never name the strategist or anyone on our team. Say "we" or "our team".
- Warm human opener, thank them for something specific, lead with what's ready and what it gets them.
- Asks go behind "no rush" and are framed around their win.
- Never explain what went wrong. End warm. 5 to 8 lines, no links.

*Strategist channel*

- Use their name, warm opener, thank them.
- What they have to work with, the timeline, one gentle ask.
- End with "drop anything you need from the client here and I'll chase it".

## 4. Emails to the client

- Reply on the existing client thread unless it's a new topic (e.g. invoice to the AP email = new email).
- Introduce yourself once as Operations Manager, the day-to-day contact.
- Short, warm, specific. Say what's attached and what they need to do, if anything.
- If a correction is needed, keep it light: "please disregard my last email about X, there's nothing more you need to do".

## 5. Research doc ("Research [client]")

Follow the client's Ads Strategist Dashboard in ClickUp, in this order:

0. Onboarding form response (goals, geo, product focus, competitors, KPIs, landing pages)
1. Ad account audit: top 5 ads by spend (last 30 days), pattern across winners. Use the client's own performance decks if Ads Manager isn't available.
2. Ad comments mining (needs Ads Manager exports)
3. Reviews mining (3A) and Reddit threads (3B)
4. Competitor gap (Atria)
5. Motivator Worksheet (7 motivators, 2 situations, 1 barrier, with evidence counts)
6. 4-Layer Strategy Map + First Sprint Plan (70% broad, 30% test)
7. Definition of Done checklist: what's left and what access is missing

Mark anything Claude couldn't reach (Ads Manager, Atria, Reddit) as "to fill" instead of guessing.

## 6. Daily 8 AM brief

Set up once per client with a routine at 7:52 AM New York time, into this chat. It reads Gmail, Slack and ClickUp (read-only) and returns: status line, what moved, waiting on client, your to-dos. On Mon/Wed/Fri it adds the client update + strategist note drafts (section 3).

## Writing rules for everything

- No em dashes.
- Short, and lead with what's in it for them.
- Don't re-state what went wrong. Say what's next.
- Client-facing: "we". Internal: plain and direct.
