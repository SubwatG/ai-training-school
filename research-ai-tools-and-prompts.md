---
topic: research-ai-tools-and-prompts
date: 2026-08-11
model: deepseek-v4-flash
provider: opencode-go
sources: verified-by-extraction + web-search
---

# Research: AI Tools + คอลเลกชัน Prompt (ตรวจสอบ 2026-08-11)

> ใช้ประกอบการออกแบบ 6 หัวข้ออบรม — ทุกข้อความอ้างอิงแหล่งที่ตรวจแล้ว

## 1. แก้ความเข้าใจเครื่องมือ (สำคัญ)

### Canva Code (AI Code Generator) — ไอเดียข้อ 1 ของผู้ถาม
- **เป็นฟีเจอร์ Premium (จ่ายเงิน)** — แหล่ง: canva.com/ai-code-generator + Reddit r/canva
- **สร้างอะไร:** เว็บไซต์/เกม/เครื่องมือ interactive (pricing calculator, countdown timer, เกม) — อธิบายแล้วได้เว็บ publish ได้ ไม่ต้องเขียนโค้ด, เก็บข้อมูลลง Canva Sheet
- **ข้อสรุป:** ไม่เหมาะเป็นเครื่องมือหลักของคอร์สฟรี และไม่ใช่เครื่องมือทำสื่อการสอนโดยตรง — เป็นไปได้ว่าใช้ทำ "เกม/แบบทดสอบ interactive" แต่ต้องจ่ายเงิน
- **สิ่งทดแทนฟรี:** Canva ฟรีมี AI จำกัด (Text to Image, Magic Write, Magic Design, Photo Editor) — ใช้ "สร้างภาพ + แก้ไข/ประกอบ" ได้ แต่เครดิตจำกัด ต้องตรวจสอบจำนวนเครดิตปัจจุบันก่อนวันอบรม

### Canva Education — ฟรีสำหรับครู K-12 (สำคัญ! ใช้ในหัวข้อ 1 + 4)
- **ฟรี 100% สำหรับครู K-12 (ประถม/มัธยม) ที่กำลังสอนจริง** — ใช้ได้ทั่วโลก ไม่จำกัดประเทศ — แหล่ง: canva.com/education/eligibility-guidelines (ตรวจ 2026-08-11)
- **พิสูจน์สิทธิ์ 2 วิธี:**
  1. อีเมลโดเมนการศึกษา (เช่น .edu / .ac.th / โดเมนโรงเรียน) → ได้สิทธิ์ทันที
  2. ยื่นเอกสาร: บัตรครู / ใบประกอบวิชาชีพ / บัตรพนักงานโรงเรียน → ตรวจภายใน 48 ชม.
- **ได้อะไร:** ฟีเจอร์ Pro ฟรี (Magic Write, Text to Image, เทมเพลตเต็ม) — สำคัญมากสำหรับหัวข้อ 4 (สร้างสื่อ)
- **ข้อจำกัด:**
  - ไม่ครอบคลุมครูมหาวิทยาลัย/อุดมศึกษา (วิทยากรเองไม่ eligible แต่ครูโรงเรียน eligible)
  - ต้อง re-verify ทุก 3 ปี
  - ครูที่ไม่ได้สอนอยู่ในตำแหน่งปัจจุบัน (เช่น เกษียณ/ย้ายออก) ไม่ eligible
- **⚠️ ตรวจสอบก่อนวันอบรม:** ครูในโรงเรียนใช้อีเมลโดเมนอะไร, แนะนำให้สมัครล่วงหน้า ~3 วัน (เผื่อ 48 ชม. ถ้ายื่นเอกสาร)

### Gemini Notebook (เดิมชื่อ NotebookLM — เปลี่ยนชื่อ กรกฎาคม 2026) — ไอเดียข้อ 2-3
- **สร้างสื่อจากเอกสารได้จริง** ผ่าน Studio panel (แหล่ง: notebooklm.google + digitalocean.com 2026-02-18 + blog.google):
  - **Audio Overview** — 4 รูปแบบ: Deep Dive / Brief / Critique / Debate; เลือกภาษาและความยาวได้
  - **Video Overview (ใหม่!)** — วิดีโออธิบายจากเอกสาร ใช้ Gemini 3 + Nano Banana Pro + Veo 3, เลือกสไตล์: whiteboard / kawaii / watercolor / classic (ใช้เวลาสร้างนาน)
  - **Slide Deck, Mind Map, Infographic, Data Table, Quiz, Flashcard, Report** (รวม Blog Post)
  - **Deep Research** — พิมพ์คำถาม → ค้นหาแหล่งจากเว็บ/Workspace → สร้างรายงานเป็นแหล่งใน notebook
- **ข้อจำกัดที่ต้องรู้:**
  - **ไม่ใช่ตัว generate ภาพเดี่ยว** (ภาพ standalone ใช้ Gemini app / Imagen หรือ Canva Text to Image)
  - ตอบจากเอกสารที่โหลดเข้า (grounded) = ลด hallucination แต่ไม่ใช่ศูนย์ — ต้องตรวจทานเสมอ
  - Audio เป็น AI สร้าง — อาจมีผิด/สะดุด (คำเตือนของ Google เอง)
  - **ตรวจสอบก่อนวันอบรม:** Video Overview / Slide อยู่ในฟรี tier หรือเป็น premium (ข้อมูลเปลี่ยนเร็ว)
- **Workflow ที่แนะนำ (จากไอเดียข้อ 2+3 ของผู้ถาม):** Gemini สร้างภาพ → Canva ฟรีแก้ไข/ประกอบ → Gemini Notebook สร้างเสียง/วิดีโอ/สไลด์จากเอกสาร

### Gemini (free) — ตัวหลัก
- สร้างภาพได้ (Imagen ใน Gemini app), อ่านภาพภาษาไทยได้ (ต้องทดสอบ), ภาษาไทยดี, ต่อ Workspace

## 2. คอลเลกชัน Prompt — ไทยและอังกฤษ

### ภาษาไทย (verified ผ่านการ extract 1 แหล่ง)
| แหล่ง | เนื้อหา | สถานะ |
|---|---|---|
| **ltic.kku.ac.th/10-prompt** (ศูนย์นวัตกรรมการเรียนการสอน มข.) | 10 prompt สร้างแบบทดสอบ: เลือกตอบ/จับคู่/เติมคำ/ไฟล์เสียง + โครงสร้าง 4 องค์ประกอบ (บทบาท/เป้าหมาย/เงื่อนไข/ขอบเขต) | ✅ ตรวจเนื้อหาจริง — คุณภาพดี ใช้สอนได้เลย |
| alisamaid.com/prompt-teacher | 16 prompt ครู-อาจารย์ (แผนการสอน ฯลฯ) | 🔍 เห็นในผลค้นหา ยังไม่ extract |
| boxmerz.com (5 ชุด prompt ใบงาน) | prompt ใบงานประถม ก๊อปวางได้ | 🔍 เห็นในผลค้นหา ยังไม่ extract |
| Facebook: "คู่มือการสร้างคุณค่าจาก AI สำหรับครูมัธยม" | คู่มือ + ตัวอย่าง prompt ครูไทย | 🔍 เห็นในผลค้นหา ยังไม่ extract |
| techintegration.ets.kmutt.ac.th (20 prompts วิชาการ) | ผู้ช่วยงานวิชาการ | ⚠️ หน้าเว็บเป็นฟอร์มลงทะเบียน — เนื้อหาไม่โหลด ใช้ไม่ได้ |

### ภาษาอังกฤษ (verified ผ่านผลค้นหา)
| แหล่ง | เนื้อหา |
|---|---|
| mentimeter.com/blog/education/ai-prompts-for-teachers | 56 prompt สำหรับครู 2026 (lesson planning, materials, ฯลฯ) |
| teachingchannel.com (65 AI Prompts for Lesson Planning) | 65 prompt: สร้างแผน/สื่อ/แบบประเมิน/rubric/differentiation |
| structural-learning.com (10 AI Prompts Every Teacher Should Master) | 10 prompt: planning, differentiation, feedback, SEND, parent comms |
| exeedcollege.com (Game-changing AI Prompts Ideas for Teachers) | prompt ไอเดียครู 2026 |

> **ข้อเสนอ:** นำโครงสร้าง KKU (4 องค์ประกอบ) + คัด prompt ที่ใช้ได้จริงจากชุดเหล่านี้ มาปรับเป็นภาษาไทยใน cheat-sheet ฉบับผู้เข้าอบรม (ของเดิมใน prompt-cheatsheet-thai.md ครอบคลุมแล้วบางส่วน)

## 3. ข้อควรระวังในการใช้ research นี้
- ฟรี tier / ฟีเจอร์ของ Canva และ Gemini Notebook เปลี่ยนเร็ว — **ต้อง re-verify ในสัปดาห์ก่อนวันอบรม** (อยู่ใน checklist-pre-day.md แล้ว)
- หน้าเว็บไทยบางแห่งเป็นฟอร์ม/โซเชียล (KMUTT, Facebook) — เนื้อหาอาจเข้าถึงยาก อย่าพึ่งเป็นแหล่งหลัก
