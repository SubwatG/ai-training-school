# แผนการพัฒนาและปรับปรุงสื่อการอบรม AI สำหรับครูไทย (Implementation Plan)

> **สำหรับ Hermes:** ใช้ทักษะ `writing-plans` และ `subagent-driven-development` เพื่อดำเนินการสร้างและปรับปรุงไฟล์สื่อ สไลด์นำเสนอ และหน้าเว็บพอร์ทัลแบบเป็นขั้นตอนที่ตรวจสอบได้จริง

**เป้าหมาย:** พัฒนาและปรับปรุงสื่อการสอน สไลด์นำเสนอ Interactive และหน้าเว็บพอร์ทัลสำหรับคุณครูโรงเรียนเทศบาล ๔ (เชาวนปรีชาอุทิศ) ให้มีขนาดตัวอักษรที่อ่านง่าย มีสไลด์อธิบายเครื่องมือสำคัญครบถ้วน (Gems, Canvas, Banana 2.0, Canva AI, NotebookLM) พร้อมแนวทางกิจกรรมฝึกปฏิบัติที่เข้าใจง่าย ชัดเจน และทำตามได้ทันที

**สถาปัตยกรรม:** ปรับปรุงและสร้างไฟล์ในระบบ 3 ส่วนหลัก:
1. **Interactive Slide Deck (`site/slide-deck.html`):** เพิ่มสไลด์อธิบายฟีเจอร์สำคัญ 4 ส่วน (Gems, Gemini Canvas, Banana 2.0, Canva AI/Magic Tools, NotebookLM Zero-Hallucination)
2. **Web Portal & Guides (`site/tutorials.html`, `site/prompts.html`, `site/mockups.html`):** ขยายการ์ดสรุปแนวทางเทคนิค Canva AI, เทมเพลตชุมชน, และสูตร Prompt สร้างภาพ Banana 2.0 เพื่อการศึกษา
3. **คู่มือวิทยากรและเอกสารหลักสูตร (`docs/`):** อัปเดตสคริปต์ขั้นตอนกิจกรรม Mini-Workshop ทั้ง 4 ช่วงให้สอดคล้องกับสื่อจริง

**เทคโนโลยี:** HTML5, CSS3 Vanilla (Pure Bright Theme, Mali + Noto Sans Thai Looped), Tailwind CSS CDN, Vanilla JavaScript (High-Performance DOM), Markdown/LaTeX notation

---

## รายการงานย่อย (Implementation Tasks)

### งานที่ 1: เพิ่มสไลด์อธิบายเจาะลึก 4 ฟีเจอร์หลักใน `site/slide-deck.html`

**วัตถุประสงค์:** เพิ่มสไลด์นำเสนอเพื่ออธิบายให้ครูเข้าใจว่า Gems, Gemini Canvas, Banana 2.0 และ Canva AI คืออะไร ทำงานอย่างไร พร้อมภาพประกอบและตัวอย่างจริง

**ไฟล์ที่เกี่ยวข้อง:**
- แก้ไข: `/home/kitti/Projects/Activities-me/ai-training-school/site/slide-deck.html`

**ขั้นตอนที่ 1: เขียนโค้ดสไลด์ใหม่ 4 สไลด์**
1. **Slide: Gemini Gems คืออะไร?**
   - คำอธิบาย: ผู้ช่วยเฉพาะวิชา/งาน ที่จำคำสั่งล่วงหน้า ไม่ต้องพิมพ์ใหม่ทุกวัน
   - ตัวอย่าง: Gem สกัดข้อความใบงานเก่า (OCR), Gem วิเคราะห์ข้อสอบ
2. **Slide: Gemini Canvas คืออะไร & สั่งแก้อย่างไร?**
   - คำอธิบาย: หน้าจอคู่แบบ Side-by-Side (ซ้ายแชทคุย ขวากระดานงานจริง)
   - ฟังก์ชันสำคัญ: ลากคลุมข้อความ (Highlight) สั่งปรับระดับภาษา ปรับความยาก หรือเพิ่มช้อยส์เฉพาะจุด
3. **Slide: Banana 2.0 (Imagen 3) กฎเหล็กสร้างภาพการศึกษา**
   - คำอธิบาย: ปัญหาตัวอักษรเละใน AI และทางแก้ด้วยสูตร `2D flat, white background, no text`
4. **Slide: Canva AI & Magic Studio พลังจัดรูปเล่ม**
   - คำอธิบาย: Magic Grab ย้ายวัตถุ, Magic Eraser ลบส่วนเกิน, และ Canva Math App สำหรับสมการเวกเตอร์คมชัด

**ขั้นตอนที่ 2: ตรวจสอบและบันทึกผล**
- ตรวจสอบลำดับสไลด์และการเปลี่ยนหน้า (Next/Prev/Overview)
- คำสั่งคอมมิต:
```bash
git add site/slide-deck.html
git commit -m "feat(slides): add in-depth explanation slides for Gems, Canvas, Banana 2.0, and Canva AI"
```

---

### งานที่ 2: อัปเกรดหน้าคู่มือ `site/tutorials.html` ให้มีคำแนะนำ Canva AI และ Banana 2.0 ชัดเจน

**วัตถุประสงค์:** เพิ่มการ์ดคำแนะนำ เทคนิคการเลือกเทมเพลตชุมชนใน Canva และสูตรภาพ Banana 2.0 ให้นักเรียน/ครูเปิดดูทำตามได้ง่าย

**ไฟล์ที่เกี่ยวข้อง:**
- แก้ไข: `/home/kitti/Projects/Activities-me/ai-training-school/site/tutorials.html`

**ขั้นตอนที่ 1: เพิ่มเนื้อหาในส่วน Canvas และ Canva**
- เพิ่มส่วนแนะนำคำค้นหา Template ชุมชน (`ใบงาน A4`, `Edu worksheet pastel`, `อินโฟกราฟิก`)
- เพิ่มการ์ดอธิบาย Magic Grab, Magic Eraser, Magic Expand
- เพิ่มตัวอย่าง Prompt ภาพ Banana 2.0 แยกตามกลุ่มสาระ (วิทย์, ภาษาไทย, สังคม, คณิต)

**ขั้นตอนที่ 2: ตรวจสอบความถูกต้องของลิงก์และเลย์เอาต์**
- คำสั่งคอมมิต:
```bash
git add site/tutorials.html
git commit -m "feat(tutorials): enrich Canva AI techniques and Banana 2.0 prompt guides"
```

---

### งานที่ 3: ซิงค์โครงสร้างกิจกรรมในเอกสารหลักสูตรและคู่มือวิทยากร (`docs/`)

**วัตถุประสงค์:** อัปเดตรายละเอียดกิจกรรมช่วงเช้า-บ่ายให้ตรงกัน 100% โดยเน้น Flow จาก OCR → Canvas (เกลาเนื้อหา) → Canva (วาง A4 ส่งออก PDF)

**ไฟล์ที่เกี่ยวข้อง:**
- แก้ไข: `/home/kitti/Projects/Activities-me/ai-training-school/docs/updated-curriculum-2026-08-25.md`
- แก้ไข: `/home/kitti/Projects/Activities-me/ai-training-school/docs/session-1-gemini-facilitator-guide.md`

**ขั้นตอนที่ 1: ปรับแก้สคริปต์วิทยากร**
- ระบุจุดเน้นย้ำเรื่อง Canvas ไม่ใช่โปรแกรมจัดหน้า แต่เป็น Smart Text Editor
- ยืนยันขั้นตอนการส่งออกผลงาน A4 ใน Canva

**ขั้นตอนที่ 2: บันทึกและสรุปผล**
- คำสั่งคอมมิต:
```bash
git add docs/
git commit -m "docs(curriculum): align workshop flow with Canvas editing and Canva A4 delivery"
```

---

## การตรวจสอบคุณภาพ (Quality Gates)
1. ไม่มีแท็ก `$\rightarrow$` หรือรหัส KaTeX ตกค้างในส่วนข้อความทั่วไป
2. หน้าเว็บทุกหน้ามีขนาดตัวอักษรใหญ่ชัดเจนสำหรับคุณครู (`base html 19px`)
3. สไลด์นำเสนอเปิดได้ลื่นไหล ไม่พบข้อผิดพลาดในคอนโซล
4. มีตัวอย่างพร้อมใช้งานสำหรับครูครบทั้ง 8 กลุ่มสาระ
