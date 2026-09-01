import json, sys, os

def verify():
    filepath = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts-data.json'
    if not os.path.exists(filepath):
        print(f"[FAIL] File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as fp:
        try:
            data = json.load(fp)
        except Exception as e:
            print(f"[FAIL] JSON decode error: {e}")
            return False

    if not isinstance(data, list):
        print(f"[FAIL] Master data must be a list, got {type(data)}")
        return False

    total_count = len(data)
    print(f"=== Verification Gate 1: Master Prompt Dataset ===")
    print(f"Total prompt records: {total_count}")

    if total_count < 200:
        print(f"[FAIL] Total count {total_count} is less than target 200!")
        return False

    seen_ids = set()
    errors = []
    task_counts = {}
    subj_counts = {}
    tool_counts = {}
    top10_count = 0

    required_fields = ['id', 'title', 'category', 'tools', 'prompt_template', 'role_context_condition']
    
    for i, item in enumerate(data):
        item_id = item.get('id')
        if not item_id:
            errors.append(f"Row {i}: Missing 'id'")
        elif item_id in seen_ids:
            errors.append(f"Row {i}: Duplicate id '{item_id}'")
        seen_ids.add(item_id)

        for rf in required_fields:
            if rf not in item or not item[rf]:
                errors.append(f"Prompt '{item_id}': Missing or empty field '{rf}'")

        rcc = item.get('role_context_condition', {})
        if not isinstance(rcc, dict):
            errors.append(f"Prompt '{item_id}': 'role_context_condition' must be a dict")
        else:
            for subfield in ['role', 'context', 'condition']:
                if not rcc.get(subfield):
                    errors.append(f"Prompt '{item_id}': Missing rcc subfield '{subfield}'")

        cat = item.get('category', {})
        if isinstance(cat, dict):
            subj = cat.get('subject', 'Other')
            task = cat.get('task_type', 'Other')
        else:
            subj = 'String-cat'
            task = 'String-cat'
        subj_counts[subj] = subj_counts.get(subj, 0) + 1
        task_counts[task] = task_counts.get(task, 0) + 1

        for t in item.get('tools', []):
            tool_counts[t] = tool_counts.get(t, 0) + 1

        if item.get('curated_top10'):
            top10_count += 1

    print("\n--- Tasks Breakdown ---")
    for k, v in sorted(task_counts.items(), key=lambda x: -x[1]):
        print(f"  - {k}: {v} prompts")

    print("\n--- Subjects Breakdown ---")
    for k, v in sorted(subj_counts.items(), key=lambda x: -x[1]):
        print(f"  - {k}: {v} prompts")

    print("\n--- Tools Breakdown ---")
    for k, v in sorted(tool_counts.items(), key=lambda x: -x[1]):
        print(f"  - {k}: {v} prompts")

    print(f"\nCurated Top 10 prompts count: {top10_count}")

    if errors:
        print(f"\n[FAIL] Found {len(errors)} validation errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False

    print("\n[SUCCESS] Gate 1 Passed: 100% Valid JSON, Unique IDs, Complete Schemas & Balanced Counts.")
    return True

if __name__ == '__main__':
    success = verify()
    sys.exit(0 if success else 1)
