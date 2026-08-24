---
topic: extra-sources-report
date: 2026-08-22
model: deepseek-v4-flash
provider: opencode-go
platform: subagent (AI training school research)
extraction-date: 2026-08-22 (13:14 +07)
status: verified-by-extraction (web_extract ทุกแหล่ง)
---

# รายงานวิจัยเพิ่มเติม: คอลเลกชัน Prompt สำหรับครู (แหล่งที่ยังไม่ extract)

> ต่อยอดจาก `research-ai-tools-and-prompts.md` (2026-08-11) — คราวนี้ **extract จริงทุกแหล่ง** ทั้ง 5 แหล่งที่เคยระบุสถานะ "🔍 ยังไม่ extract" + โบนัสคลัง prompt เพิ่ม 1 แหล่ง
> รวม prompt ที่สกัดได้: **278 รายการ** (ไทย 147 + อังกฤษ 131) — ใช้เติมช่องว่างใน `site/prompts-data.json` (262 prompts) ตาม gap analysis ของโปรเจกต์

## สรุปภาพรวม

| แหล่ง | ภาษา | จำนวน prompt | ประเภทงาน | สถานะคุณภาพ |
|---|---|---|---|---|
| alisamaid.com/prompt-teacher | 🇹🇭 | 16 | แผนการสอน ข้อสอบ กิจกรรม เกม ทัศนศึกษา | ✅ ใช้ได้จริง เป็นภาษาไทย แต่นามธรรม (กรอกตัวแปร `[ ]` เอง) |
| boxmerz.com/blog/best-ai-prompts-for-worksheets-elementary | 🇹🇭 | 5 ชุด (หลัก) + 25 ไอเดียย่อย | ใบงาน 5 วิชา (ไทย/วิทย์/คณิต/อังกฤษ/สังคม) | ✅ ดีมาก — มีตัวแปร + ตัวอย่างผลลัพธ์ + ตารางทดสอบโมเดล |
| boxmerz.com/prompts (โบนัส) | 🇹🇭 | 126 | ข้อสอบ/ใบงาน อนุบาล-ม.6 ครบ 8 กลุ่มสาระ | ✅ เยอะสุด เจาะหลักสูตรไทย ตรงรหัสตัวชี้วัด |
| mentimeter.com/blog/education/ai-prompts-for-teachers | 🇬🇧 | 56 | 8 หมวด: แผน/สื่อ/engaging/differentiation/ประเมิน/feedback/จัดการชั้นเรียน/สื่อสาร | ✅ ครอบคลุมงานครูทุกด้าน แต่อังกฤษล้วน |
| teachingchannel.com (PDF 65 prompts) | 🇬🇧 | 65 | แผน/สื่อ/ข้อสอบ/differentiation/rubric/feedback | ✅ ละเอียด มีตัวอย่างเฉพาะเจาะจง + เตือนห้ามใส่ข้อมูลนักเรียน |
| structural-learning.com/post/10-ai-prompts-every-teacher-should-master | 🇬🇧 | 10 | 10 ภารกิจหลักครู (ต่างระดับ บทเรียน retrieval feedback SEND สื่อสารผู้ปกครอง ฯลฯ) | ✅ คุณภาพสูงสุด มีกรอบ 4 องค์ประกอบ (Role/Task/Context/Format) + งานวิจัยรองรับ |

> **หมายเหตุ:** Facebook "คู่มือ AI ครูมัธยม" ยังไม่ได้ extract (ต้องล็อกอิน) — ไม่นับในรายงานนี้

---

## 1. alisamaid.com/prompt-teacher (16 prompts — ไทย)

**URL:** https://alisamaid.com/prompt-teacher/ · **สกัดเมื่อ:** 2026-08-22

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 6 จาก 16)

1. "ช่วยเขียนแผนการสอนวิชาวิทยาศาสตร์ของนักเรียนชั้น [มัธยมศึกษาปีที่ 1] ในเรื่อง [สารและการจำแนกสาร]"
2. "ช่วยเขียนวิธีประเมินผลการเรียนของนักเรียนชั้น [มัธยมศึกษาปีที่ 2] [วิชาภาษาไทย] ในเรื่อง [การพัฒนาทักษะการพูด]"
3. "ช่วยเขียนจุดประสงค์การเรียนรู้ ด้านความรู้ ทักษะ และคุณลักษณะของเนื้อหาด้าน [ประวัติศาสตร์ของสมัยสุโขทัย] ของนักเรียน [มัธยมศึกษาปีที่ 1]"
4. "ช่วยเขียนแผนการสอนในรูปแบบ Active Learning สำหรับวิชา[วิทยาศาสตร์] ของนักเรียนชั้น[มัธยมปีที่ 6]"
5. "ออกแบบข้อสอบปรนัย [20] ข้อ สำหรับ วิชา [สังคมศึกษา] เรื่อง [พระพุทธ]ของนักเรียน[ประถมศึกษาปีที่ 6] พร้อมเฉลย"
6. "ออกแบบเกมสำหรับส่งเสริมการเรียนรู้ในวิชา[ภาษาอังกฤษ] เรื่อง [Present Simple Tense]ของนักเรียน[มัธยมศึกษาปีที่ 2]"

หมวดอื่นๆ: แบบสอบถามความพึงพอใจนักเรียน, ข้อสอบอัตนัย, ข้อสอบกลางภาค, ข้อสอบจับคู่/เติมคำ, โต้วาที, กรณีศึกษา, ทัศนศึกษา

### แนวคิดที่นำมาปรับใช้ได้
- **จุดประสงค์การเรียนรู้ครบ 3 ด้าน** (ความรู้/ทักษะ/คุณลักษณะ) — ตรงกับหัวข้ออบรม "งานสอน" ของเรา
- การออกแบบข้อสอบหลาก format (ปรนัย/อัตนัย/จับคู่/เติมคำ/กลางภาค) — ใช้เป็นแม่แบบใน workshop ข้อสอบ
- กิจกรรมนอกห้องเรียน (ทัศนศึกษา) + เกม + โต้วาที — กลุ่ม "กิจกรรม/engagement" ที่ในคลังเรายังน้อย

### ข้อเสนอแนะการปรับเป็น RCC (บทบาท-บริบท-เงื่อนไข)
Prompt เดิมสั้นไป (ขาดบทบาทและเงื่อนไข) — ขยายเป็นสูตร RCC 3 ส่วน เช่น:

```text
[บทบาท] คุณเป็นครูวิทยาศาสตร์ ม.1 ที่เชี่ยวชาญการออกแบบตามแนว Active Learning
[บริบท] ห้องเรียนมี 40 คน เก่งปานกลาง เวลา 50 นาที ตรงตามหลักสูตรแกนกลาง
[เงื่อนไข] ออกแบบแผนการสอน เรื่อง สารและการจำแนกสาร ให้ครบ: จุดประสงค์, กิจกรรมขั้นนำ/สอน/สรุป, สื่อ, การวัดผล
ใช้ภาษาไทยที่นักเรียนเข้าใจ พร้อมระบุเวลากิจกรรมเป็นนาที
```

---

## 2. boxmerz.com — ใบงาน 5 วิชา (5 ชุดหลัก + ไอเดียย่อย) — ไทย

**URL:** https://boxmerz.com/blog/best-ai-prompts-for-worksheets-elementary · **สกัดเมื่อ:** 2026-08-22

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 3 ใน 5)

**ชุด 1 — การอ่านจับใจความ (ภาษาไทย):**
> "ช่วยสร้างเนื้อหาสำหรับใบงานการอ่านจับใจความ สำหรับนักเรียนชั้น [ป.3] เรื่อง [ความสำคัญของวันสงกรานต์] โดยให้มีเนื้อเรื่องสั้นๆ ประมาณ [10-15 บรรทัด] ใช้ภาษาที่เข้าใจง่าย เหมาะกับวัย และสร้างคำถามปรนัย 4 ตัวเลือก จำนวน [5 ข้อ] พร้อมเฉลยท้ายบทความ โดยคำถามต้องครอบคลุมทั้งการจับใจความสำคัญ รายละเอียด และการอนุมาน"

**ชุด 3 — คณิตศาสตร์ (โจทย์ปัญหา):**
> "สร้างโจทย์ปัญหาคณิตศาสตร์ เรื่อง [การบวกลบเศษส่วน] จำนวน [8 ข้อ] สำหรับนักเรียนชั้น [ป.5] โดยใช้สถานการณ์จาก [ตลาดและร้านค้า] (เช่น ซื้อขนม แบ่งวัตถุดิบทำอาหาร) แบ่งเป็น 3 ระดับ: ง่าย 3 ข้อ / กลาง 3 ข้อ / ท้าทาย 2 ข้อ พร้อมแสดงวิธีทำทีละขั้น และเฉลยคำตอบทุกข้อ"

**ชุด 4 — อังกฤษ (Vocabulary):**
> "Create an English worksheet for Grade [4] about [Animals in the Zoo]. Include 5 matching vocabulary items (English to Thai), 5 fill-in-the-blank sentences, and 1 creative drawing task description."

(อีก 2 ชุด: วิทย์ "วัฏจักรของน้ำ" 3 ส่วน คำอธิบาย+เติมคำ+คำถามชวนคิด / สังคม "สรุปบทเรียน + ใบงาน Mind Map + คำถามเขียนตอบ 3 ข้อ")

### จุดเด่นพิเศษของแหล่งนี้ (ไม่ค่อยมีที่ไหน)
- **ให้ "ตัวแปรที่ต้องเตรียม"** + **ไอเดีย prompt 5 แบบต่อชุด** (เช่น นิทานพื้นบ้าน, วรรณคดี, สุภาษิต, สารคดี, ร้อยกรอง) — ใช้เป็นใบงาน "ดัดแปลงได้ทันที" ในอบรม
- **มีตัวอย่างผลลัพธ์จริง** (เนื้อเรื่อง + ข้อสอบ + เฉลย) ให้ครูเห็นภาพก่อนก๊อป
- **ตารางทดสอบโมเดล** (Gemini/ChatGPT/Claude) — แนะนำ Claude สำหรับงานวิทยาศาสตร์ ฯลฯ
- **สูตรจำ TBFT:** "ใคร (Target) + ทำอะไร + ระดับไหน + รูปแบบใด (Format)" + Tone — เทียบเท่า RCC ของเรา

### ข้อเสนอแนะการปรับเป็น RCC
จุดแข็ง: prompt เหล่านี้มี **บริบท** (ชั้น/หัวข้อ/จำนวนข้อ) และ **เงื่อนไข** (พร้อมเฉลย/ระดับยากง่าย) ค่อนข้างครบ แค่เติม **บทบาท** นำหน้าและ**เงื่อนไขเรื่อง PDPA** เช่น:

```text
[บทบาท] คุณเป็นครูประถมศึกษาผู้เชี่ยวชาญด้านการวัดผล
[บริบท] สร้างใบงานการอ่านจับใจความ ชั้น ป.3 เรื่อง ความสำคัญของวันสงกรานต์
เนื้อเรื่องสั้น 10-15 บรรทัด ภาษาวัยเด็ก คำถามปรนัย 4 ตัวเลือก 5 ข้อ พร้อมเฉลย
[เงื่อนไข] คำถามครอบคลุมจับใจความ/รายละเอียด/การอนุมาน ห้ามใช้ข้อมูลบุคคลจริง
สร้างเป็นตาราง 2 คอลัมน์ (คำถาม/คำตอบ) พิมพ์ A4 ได้ทันที
```

---

## 3. boxmerz.com/prompts — คลัง 126 prompt (โบนัส — ไทย) ⭐

**URL:** https://boxmerz.com/prompts · **สกัดเมื่อ:** 2026-08-22
**เนื้อหา:** 126 prompt ข้อสอบ/ใบงาน เรียนตามระดับชั้น (อนุบาล/ประถม/มัธยม) × วิชา (คณิตศาสตร์ ภาษาไทย อังกฤษ สังคม วิทยาศาสตร์ ชีววิทยา ฟิสิกส์ เคมี สุขศึกษา การงานอาชีพ ศิลปะ วิทยาการคำนวณ ประวัติศาสตร์ เทคโนโลยี)

### โครงสร้าง prompt มาตรฐานของคลังนี้ (ซ้ำกันทุกข้อ — ดีมากสำหรับสอนตามแม่แบบ)
```text
ช่วยสร้างข้อสอบแบบ [type] จำนวน [count] ข้อ สำหรับนักเรียนระดับชั้น [level] ปีที่ [grade]
ตรงตามรหัสตัวชี้วัด [standard_code] เรื่อง [หัวข้อ] ...
สรุปเฉลยและคำอธิบายละเอียดไว้ท้ายสุด
```

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 6 จาก 126)
1. **คณิตศาสตร์ ประถม:** "ช่วยสร้างข้อสอบแบบ [type] จำนวน [count] ข้อ ... เรื่องการบวกและลบเลขไม่เกิน 100 เน้นโจทย์ปัญหาในชีวิตประจำวัน (เช่น การซื้อของ, การนับเงิน, การแบ่งของ) ใช้ภาษาเข้าใจง่าย ตัวเลขต้องคำนวณลงตัว ไม่มีทศนิยม และสถานการณ์สมเหตุสมผล"
2. **ภาษาไทย ประถม:** "...หัวข้อ 'การใช้ภาษาเพื่อการสื่อสารและเรียงความ' เน้นเรื่องการเลือกใช้คำเชื่อมที่ถูกต้อง, การเรียงลำดับประโยคให้เป็นเรื่องราวที่สมบูรณ์, และหลักการเขียนบรรยายโวหารเกี่ยวกับหัวข้อ 'เพื่อนที่ดีที่สุด'"
3. **ชีววิทยา มัธยม:** "...เรื่อง 'วงจรชีวิตของพืชดอก' (Angiosperm Life Cycle) เน้นถามหน้าที่ของส่วนประกอบต่างๆ (เช่น เกสร, รังไข่, ไซโกต) และกระบวนการปฏิสนธิซ้อน (Double Fertilization)"
4. **อนุบาล ภาษาไทย:** "...เพื่อทดสอบความจำพยัญชนะไทย เน้นการเชื่อมโยงรูปภาพกับพยัญชนะ เช่น 'ข้อใดคือตัว ก.ไก่' ... พร้อมระบุ Image Prompt สำหรับสร้างรูปภาพประกอบโจทย์"
5. **อังกฤษ Cloze Test:** "...โจทย์และตัวเลือกต้องเป็นภาษาอังกฤษเท่านั้น ห้ามแปลโจทย์เป็นไทย ส่วนคำอธิบายเฉลยต้องเป็นภาษาไทยเพื่อให้ผู้เรียนเข้าใจ"
6. **การงานอาชีพ/ศิลปะ (เติม gap กลุ่มสาระที่คลังเราน้อย):** "งานบ้านและอุปกรณ์", "การประดิษฐ์ของเล่น", "ทฤษฎีสี (วงจรสี)", "ทัศนียภาพ (Perspective)", "การออกแบบกราฟิก"

### แนวคิดที่นำมาปรับใช้ได้
- **ตรงรหัสตัวชี้วัดหลักสูตรแกนกลาง** — จุดขายที่ครูไทยต้องการมากที่สุด (อ้าง `[standard_code]`)
- **เงื่อนไข "ตัวเลขคำนวณลงตัว/ไม่มีทศนิยม"** และ "ห้ามแปลโจทย์เป็นไทย (วิชาอังกฤษ)" — ตัวอย่างเงื่อนไขชั้นดีให้ครูเห็นว่าคุม AI ได้แค่ไหน
- **Image Prompt ในข้อสอบอนุบาล** — สอนเชื่อม Gemini สร้างภาพ → ใส่ข้อสอบ (หัวข้อ 4 ของอบรม)
- **ครอบคลุมกลุ่มสาระที่ gap:** การงานอาชีพ (3), ศิลปะ (9), สุขศึกษา (3), วิทยาการคำนวณ (2), เทคโนโลยี/รู้เท่าทันสื่อ (1)
- ข้อสอบ "รู้เท่าทันสื่อดิจิทัล (Fake News)" — ต่อยอดหัวข้อ 6 (เท่าทัน AI/PDPA)

### ข้อเสนอแนะการปรับเป็น RCC
โครงสร้างเดิมมีบริบท+เงื่อนไขครบแล้ว แต่เป็น "ข้อสอบอย่างเดียว" — เพิ่มบทบาทและงานอื่น (ใบความรู้/ใบงาน/แผน) โดยใช้แม่แบบเดียวกัน:

```text
[บทบาท] คุณเป็นครูผู้เชี่ยวชาญการออกแบบข้อสอบตามหลักสูตรแกนกลางไทย
[บริบท] สร้างข้อสอบปรนัย 20 ข้อ ชั้น ม.1 วิชาวิทยาศาสตร์ เรื่อง วงจรชีวิตของพืชดอก
ตรงตามรหัสตัวชี้วัด ว 1.1 ม.1/2 เน้นหน้าที่ของส่วนประกอบและกระบวนการปฏิสนธิซ้อน
[เงื่อนไข] โจทย์ไม่กำกวม ตัวเลือกเรียงแบบสุ่ม ไม่ซ้ำกัน ทุกข้อมีเฉลยพร้อมคำอธิบายสั้นๆ
ภาษาไทยเป็นทางการระดับข้อสอบจริง พิมพ์ได้ทันที (ไม่ต้องมีข้อมูลนักเรียน)
```

---

## 4. Mentimeter — 56 prompts (อังกฤษ, 8 หมวด)

**URL:** https://www.mentimeter.com/blog/education/ai-prompts-for-teachers · **สกัดเมื่อ:** 2026-08-22 · **เผยแพร่:** 2025-12-16 (ผู้เขียน Oscar Svernlöv)

### หมวด 8 กลุ่ม
Lesson planning (1-7) · Educational materials (8-12) · Student engagement (13-20) · Differentiated instruction (21-25) · Assessment (26-32) · Feedback and grading (33-39) · Classroom management (40-46) · Communication (47-56)

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 10 จาก 56)
1. **#1 แผน:** "Think like a [grade or university level] teacher and design a lesson plan to teach students about [topic]. Include at least [number] ideas and focus on [specific topics]. Include the ideal schedule to roll out the lesson plan."
2. **#3 คำสั่งงาน:** "Write detailed instructions for an assignment on [topic] for [grade or university level] students. Include the requirements, the exact steps to follow to complete the assignment, and any specific formatting or length expectations."
3. **#5 โจทย์คณิต:** "Generate practice math problems for [grade or university level] students, focusing on [math concept/lesson]. Provide problems with varying difficulty levels and include an answer key."
4. **#13 icebreaker:** "Provide unique icebreaker activities to help a class of [grade or university level] students with a class size of [size] share about themselves and get to know each other."
5. **#18 ทัศนศึกษาเสมือน:** "Plan a virtual field trip to help [grade or university level] students learn about [topic]. Share links to resources, activities, and reflection questions."
6. **#22 แผนการเรียนรู้รายบุคคล:** "Design a personalized learning plan for a [grade or university level] student with [specific needs] student studying [topic]. Include specific strategies, resources, and support to enhance progress."
7. **#26 ควิซตรงจุดประสงค์:** "Create a quiz for [grade or university level] students on [topic] that aligns with [learning objectives]. Include multiple-choice, true or false, and short-answer questions."
8. **#27 rubric:** "Develop a rubric to grade a [grade or university level] assignment on [topic]. Include details of each section's criteria, weight, and performance level."
9. **#43 จัดการชั้นเรียน:** "Generate a seating chart for a classroom of [#] [grade or university level] students. Ensure accessibility, teacher visibility, and student collaboration."
10. **#50 ประชุมผู้ปกครอง:** "Create an agenda for [grade level] parent-teacher conferences, allowing 30 minutes of discussion time. Include topics like [insert topics]."

(หมวดอื่นๆ ที่น่าสนใจ: #33 feedback รายบุคคล, #45 ระบบรางวัล, #47 ตอบคำถามผู้ปกครอง, #48 progress report, #56 agenda ประชุมกรรมการ)

### แนวคิดที่นำมาปรับใช้ได้
- **8 หมวดครอบคลุมบทบาทครูทั้งหมด** — แผนผัง "ครู = manager + instructional designer + writer + coach" ใช้เปิดหัวข้ออบรมได้ดี
- หมวด **Classroom management (40-46)** และ **Communication (47-56)** — เติม gap งานธุรการ/สื่อสารของเราที่มีน้อย (ปพ 5, เยี่ยมบ้าน 1): progress report, จดหมายผู้ปกครอง, agenda ประชุม
- **Personalized learning plan + tiered activities (21-23)** — กลุ่ม differentiation ที่คลังเรายังเบา
- **แนวคิด "Follow-up prompt"** — สอนครูว่า prompt เดียวไม่พอ ต้องถามต่อ (iteration) — สอดคล้อง Protocol ตรวจทานของเรา
- คำแนะนำท้ายบท: "Try role-based prompts", "review outputs" — ตรงกับ RCC + ตรวจทาน 3 ขั้น

### ข้อเสนอแนะการปรับเป็น RCC (ตัวอย่าง 1 prompt)
**ต้นฉบับ #26:** "Create a quiz ... that aligns with [learning objectives]. Include multiple-choice, true or false, and short-answer questions."
→ **RCC ไทย:**
```text
[บทบาท] คุณเป็นครูที่เชี่ยวชาญการสร้างข้อสอบวัดตามจุดประสงค์การเรียนรู้
[บริบท] สร้างแบบทดสอบเรื่อง [หัวข้อ] ชั้น [ระดับ] ให้ตรงจุดประสงค์ที่กำหนด:
[วางจุดประสงค์]
[เงื่อนไข] มี 3 ส่วน: ปรนัย / ถูก-ผิด / เขียนตอบสั้น พร้อมเฉลยทุกข้อ
ทุกข้อระบุว่าวัดจุดประสงค์ข้อใด ภาษาไทย ใช้ในห้องจริงได้
```

---

## 5. Teaching Channel — 65 prompts (อังกฤษ, PDF ทางการ)

**URL:** https://www.teachingchannel.com/k12-hub/blog/65-ai-prompts-for-lesson-planning/ (PDF: https://www.teachingchannel.com/wp-content/uploads/2024/05/K12Hub-65-AI-Prompts-for-Lesson-Planning.pdf) · **สกัดเมื่อ:** 2026-08-22

### หมวด 6 กลุ่ม
Create Lesson Plans · Design Materials · Build Assessments · Differentiate Instruction Ideas · Develop Rubrics · Provide Feedback and Grading

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 10 จาก 65)
1. **แผนหน่วย 5 วัน:** "Develop a 5 day unit plan outline for teaching students about ancient civilizations including Aztec, Roman, Greek, Chinese and Mayan."
2. **บทนำน่าสนใจ:** "Give me 5 fun ways to introduce a lesson on surface tension as a property of water."
3. **อธิบายตามวัย:** "Explain a lunar eclipse for an 8 year old."
4. **บทอ่านแยกตามระดับ:** "Give me 3 differentiated reading passages about the American Civil War for a 6th grade social studies class, with options for struggling readers, grade-level readers, and advanced readers."
5. **Flashcard:** "Give me 10 flashcards for key vocabulary in [insert book title or concept]. Include definitions, synonyms, example/nonexamples and sentences suitable for [grade level]."
6. **ข้อสอบ Bloom's:** "Design an innovative assessment on [topic] that covers the following objectives/standards [insert objectives/standards]. Provide questions at each level of Bloom's Taxonomy and include 2 scenario-based questions. Give me some key 'look fors' for each response."
7. **Exit ticket:** "Create 5 exit ticket ideas I can use in my 4th grade math class after a geometry lesson on identifying, labeling, and measuring angles. Keep the exit ticket activities/questions very brief."
8. **Misconception:** "Identify 5 common misconceptions that 7th-grade students may have about the process of photosynthesis, including inaccurate ideas about the roles of sunlight, water, and carbon dioxide."
9. **Rubric งานกลุ่ม:** "Generate a rubric for a 12th grade English group project on a Shakespeare play, evaluating the effectiveness of collaboration, individual contribution of each member, and overall quality of the final product."
10. **Feedback:** "Provide specific feedback for a 5th grade student's science essay on climate change, focusing on clarity, accuracy, and use of evidence."

### จุดเด่น/แนวคิดที่นำมาปรับใช้ได้
- **มีคำเตือน PDPA ชัดเจน:** "*Remember to never include any personally identifiable student information in your prompts to protect student privacy*" — นำไปใส่ในใบงานอบรมของเรา (หัวข้อ 6)
- **101: แนวคิด "explain ... for an 8 year old"** = อธิบายให้เด็กเข้าใจ — สอนครูเรื่องระดับภาษา/วัย
- **Tiered assignment / choice board / 3 ระดับบทอ่าน** — เทคนิค differentiation เต็มรูปแบบ
- **ข้อสอบ Bloom's Taxonomy + scenario-based** — ยกระดับข้อสอบของเรา (สร้างข้อสอบ 18 → เพิ่มมิติ Bloom's)
- **Misconception mapping** — ไอเดียหา "ความเข้าใจคลาดเคลื่อน" ที่ครูไทยยังไม่ค่อยใช้
- แยกหมวด Rubrics 7 ชนิด (เรียงความ/presentation/lab/กลุ่ม/รายงาน/โต้วาที/ศิลปะ/คณิต) — ครบทุกบริบท

### ข้อเสนอแนะการปรับเป็น RCC (ตัวอย่าง 1 prompt)
**ต้นฉบับ:** "Explain a lunar eclipse for an 8 year old."
→ **RCC ไทย (อธิบายตามวัย):**
```text
[บทบาท] คุณเป็นครูวิทยาศาสตร์ที่อธิบายเรื่องยากให้เด็กเข้าใจง่าย
[บริบท] นักเรียนชั้น ป.3 (8 ขวบ) ยังไม่เรียนเรื่องแสงและเงา
[เงื่อนไข] อธิบาย "จันทรุปราคา" ด้วยคำศัพท์เด็ก ใช้ตัวอย่างใกล้ตัว
ไม่เกิน 6 ประโยค มีคำถามเช็คความเข้าใจ 1 ข้อ พร้อมเฉลย
```

---

## 6. Structural Learning — 10 prompts (อังกฤษ, คุณภาพสูงสุด)

**URL:** https://www.structural-learning.com/post/10-ai-prompts-every-teacher-should-master · **สกัดเมื่อ:** 2026-08-22 · **เผยแพร่:** 2025-11-18, อัปเดต 2026-08-14 (ผู้เขียน Paul Main)

### เหตุผลที่แหล่งนี้สำคัญที่สุด
- เสนอ **กรอบ 4 องค์ประกอบ**: Role / Task / Context / Format — ตรงกับสูตร **RCC** ของเรา (บทบาท-บริบท-เงื่อนไข) โดยเพิ่ม Task + Format
- ทุก prompt มี **"The Problem"** (ปัญหาจริงของครู) + "Why It Works" (อ้างงานวิจัย: Hattie & Timperley 2007, Black & Wiliam 1998, Dunlosky et al. 2013, Woo et al. 2024) + "Time Saved" — ใช้ประกอบการอบรมได้เลย

### ตัวอย่าง prompt ดั้งเดิม (คัดมา 6 จาก 10)

**1) บทอ่าน 3 ระดับ (Differentiation):**
> "You are a primary teacher in England. Take this text about [TOPIC] and rewrite it at three reading levels: 1. Emerging (Year 3-4 reading age): Simple sentences, high-frequency vocabulary, one concept per sentence ... 3. Greater depth (Year 7-8 reading age): Complex sentences, subject-specific terminology, inference required. Maintain the same key facts in all versions. Length: 150-200 words per version."

**2) Retrieval practice 10 ข้อ:**
> "You are a [SUBJECT] teacher for Year [X] in England. Generate 10 retrieval practice questions based on this topic: [TOPIC]. Requirements: Questions 1-3: Recall of basic facts (What? When? Who?) ... Questions 8-10: Links to prior units we studied: [LIST PREVIOUS TOPICS] ... Avoid multiple choice. Focus on short written responses."

**3) Feedback 3-4 ประโยค:**
> "You are an educator in [subject] marking Year [X] work. A learner has written this [TYPE OF WORK]: [PASTE LEARNER WORK]. Their current target: [SPECIFIC TARGET]. Provide feedback using this structure: 1. One specific success (reference exact words or techniques they used) 2. One clear next step linked to their target ... Tone: Encouraging but honest. Length: 3-4 sentences maximum. Avoid general praise like 'good work'."

**4) สนับสนุนเด็กพิเศษ/ภาษาที่ 2 (SEND/EAL):**
> "You are a teacher in England with learners who have [SPECIFIC NEEDS: e.g., dyslexia, limited English proficiency, working memory difficulties]. Original classroom task: [DESCRIBE TASK]. Create 3 modified versions: 1. Visual scaffold ... 2. Language scaffold: Simplified instructions, sentence stems, word banks 3. Cognitive scaffold: Break task into smaller steps ... Each version should achieve the same learning objective but make success more accessible."

**5) สื่อสารผู้ปกครอง:**
> "You are a Year [X] teacher in England. Draft a brief email (150-200 words) to a parent about: [SITUATION]. Learner context: [RELEVANT DETAILS]. Tone: Professional, solution-focussed, partnership-oriented. Structure: Acknowledge the situation directly ... Explain what you're doing in school ... Suggest one clear action for home support ... End with an invitation for dialogue. Avoid educational jargon."

**6) สะท้อนผลงานครู (PLC/PA):**
> "You are an experienced teacher mentor. Generate 5 reflection questions for a teacher who has just completed a half-term focusing on [SPECIFIC GOAL ...]. Requirements: Questions should prompt specific examples from lessons ... Include one question about what learners' responses revealed ... Include one question that asks 'What would you do differently next time?' ... Avoid vague questions like 'How did it go?'"

(อีก 4 ข้อ: แผน 50 นาที + Thinking Framework, คำถามอภิปรายเชิงลึก, Success criteria "I can" statements, Rubric 4 ระดับ Emerging/Developing/Secure/Mastery)

### แนวคิดที่นำมาปรับใช้ได้ — ตรง gap analysis ของเราเป๊ะ
- **Feedback ตามโครงสร้าง (ชมจริง→ขั้นต่อไป→คำถาม)** — หัวข้อ "ตรวจทาน" ในอบรม (Protocol 3 ขั้น)
- **Retrieval practice: ข้อ 1-3 ทวน, 4-7 ประยุกต์, 8-10 เชื่อมโยงบทเรียนก่อน** — ใช้ทำ "ทบทวนก่อนเรียน" ทุกคาบ
- **Success criteria "I can..."** — สอนครูเขียนจุดประสงค์แบบ Observable (verb เจาะจง ไม่ใช้ "เข้าใจ/รู้")
- **Rubric 4 ระดับไร้คำเปรียบเทียบ** ("avoid comparative language like better than") — เกณฑ์ประเมินงานนักเรียน
- **Reflection ครู (PD prompt)** — เติม gap **PLC 1, PA/วิทยฐานะ** โดยตรง
- **Parent email ไร้ศัพท์วิชาการ** — เติม gap **เยี่ยมบ้าน/สื่อสารผู้ปกครอง**
- **SEND/EAL scaffold 3 แบบ** — ใช้กับห้องเรียนรวมของไทย (แม้ไม่มีระบบ IEP เป็นทางการ)
- **Ethical considerations section** — อ้างอิง UK DfE framework (specificity/context/constraints) — ตอกย้ำหัวข้อ 6 (AI literacy/PDPA)

### ข้อเสนอแนะการปรับเป็น RCC (ตัวอย่าง 1 prompt)
**ต้นฉบับ (retrieval 10 ข้อ)** → **RCC ไทย:**
```text
[บทบาท] คุณเป็นครูกระตุ้นการทบทวนความรู้ (retrieval practice) ที่ชำนาญ
[บริบท] นักเรียนชั้น ม.2 วิชาวิทยาศาสตร์ เพิ่งเรียนเรื่อง [หัวข้อ] และเคยเรียน
[บทเรียนก่อนหน้า: ...]
[เงื่อนไข] สร้างคำถามทบทวน 10 ข้อ: ข้อ 1-3 ทวนข้อเท็จจริง (อะไร/เมื่อไร/ใคร),
ข้อ 4-7 ประยุกต์ใช้ (ทำไม/อย่างไร), ข้อ 8-10 เชื่อมกับบทเรียนก่อน
ตอบสั้น 1-2 ประโยค ไม่ใช้แบบปรนัย มีเฉลยทุกข้อ ภาษาไทย
```

---

## สรุปคัดเลือก prompt ที่แนะนำนำเข้าระบบ (≥20 ตัวอย่าง สำหรับครูไทย)

ครบตามเงื่อนไข 20+ ตัวอย่างจากต้นฉบับจริง (นับรวมทั้งหมดที่ยกมาข้างต้น = **41 ตัวอย่าง** คัดจาก 278)

### ลำดับความสำคัญนำไปเติมใน prompts-data.json (อิง gap analysis)

| ลำดับ | Prompt (ไทย, รูปแบบ RCC) | แหล่งต้นทาง | Gap ที่เติม |
|---|---|---|---|
| 1 | แผน Active Learning 1 คาบ (RCC) | alisamaid #5 | ออกแบบการสอน (17) |
| 2 | จุดประสงค์ 3 ด้าน (K/S/A) | alisamaid #4 | ออกแบบการสอน |
| 3 | ใบงานอ่านจับใจความ + เฉลย | boxmerz ชุด 1 | ใบงาน |
| 4 | โจทย์คณิต 3 ระดับ (ง่าย/กลาง/ท้าทาย) | boxmerz ชุด 3 | ใบงาน/ข้อสอบ |
| 5 | ใบงานวิทย์ 3 ส่วน (อธิบาย/เติมคำ/ชวนคิด) | boxmerz ชุด 2 | ใบงาน |
| 6 | ใบงาน Mind Map + คำถามความคิดเห็น | boxmerz ชุด 5 | ใบงาน/สังคม |
| 7 | ข้อสอบปรนัยตรงรหัสตัวชี้วัด | boxmerz/prompts | ข้อสอบ (18) |
| 8 | ข้อสอบ Cloze Test (โจทย์อังกฤษ-เฉลยไทย) | boxmerz/prompts #128 | ข้อสอบ/อังกฤษ |
| 9 | ข้อสอบอนุบาลพร้อม Image Prompt | boxmerz/prompts #8 | ข้อสอบ/ปฐมวัย |
| 10 | ข้อสอบการงานอาชีพ (งานบ้าน/ประดิษฐ์) | boxmerz/prompts #99,#119 | **การงาน (8)** |
| 11 | ข้อสอบศิลปะ (ทฤษฎีสี/ทัศนียภาพ/กราฟิก) | boxmerz/prompts #100,#105,#127 | **ศิลปะ (11)** |
| 12 | ข้อสอบรู้เท่าทันสื่อ (Fake News) | boxmerz/prompts #112 | เทคโนโลยี/เท่าทัน (ethics) |
| 13 | แผน + ตารางเวลา (lesson plan + schedule) | mentimeter #1 | ออกแบบการสอน |
| 14 | ข้อสอบตรงจุดประสงค์ (3 รูปแบบ) | mentimeter #26 | ข้อสอบ |
| 15 | แผนรายบุคคล (personalized learning plan) | mentimeter #22 | differentiation |
| 16 | กิจกรรม 3 ระดับ (tiered activities) | mentimeter #21 | differentiation |
| 17 | Rubric งานกลุ่ม/โครงงาน | mentimeter #27 / teachingchannel | การประเมิน |
| 18 | ข้อสอบตาม Bloom's Taxonomy + scenario | teachingchannel | ข้อสอบ/ประเมิน |
| 19 | Exit ticket สั้นๆ | teachingchannel | ประเมินระหว่างเรียน |
| 20 | หา Misconception ของนักเรียน | teachingchannel | ออกแบบการสอน |
| 21 | อธิบายเรื่องยากให้เด็ก 8 ขวบเข้าใจ | teachingchannel | ออกแบบการสอน |
| 22 | บทอ่าน 3 ระดับ (เก่ง/กลาง/อ่อน) | structural #1 | differentiation |
| 23 | Retrieval practice ทวนบทเรียน 10 ข้อ | structural #2 | ออกแบบการสอน |
| 24 | Feedback 3-4 ประโยค (ชมจริง→ขั้นต่อไป→คำถาม) | structural #3 | ตรวจงาน/feedback |
| 25 | สื่อสารผู้ปกครอง (อีเมลไร้ศัพท์วิชาการ) | structural #11 | **เยี่ยมบ้าน/ผู้ปกครอง (1)** |
| 26 | Success criteria "I can" แบบ observable | structural #9 | จุดประสงค์ |
| 27 | สะท้อนผลงานครู 5 คำถาม (PLC/PA) | structural #12 | **PLC (1)/PA** |
| 28 | Scaffold 3 แบบ สำหรับเด็กพิเศษ/EAL | structural #6 | ห้องเรียนรวม |
| 29 | Rubric 4 ระดับ (Emerging→Mastery) | structural #10 | การประเมิน |
| 30 | ประชุมผู้ปกครอง (agenda 30 นาที) | mentimeter #50 | **เยี่ยมบ้าน/ผู้ปกครอง** |
| 31 | Progress report นักเรียน | mentimeter #48 | **ปพ (5)** |
| 32 | Icebreaker/กิจกรรมกลุ่มรู้จักกัน | mentimeter #13 | โฮมรูม |
| 33 | เกมเช็คความรู้กลุ่ม (check-in games) | mentimeter #32 | **โฮมรูม (3)** |
| 34 | ทัศนศึกษาเสมือน (virtual field trip) | mentimeter #18 | กิจกรรม |
| 35 | ระบบรางวัลในห้องเรียน | mentimeter #45 | จัดการชั้นเรียน |
| 36 | แผนที่ seating chart | mentimeter #43 | จัดการชั้นเรียน |
| 37 | เกมการศึกษา (icebreaker/เกมภาษา) | alisamaid #15 | กิจกรรม |
| 38 | กรณีศึกษา (case-based learning) | alisamaid #14 | ออกแบบการสอน |
| 39 | จดหมายราชการ/ตอบอีเมลผู้ปกครอง | mentimeter #55 | **ปพ/ธุรการ** |
| 40 | ข้อสอบกลางภาคผสม (ปรนัย+อัตนัย) | alisamaid #10 | ข้อสอบ |
| 41 | ใบงานอังกฤษ (match/fill/draw) | boxmerz ชุด 4 | ใบงาน/อังกฤษ |

> **ข้อควรระวังสำหรับผู้ปรับ:** ตรวจทานทุกผลลัพธ์กับ Protocol 3 ขั้นเสมอ (AI แต่งสถิติ/กฎหมาย/เกณฑ์ได้) + ไม่ใส่ข้อมูลนักเรียน (PDPA) — ตาม prompt-cheatsheet-thai.md ข้อ "ข้อควรระวัง"

---

## Citations (URL + วันที่สกัด — ทุกแหล่งสกัด 2026-08-22)

1. Alisa AI. *ตัวอย่าง Prompt ใช้ AI สำหรับ ครู-อาจารย์* (16 prompts). https://alisamaid.com/prompt-teacher/ · สกัด 2026-08-22
2. BoxMerZ. *แจกฟรี 5 ชุด Prompt สร้างใบงาน AI สำเร็จรูป ก๊อปวางได้เลย!* https://boxmerz.com/blog/best-ai-prompts-for-worksheets-elementary · สกัด 2026-08-22
3. BoxMerZ. *คลัง Prompt AI สำหรับครู 126 แบบ สร้างข้อสอบ-ใบงานอัตโนมัติ*. https://boxmerz.com/prompts · สกัด 2026-08-22
4. Svernlöv, O. (2025, Dec 16). *56 game-changing AI prompts for teachers for 2026*. Mentimeter. https://www.mentimeter.com/blog/education/ai-prompts-for-teachers · สกัด 2026-08-22
5. Teaching Channel K12 Hub. *65 AI Prompts for Lesson Planning* (PDF). https://www.teachingchannel.com/k12-hub/blog/65-ai-prompts-for-lesson-planning/ ; PDF: https://www.teachingchannel.com/wp-content/uploads/2024/05/K12Hub-65-AI-Prompts-for-Lesson-Planning.pdf · สกัด 2026-08-22
6. Main, P. (2025, Nov 18; อัปเดต 2026-08-14). *10 AI Prompts Every Teacher Should Master [2026]*. Structural Learning. https://www.structural-learning.com/post/10-ai-prompts-every-teacher-should-master · สกัด 2026-08-22

> ⚠️ วันที่ "เผยแพร่" เป็นข้อมูลที่แปะไว้บนหน้าเว็บของแต่ละแหล่ง — เนื้อหาอาจมีการอัปเดตภายหลัง (เช่น structural-learning มีคำว่า "Updated on August 14, 2026") ตรวจซ้ำก่อนวันอบรม

---

## ข้อเสนอแนะเชิงปฏิบัติ

1. **ใช้ structural-learning เป็น "แม่แบบกรอบ"** ในการอบรม: กรอบ 4 องค์ประกอบ (Role/Task/Context/Format) = RCC + เพิ่มงาน/รูปแบบ — สอนครูให้เห็นหลักการก่อนก๊อป prompt
2. **boxmerz.com/prompts (126) = แหล่งก๊อปวางทันทีที่เจาะหลักสูตรไทย** — ให้ครูเปลี่ยน `[standard_code]` และหัวข้อเองได้ ใช้เป็น workshop หลัก
3. **เติม gap ตามตารางลำดับความสำคัญ 41 รายการ** ข้างต้นลง `site/prompts-data.json` (ต้องมี id ไม่ซ้ำ, fields: id/title/category/tools/prompt_template/role_context_condition ที่ role/context/condition แยก — ตั้งใจแปลงจาก prompt เดิมเป็นโครงสร้าง RCC)
4. **ทุก prompt ภาษาอังกฤษ → แปลเป็นไทย + เติมเงื่อนไขวัฒนธรรมไทย** (เช่น ตัวเลขไทย, วันสำคัญไทย, สถานการณ์ตลาด/สหกรณ์, ระดับชั้น ป./ม. ไม่ใช่ Year/grade)
5. **นำไอเดีย "Time Saved" และ "Why It Works"** ของ structural-learning ใส่สไลด์อบรม — ครูเชื่อเมื่อเห็นเวลาที่ประหยัดได้ + งานวิจัย
6. สร้าง "ตารางทดสอบโมเดล" แบบ boxmerz (Gemini/ChatGPT/Claude ดีต่างกันตามงาน) เป็นสื่ออบรมหัวข้อ 1