# Implementation Plan: AI Training School Web & Prompt Ecosystem Upgrade
**Loop-Engineered Quality & Verification Protocol**

- **Date:** 2026-08-18 21:42 (+07)
- **Target Project:** `ai-training-school` (AI Teacher Training Workshop, 29 Aug 2026)
- **Workspace:** `/home/kitti/Projects/Activities-me/ai-training-school/`
- **Methodology:** Strict **Loop-Engineering & Re-check Gate** (Automated DOM/Syntax/Contrast/Interactive verification after each HTML/Data phase before proceeding to next phase)

---

## 1. Executive Summary & Goals

ยกระดับระบบนิเวศเว็บไซต์และคลัง Prompt (`site/`) สำหรับการอบรมครู 1 วัน (29 ส.ค. 2569) ให้มีความสมบูรณ์แบบสูงสุด ครอบคลุมภาระงานจริงของครูไทย 100% ใช้งานง่ายบนมือถือและคอมพิวเตอร์ และมีความเสถียรไร้ข้อผิดพลาดทางเทคนิค

### Key Deliverables:
1. **คลัง Prompt ครอบคลุมภาระงานครูไทย 8 กลุ่มสาระ + 4 เสาหลักภาระงานโรงเรียน:**
   - ระบบดูแลช่วยเหลือนักเรียน (SDQ / เยี่ยมบ้าน / โฮมรูม / ปพ.6)
   - งานวัดและประเมินผล (แบบฝึกซ่อมเสริม 0-ร-มส / Item Analysis / Rubrics 5 สมรรถนะ)
   - งานพัฒนาวิชาชีพ (PLC Log 5 ขั้น / CAR วิจัยในชั้นเรียนฉบับย่อ 3 หน้า)
   - กิจกรรมพัฒนาผู้เรียน (ลูกเสือ-เนตรนารี / แนะแนว / ชุมนุม / SAR โครงการ)
   - Math Equation Bridge & STEM Scaffolding
2. **UX/UI Interactive Enhancement (Paper/Ink/Rust Theme):**
   - แถบ **"Top 10 Teacher Survival Kit (10 Prompt กู้ชีพครูไทย)"** คัดสรรด้านบนสุด
   - ตัวกรอง 8 กลุ่มสาระการเรียนรู้ตามหลักสูตรแกนกลาง 2551
   - Modal หรือ Drawer แสดงตัวอย่างวิธีนำไปใช้จริง และปุ่ม Copy 1-click ที่เสถียร
   - Contrast & Math safety (KaTeX Delimiter verification, Dark/Light mode safety)
3. **Loop-Engineering Quality Gate:**
   - เขียน Verification Script ตรวจสอบทุกรอบ: JSON Schema, HTML Tag Pairing, Broken Links, JS Error, KaTeX Delimiters, WCAG Contrast

---

## 2. Architecture & File Mapping

```
ai-training-school/
├── site/
│   ├── index.html                   # Landing page & Workshop Framework (Phase 3)
│   ├── prompts.html                 # Prompt Library with Filters & Top 10 Kit (Phase 2)
│   ├── tutorials.html               # Step-by-step Guides with GIF (Phase 3)
│   ├── showcase.html                # Gallery & Padlet Integration (Phase 3)
│   ├── prompts-data.json            # Master Prompt JSON (Phase 1)
│   ├── assets/
│   │   ├── css/styles.css           # Design Tokens & UI Styles (Phase 2)
│   │   └── js/app.js                # Core JS logic & Event Listeners (Phase 2)
└── tests/ (or scripts/verify/)
    ├── verify_prompts_json.py       # JSON schema & sanity validator
    ├── verify_html_pages.py         # Static HTML/DOM validator
    └── verify_browser_render.py     # Headless DOM & console error test
```

---

## 3. Step-by-Step Implementation Plan with Loop-Engineer Gates

### Phase 1: Master Prompt Dataset Expansion & Normalization (`prompts-data.json`)
*เป้าหมาย: เพิ่ม Prompt ให้ครอบคลุมภาระงานครูไทยจริง เติมเต็มสัดส่วน 8 กลุ่มสาระ และปรับ Schema ให้สมบูรณ์ 100%*

- **Task 1.1: Schema Normalization & Variable Tags**
  - ตรวจสอบให้ทุกรายการมีโครงสร้าง: `id`, `title`, `category` (`subject`, `task_type`), `tools`, `tags`, `role_context_condition` (`role`, `context`, `condition`), `prompt_template`, `tips`, `source`, `curated_top10` (boolean)
  - ปรับปรุง Placeholder ตัวแปรให้เป็นรูปแบบมาตรฐาน `[ระบุตัวชี้วัด เช่น ค 1.1 ม.2/1]` พร้อมตัวอย่างคำตอบ
- **Task 1.2: Add Missing Thai Teacher Core Tasks (25+ New High-Signal Prompts)**
  - *Student Support:* `sdq-screening-action-plan`, `home-visit-5-dimensions`, `homeroom-sel-weekly`, `pp6-positive-growth-comments`
  - *Assessment & Remedial:* `remedial-task-generator-zero-r`, `item-analysis-difficulty-discrimination`, `core-competency-rubric-5`
  - *PLC & CAR:* `plc-meeting-log-5steps`, `car-3page-sar-summary`, `peer-observation-coaching`
  - *Activities & School Admin:* `scout-base-learning-skills`, `guidance-career-exploration`, `project-sar-5parts-evaluation`
  - *8 Subject-Specific Prompts:* ภาษาไทย (อ่านเอาเรื่อง), สังคมฯ (แก้ปัญหาประวัติศาสตร์ท้องถิ่น), วิทยาศาสตร์ (สะเต็มสืบเสาะ), ภาษาต่างประเทศ (CEFR A1-B1 Dialogue), ศิลปะ/ดนตรี, สุขศึกษา/พละ, การงานอาชีพ
- 🔁 **Loop-Engineer Gate 1 (Data Verification):**
  - รันสคริปต์ `verify_prompts_json.py`:
    1. ตรวจสอบ Valid JSON & UTF-8 Encoding
    2. ตรวจสอบ Unique IDs ไม่ซ้ำกัน
    3. ตรวจสอบความครบถ้วนของ Field บังคับทุก Record
    4. ตรวจสอบว่าไม่มี raw unescaped characters ที่ทำให้ JS พัง
  - *Rule:* ต้องผ่าน 100% (Exit code 0) ก่อนเริ่ม Phase 2

---

### Phase 2: UI/UX & Interactive Features Upgrade (`prompts.html`, `app.js`, `styles.css`)
*เป้าหมาย: เพิ่มแถบ Top 10 กู้ชีพครูไทย, ตัวกรอง 8 กลุ่มสาระ, ปรับปรุงระบบค้นหา และระบบคัดลอก*

- **Task 2.1: Implement "Top 10 Teacher Survival Kit" Carousel/Grid**
  - เพิ่ม Hero Section / Pinned Tab ด้านบนของ `prompts.html` แสดง 10 Prompt ที่ครูจำเป็นต้องใช้มากที่สุด ใช้งานได้ทันทีใน 1 คลิก
- **Task 2.2: Implement 8 Standard Subject Filter Chips**
  - เพิ่มตัวกรองกลุ่มสาระ: ทุกวิชา / ภาษาไทย / คณิตศาสตร์ / วิทยาศาสตร์และเทคโนโลยี / สังคมศึกษาฯ / สุขศึกษาและพลศึกษา / ศิลปะ / การงานอาชีพ / ภาษาต่างประเทศ
  - อัปเดต Filter Logic ใน `app.js` รองรับ Multi-tag Filtering (Subject + Task Type + Tool + Search Query)
- **Task 2.3: Interactive Copy & Template Fill Drawer (Modal / Preview)**
  - ปรับปรุงการกดการ์ดเพื่อเปิดดูสูตร 3 ส่วน (Role / Context / Condition) แบบขยาย พร้อมปุ่ม "คัดลอกเฉพาะ Prompt" และ "คัดลอกคำแนะนำ (Tips)"
  - เพิ่ม Toast Notification แจ้งเตือนเมื่อคัดลอกสำเร็จที่สวยงามและชัดเจน
- **Task 2.4: Styling & Contrast Refinement (Paper/Ink/Rust)**
  - ใช้ Token Design: Light Paper (`#FAF8F5`), Ink (`#1C1917`), Rust (`#A63D1C`), Slate (`#2B5C8F`)
  - ตรวจสอบ `.katex` formula styling, line-height, text wrapping ไม่ให้ตัวอักษรตกบรรทัด
- 🔁 **Loop-Engineer Gate 2 (UI & Interactive Testing):**
  - รันการตรวจสอบ Static HTML & JavaScript Syntax
  - รัน headless test / local server query เพื่อทดสอบ:
    1. Search query ทดสอบ 10 คำหลัก (เช่น "คณิต", "SDQ", "แผน", "ว.PA") ต้องคืนผลลัพธ์ถูกต้อง ไม่ว่างเปล่า
    2. Filter chips ทุกปุ่มทำงานถูกต้อง แสดงจำนวน prompt count สอดคล้องจริง
    3. Copy button handler ไม่ throw Exception
    4. ไม่เกิด layout shift หรือ horizontal overflow บน viewport 375px (Mobile) และ 1440px (Desktop)
  - *Rule:* ต้องผ่านการ Re-check ครบทุกข้อก่อนเริ่ม Phase 3

---

### Phase 3: Site-Wide Consistency, Guides & Polish (`index.html`, `tutorials.html`, `showcase.html`)
*เป้าหมาย: ปรับเนื้อหาหน้าอื่นๆ ให้สอดคล้องกับคลัง Prompt ใหม่ และโครงร่างการอบรม v2 (Tool-based 3 ตัว + สปีดรัน 80 นาที)*

- **Task 3.1: Sync `index.html` Roadmap & Mental Models**
  - อัปเดต Roadmap สู่ 3 เสาหลัก: คุยให้ถูกทาง (Prompting) $\rightarrow$ วางงานให้ถูกตัว (Gemini+NotebookLM $\rightarrow$ Canva) $\rightarrow$ ตรวจให้ชัวร์ก่อนใช้ (Verification & Privacy)
  - เชื่อมโยง CTA Card ตรงสู่ `prompts.html#top10`
- **Task 3.2: Enhance `tutorials.html` with Math Bridge & Speedrun Guides**
  - เพิ่มหัวข้อย่อย "เทคนิคแปลงสูตรคณิตศาสตร์ (LaTeX $\rightarrow$ Word Alt+= / Canva Math)"
  - เพิ่มหัวข้อย่อย "สูตรสปีดรัน 80 นาที (ย่อยเนื้อหา $\rightarrow$ ทำเสียง $\rightarrow$ จัดโปสเตอร์)"
- **Task 3.3: Update `showcase.html` Templates & Submission Links**
  - เตรียม Slot แสดงตัวอย่างผลงาน AI Speedrun (โปสเตอร์ + ไฟล์เสียง Audio Overview + ใบงาน)
- 🔁 **Loop-Engineer Gate 3 (Full Site Integration Check):**
  - ตรวจสอบ Hyperlink ทั้งระบบ (Navigation, Footer, Internal Anchors `#...`) ไม่มี broken link
  - ตรวจสอบ Asset paths (GIFs, CSS, JS) โหลดได้ครบ 100%
  - ตรวจสอบความถูกต้องของภาษาไทย (No CJK contamination, No raw unrendered KaTeX escape codes)

---

### Phase 4: Production Deployment & Handout Assets Readiness
*เป้าหมาย: เตรียม Deploy สู่ GitHub Pages และสร้าง QR Code สำหรับแจกในห้องอบรม*

- **Task 4.1: Production Build & Asset Optimization**
  - ตรวจสอบ Base URL สำหรับ GitHub Pages ให้รองรับ relative path อย่างถูกต้อง
- **Task 4.2: Final End-to-End Verification & Documentation**
  - บันทึกรายงานสถานะการทดสอบลงใน `progress-dashboard.html`
  - สรุป QR Code Link และเอกสารคู่มือพร้อมใช้งาน

---

## 4. Verification Checklist (Loop-Engineer Gateways)

| Phase | Check Item | Tool / Method | Acceptance Criteria |
|---|---|---|---|
| **Phase 1** | Schema & JSON Integrity | Python `json.load` + Custom Validator | Valid JSON, 0 missing fields, 0 duplicate IDs |
| **Phase 1** | Thai Pedagogy Coverage | Coverage Analyzer Script | ครบ 8 กลุ่มสาระ + 4 งานโรงเรียน (SDQ/PLC/CAR/ปพ.) |
| **Phase 2** | UI Component Rendering | Automated DOM Query / Node / Python | Filter ทำงานได้ทุกปุ่ม, Count ตรงกับ Data |
| **Phase 2** | Responsive & Mobile UI | CSS / Viewport Validation | ไม่มี element ล้นจอที่ 375px, font อ่านง่าย |
| **Phase 3** | Link & Asset Resolution | HTTP Server Link Checker | 200 OK ทุก URL, ไม่มี 404 Assets/GIFs |
| **Phase 3** | Typography & Math Escape | Regex & Content Scanner | ไม่มี `\begin` ค้างนอกบล็อก, แสดงผลภาษาไทยถูกต้อง |
| **Phase 4** | E2E Usability Test | User Journey Simulation | เปิดหน้าเว็บ $\rightarrow$ ค้นหา $\rightarrow$ กดคัดลอก $\rightarrow$ แสดง Toast ภายใน < 1 วิ |

---

## 5. Risks & Mitigation Strategies

1. **Risk:** ปริมาณ Prompt เยอะเกินไป (200+ รายการ) ทำให้ครูหาไม่เจอในเวลาจำกัด 1 วัน
   - *Mitigation:* บังคับให้มีแท็บ **Top 10 Teacher Survival Kit** เด่นชัดที่ส่วนบนสุด เพื่อให้ครูเปิดใช้งานได้ทันทีโดยไม่ต้องค้นหา
2. **Risk:** ครูนำ Prompt ไปใช้แล้วใส่ข้อมูลไม่ถูก หรือลบตัวแปรไม่หมด
   - *Mitigation:* กำกับตัวอย่างในวงเล็บ `[... เช่น ค 1.1 ม.2/1]` และมีคำอธิบาย Tips สั้นๆ ทุกการ์ด
3. **Risk:** ปัญหาการแสดงผลฟอนต์ภาษาไทยหรือสูตรคณิตศาสตร์ในบางเบราว์เซอร์
   - *Mitigation:* ใช้ Web Fonts มาตรฐาน Google Fonts (`Chakra Petch` + `IBM Plex Sans Thai Looped`) พร้อม Fallback ระบบ และใช้ KaTeX CDN แบบเสถียร
