# Research Brief: หา Prompt สร้างภาพจริง (Nano Banana / Gemini Image + ChatGPT Image) สำหรับครู

## Mission
ค้นหา **prompt สร้างภาพที่ผู้ใช้งานจริงแชร์กันบนอินเทอร์เน็ต** (ไม่ใช่ prompt ที่เดาขึ้นมาเอง) โดยเน้น:
1. **Nano Banana** = โมเดลภาพของ Google (Gemini 2.5 Flash Image → Gemini 3 Pro Image) ใช้ใน Gemini app
2. **ChatGPT Image** = การสร้างภาพใน ChatGPT (GPT-4o image generation / GPT Image)

**ธีม use case ที่ต้องเก็บ (เน้นเหล่านี้):**
- 🎓 การศึกษา (education: สื่อการสอน, ภาพประกอบบทเรียน, infographic, flashcard, โปสเตอร์ห้องเรียน)
- 📣 การสื่อสาร/ประชาสัมพันธ์ (announcement, newsletter, social media post, โปสเตอร์ประกาศ)
- 🚀 การโปรโมท (promotion, event poster, marketing-style)
- 📝 การสรุป (summary visual, one-pager, cheat sheet)
- 🔢 การแสดงขั้นตอน (step-by-step process diagram, how-to sequence, flowchart ภาพ)
- ✨ อื่นๆ ที่หลากหลายและน่าสนใจ

## Hard Rules
1. **No fabrication.** ทุก prompt ที่เก็บต้องมาจากแหล่งจริงที่เปิดดูได้ ถ้าเข้าไม่ได้ให้บอกและใช้แหล่ง alternative
2. **Every claim needs a source URL** — ทุก prompt ต้องมีลิงก์กลับไปยังโพสต์/เว็บต้นทาง + วันที่โพสต์ (ถ้ามี)
3. Quote prompt เดิม **ตามตัวอักษร** (ภาษาเดิม) — ถ้าเป็นอังกฤษให้แนบคำแปลไทยสั้นๆ ถ้าเป็นไทยให้แนบ EN gloss สั้นๆ
4. ระบุ context สั้นๆ ว่า "ใครใช้ทำอะไร ผลเป็นอย่างไร" จากโพสต์ต้นทาง
5. Do NOT store secrets.
6. ห้าม duplicate คอนเซปต์ที่มีอยู่ใน `existing-concepts-dedupe.md` (อ่านก่อนเริ่ม)
7. เขียนไฟล์ output แบบ **incremental**: เขียน skeleton + header ก่อน แล้ว append ทีละ section (อย่า write ครั้งเดียวยาวมาก)

## Output Format (per prompt entry)
```markdown
### [ชื่อคอนเซปต์] — [หมวด: education/promotion/summary/steps/other]
- **แหล่ง:** URL (+วันที่โพสต์, platform)
- **บริบท:** ใครใช้ ทำอะไร ได้ผลอย่างไร (1-2 ประโยค)
- **Prompt (EN):** "..." *(แปลไทยสั้น)* หรือ **Prompt (TH):** "..." *(EN gloss)*
- **Tool:** Nano Banana (Gemini) / ChatGPT Image / ทั้งคู่
```

## Search Entry Points
- web_search: `nano banana prompt` + ธีม (education/teacher/infographic/infographic), `ChatGPT image prompt viral`, `site:reddit.com nano banana prompt`, `nano banana โปรโมต สร้างภาพ ครู อบรม`
- Reddit: r/notebooklm, r/GeminiAI, r/ChatGPT, r/Teachers, r/Professors, r/PromptEngineering
- Thai: Pantip, Facebook groups (ครู), insKru, MarketingOops, Techsauce, blog .ac.th
- GitHub: awesome-nano-banana, prompt collections
- X/Twitter threads (via web_search indexed content only)
