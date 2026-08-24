# -*- coding: utf-8 -*-
import json
import os

nlm_media_prompts = [
    # =========================================================================
    # 1. MINDMAP & CONCEPT MAPPING (แผนผังความคิด & ผังมโนทัศน์)
    # =========================================================================
    {
        "id": "nlm-media-mindmap-mermaid",
        "title": "NotebookLM: สกัดโครงสร้างแผนผังความคิด (Mindmap) เป็นโค้ด Mermaid / Markdown จากเอกสาร PDF",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "Mindmap", "Mermaid", "ผังมโนทัศน์", "สรุปบทเรียน"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญการจัดระบบสารสนเทศเชิงภาพและผังมโนทัศน์ (Concept Mapping Specialist)",
            "context": "ฉันได้อัปโหลดเอกสารบทเรียน PDF และต้องการแปลงเนื้อหาที่ซับซ้อนให้เป็นแผนผังความคิดลำดับชั้น (Mindmap)",
            "condition": "จากเนื้อหาทั้งหมดในเอกสาร สกัดแผนผังความคิดออกเป็น 2 รูปแบบ: 1) ลำดับหัวข้อแบบ Bullet Indented Markdown (หัวข้อหลัก -> หัวข้อย่อย -> รายละเอียด) 2) โค้ดไดอะแกรม Mermaid syntax (`mindmap`) ที่พร้อมนำไปเรนเดอร์เป็นภาพผังความคิด"
        },
        "prompt_template": "จากเอกสารที่ฉันอัปโหลดไว้ ช่วยสกัดแผนผังมโนทัศน์ (Mindmap) ของเรื่อง [หัวข้อในเอกสาร] โดยแบ่งเป็น: 1. หัวข้อแก่นกลาง (Central Idea) 2. กิ่งหลัก 4-5 กิ่ง (Main Branches) 3. กิ่งย่อยและตัวอย่างประกอบ (Sub-branches) พร้อมเขียนเป็นโครงสร้างโค้ด Mermaid.js ให้ด้วย",
        "tips": "นำโค้ด Mermaid ที่ได้ไปวางในเว็บ mermaid.live หรือเครื่องมือสร้างผังความคิดใน Canva เพื่อแปลงเป็นกราฟิกสวยงามทันที",
        "source": "NotebookLM Mindmap & Knowledge Graph Framework",
        "curated_top10": False
    },
    {
        "id": "nlm-media-cornell-notes-sheet",
        "title": "NotebookLM: แปลงเนื้อหาเอกสารเป็นใบสรุปการจดบันทึกแบบคอร์เนลล์ (Cornell Notes Matrix)",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "เอกสาร & สรุปรายงาน"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "Cornell Notes", "เทคนิคการเรียน", "ใบความรู้", "สรุปหน้าเดียว"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญด้านกลยุทธ์การเรียนรู้และการจดบันทึกแบบคอร์เนลล์ (Cornell Note-Taking System)",
            "context": "ฉันต้องการทำใบความรู้สรุปบทเรียนที่ฝึกให้นักเรียนตั้งคำถามและสรุปใจความสำคัญด้วยตนเอง",
            "condition": "จัดระเบียบเนื้อหาจากเอกสารให้อยู่ในโครงสร้าง Cornell Notes 3 ส่วน: 1) แถบซ้าย (Cue Column): คีย์เวิร์ดและคำถามสำคัญ 2) แถบขวา (Notes Column): คำอธิบายและรายละเอียดสั้นกระชับ 3) แถบล่าง (Summary): สรุปใจความสำคัญ 2-3 บรรทัด"
        },
        "prompt_template": "ช่วยจัดทำใบสรุปเนื้อหาแบบ 'Cornell Notes' จากเอกสารที่อัปโหลด เรื่อง [หัวข้อ] สำหรับนักเรียนชั้น [ระดับชั้น] โดยทำเป็นตารางที่มี: 1. คำถามกระตุ้นคิดและคำสำคัญ (Cue Column) 2. เนื้อหาสาระและตัวอย่าง (Notes Column) 3. บทสรุปภาพรวมท้ายบท (Summary)",
        "tips": "พิมพ์ตารางนี้แจกให้นักเรียนทบทวน หรือเว้นช่อง Notes ไว้บางส่วนให้นักเรียนเติมระหว่างฟังบรรยาย",
        "source": "Cornell University Learning Strategies",
        "curated_top10": False
    },

    # =========================================================================
    # 2. INFOGRAPHIC & DATA TABLES (อินโฟกราฟิก & ตารางข้อมูลเปรียบเทียบ)
    # =========================================================================
    {
        "id": "nlm-media-infographic-data-brief",
        "title": "NotebookLM: สกัดชุดข้อมูล 5 ประเด็นสำคัญ + สถิติตัวเลข สำหรับทำ Infographic ใน Canva",
        "category": {
            "subject": "วิทยาศาสตร์และเทคโนโลยี",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "Canva", "Infographic Brief", "สถิติข้อมูล", "สื่อการสอน"],
        "role_context_condition": {
            "role": "คุณเป็น Information Designer และ Data Journalist ผู้เชี่ยวชาญการแปลงเอกสารวิชาการเป็นสื่อภาพ",
            "context": "ฉันต้องการทำ Infographic สรุปบทเรียน 1 หน้าใน Canva แต่ไม่อยากอ่านคัดแยกตัวเลขและข้อความเองจาก PDF 30 หน้า",
            "condition": "สกัดข้อมูลสำคัญจากเอกสารออกมา 5 กล่องเนื้อหา: 1) พาดหัวข่าวที่ดึงดูดใจ 2) ข้อมูลสถิติหรือตัวเลขสำคัญ (Key Metrics) 3-4 ตัว 3) ไทม์ไลน์หรือกระบวนการ 4 สเต็ป 4) ข้อควรระวังหรือ Do & Don't 5) คำค้นหาไอคอนใน Canva ที่เข้ากับแต่ละจุด"
        },
        "prompt_template": "จากเอกสารทั้งหมด ช่วยสรุป 'Brief ข้อมูลสำหรับทำ Infographic ใน Canva' เรื่อง [หัวข้อ เช่น การเปลี่ยนแปลงสภาพภูมิอากาศ / พลังงานทดแทน] โดยสกัด: 1. พาดหัวหลัก 2. ตัวเลขสถิติเด่น 3 ตัว 3. ขั้นตอนสำคัญ 4 สเต็ป (ข้อความสั้นไม่เกิน 15 คำต่อขั้น) 4. คำค้นหา Element ใน Canva ที่ตรงกับเนื้อหา",
        "tips": "นำผลลัพธ์ที่ได้ไปวางในเทมเพลต 'Education Infographic' ใน Canva ได้ทันทีโดยไม่ต้องเรียบเรียงคำใหม่",
        "source": "NotebookLM to Canva Infographic Pipeline",
        "curated_top10": False
    },
    {
        "id": "nlm-media-comparative-matrix-table",
        "title": "NotebookLM: สร้างตารางเปรียบเทียบเชิงลึก (Multi-dimensional Comparison Matrix) จากเอกสาร",
        "category": {
            "subject": "วิทยาศาสตร์และเทคโนโลยี",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "ตารางเปรียบเทียบ", "Matrix", "วิเคราะห์เชิงเปรียบเทียบ", "ตารางสรุป"],
        "role_context_condition": {
            "role": "คุณเป็นนักวิเคราะห์ข้อมูลวิชาการที่เชี่ยวชาญการสังเคราะห์ตารางเปรียบเทียบหลายมิติ",
            "context": "ฉันมีเอกสารที่อธิบายทฤษฎี สิ่งมีชีวิต หรือสารเคมีหลายชนิดที่คล้ายคลึงกัน และนักเรียนมักจำสับสน",
            "condition": "สร้างตารางเปรียบเทียบแบบ Markdown Matrix เปรียบเทียบ [ระบุหัวข้อเปรียบเทียบ เช่น เซลล์พืช vs เซลล์สัตว์ หรือ ดาวเคราะห์หิน vs ดาวเคราะห์แก๊ส] ใน 5 มิติ: โครงสร้าง, หน้าที่, แหล่งพลังงาน, ลักษณะเด่น, และตัวอย่าง พร้อมระบุหน้าในเอกสารที่ใช้เป็นแหล่งอ้างอิง"
        },
        "prompt_template": "จากเอกสารที่อัปโหลด ช่วยสร้าง 'ตารางเปรียบเทียบเชิงลึก (Comparison Table)' เรื่อง [หัวข้อ เช่น ความแตกต่างระหว่างสารประกอบอินทรีย์และอนินทรีย์] โดยทำเป็นตาราง Markdown เปรียบเทียบในมิติต่างๆ อย่างน้อย 5 ด้าน พร้อมสรุปข้อสังเกตจุดที่มักจำสลับกัน",
        "tips": "ตารางเปรียบเทียบช่วยให้นักเรียนเห็นภาพความแตกต่างได้ชัดเจนกว่าการอ่านร้อยแก้วยาวๆ",
        "source": "NotebookLM Analytical Matrix Synthesis",
        "curated_top10": False
    },

    # =========================================================================
    # 3. FLASHCARDS & GAMIFIED QUIZ (แฟลชการ์ด & ควิซเกม)
    # =========================================================================
    {
        "id": "nlm-media-flashcard-qa-pairs",
        "title": "NotebookLM: สร้างชุดการ์ดคำถาม-คำตอบ (Flashcard Deck 20 ใบ) พร้อมเฉลยและระดับความยาก",
        "category": {
            "subject": "ภาษาต่างประเทศ",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "Flashcard", "บัตรคำ", "ทบทวนความจำ", "Canva Bulk"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญด้านเทคนิคการจำแบบ Spaced Repetition และการสร้างชุดแฟลชการ์ด",
            "context": "ฉันต้องการทำชุดบัตรคำถาม-คำตอบ (Flashcard) 15-20 คู่ เพื่อให้นักเรียนจับคู่เล่นเกมทบทวนบทเรียน",
            "condition": "สกัดชุดคำถาม-คำตอบ 15-20 คู่จากเอกสาร ทำเป็นตาราง 4 คอลัมน์: 1. Card_ID 2. ด้านหน้าการ์ด (คำถาม/คำศัพท์) 3. ด้านหลังการ์ด (คำตอบ/คำอธิบายกระชับ) 4. ระดับความยาก (ง่าย/กลาง/ท้าทาย)"
        },
        "prompt_template": "จากเอกสารบทเรียนที่อัปโหลด ช่วยสร้างชุดการ์ดทบทวนความจำ (Flashcard Deck) จำนวน [15] คู่ เรื่อง [หัวข้อ] โดยทำเป็นตาราง Markdown ที่มี: ด้านหน้าการ์ด (คำถามสั้นกระชับ) / ด้านหลังการ์ด (คำตอบที่ถูกต้องชัดเจน) / เลขหน้าอ้างอิง",
        "tips": "นำตารางนี้ไป Export เป็น CSV แล้วใช้ฟังก์ชัน Bulk Create ใน Canva เพื่อสร้าง Flashcard 15 ใบใน 10 วินาที",
        "source": "NotebookLM Flashcard Automation",
        "curated_top10": False
    },
    {
        "id": "nlm-media-gamified-quiz-kahoot-prep",
        "title": "NotebookLM: สกัดข้อสอบ 4 ตัวเลือกในรูปแบบตารางพร้อม Import เข้า Kahoot / Quizizz",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "ข้อสอบ & การวัดผล"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "Kahoot", "Quizizz", "เกมตอบคำถาม", "Import CSV"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญการสร้างเกมตอบคำถามออนไลน์ (Gamified Quiz Creator)",
            "context": "ฉันต้องการนำเนื้อหาในเอกสาร PDF ไปสร้างเกมตอบคำถาม Kahoot หรือ Quizizz 10 ข้อสำหรับเล่นท้ายคาบ",
            "condition": "สร้างข้อสอบ 4 ตัวเลือก 10 ข้อ จากเอกสาร โดยจัดรูปแบบตามเทมเพลตมาตรฐาน Kahoot: 1. Question (ไม่เกิน 95 ตัวอักษร) 2. Option 1 3. Option 2 4. Option 3 5. Option 4 6. Time limit (sec) 7. Correct answer (1-4)"
        },
        "prompt_template": "จากเอกสารที่ฉันอัปโหลดไว้ ช่วยสร้างข้อสอบ 4 ตัวเลือก จำนวน [10] ข้อ เรื่อง [หัวข้อ] สำหรับนำไปใส่ใน Kahoot/Quizizz โดยขอตารางที่มีคอลัมน์: คำถาม / ช้อยส์ 1-4 / ข้อที่ถูก / เวลาตอบ (20 วินาที) โดยทุกข้อต้องตรงตามเนื้อหาในเอกสารเท่านั้น",
        "tips": "ก๊อปปี้ตารางนี้ไปวางใน Excel Template ของ Kahoot แล้วกด Import Spreadsheet เพื่อสร้างเกมได้ทันที",
        "source": "Gamified EdTech Integration with NotebookLM",
        "curated_top10": False
    },

    # =========================================================================
    # 4. AUDIO & PODCAST OVERVIEW (เสียงบรรยาย & พอดแคสต์การสอน)
    # =========================================================================
    {
        "id": "nlm-audio-roleplay-interview-host",
        "title": "NotebookLM: ปรับแต่ง Audio Overview เป็นบทสัมภาษณ์บุคคลในประวัติศาสตร์/ผู้เชี่ยวชาญ",
        "category": {
            "subject": "สังคมศึกษา ศาสนา และวัฒนธรรม",
            "task_type": "นวัตกรรม & กิจกรรม"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "Audio Overview", "สัมภาษณ์จำลอง", "ประวัติศาสตร์", "เสียงพอดแคสต์"],
        "role_context_condition": {
            "role": "คุณเป็นผู้กำกับรายการวิทยุการศึกษาและละครเสียง (Audio Drama Director)",
            "context": "ฉันต้องการใช้ฟังก์ชัน Customize ใน Audio Overview ของ NotebookLM เพื่อสร้างบทสนทนาเสียงจำลองการสัมภาษณ์บุคคลในบทเรียน",
            "condition": "เขียนคำสั่งปรับแต่งเสียง (Customize Prompt) สั่งให้ AI Host ทั้งสอง: คนหนึ่งเป็นผู้ดำเนินรายการนักข่าว และอีกคนสวมบทบาทเป็น [บุคคลสำคัญ เช่น นักวิทยาศาสตร์/บุคคลประวัติศาสตร์] เล่าถึงเบื้องหลังการค้นพบหรือการตัดสินใจในอดีตอย่างตื่นเต้นและสมจริง"
        },
        "prompt_template": "ช่วยเขียน Customize Instructions สำหรับใส่ในกล่อง Audio Overview ของ NotebookLM โดยสั่งให้ผู้ดำเนินรายการ 2 คนจำลองเป็น: 'ผู้ดำเนินรายการนักข่าวสัมภาษณ์ [บุคคลสำคัญ เช่น กาลิเลโอ / ท้าวสุรนารี]' เพื่อเจาะลึกเหตุการณ์ [ระบุเหตุการณ์] โดยให้มีน้ำเสียงตื่นเต้น ดึงดูด และเล่าเรื่องแบบเห็นภาพ",
        "tips": "กดปุ่ม Customize ในกล่อง Audio Overview ก่อนกด Generate เพื่อให้เสียงที่ออกมาเป็นรูปแบบการสัมภาษณ์สด",
        "source": "NotebookLM Audio Roleplay Engineering",
        "curated_top10": False
    },
    {
        "id": "nlm-audio-mini-lecture-podcast",
        "title": "NotebookLM: สร้างพอดแคสต์สรุปบทเรียน 5 นาทีสำหรับการเรียนรู้แบบห้องเรียนกลับด้าน (Flipped Classroom)",
        "category": {
            "subject": "วิทยาศาสตร์และเทคโนโลยี",
            "task_type": "นวัตกรรม & กิจกรรม"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "Flipped Classroom", "Podcast สรุป", "ห้องเรียนกลับด้าน", "Audio"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญการจัดการเรียนรู้แบบห้องเรียนกลับด้าน (Flipped Classroom Pedagogy)",
            "context": "ฉันต้องการให้นักเรียนฟังคลิปเสียงสรุปภาพรวมบทเรียน 5 นาทีก่อนเข้าชั้นเรียน เพื่อให้ในคาบมีเวลาทำกิจกรรมปฏิบัติ",
            "condition": "เขียนคำสั่ง Customize Audio Overview ให้โฟกัสเฉพาะ: 1) ปรากฏการณ์ในชีวิตจริงที่เชื่อมโยงกับบทเรียน 2) นิยามแก่น 2-3 ข้อ 3) คำถามท้าทาย 1 คำถามเพื่อให้นักเรียนนำมาถกเถียงกันในคาบเรียนวันพรุ่งนี้"
        },
        "prompt_template": "ช่วยเขียนคำสั่งปรับแต่งเสียง Audio Overview ใน NotebookLM สำหรับเตรียมพอดแคสต์ล่วงหน้า (Pre-class Podcast) เรื่อง [หัวข้อ เช่น แรงลอยตัวและการจม-ลอย] โดยสั่งให้ Host เน้นเปิดประเด็นด้วยคำถามปริศนา สรุปหลักการง่ายๆ และทิ้งคำถามท้าทายให้นักเรียนนำมาตอบครูในห้อง",
        "tips": "ดาวน์โหลดไฟล์เสียง .mp4 หรือแชร์ลิงก์ Notebook ให้นักเรียนเปิดฟังบนมือถือระหว่างเดินทางมาโรงเรียน",
        "source": "Flipped Classroom Audio Strategy",
        "curated_top10": False
    },
    {
        "id": "nlm-audio-storytelling-dramatization",
        "title": "NotebookLM: ปรับแต่ง Audio Overview เป็นการเล่าเรื่องเชิงวรรณกรรม/นิทานเสียง (Storytelling Podcast)",
        "category": {
            "subject": "ภาษาไทย",
            "task_type": "นวัตกรรม & กิจกรรม"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "นิทานเสียง", "วรรณคดี", "Storytelling", "Audio Overview"],
        "role_context_condition": {
            "role": "คุณเป็นนักเล่านิทานและผู้ผลิตสื่อนวนิยายเสียง (Narrative Audio Producer)",
            "context": "ฉันต้องการเปลี่ยนเอกสารวรรณคดีหรือประวัติศาสตร์ที่ยาวและน่าเบื่อ ให้กลายเป็นเรื่องเล่าเสียงที่มีอารมณ์ร่วม",
            "condition": "เขียนคำสั่ง Customize Instructions ให้ Audio Overview เล่าเรื่องแบบ Storytelling: มีการปูพื้นบรรยากาศ, เล่าถึงปมขัดแย้งของตัวละคร, บรรยายฉากการต่อสู้หรือการตัดสินใจสำคัญ, และสรุปข้อคิดเตือนใจ"
        },
        "prompt_template": "ช่วยเขียนข้อความคำสั่ง Customize Audio Overview ใน NotebookLM เพื่อสั่งให้ AI เล่าเรื่องวรรณคดีเรื่อง [ชื่อเรื่อง เช่น สังข์ทอง ตอน กำเนิดพระสังข์] ในรูปแบบ 'นิทานเสียงชวนติดตาม' โดยให้ผู้จัดทั้งสองใช้น้ำเสียงตื่นเต้น มีการสลับบทพูดและวิเคราะห์ความรู้สึกของตัวละครอย่างลึกซึ้ง",
        "tips": "เหมาะสำหรับใช้เปิดกระตุ้นความสนใจ (Warm-up / Hook) 3 นาทีแรกของคาบเรียนวิชาภาษาไทย",
        "source": "Literary Dramatization via NotebookLM",
        "curated_top10": False
    },

    # =========================================================================
    # 5. VIDEO OVERVIEW & STORYBOARD SCRIPTS (วิดีโอ & สตอรี่บอร์ด)
    # =========================================================================
    {
        "id": "nlm-media-video-lesson-script",
        "title": "NotebookLM: แปลงเอกสารวิชาการเป็นสคริปต์วิดีโอบทเรียน 3 นาที (3-Minute Micro-lesson Script)",
        "category": {
            "subject": "วิทยาศาสตร์และเทคโนโลยี",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "สคริปต์วิดีโอ", "Micro-lesson", "Storyboard", "Canva Video"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เขียนบทสารคดีสั้นเพื่อการศึกษา (Educational Video Scriptwriter)",
            "context": "ฉันต้องการทำคลิปวิดีโอสั้น 3 นาทีอธิบายบทเรียนลง YouTube หรือ Canva Video",
            "condition": "สกัดเนื้อหาจากเอกสารมาเขียนเป็นสคริปต์วิดีโอ 2 คอลัมน์ (ภาพ Visual / เสียง Audio): Scene 1 (Hook 0-30 วินาที), Scene 2-4 (เนื้อหาหลัก 3 สเต็ป 30-150 วินาที), Scene 5 (สรุปและ Call to Action 150-180 วินาที)"
        },
        "prompt_template": "จากเอกสารที่ฉันอัปโหลด ช่วยเขียน 'สคริปต์วิดีโอการสอนความยาว 3 นาที' เรื่อง [หัวข้อ] สำหรับนักเรียนชั้น [ระดับชั้น] โดยแบ่งเป็นตาราง 2 คอลัมน์: 1. ภาพบนจอ/มุมกล้อง (Visual Prompt) 2. บทพูดบรรยายของผู้สอน (Audio Voiceover) ภาษาเข้าใจง่าย ชัดเจน",
        "tips": "นำสคริปต์ฝั่ง Visual ไปค้นหาคลิปวิดีโอใน Canva แล้วอัดเสียงพูดตามช่อง Audio Voiceover ได้ทันที",
        "source": "NotebookLM Video Scriptwriting Module",
        "curated_top10": False
    },
    {
        "id": "nlm-media-interactive-slide-content",
        "title": "NotebookLM: สกัดหัวข้อย่อยและเนื้อหากระชับ 10 สไลด์ สำหรับนำไปจัดทำสไลด์การสอน",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "สไลด์การสอน", "Canva Slides", "PowerPoint", "สรุปสไลด์"],
        "role_context_condition": {
            "role": "คุณเป็น Presentation Designer และผู้เชี่ยวชาญการย่อยเนื้อหาบทเรียน (Content Distiller)",
            "context": "ฉันมีเอกสารวิชาการ 40 หน้า และต้องการย่อยเป็นสไลด์สอน 10 หน้า ที่ตัวหนังสือไม่แน่นเกินไป",
            "condition": "สกัดเนื้อหาออกเป็นโครงสร้าง 10 สไลด์: หน้า 1 (Title), หน้า 2 (จุดประสงค์การเรียนรู้), หน้า 3-8 (เนื้อหาหลัก 6 ประเด็น แต่ละหน้ามีหัวข้อ + 3 bullet points สั้นๆ + คำแนะนำรูปภาพ), หน้า 9 (คำถามวัดผล), หน้า 10 (สรุปบทเรียน)"
        },
        "prompt_template": "จากเอกสารทั้งหมด ช่วยสกัดเนื้อหาออกเป็น 'โครงร่างสไลด์ 10 หน้า' เรื่อง [หัวข้อ] โดยแต่ละหน้าให้ระบุ: 1. หัวข้อสไลด์ 2. ข้อความสำคัญ 3 บรรทัด (ห้ามยาวเกินไป) 3. คีย์เวิร์ดสำหรับค้นหารูปภาพประกอบใน Canva",
        "tips": "นำข้อความไปใส่ใน Canva Slides หรือ PowerPoint ได้รวดเร็วโดยไม่ต้องนั่งคัดลอกและตัดทอนคำเอง",
        "source": "Slide Content Distillation Protocol",
        "curated_top10": False
    },

    # =========================================================================
    # 6. CLASSROOM ACTIVITIES & WORKSHEETS (ใบกิจกรรม & การจัดกิจกรรมในห้อง)
    # =========================================================================
    {
        "id": "nlm-media-fill-in-the-blank-summary",
        "title": "NotebookLM: สร้างใบสรุปความรู้แบบเติมคำ (Guided Cloze Summary Sheet) จากเอกสาร",
        "category": {
            "subject": "ภาษาไทย",
            "task_type": "ข้อสอบ & การวัดผล"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "ใบงานเติมคำ", "Cloze Test", "สรุปบทเรียน", "วัดผล"],
        "role_context_condition": {
            "role": "คุณเป็นผู้ออกแบบใบกิจกรรมการเรียนรู้แบบมีโครงสร้างชี้แนะ (Guided Notes Specialist)",
            "context": "ฉันต้องการทำใบงานสรุปเนื้อหา 1 หน้า A4 ให้นักเรียนฟังบรรยายไปแล้วเติมคำสำคัญลงในช่องว่าง",
            "condition": "เขียนบทสรุปเนื้อหา 3 ย่อหน้าจากเอกสาร โดยเว้นช่องว่าง `[ ........ ]` ตรงคำศัพท์เทคนิค คีย์เวิร์ด หรือตัวเลขสำคัญ รวม 10-15 ช่อง พร้อมแนบ 'ธนาคารคำศัพท์ (Word Bank)' และเฉลยท้ายใบงาน"
        },
        "prompt_template": "จากเอกสารที่อัปโหลด ช่วยสร้าง 'ใบสรุปความรู้แบบเติมคำในช่องว่าง (Guided Notes)' เรื่อง [หัวข้อ] ความยาว 1 หน้า สำหรับชั้น [ระดับชั้น] โดยเว้นช่องว่างสำหรับคำสำคัญ 12 จุด พร้อมมี Word Bank ให้เด็กเลือกคำมาเติม และมีเฉลยละเอียดกำกับ",
        "tips": "เหมาะมากสำหรับช่วยให้นักเรียนมีสมาธิจดจ่ออยู่กับการฟังและอ่านจับใจความตลอดคาบเรียน",
        "source": "Guided Notes Instructional Scaffolding",
        "curated_top10": False
    },
    {
        "id": "nlm-media-case-study-extractor",
        "title": "NotebookLM: สกัดกรณีศึกษาจริงและตัวอย่างจากตำรา เพื่อทำใบกิจกรรมแก้ปัญหา (Real-world Case Studies)",
        "category": {
            "subject": "สังคมศึกษา ศาสนา และวัฒนธรรม",
            "task_type": "นวัตกรรม & กิจกรรม"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "กรณีศึกษา", "Case Study", "การแก้ปัญหา", "Active Learning"],
        "role_context_condition": {
            "role": "คุณเป็นผู้เชี่ยวชาญการจัดการเรียนรู้โดยใช้กรณีศึกษาเป็นฐาน (Case-Based Learning)",
            "context": "ฉันต้องการตัวอย่างเหตุการณ์จริงหรือกรณีศึกษาที่มีในเอกสาร เพื่อให้นักเรียนกลุ่มย่อยได้ระดมสมองวิเคราะห์",
            "condition": "ค้นหาและสกัดกรณีศึกษา 2 กรณีจากเอกสาร: ระบุบริบทและปัญหาที่เกิดขึ้น, ข้อมูลตัวเลขหลักฐาน, คำถามท้าทาย 3 ข้อสำหรับนักเรียนอภิปราย, และแนวทางแก้ปัญหาตามทฤษฎีในเล่ม"
        },
        "prompt_template": "ช่วยสกัด 'กรณีศึกษาตัวอย่างจริง (Case Study)' จำนวน 2 เรื่องจากเอกสารที่ฉันอัปโหลด เรื่อง [หัวข้อ เช่น ปัญหาการจัดการขยะชุมชน / การฟ้องร้องสิทธิผู้บริโภค] พร้อมตั้งคำถามวิเคราะห์ 3 ข้อต่อกรณีศึกษา เพื่อให้นักเรียนแบ่งกลุ่มถกเถียง",
        "tips": "การนำกรณีศึกษาจริงจากเอกสารมาใช้จะช่วยให้นักเรียนเห็นคุณค่าและการนำความรู้ไปใช้ในชีวิตจริง",
        "source": "Case-Based Learning Pedagogical Design",
        "curated_top10": False
    },
    {
        "id": "nlm-media-debate-motion-prep",
        "title": "NotebookLM: สกัดประเด็นขัดแย้งและหลักฐานสนับสนุน-คัดค้านสำหรับจัดโต้วาทีในห้องเรียน",
        "category": {
            "subject": "สังคมศึกษา ศาสนา และวัฒนธรรม",
            "task_type": "นวัตกรรม & กิจกรรม"
        },
        "tools": ["NotebookLM"],
        "tags": ["NotebookLM", "โต้วาที", "หลักฐานสนับสนุน", "คิดวิเคราะห์", "Debate"],
        "role_context_condition": {
            "role": "คุณเป็นโค้ชโต้วาทีและผู้เชี่ยวชาญการโต้แย้งโดยใช้หลักฐานเชิงประจักษ์ (Evidence-based Argumentation)",
            "context": "ฉันต้องการจัดกิจกรรมโต้วาทีในห้องเรียนโดยให้นักเรียนอ้างอิงข้อมูลจากเอกสารประกอบการสอน",
            "condition": "สกัดญัตติการโต้วาที 1 ญัตติจากเอกสาร พร้อมจัดทำ: 1) ฝ่ายเสนอ (Affirmative): ข้อโต้แย้ง 3 ข้อ + ข้อมูลหลักฐานในเอกสาร 2) ฝ่ายค้าน (Negative): ข้อโต้แย้ง 3 ข้อ + ข้อมูลหลักฐานในเอกสาร 3) เกณฑ์การตัดสินจากความถูกต้องของหลักฐาน"
        },
        "prompt_template": "จากเอกสารทั้งหมด ช่วยตั้งญัตติโต้วาที 1 ญัตติ เรื่อง [หัวข้อ เช่น การใช้พลังงานนิวเคลียร์ในประเทศไทย / นโยบายสวัสดิการแห่งรัฐ] และสรุปคลังหลักฐานจากเอกสารแบ่งเป็น: ฝ่ายสนับสนุน 3 ประเด็น และ ฝ่ายคัดค้าน 3 ประเด็น พร้อมเลขหน้าอ้างอิง",
        "tips": "ช่วยฝึกทักษะการรู้เท่าทันข้อมูลและทักษะการอ้างอิงหลักฐานทางวิชาการ (Academic Referencing) ให้แก่นักเรียน",
        "source": "Evidence-Based Debate Architecture",
        "curated_top10": False
    },
    {
        "id": "nlm-media-glossary-cheat-sheet",
        "title": "NotebookLM: สร้างแผ่นพับพจนานุกรมคำศัพท์และนิยามทางการพร้อมหน้าอ้างอิง (Glossary Cheat Sheet)",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "คำศัพท์เฉพาะทาง", "Glossary", "แผ่นพับ", "สรุปคำศัพท์"],
        "role_context_condition": {
            "role": "คุณเป็นบรรณาธิการพจนานุกรมวิชาการเฉพาะสาขา",
            "context": "ฉันต้องการทำแผ่นสรุปคำศัพท์เฉพาะทาง 20 คำ พร้อมคำนิยามทางการที่ปรากฏในเอกสาร แจกนักเรียนก่อนสอบ",
            "condition": "สกัดคำศัพท์เชิงเทคนิค 20 คำ เรียงตามลำดับอักษร ก-ฮ หรือ A-Z: คำศัพท์, คำแปล, นิยามความหมายตามเอกสาร (อย่างกระชับ), ตัวอย่างประโยค/สูตร, และเลขหน้าในเอกสาร"
        },
        "prompt_template": "จากเอกสารที่ฉันอัปโหลด ช่วยสกัด 'พจนานุกรมคำศัพท์สำคัญ (Glossary)' จำนวน [20] คำ เรื่อง [หัวข้อ] เรียงตามลำดับตัวอักษร โดยระบุ: คำศัพท์ / คำนิยามสั้น 1-2 บรรทัด / ตัวอย่างบริบท / เลขหน้าอ้างอิง ทำเป็นตาราง Markdown ที่อ่านง่าย",
        "tips": "นำตารางคำศัพท์ไปจัดเลย์เอาต์แผ่นพับ 3 ตอนใน Canva เพื่อเป็นคู่มือพกพาสำหรับนักเรียน",
        "source": "Academic Lexicon Curation Standards",
        "curated_top10": False
    },
    {
        "id": "nlm-media-canva-visual-prompt-ideas",
        "title": "NotebookLM: สกัดไอเดียภาพประกอบและคีย์เวิร์ดค้นหาใน Canva จากคำอธิบายในเอกสาร",
        "category": {
            "subject": "ทุกวิชา/ทั่วไป",
            "task_type": "สร้างสื่อ & ภาพประกอบ"
        },
        "tools": ["NotebookLM", "Canva"],
        "tags": ["NotebookLM", "Canva Prompts", "ไอเดียภาพประกอบ", "คีย์เวิร์ด Canva", "สื่อการสอน"],
        "role_context_condition": {
            "role": "คุณเป็น Visual Metaphor Specialist และผู้เชี่ยวชาญการค้นหาสื่อใน Canva",
            "context": "ฉันต้องการหารูปภาพประกอบหรือภาพกราฟิกใน Canva ที่สื่อถึงเนื้อหานามธรรมในเอกสาร",
            "condition": "จากเนื้อหาในเอกสารเรื่อง [หัวข้อ] ช่วยวิเคราะห์และเสนอไอเดียภาพเชิงเปรียบเทียบ (Visual Metaphors) 6 ไอเดีย พร้อมระบุ: 1. มโนทัศน์ที่ต้องการสื่อ 2. คำอธิบายภาพที่ควรใช้ 3. คีย์เวิร์ดภาษาอังกฤษสำหรับค้นหา Element / Photo ใน Canva"
        },
        "prompt_template": "จากเอกสารที่อัปโหลด ช่วยเสนอ 'ไอเดียภาพประกอบและคีย์เวิร์ดค้นหาใน Canva' สำหรับเรื่อง [หัวข้อ เช่น โครงสร้างอะตอม / ห่วงโซ่อาหาร] จำนวน 6 ไอเดีย โดยระบุ: มโนทัศน์ / ภาพเปรียบเทียบที่แนะนำ / คำค้นหาภาษาอังกฤษใน Canva",
        "tips": "ช่วยให้ครูค้นหาภาพใน Canva ได้ตรงจุด ไม่เสียเวลาค้นหาคำศัพท์ภาษาอังกฤษด้วยตนเอง",
        "source": "NotebookLM to Canva Visual Search Bridge",
        "curated_top10": False
    }
]

master_path = '/home/kitti/Projects/Activities-me/ai-training-school/site/prompts-data.json'
with open(master_path, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

existing_ids = {p['id'] for p in master_data}
added = 0

for p in nlm_media_prompts:
    if p['id'] in existing_ids:
        print(f"Warning: duplicate {p['id']}, skipping...")
    else:
        master_data.append(p)
        existing_ids.add(p['id'])
        added += 1

print(f"Added {added} specialized NotebookLM media prompts. Master total now: {len(master_data)}")

with open(master_path, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {master_path} ({os.path.getsize(master_path)} bytes)")
