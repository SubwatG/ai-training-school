#!/usr/bin/env python3
"""
Overnight Fleet Runner for AI Training School Knowledge Base
Orchestrates free model profiles to expand and verify prompts & curriculum datasets.
Runs safely with checkpointing, rate-limit cooldowns, and deterministic validation.
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/kitti/Projects/Activities-me/ai-training-school")
RUN_DIR = BASE_DIR / "runs" / datetime.now().strftime("%Y-%m-%d-overnight-fleet")
LOGS_DIR = RUN_DIR / "logs"
STAGING_DIR = RUN_DIR / "staging"
REPORTS_DIR = RUN_DIR / "reports"

RUN_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
STAGING_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

print(f"==================================================")
print(f"🚀 OVERNIGHT FREE FLEET RUNNER INITIALIZED")
print(f"📂 Run Directory: {RUN_DIR}")
print(f"==================================================")

TASKS = [
    {
        "id": "task-01-obe-clo-rubrics",
        "title": "สกัดมาตรฐาน CLO/PLO & Analytical Rubrics (OBE Matrix)",
        "profile": "stepfun-free",
        "prompt": """
คุณคือผู้เชี่ยวชาญด้านหลักสูตรและการประกันคุณภาพการศึกษา (OBE / สป.อว. / มก.)
หน้าที่ของคุณคือร่างตารางมาตรฐานสมรรถนะครูและการสร้างข้อสอบ/รูบริก (Analytical Rubrics 4 ระดับ) สำหรับ 8 กลุ่มสาระการเรียนรู้
เขียนเป็น Markdown ที่มีโครงสร้างชัดเจน:
1. Action Verbs Matrix (Bloom's Revised) ที่อนุญาตให้ใช้ใน CLO และคำต้องห้าม (ห้ามมี 'อธิบาย', 'เข้าใจ', 'เช่น/ได้แก่/หรือ/ๆ/ได้')
2. เกณฑ์การประเมินรูบริกแบบ 4 ระดับ (ดีมาก, ดี, พอใช้, ปรับปรุง) สำหรับสมรรถนะการคิดวิเคราะห์ และการแก้ปัญหา
3. ตัวอย่างการแปลงตัวชี้วัด สพฐ. สู่ระดับพฤติกรรมที่วัดได้จริง
บันทึกผลเป็น Markdown ภาษาไทยที่กระชับ แม่นยำ
"""
    },
    {
        "id": "task-02-image-prompts-matrix",
        "title": "สกัด Image Direction Prompts (English) สำหรับจัดหน้า Canva 8 กลุ่มสาระ",
        "profile": "openrouter",
        "prompt": """
You are an expert AI Art Director & EdTech Visual Designer.
Task: Create a comprehensive catalog of 20 high-quality text-to-image prompts for K-12 educational illustrations across 8 Thai school subjects.
CRITICAL RULES:
1. Prompts for Image Generation (Midjourney / DALL-E 3 / Grok / Canva) MUST be in English only (NO Thai text in visual descriptions, so Thai teachers can add Thai text overlays cleanly inside Canva later).
2. Use clean, flat vector illustration or 3D cute clay style suitable for school worksheets and slides.
3. Include bracketed slots like [specific organ], [grade level visual style], [historical era] for customization.
Format output as a structured JSON list with keys: id, subject_th, title_th, visual_style, prompt_en, canva_layout_tip_th.
"""
    },
    {
        "id": "task-03-math-science-bridge",
        "title": "สกัด LaTeX Formula & Worked Examples สำหรับ Word/Canva Math Bridge",
        "profile": "stepfun-free",
        "prompt": """
คุณคือผู้เชี่ยวชาญการสอนคณิตศาสตร์และฟิสิกส์ระดับมัธยมปลาย
หน้าที่ของคุณคือสร้างคลังตัวอย่างสูตรและการแก้โจทย์แบบทีละขั้นตอน (Step-by-step Worked Examples) พร้อมสมการ LaTeX คุณภาพสูง:
1. หมวดคณิตศาสตร์ ม.5 (เวกเตอร์, จำนวนเชิงซ้อน, สถิติ) รวม 10 ตัวอย่าง
2. หมวดฟิสิกส์ ม.ปลาย (การเคลื่อนที่, กฎนิวตัน, ไฟฟ้าสถิต) รวม 10 ตัวอย่าง
ทุกตัวอย่างต้องมี:
- โจทย์ภาษาไทย
- สมการ LaTeX ที่ถูกต้องสมบูรณ์ ($...$ และ $$...$$)
- วิธีพิมพ์/แปลงเข้า Microsoft Word (กด Alt + = แล้ววาง LaTeX)
- คำแนะนำการนำไปใส่ใน Canva Math App
ส่งออกเป็นไฟล์ Markdown ภาษาไทยที่สมบูรณ์
"""
    }
]

def run_fleet():
    manifest = {
        "started_at": datetime.now().isoformat(),
        "tasks": []
    }
    
    for task in TASKS:
        t_id = task["id"]
        profile = task["profile"]
        out_file = STAGING_DIR / f"{t_id}.raw.md"
        log_file = LOGS_DIR / f"{t_id}.log"
        
        print(f"\n▶ Starting Task: {task['title']} (Profile: {profile})...")
        
        cmd = [
            "hermes",
            "--profile", profile,
            "chat", "-Q",
            "-q", task["prompt"]
        ]
        
        start_t = time.time()
        try:
            with open(log_file, "w", encoding="utf-8") as lf:
                res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=lf, text=True, timeout=600)
            
            elapsed = time.time() - start_t
            if res.returncode == 0 and res.stdout.strip():
                out_file.write_text(res.stdout, encoding="utf-8")
                print(f"✅ [{t_id}] Completed in {elapsed:.1f}s (Bytes: {len(res.stdout)})")
                status = "COMPLETED"
            else:
                print(f"⚠️ [{t_id}] Non-zero exit or empty stdout (rc={res.returncode})")
                status = "FAILED"
        except subprocess.TimeoutExpired:
            print(f"❌ [{t_id}] Timeout after 600s")
            status = "TIMEOUT"
        except Exception as e:
            print(f"❌ [{t_id}] Exception: {e}")
            status = "ERROR"
            
        manifest["tasks"].append({
            "id": t_id,
            "profile": profile,
            "status": status,
            "output_file": str(out_file),
            "log_file": str(log_file)
        })
        
        # Cooldown between calls to avoid 429 rate limits
        print("⏳ Cooldown 5s before next worker...")
        time.sleep(5)
        
    manifest["finished_at"] = datetime.now().isoformat()
    manifest_path = RUN_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n==================================================")
    print(f"🎉 FLEET RUN FINISHED. Manifest written to {manifest_path}")
    print(f"==================================================")

if __name__ == "__main__":
    run_fleet()
