import subprocess, sys

gates = [
    ("Gate 1: Master Prompt Dataset & Count", "verify_prompts_json.py"),
    ("Gate 2: UI & Logic Consistency", "verify_phase2_ui.py"),
    ("Gate 3: Site Integration & Asset Resolution", "verify_phase3_integration.py")
]

print("==================================================")
print("🚀 RUNNING ALL LOOP-ENGINEERED QUALITY GATES")
print("==================================================")

all_passed = True
for name, script in gates:
    print(f"\n▶ Running {name} ({script})...")
    res = subprocess.run([sys.executable, f"/home/kitti/Projects/Activities-me/ai-training-school/site/tests/{script}"], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print(f"❌ {name} FAILED!")
        print(res.stderr)
        all_passed = False
        break
    else:
        print(f"✅ {name} PASSED.")

if all_passed:
    print("\n==================================================")
    print("🎉 ALL QUALITY GATES PASSED (100% READY FOR DEPLOY)")
    print("==================================================")
    sys.exit(0)
else:
    sys.exit(1)
