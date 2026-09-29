#!/usr/bin/env python3
"""Read a public (Share to web) Notion pipeline and print each batch's status.

Usage: python3 ops/scripts/notion_pipeline.py <notion.site URL> [--all]
Groups batches by status (hours since last edit, ⚠️ at 36h+).
Hides Briefing rows unless --all is passed.
"""
import datetime
import json
import re
import subprocess
import sys


def post(host, endpoint, body):
    out = subprocess.run(
        ["curl", "-s", "-X", "POST", f"https://{host}/api/v3/{endpoint}",
         "-H", "content-type: application/json", "-d", json.dumps(body)],
        capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def unwrap(record):
    record = record.get("value", record)
    return record.get("value", record)


def text(prop):
    return "".join(part[0] for part in prop or [] if part[0] != "‣")


def main():
    url = sys.argv[1]
    host = re.search(r"https://([^/]+)", url).group(1)
    raw = re.search(r"([0-9a-f]{32})", url).group(1)
    page_id = f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"

    chunk = post(host, "loadPageChunk", {"pageId": page_id, "limit": 100,
                 "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False})
    space_id = None
    groups = {}
    for record in chunk["recordMap"]["block"].values():
        block = unwrap(record)
        space_id = space_id or block.get("space_id")
        if block.get("type") != "collection_view":
            continue
        result = post(host, "queryCollection", {
            "source": {"type": "collection", "id": block["collection_id"], "spaceId": space_id},
            "collectionView": {"id": block["view_ids"][0], "spaceId": space_id},
            "loader": {"type": "reducer", "reducers": {"collection_group_results":
                       {"type": "results", "limit": 500}}, "searchQuery": "",
                       "userTimeZone": "America/New_York"}})
        rm = result["recordMap"]
        schema = unwrap(list(rm["collection"].values())[0])["schema"]
        names = {key: col["name"] for key, col in schema.items()}
        for block_id in result["result"]["reducerResults"]["collection_group_results"]["blockIds"]:
            row = unwrap(rm["block"][block_id])
            props = {names[k]: text(v) for k, v in row.get("properties", {}).items() if k in names}
            status = props.get("Status", "")
            if status == "Briefing" and "--all" not in sys.argv:
                continue
            edited = datetime.datetime.fromtimestamp(row["last_edited_time"] / 1000, datetime.timezone.utc)
            hours = (datetime.datetime.now(datetime.timezone.utc) - edited).total_seconds() / 3600
            groups.setdefault(status, []).append(
                f"{props.get('Name', '').strip()} ({props.get('Ad Format', '')}, {hours:.0f}h{' ⚠️' if hours >= 36 else ''})")
    for status, rows in groups.items():
        print(f"{status}: {len(rows)} batches · " + ", ".join(rows))


if __name__ == "__main__":
    main()
