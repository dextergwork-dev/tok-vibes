---
name: fireflies-to-ops
description: Turn the action items from a Fireflies call (usually an Oli <> Dexter sync) into individual tasks in ClickUp Operations > Ops & Systems > Ops Tasks. Use when Dexter asks to add a call's tasks to Ops Tasks, or runs /fireflies-to-ops after a meeting.
---

# Fireflies to Ops Tasks

After every call, each task Dexter owns goes into **Ops Tasks** as its own ClickUp task. Dexter sets the assignee and due date by hand afterwards.

## 1. Find the call

- If the user names a call or pastes a Fireflies link, use that one.
- Otherwise, list today's meetings with `fireflies_get_transcripts` (`fromDate` = today). If one is still live, check `fireflies_get_active_meetings` and read its live transcript.
- If more than one call qualifies, pick the latest Oli <> Dexter sync and say which one you used.

## 2. Pull the tasks

- Read the **full transcript** with `fireflies_get_transcript`, not just the summary. Fireflies summaries sometimes get dates wrong (e.g. "June 12" for Oct 12), so take dates from what was actually said.
- Keep only tasks for **Dexter (ops)**. Note Oli's own tasks in the chat reply, but don't create them.
- One task per action. Split combined asks (e.g. "build the tracker and send the client update" is two tasks).
- Skip anything already done during the call.
- Before creating, search Ops Tasks for an open task with the same intent. If one exists, mention it instead of duplicating it.

## 3. Create them in ClickUp

- **List:** Ops Tasks, list ID `901220530358` (Operations > Ops & Systems).
- **Name:** `<Client or Area>: <verb-first action>`, e.g. `Tulas: set up DFY-5 sprint in DFY Engine`.
- **Priority:**
  - `urgent`: must happen today or tomorrow, or blocks a client delivery
  - `high`: this week, client-facing
  - `normal`: this week, internal
  - `low`: process or habit reminders
- **Status:** leave the default (`to do`). Use `in progress` only for ongoing work Oli said to chip away at daily.
- **Do not set** assignee or due date. Dexter does that.
- **Description** (markdown):
  - What to do, as short bullets, with the specifics from the call (dates, batch counts, names, links)
  - Anything to keep from the client, e.g. "Do **not** mention which strategist is on it"
  - Last line: `Source: [<Meeting title>, <Mon D>](https://app.fireflies.ai/view/<id>?t=<seconds>)` pointing at the moment the task was given

## 4. Reply to Dexter

- List the created tasks grouped by priority, each as an inline markdown link with the task name as the anchor text.
- Add one line on Oli's own action items, so Dexter knows what's waiting on them.
- Keep it short. No em dashes.
