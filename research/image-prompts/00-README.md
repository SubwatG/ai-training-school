---
topic: "Image-Gen Prompt Research (Nano Banana/Gemini + ChatGPT Image) — master index"
date: 2026-08-23
model: ox-alpha-free
provider: opencode-go
sources_count: 132
---

# คลังวิจัย Prompt สร้างภาพจริง — Nano Banana & ChatGPT Image

> Research feed สำหรับ workshop อบรมครู 29 ส.ค. 2569 (Gemini · Canva · NotebookLM)
> ทุก prompt เป็นของจริงที่แชร์ในโพสต์สาธารณะ — quote verbatim + URL + วันที่ทุกรายการ (no fabrication)
> คอนเซปต์ที่ไม่ซ้ำกับ prompts-data.json (357 รายการ) — ดูรายการเดิมที่ `existing-concepts-dedupe.md`

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | เนื้อหา | Sources |
|---|---|---|
| `international-en.md` | 55 entries EN: OpenAI education newsletter official, ครูบล็อก, Reddit, ZDNET Images 2.0, JSON-prompt (TCEA) | 25 URL |
| `thailand-th.md` | 16 entries ไทย: MarketingOops, RMUTT ARIT คู่มือครู, Techsauce, Lemon8, Pantip, ไทยรัฐ + บริบทนโยบาย (สพฐ./สสวท.) | 22 URL |
| `github-official.md` | 18 repos (PicoTrex 23.5k★, YouMind 13.3k★ มี README ไทย, ZeroLu 10.3k★ หมวด Education) + 17 prompts + official guides ทั้งสองค่าย + free tools 9 รายการ | 35 URL |
| `use-case-workflows.md` | 13 end-to-end workflows: consistent character, infographic pipeline, comic explainer, flashcard deck, brand series (มีครูไทย 3 รายการ) | 14 URL |
| `chatgpt-image-updates.md` | Timeline GPT-4o→gpt-image-2 (9 milestones) + trends 2025–26 + copy-paste prompts 15+ + GPT Image 2.0 deep-dive | 36 URL |
| `_parent-crosscheck.md` | Base facts ที่ parent verify เอง (official guides, KMUTT-style spot checks) | — |

## ภูมิทัศน์โมเดล ณ ส.ค. 2026 (สำคัญที่สุดสำหรับ facilitator)

| ฝั่ง Google | ฝั่ง OpenAI |
|---|---|
| **Nano Banana** = Gemini 2.5 Flash Image (ส.ค. 2025) | **GPT-4o images** (มี.ค. 2025) — เก่าแล้ว |
| **Nano Banana Pro** = Gemini 3 Pro Image (20 พ.ย. 2025) — infographic/text เก่งสุดตอนนั้น, Search grounding | **GPT Image 1.5** (16 ธ.ค. 2025) — text แน่นขึ้น 4× เร็วขึ้น |
| **Nano Banana 2** = Gemini 3.1 Flash Image (~ต้นปี 2026) — photorealism + 4K, consistency 5 ตัวละคร | **ChatGPT Images 2.0 / gpt-image-2** (21 เม.ย. 2026) — ตัวปัจจุบัน: text ~99%, Thinking Mode, 2K, multilingual (OpenAI ใช้ป้ายไทยเป็น demo!) |

- เลือกเครื่องมือตามงาน: **ตัวหนังสือ/โปสเตอร์/infographic → GPT Image 2 หรือ Nano Banana Pro** · **ภาพสมจริง/ตัวละคร → Nano Banana 2**
- ภาษาไทย: NB Pro + Images 2.0 อ่านภาษาไทยในภาพได้ดีขึ้นมาก แต่ **ต้อง proofread ทุกครั้ง** (ยังพบสะกดผิด)

## Top 10 คอนเซปต์พร้อมใช้ (เรียงตามความเหมาะกับครู)

1. **Infographic จาก learning goal** — diorama poster (Alcock, เม.ย. 2026) / photosynthesis slide (OpenAI Edu newsletter, มิ.ย. 2026) → `international-en.md`
2. **สรุปบทเรียนเป็น Mind Map ไทย 1 นาที** (Lemon8 ธ.ค. 2025: โหนดกลาง 1 + 5 กิ่ง × 2) → `thailand-th.md` #7
3. **Flashcard 3D Chibi พิมพ์ A4** — คู่มือ RMUTT ARIT (Role–Task–Context–Format) → `thailand-th.md` #8
4. **ตัวละครเดิมทั้งชุด** — "Same character from previous image..." (Vofy/Christy Tucker) + ครูไทยใช้ทำนิทานปฐมวัย → `use-case-workflows.md` #3, #5, #10
5. **Step-by-step ภาพลำดับ** — handwashing tutorial, elaichi chai (Google official), manga motion breakdown (Images 2.0) → หลายไฟล์
6. **โปสเตอร์โฆษณา/ประชาสัมพันธ์ไทยไม่เพี้ยน** — น้ำปลาทิพรส (MarketingOops): Context + "ข้อความในคำพูด" + ฟอนต์ไทย → `thailand-th.md` #1
7. **Hand-drawn whiteboard → flowchart สวย** (ZeroLu McKinsey-style) — ครูถ่ายกระดานตัวเองแล้วให้ AI เรียบเรียง → `github-official.md` 2.4
8. **Coloring page จากรูปจริง** — "Make this image a coloring page" + bold outlines, no shading → `chatgpt-image-updates.md` E2
9. **Art Toy/ฟิกเกอร์ตัวเอง** (กระแสไทยใหญ่ 2568) — ใช้เป็นกิจกรรม "ตัวละครวรรณคดี/มาสคอตห้อง" → `thailand-th.md` #2–6
10. **JSON prompt คุมฉากครู+นักเรียน** (TCEA สอนครู) + reverse-engineer ภาพ→JSON → `international-en.md` §12

## Pattern เด่นข้ามแหล่ง (ใส่ cheat-sheet ได้เลย)

1. **Quote ข้อความเป๊ะใน ""** + negative line ("no watermark, no extra text") — ทุกคู่มือ official ย้ำ
2. **Anatomy ที่ Google แนะ**: Subject + Composition + Action + Location + Style (+ aspect ratio + lighting)
3. **"Name the Job Before the Style"** (GPT Image 2): บอก use case ก่อนสไตล์
4. **Consistency = ย้ำ descriptor ทุก prompt** + reference image เมื่อ drift
5. **Edit, don't re-roll** — แก้ทีละจุดแบบ conversational ดีกว่าเจนใหม่
6. **Template = prompt**: กำหนด layout เดียว (4:5 card / A4 sheet) แล้วเจนทั้งชุด

## ข้อควรระวังสำหรับ workshop

- ⚠️ สไตล์ "ศิลปินมีชีวิต" ถูกปฏิเสธ; ภาพคนจริง→การ์ตูน มีข้อจำกัดนโยบาย (Ghibli aftermath) — ใช้สไตล์ studio/generic ปลอดภัยกว่า [chatgpt-image-updates.md 2.1]
- ⚠️ ตรวจตัวสะกดไทย/ตัวเลข/สถิติในภาพเสมอ — ทั้ง Google ("Always verify factual accuracy") และผู้ทดสอบยืนยันว่ายังพลาดได้
- ⚠️ Facebook/TikTok/Lemon8 บางโพสต์ scrape ไม่ได้ทั้งหมด — entry ที่ quote จาก snippet มี flag "quote บางส่วน" ในไฟล์ (methodology ระบุท้ายไฟล์)
- ⚠️ Interactive features ฝั่ง paid: Thinking Mode/web search/multi-image (Plus+) — workshop ควรโชว์ของ free tier เป็นหลัก

## Method & limitations

- Fan-out 5 subagents (EN / TH / GitHub+official / workflows / ChatGPT timeline) + parent verification (web_extract ตรงบน URL สำคัญ: blog.google, cloud.google.com, inspirelearner, MarketingOops, openai.com gallery)
- วันที่ Lemon8/FB บางรายการ "ประมาณ" จาก post ID/snippet — flagged ใน entry
- PromptBase marketplace listing เป็นสินค้าขาย — เก็บเฉพาะคำอธิบายสาธารณะ
