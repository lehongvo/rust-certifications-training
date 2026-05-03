#!/usr/bin/env python3
"""Test parser: parse W1 Monday and print blocks before uploading."""
import sys
sys.path.insert(0, '.')
from _upload_daily import parse_makeplan, extract_section_blocks, extract_tasks

days = parse_makeplan(1)
w1_mon = next((d for d in days if d["week"] == 1 and "MON" in d["day_name"].upper()), None)

if not w1_mon:
    print("W1 Monday not found")
    sys.exit(1)

print(f"=== W1 Mon {w1_mon['date']} ===")
print(f"Theme: {w1_mon['theme']}")
print(f"Body length: {len(w1_mon['body'])} chars")
print()
print("--- Extracted tasks ---")
for t in extract_tasks(w1_mon['body']):
    print(f"  [ ] {t}")
print()
print("--- Notion blocks (page body) ---")
blocks = extract_section_blocks(w1_mon['body'])
for i, b in enumerate(blocks):
    btype = b["type"]
    text = ""
    if btype in ("paragraph", "bulleted_list_item"):
        rt = b[btype]["rich_text"]
        text = "".join(r["text"]["content"] for r in rt)
    elif btype.startswith("heading_"):
        rt = b[btype]["rich_text"]
        text = "".join(r["text"]["content"] for r in rt)
    elif btype == "to_do":
        rt = b["to_do"]["rich_text"]
        text = "".join(r["text"]["content"] for r in rt)
    print(f"  {i:2}. [{btype:25}] {text[:100]}")
print()
print(f"Total blocks: {len(blocks)}")
