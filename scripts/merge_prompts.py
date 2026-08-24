import json
import os
import sys

master_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts-data.json'
missing_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts-missing-2026-08-22.json'

with open(master_path, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

with open(missing_path, 'r', encoding='utf-8') as f:
    missing_data = json.load(f)

print(f"Master prompts before: {len(master_data)}")
print(f"New prompts to merge: {len(missing_data)}")

existing_ids = {p['id'] for p in master_data}
merged_count = 0

for item in missing_data:
    if item['id'] in existing_ids:
        print(f"Warning: duplicate ID {item['id']}, skipping...")
    else:
        master_data.append(item)
        existing_ids.add(item['id'])
        merged_count += 1

print(f"Successfully added {merged_count} new prompts.")
print(f"Master prompts after: {len(master_data)}")

with open(master_path, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Updated {master_path} ({os.path.getsize(master_path)} bytes)")
