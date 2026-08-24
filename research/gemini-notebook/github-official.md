---
topic: NotebookLM — GitHub ecosystem + official Google sources (features timeline & education)
date: 2026-08-23
sources_count: 47
---
# NotebookLM (Gemini Notebook): GitHub Ecosystem + Official Google Timeline

> **หมายเหตุสำคัญ (Rebrand):** ตั้งแต่กรกฎาคม 2026 NotebookLM เปลี่ยนชื่อเป็น **Gemini Notebook** — ผลิตภัณฑ์เดิมเดียวกัน ใช้โดเมน notebooklm.google เหมือนเดิม และ notebook เดิมเข้าถึงได้ทั้งหมด [Source: notebooklm.google FAQ](https://notebooklm.google/) (2026-07)
>
> **จุดยืนเรื่อง API:** Google ยังไม่เปิด API สาธารณะ (consumer) สำหรับ NotebookLM ผู้ใช้ทั่วไป — เครื่องมือ GitHub ส่วนใหญ่จึงเป็น wrapper เรียก Web API แบบไม่เป็นทางการ ขณะที่ **NotebookLM Enterprise (บน Google Cloud)** มี API อย่างเป็นทางการสำหรับองค์กร [Source: Google AI Developers Forum](https://discuss.ai.google.dev/t/notebooklm-api/55950) (n.d.) · [Source: Google Cloud docs](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) (n.d.)

## Executive summary (Thai)

NotebookLM (ปัจจุบันคือ Gemini Notebook) เป็นเครื่องมือ AI "อิงแหล่งข้อมูล" (source-grounded) ของ Google ที่ผู้ใช้ upload เอกสาร/เว็บ/YouTube แล้วถามคำถามโดย AI ตอบพร้อม citation — และสร้างผลผลิตหลากหลายรูปแบบ (Audio Overview แบบพอดแคสต์, Video Overview, Mind Map, แบบทดสอบ, แฟลชการ์ด) จากการสำรวจครั้งนี้:

- **GitHub เติบโตเป็นระบบนิเวศใหญ่** — มี wrapper/เครื่องมือ >18,000 stars เช่น `notebooklm-py` (Python API), `open-notebook` (>37k stars, NotebookLM แบบ open-source), MCP servers, CLI (nlm), ตัวแปลง PDF→PPT, และกระแสสร้าง "NotebookLM ทางเลือก" (SurfSense, notebookllama, PageLM)
- **Timeline ทางการ** — Audio Overviews เปิดตัว ก.ย. 2024 → 50+ ภาษา เม.ย. 2025 (รวมไทย) → Mind Maps เม.ย. 2025 → Video Overviews ก.ค. 2025 (80 ภาษา ส.ค. 2025) → NotebookLM Plus (ธ.ค. 2024, เข้า Google One AI Premium ก.พ. 2025) → Nano Banana ภาพประกอบ ก.ย.–ต.ค. 2025 → Gemini 3/Nano Banana Pro/Veo 3 + Cinematic Video Mar 2026 → Gemini 3.5/Agentic มิ.ย. 2026 → Rebrand เป็น Gemini Notebook ก.ค. 2026
- **ด้านการศึกษา** — Google ผลัก NotebookLM เข้าสู่ห้องเรียนจริงจัง: เป็น Core Workspace Service ของ Google Workspace for Education (ส.ค. 2025, ครอบคลุม FERPA/COPPA), มี Learning Guide, เชื่อม Google Classroom (เม.ย. 2026), และมีกรณีศึกษา FSU (มิ.ย. 2026)

## Findings (grouped by theme)

### 1. GitHub: Repos ที่สร้างบน/รอบ NotebookLM (stars ณ 2026-08-23)

**สรุปภาพรวม:** ระบบนิเวศ GitHub แบ่งเป็น 5 กลุ่มหลัก — (a) API wrappers/CLI/MCP สำหรับควบคุม NotebookLM จริง, (b) "NotebookLM ทางเลือก" แบบ open-source, (c) เครื่องมือแปลงเนื้อหาเข้าออก (exporter/PPT/หนังสือ), (d) รวมรวม prompt/awesome-list, (e) เครื่องมือที่เลียนแบบ Audio Overview (podcast generation)

#### a) API wrappers / CLI / MCP servers (ควบคุม NotebookLM จริงแบบไม่เป็นทางการ)

| Repo | Stars | ทำอะไร | URL |
|---|---|---|---|
| teng-lin/notebooklm-py | 18,869 | **Unofficial Python API + agentic skill** สำหรับ Gemini Notebook — เข้าถึงฟีเจอร์ครบผ่าน Python/CLI/MCP (รวมฟีเจอร์ที่ UI ไม่มี) ใช้กับ Claude Code, Codex, OpenClaw | https://github.com/teng-lin/notebooklm-py |
| jacob-bd/gemini-notebook-mcp-cli | 5,913 | **CLI + MCP server** ครบวงจร: `nlm notebook list/create`, เพิ่ม source, สร้าง Audio Overview, download artifacts, share public link; มีบน PyPI ชื่อ `notebooklm-mcp-cli` | https://github.com/jacob-bd/gemini-notebook-mcp-cli |
| PleasePrompto/notebooklm-mcp | 3,316 | **MCP server** ให้ AI agents (Claude Code, Codex) ค้นใน NotebookLM ได้คำตอบอิง citation — `npx notebooklm-mcp@latest` | https://github.com/PleasePrompto/notebooklm-mcp |
| PleasePrompto/notebooklm-skill | 7,670 | **Claude Code skill** ให้ Claude คุยกับ notebook ของผู้ใช้โดยตรง (browser automation + auth ถาวร) | https://github.com/PleasePrompto/notebooklm-skill |
| tmc/nlm | 387 | CLI สำหรับ NotebookLM — export flashcard เป็น Markdown/JSON/TSV/HTML, มี MCP server ในตัว | https://github.com/tmc/nlm |
| gnh1201/notebooklm-rest-api | 83 | REST API wrapper (FastAPI) ครอบ notebooklm-py | https://github.com/gnh1201/notebooklm-rest-api |

#### b) "NotebookLM ทางเลือก" แบบ open-source / self-hosted

| Repo | Stars | ทำอะไร | URL |
|---|---|---|---|
| lfnovo/open-notebook | 37,318 | **Open Source implementation ของ NotebookLM** — ใช้ local/multi-model, 100% ควบคุมข้อมูลเอง | https://github.com/lfnovo/open-notebook |
| MODSetter/SurfSense | 15,993 | NotebookLM ทางเลือกสำหรับค้น web แบบ live (Reddit, YT, IG, TikTok, Google Search, Maps ฯลฯ) ผ่าน platform เดียว, API หรือ MCP server | https://github.com/MODSetter/SurfSense |
| run-llama/notebookllama | 1,965 | ทางเลือกแบบ open-source (จากทีม LlamaIndex) — ใช้ LlamaCloud ไม่พึ่ง Gemini | https://github.com/run-llama/notebookllama |
| CaviraOSS/PageLM | 1,878 | เวอร์ชัน community ของ NotebookLM เน้นการศึกษา — แปลงสื่อเรียนเป็น quiz, flashcard, notes, podcast | https://github.com/CaviraOSS/PageLM |
| Goekdeniz-Guelmez/Local-NotebookLM | 1,027 | "Google's NotebookLM but local" | https://github.com/Goekdeniz-Guelmez/Local-NotebookLM |
| theaiautomators/insights-lm-public | 658 | ทางเลือก self-hosted — chat กับเอกสาร + สร้าง audio summaries (Supabase + N8N + React) | https://github.com/theaiautomators/insights-lm-public |

#### c) เครื่องมือแปลงเนื้อหา / สร้างผลผลิต (exporters, PPT, pipeline)

| Repo | Stars | ทำอะไร | URL |
|---|---|---|---|
| joeseesun/qiaomu-anything-to-notebooklm | 5,782 | ตัวป้อนเนื้อหาหลายแหล่ง (WeChat, web, YouTube, PDF, Markdown) เข้า NotebookLM → สร้าง Podcast/PPT/MindMap/Quiz | https://github.com/joeseesun/qiaomu-anything-to-notebooklm |
| zstmfhy/zlibrary-to-notebooklm | 1,704 | ดาวน์โหลดหนังสือจาก Z-Library อัตโนมัติแล้วอัปโหลดเข้า NotebookLM | https://github.com/zstmfhy/zlibrary-to-notebooklm |
| brianxiadong/auto-paper-digest | 581 | ติดตาม paper AI รายสัปดาห์บน Hugging Face → ดาวน์โหลด PDF → เข้า NotebookLM → สร้าง Video Overview เป็น digest อัตโนมัติ | https://github.com/brianxiadong/auto-paper-digest |
| elliottzheng/NotebookLM2PPT | 492 | แปลงสไลด์/โครงร่างจาก NotebookLM เป็น PPT ที่แก้ไขได้จริง (PDF → PPT) | https://github.com/elliottzheng/NotebookLM2PPT |

#### d) Audio Overview / podcast แบบเปิด

| Repo | Stars | ทำอะไร | URL |
|---|---|---|---|
| souzatharsis/podcastfy | 6,515 | **ทางเลือก open-source ของ Audio Overview** — แปลงเนื้อหาหลายรูปแบบเป็นบทสนทนาพอดแคสต์หลายภาษา (GenAI) | https://github.com/souzatharsis/podcastfy |

#### e) Awesome-lists / prompts

| Repo | Stars | ทำอะไร | URL |
|---|---|---|---|
| serenakeyitan/awesome-notebookLM-prompts | 4,533 | รวม prompt สำหรับสร้างสไลด์ด้วย NotebookLM ("AI powerpoint") | https://github.com/serenakeyitan/awesome-notebookLM-prompts |

**ข้อสังเกต:** repo wrapper ทั้งหมด (กลุ่ม a) เป็น **unofficial** — ต้องใช้ cookie/secrets ส่วนตัว (เช่น `nlm auth --print-env` ใน tmc/nlm) และอาจพังเมื่อ Google เปลี่ยน Web API; เหมาะสำหรับงานส่วนตัว/ทดลอง ไม่เหมาะกับองค์กรที่ต้องการ SLA (ผู้พัฒนาเองยอมรับจุดนี้ เช่น jacob-bd/gemini-notebook-mcp-cli อธิบายว่าเป็น "wrapper around an unofficial NotebookLM browser API" พร้อม "Honest constraints: Cookie..." — [Source](https://github.com/CreatmanCEO/notebooklm-claude-workflows) ซึ่งสร้างต่อจาก repo นั้น (2025)) — ส่วนองค์กรที่ต้องการ API จริง Google แนะนำ NotebookLM Enterprise [Source: Google Cloud](https://cloud.google.com/resources/notebooklm-enterprise) (n.d.)

### 2. Official Google: Feature Timeline 2024–2026

#### 2024
- **ก.ย. 2024 (11) — Audio Overviews เปิดตัว** ("Deep Dive" podcast 2 โฮสต์ AI จาก sources ของเรา; ตอนนั้นอังกฤษเท่านั้น, ยัง experimental, โหลดไฟล์เสียงได้) [Source: blog.google](https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/) (2024-09-11)
- **ธ.ค. 2024 (13) — เปิดตัว NotebookLM Plus** (แผนพรีเมียมสำหรับ power users/ทีม/องค์กร: notebook 500 อัน, 300 sources/notebook, Audio Overviews มากกว่าแบบฟรี ~5 เท่า, shared team notebooks, analytics) พร้อม Studio ใหม่ และ Audio Overview แบบโต้ตอบ (interactive audio) [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-new-features-december-2024/) (2024-12-13)

#### 2025
- **ก.พ. 2025 (10) — NotebookLM Plus เข้าแผน Google One AI Premium** (Gemini Advanced + 2TB + NotebookLM Plus ราคาเดิม); มีส่วนลดนักศึกษา 50% ($9.99/เดือน สหรัฐฯ อายุ 18+) [Source: blog.google](https://blog.google/feed/notebooklm-google-one/) (2025-02-10)
- **เม.ย. 2025 (3) — Mind Maps + ค้นหาแหล่งข้อมูล + อ่าน PDF พร้อมรูป/กราฟ**; ประกาศว่า "tens of thousands of schools" ใช้ NotebookLM เพื่อเรียน/วิจัย/สอน [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-studying-help/) (2025-04-03)
- **เม.ย. 2025 (29) — Audio Overviews ใน 50+ ภาษา** (Afrikaans→Turkish) เพิ่มการตั้งค่า "Output Language" — ตัวอย่างครูให้นักเรียนสร้าง Audio Overview จากแหล่งข้อมูลหลายภาษาในภาษาที่ตัวเองถนัด [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-audio-overviews-50-languages/) (2025-04-29)
- **ก.ค. 2025 (29) — Video Overviews เปิดตัว** (วิดีโอเล่าแบบมีสไลด์ + เสียง AI) + Studio อัปเกรด: สร้าง overview หลายรูปแบบต่อ notebook, ปรับเวอร์ชันตามภาษา/บทบาท [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/) (2025-07-29)
- **ส.ค. 2025 — NotebookLM ใช้ได้ทุกบัญชี Workspace for Education** (เป็น Core Workspace Service ครอบ FERPA/COPPA — ไม่เอา data นักเรียนไปเทรน) [Source: Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/08/notebooklm-is-now-available-to-all.html) (2025-08)
- **ส.ค. 2025 (25) — Video Overviews ขยายเป็น 80 ภาษา** + Audio Overviews ทุกภาษาเป็นแบบ full-length (ลึกเท่าภาษาอังกฤษ) และเลือกความยาวสั้น/ยาวได้ [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/) (2025-08-25)
- **ก.ย. 2025 (8) — ฟีเจอร์นักเรียน: Learning Guide, flashcards, quizzes, reports** ("6 ways to use NotebookLM to master any subject") [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/) (2025-09-08); Learning Guide พร้อมใช้กับ Workspace for Education ทุกบัญชี [Source: Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/09/learning-guide-notebook-lm-workspace-education.html) (2025-09)
- **ต.ค. 2025 (13) — Video Overviews ใช้ Nano Banana** (โมเดลภาพ Gemini 2.5 Flash Image) — 6 สไตล์ภาพ: Watercolor, Papercraft, Anime, Whiteboard, Retro Print, Heritage + รูปแบบ "Brief" สำหรับสรุปไว [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/video-overviews-nano-banana/) (2025-10-13)
- **ต.ค. 2025 (29) — Chat อัปเกรดใหญ่** — context window ใหญ่ขึ้น 8 เท่า, จำบทสนทนาได้นานขึ้น 6 เท่า, คุณภาพตอบดีขึ้น 50%, ตั้ง "goals" (persona) ให้ notebook ได้ เช่น "ทำตัวเป็นครู" [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/) (2025-10-29)
- **พ.ย. 2025 — Nano Banana Pro เปิดตัวใน Workspace** (Slides, Vids, Gemini app, NotebookLM) — ยุค Gemini 3 (Gemini 3 เปิดตัว Nov 2025; ข่าว: NotebookLM หนึ่งในผลิตภัณฑ์ที่ได้พลังจาก Gemini 3/Nano Banana Pro) [Source: Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/11/workspace-nano-banana-pro.html) (2025-11) · [Source: CNBC (ข่าว)](https://www.cnbc.com/2025/11/20/google-nano-banana-pro-gemini-3.html) (2025-11-20)

#### 2026
- **มี.ค. 2026 (4) — Cinematic Video Overviews** — วิดีโอแบบ cinematic จาก Gemini 3 (เป็น "creative director" ตัดสินใจสไตล์ทั้งหมด) + Nano Banana Pro + วิดีโอจาก Veo 3; อังกฤษก่อน, เฉพาะ Google AI Ultra (18+) [Source: blog.google](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/) (2026-03-04)
- **เม.ย. 2026 — NotebookLM เข้า Google Classroom** (ครูสร้าง/มอบหมาย notebook + Gems; นักเรียนสร้าง "personal class notebooks" ใน Classroom ได้) และขยายขีดจำกัดฟีเจอร์สำหรับ Education Plus / Teaching & Learning add-on [Source: Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/04/students-can-now-create-personal-class-notebooks-with-NotebookLM-in-Google-Classroom.html) (2026-04) · [Source: Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/04/expanded-notebooklm-capabilities-for-Education-Plus-and-Teaching-and-Learning-add-on-customers.html) (2026-04)
- **มิ.ย. 2026 (8) — อัปเกรดเป็น Gemini 3.5 + Antigravity** — research แบบ agentic (วางแผนหลายขั้น), รันโค้ด/วิเคราะห์ข้อมูล, สร้าง charts/spreadsheets/slide decks, "start with a loose idea" แล้ว AI หา source ให้; เริ่มจาก Google AI Ultra และ Workspace business บางแผน [Source: blog.google](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/) (2026-06-08, updated 2026-07-16)
- **ก.ค. 2026 — Rebrand: NotebookLM → Gemini Notebook** (ชื่อใหม่ ผลิตภัณฑ์เดิม) [Source: notebooklm.google](https://notebooklm.google/) (2026-07)

#### ภาษาไทย & การเข้าถึง (support ทางการ)
- **Audio Overviews สนับสนุนภาษาไทย** — อยู่ในรายชื่อ 80+ ภาษาของหน้าอย่างเป็นทางการ (list: Thai) [Source: support.google.com](https://support.google.com/gemininotebook/answer/16212820?hl=en) (ปัจจุบัน) — หมายเหตุ: interactive mode (พูดคุยกับโฮสต์) ยังอังกฤษเท่านั้น
- Video Overviews 80 ภาษา — ลิงก์รายชื่อภาษาทางการจากบล็อก Google [Source: support.google.com](https://support.google.com/notebooklm/answer/16454555?hl=en) (อ้างอิงในบล็อก 2025-08-25)

#### Enterprise / API
- **NotebookLM Enterprise (Gemini Notebook for enterprise)** — มีหน้าโปรดักต์บน Google Cloud และ **API สำหรับสร้าง/จัดการ notebooks อย่างเป็นทางการ** (ผ่าน Discovery Engine API, ใช้ gcloud auth) [Source: Google Cloud](https://cloud.google.com/resources/notebooklm-enterprise) (n.d.) · [Source: Cloud docs (API)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) (n.d.)
- **ยังไม่มี API สาธารณะสำหรับผู้ใช้ทั่วไป** — ยืนยันโดยทีม Google ในฟอรัมนักพัฒนา (ตอบ "no official date announced") [Source: discuss.ai.google.dev](https://discuss.ai.google.dev/t/notebooklm-api/55950) (n.d.)

### 3. กรณีศึกษาเพื่อการศึกษา (Official Google)

- **Florida State University (FSU) — มหาวิทยาลัย** (มิ.ย. 2026): pilot กับ Google for Education; NotebookLM ทำหน้าที่ "24/7 study partner" — สร้าง quiz และ study guide จากเนื้อหาคอร์สที่อาจารย์กำหนดโดยเฉพาะ (grounded ใน facts ของคอร์สเท่านั้น) นักเรียนที่เกรด C พลิกฟื้นเกรดในไม่กี่สัปดาห์; อาจารย์ประหยัดเวลา prep เพื่อไปโฟกัส mentoring [Source: blog.google (เขียนโดย CIO ของ FSU)](https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/) (2026-06-22)
- **Google for Education — หน้า customer stories**: ระบุว่ามีโรงเรียน/มหาวิทยาลัยหลายหมื่นแห่งใช้ NotebookLM สำหรับทำแบบฝึก, เขียน, research และเรียนรู้เชิงโต้ตอบด้วย Audio Overviews [Source: blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-studying-help/) (2025-04-03) → ลิงก์ customer stories: [blog.google/outreach-initiatives/education/customer-stories-gemini](https://blog.google/outreach-initiatives/education/customer-stories-gemini/)
- **หน้าโปรดักต์เพื่อการศึกษา**: Gemini Notebook สำหรับ K-12 และอุดมศึกษา — lesson plans, study guides, quizzes ที่อิงเนื้อหาของตัวเอง [Source: edu.google.com](https://edu.google.com/intl/ALL_us/ai-gemini-notebook/) (n.d.)

## Use-case table

| Use case | Who | Workflow | Source |
|---|---|---|---|
| ทบทวนบทเรียนด้วย "พอดแคสต์" จากเนื้อหาคอร์ส | นักเรียน/นักศึกษา | อัปโหลด PDF/สไลด์/YouTube lecture → กด Generate Audio Overview (เลือก Output Language เช่น ไทย) → ฟัง/ดาวน์โหลดได้ | [blog.google](https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/) (2024-09-11); [support: 80+ ภาษา](https://support.google.com/gemininotebook/answer/16212820?hl=en) |
| สร้างแบบทดสอบ/แฟลชการ์ด/study guide อัตโนมัติ | ครู & นักเรียน | ครูอัปโหลดเนื้อหาหน่วยเรียน → NotebookLM สร้าง quiz/flashcards/Learning Guide (ตัวช่วยติวแบบถาม-ตอบ) → แจกนักเรียนใน Classroom | [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/) (2025-09-08); [Workspace Classroom](https://workspaceupdates.googleblog.com/2026/04/students-can-now-create-personal-class-notebooks-with-NotebookLM-in-Google-Classroom.html) (2026-04) |
| "ติวเตอร์ 24/7" ระดับมหาวิทยาลัย | นักศึกษาปี 1–4 (กรณี FSU) | อัปโหลดเนื้อหาคอร์สที่อาจารย์กำหนด → ถามคำถามได้ตลอด 24 ชม. ได้คำตอบอิง citation เฉพาะคอร์ส → นักเรียนเกรด C พลิกเป็นผ่านในไม่กี่สัปดาห์ | [blog.google/FSU](https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/) (2026-06-22) |
| สร้าง Mind Map เชื่อมโยงแนวคิด | ครู/นักเรียน | กด chip "Mind Map" ใน chat → ได้แผนภาพแตกกิ่ง คลิกโหนดเพื่อถามเจาะหัวข้อนั้น | [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-studying-help/) (2025-04-03); [support](https://support.google.com/gemininotebook/answer/16212283?hl=en) |
| สรุปประเด็นใหญ่เป็นวิดีโอสไลด์/คลิป | ครู (สื่อการสอน), นักเรียน (ทบทวนก่อนสอบ) | สร้าง Video Overview (80 ภาษา, 6 สไตล์ภาพ Nano Banana) หรือ Cinematic Video (AI Ultra, EN) → แชร์/ดาวน์โหลด | [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/) (2025-07-29); [Nano Banana](https://blog.google/innovation-and-ai/models-and-research/google-labs/video-overviews-nano-banana/) (2025-10-13); [Cinematic](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/) (2026-03-04) |
| ระบบอัตโนมัติ: paper → notebook → video digest | นักวิจัย/ครูสายวิจัย | ใช้ auto-paper-digest ติดตาม paper บน Hugging Face → อัปโหลด PDF เข้า NotebookLM → สร้าง Video Overview อัตโนมัติสัปดาห์ละครั้ง | [github.com/brianxiadong/auto-paper-digest](https://github.com/brianxiadong/auto-paper-digest) (2026) |
| อัปโหลดเนื้อหาเป็นชุดจากหลายแหล่ง | ครู (รวมสื่อ), นักเรียน | ใช้ qiaomu-anything-to-notebooklm ป้อน WeChat article/web/YouTube/PDF → สร้าง Podcast/PPT/MindMap/Quiz ให้ NotebookLM | [github.com/joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) (2026) |
| ให้ AI agent ถามข้อมูลใน notebook ของเรา (RAG อิง citation) | ครู/นักวิจัยที่ใช้ Claude Code/Codex | ติดตั้ง notebooklm-mcp (npx) หรือ notebooklm-skill → agent ถาม notebook ได้คำตอบอิงแหล่ง + จัดการ library ได้ | [github.com/PleasePrompto/notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp) (2026) |
| ควบคุม/export notebook ผ่าน CLI | คนทำสื่อ/อัตโนมัติ | `nlm notebook list`, `nlm source add`, `nlm audio create`, `nlm download all` (gemini-notebook-mcp-cli หรือ tmc/nlm) | [github.com/jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) (2026) |
| สร้างสไลด์จาก NotebookLM เป็น PPT แก้ไขได้ | ครูทำสื่อการสอน | ใช้ NotebookLM2PPT แปลงโครงร่าง/สไลด์ที่สร้างด้วย NotebookLM เป็นไฟล์ PPT | [github.com/elliottzheng/NotebookLM2PPT](https://github.com/elliottzheng/NotebookLM2PPT) (2026) |
| องค์กร/มหาวิทยาลัยที่ต้องการ API + ควบคุมข้อมูล | IT มหาวิทยาลัย | ใช้ NotebookLM Enterprise บน Google Cloud — สร้าง/จัดการ notebooks ผ่าน API ทางการ (Discovery Engine) | [cloud.google.com](https://cloud.google.com/resources/notebooklm-enterprise); [API docs](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) |

## Pitfalls / limitations

- **ยังไม่มี API สาธารณะสำหรับผู้ใช้ทั่วไป** — wrapper บน GitHub ล้วน "unofficial" (เข้าผ่าน browser API/cookies) เสี่ยงพังเมื่อ Google เปลี่ยนฝั่ง server; องค์กรต้องซื้อ Enterprise ถึงได้ API ทางการ [Source](https://discuss.ai.google.dev/t/notebooklm-api/55950) · [Source](https://github.com/teng-lin/notebooklm-py) · [Source](https://github.com/jacob-bd/gemini-notebook-mcp-cli)
- **การันตีได้ว่าไม่ใช่ "แหล่งรวมที่ถูกต้องเสมอ"** — Google ระบุเองว่า Audio/Video Overviews เป็น AI-generated "may contain inaccuracies or audio glitches" และ Audio Overview "ไม่ใช่ภาพรวมที่ครบถ้วน/เป็นกลาง แต่สะท้อนแหล่งที่อัปโหลดเท่านั้น" [Source](https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/) (2024-09-11) · [Source](https://support.google.com/gemininotebook/answer/16212820?hl=en)
- **ข้อจำกัดด้านภาษา** — interactive Audio Overview (คุยกับโฮสต์) ยังอังกฤษเท่านั้นแม้ภาษาไทยจะสร้างไฟล์เสียงได้แล้ว [Source](https://support.google.com/gemininotebook/answer/16212820?hl=en); Cinematic Video Overviews เริ่มจากอังกฤษเท่านั้น [Source](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/) (2026-03-04)
- **ฟีเจอร์พรีเมียมอยู่หลัง paywall** — ฟีเจอร์ใหม่ขั้นสูง (Cinematic Video, Gemini 3.5 agentic) เริ่มจาก Google AI Ultra/Workspace บางแผนเท่านั้น; Plus ต้องสมัคร Google One AI Premium/Workspace [Source](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/) (2026-06-08)
- **เครื่องมือ GitHub ส่วนใหญ่เป็นงานอดิเรก** — อายุ repo สั้น, ผู้ดูแล 1–2 คน, ไม่มี SLA; ควรสำรองข้อมูล (เช่น export artifacts ผ่าน CLI) ก่อนพึ่งพา
- **ความเป็นส่วนตัว** — ฝั่งองค์กร/โรงเรียน: data ไม่ถูกนำไปเทรนและครอบ FERPA/COPPA (ประกาศทางการ) [Source](https://workspaceupdates.googleblog.com/2025/08/notebooklm-is-now-available-to-all.html) (2025-08) — แต่ wrapper unofficial ที่เก็บ cookies มีความเสี่ยงต่างออกไป (ผู้ใช้ต้องระวังเอง)

## Source list (numbered, full URLs)

### GitHub repos (stars ณ 2026-08-23)
1. lfnovo/open-notebook (37,318★) — https://github.com/lfnovo/open-notebook
2. teng-lin/notebooklm-py (18,869★) — https://github.com/teng-lin/notebooklm-py
3. MODSetter/SurfSense (15,993★) — https://github.com/MODSetter/SurfSense
4. PleasePrompto/notebooklm-skill (7,670★) — https://github.com/PleasePrompto/notebooklm-skill
5. souzatharsis/podcastfy (6,515★) — https://github.com/souzatharsis/podcastfy
6. jacob-bd/gemini-notebook-mcp-cli (5,913★) — https://github.com/jacob-bd/gemini-notebook-mcp-cli
7. joeseesun/qiaomu-anything-to-notebooklm (5,782★) — https://github.com/joeseesun/qiaomu-anything-to-notebooklm
8. serenakeyitan/awesome-notebookLM-prompts (4,533★) — https://github.com/serenakeyitan/awesome-notebookLM-prompts
9. PleasePrompto/notebooklm-mcp (3,316★) — https://github.com/PleasePrompto/notebooklm-mcp
10. run-llama/notebookllama (1,965★) — https://github.com/run-llama/notebookllama
11. CaviraOSS/PageLM (1,878★) — https://github.com/CaviraOSS/PageLM
12. zstmfhy/zlibrary-to-notebooklm (1,704★) — https://github.com/zstmfhy/zlibrary-to-notebooklm
13. Goekdeniz-Guelmez/Local-NotebookLM (1,027★) — https://github.com/Goekdeniz-Guelmez/Local-NotebookLM
14. theaiautomators/insights-lm-public (658★) — https://github.com/theaiautomators/insights-lm-public
15. brianxiadong/auto-paper-digest (581★) — https://github.com/brianxiadong/auto-paper-digest
16. elliottzheng/NotebookLM2PPT (492★) — https://github.com/elliottzheng/NotebookLM2PPT
17. tmc/nlm (387★) — https://github.com/tmc/nlm
18. gnh1201/notebooklm-rest-api (83★) — https://github.com/gnh1201/notebooklm-rest-api
19. CreatmanCEO/notebooklm-claude-workflows (workflow layer บน gemini-notebook-mcp-cli; ใช้เป็นหลักฐานเรื่องข้อจำกัด cookie) — https://github.com/CreatmanCEO/notebooklm-claude-workflows

### Official Google — blog.google / Google Labs / Google Cloud
20. Audio Overviews เปิดตัว — https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/ (2024-09-11)
21. NotebookLM Plus เปิดตัว — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-new-features-december-2024/ (2024-12-13)
22. NotebookLM Plus ใน Google One AI Premium + ส่วนลดนักเรียน — https://blog.google/feed/notebooklm-google-one/ (2025-02-10)
23. Mind Maps + ฟีเจอร์ศึกษา + "tens of thousands of schools" — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-studying-help/ (2025-04-03)
24. Audio Overviews 50+ ภาษา — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-audio-overviews-50-languages/ (2025-04-29)
25. Video Overviews เปิดตัว + Studio — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/ (2025-07-29)
26. Video Overviews 80 ภาษา + Audio full-length — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/ (2025-08-25)
27. ฟีเจอร์นักเรียน 6 อย่าง (Learning Guide ฯลฯ) — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/ (2025-09-08)
28. Video Overviews + Nano Banana (6 สไตล์) — https://blog.google/innovation-and-ai/models-and-research/google-labs/video-overviews-nano-banana/ (2025-10-13)
29. Chat อัปเกรด 8x context + custom goals — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/ (2025-10-29)
30. Cinematic Video Overviews (Gemini 3 + Nano Banana Pro + Veo 3) — https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/ (2026-03-04)
31. อัปเกรด Gemini 3.5 + Antigravity (agentic research) — https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/ (2026-06-08, upd. 2026-07-16)
32. หน้าโปรดักต์ Gemini Notebook + FAQ rebrand — https://notebooklm.google/ (2026-07)
33. กรณีศึกษา FSU (เขียนโดย CIO FSU) — https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/ (2026-06-22)
34. Google for Education customer stories (Gemini) — https://blog.google/outreach-initiatives/education/customer-stories-gemini/ (n.d.)
35. หน้าโปรดักต์การศึกษา (K-12/อุดมศึกษา) — https://edu.google.com/intl/ALL_us/ai-gemini-notebook/ (n.d.)
36. NotebookLM Enterprise (Google Cloud) — https://cloud.google.com/resources/notebooklm-enterprise (n.d.)
37. API สร้าง/จัดการ notebooks (NotebookLM Enterprise) — https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks (n.d.)

### Official Google — Workspace Updates & Support
38. NotebookLM สำหรับทุกบัญชี Workspace for Education (FERPA/COPPA) — https://workspaceupdates.googleblog.com/2025/08/notebooklm-is-now-available-to-all.html (2025-08)
39. Learning Guide สำหรับ Workspace for Education — https://workspaceupdates.googleblog.com/2025/09/learning-guide-notebook-lm-workspace-education.html (2025-09)
40. Nano Banana Pro ใน Workspace (รวม NotebookLM) — https://workspaceupdates.googleblog.com/2025/11/workspace-nano-banana-pro.html (2025-11)
41. นักเรียนสร้าง personal class notebooks ใน Classroom — https://workspaceupdates.googleblog.com/2026/04/students-can-now-create-personal-class-notebooks-with-NotebookLM-in-Google-Classroom.html (2026-04)
42. ขยายขีดจำกัดสำหรับ Education Plus / Teaching & Learning add-on — https://workspaceupdates.googleblog.com/2026/04/expanded-notebooklm-capabilities-for-Education-Plus-and-Teaching-and-Learning-add-on-customers.html (2026-04)
43. Audio Overviews: 80+ ภาษา (รวมภาษาไทย) + ข้อจำกัด — https://support.google.com/gemininotebook/answer/16212820?hl=en (n.d., ดูปัจจุบัน)
44. ภาษา Video Overviews (80 ภาษา) — https://support.google.com/notebooklm/answer/16454555?hl=en (n.d.)
45. Mind Maps — วิธีใช้ทางการ — https://support.google.com/gemininotebook/answer/16212283?hl=en (n.d.)

### ข่าวที่ใช้ยืนยันไทม์ไลน์ Gemini 3
46. CNBC: Nano Banana Pro ขับเคลื่อนด้วย Gemini 3 — https://www.cnbc.com/2025/11/20/google-nano-banana-pro-gemini-3.html (2025-11-20)
47. Google AI Developers Forum: ยังไม่มี public API — https://discuss.ai.google.dev/t/notebooklm-api/55950 (n.d.)