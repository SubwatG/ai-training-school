import json, re, sys, os

def verify():
    print("=== Verification Gate 2: UI & Logic Consistency ===")
    
    # 1. Read prompts.html
    html_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts.html'
    with open(html_path, 'r', encoding='utf-8') as fp:
        html = fp.read()
        
    # Check top 10 elements
    if 'id="btn-show-top10"' not in html or 'id="btn-show-all"' not in html:
        print("[FAIL] Missing Top 10 filter buttons in prompts.html")
        return False
        
    # Check 8 learning areas
    areas = [
        "ภาษาไทย", "คณิตศาสตร์", "วิทยาศาสตร์และเทคโนโลยี", 
        "สังคมศึกษา ศาสนา และวัฒนธรรม", "สุขศึกษาและพลศึกษา", 
        "ศิลปะ", "การงานอาชีพ", "ภาษาต่างประเทศ"
    ]
    for area in areas:
        if f'data-subject="{area}"' not in html:
            print(f"[FAIL] Missing subject chip for '{area}' in prompts.html")
            return False
            
    print("[PASS] HTML Structure has Top 10 buttons and all 8 Subject chips.")

    # 2. Read app.js
    js_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/assets/js/app.js'
    with open(js_path, 'r', encoding='utf-8') as fp:
        js = fp.read()
        
    if 'onlyTop10' not in js or 'curated_top10' not in js:
        print("[FAIL] app.js does not handle curated_top10 logic")
        return False
        
    if 'setupTop10Buttons' not in js:
        print("[FAIL] app.js missing setupTop10Buttons handler")
        return False
        
    print("[PASS] app.js contains Top 10 toggle logic and event listeners.")

    # 3. Simulate Filter logic in Python (matches JS)
    json_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts-data.json'
    with open(json_path, 'r', encoding='utf-8') as fp:
        data = json.load(fp)

    # Test Top 10 count
    top10_items = [p for p in data if p.get('curated_top10')]
    print(f"[INFO] Curated Top 10 items in DB: {len(top10_items)}")
    if len(top10_items) < 10:
        print(f"[FAIL] Expected at least 10 items in top10, found {len(top10_items)}")
        return False

    # Test Search Keywords Simulation
    test_queries = ["คณิต", "SDQ", "แผน", "ว.PA", "ข้อสอบ", "Canva", "LaTeX", "สปีดรัน"]
    for q in test_queries:
        matches = [p for p in data if q.lower() in (p.get('title','') + p.get('prompt_template','') + ' '.join(p.get('tags',[]))).lower()]
        print(f"  - Search query '{q}': found {len(matches)} matches")
        if len(matches) == 0:
            print(f"[FAIL] Query '{q}' returned 0 matches!")
            return False

    print("\n[SUCCESS] Gate 2 Passed: UI markup, JS state management, and search queries verified.")
    return True

if __name__ == '__main__':
    success = verify()
    sys.exit(0 if success else 1)
