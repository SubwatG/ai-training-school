---
topic: "Use-Case Deep-Dives: End-to-End Image-Gen Workflows (Nano Banana/Gemini Image + ChatGPT Image)"
date: "2026-08-23"
model: "Gemini 2.5 Flash Image (Nano Banana) / Gemini 3 Pro Image (Nano Banana Pro) / GPT-4o Image & GPT Image 2 (ChatGPT Image)"
provider: "Google / OpenAI"
sources_count: 13
---

# Use-Case Deep-Dives: Workflows ที่รวมหลาย Image Prompt เป็นกระบวนการครบจบ

> เน้น **workflow end-to-end** ที่ผู้ใช้จริงบันทึกไว้ (blog/โพสต์/วิดีโอ) ว่าเอา prompt หลายตัวมาต่อกันเป็นกระบวนการ เช่น ทำใบงานทั้งชุดด้วยตัวละครเดียวกัน, ทำชุดโปสเตอร์, ทำ infographic pipeline, ทำ flashcard ชุดเดียวกันทั้งกอง
> ทุก prompt ต้องเป็นคำพูดจริงจากแหล่ง (verbatim) + URL + วันที่

## วิธีอ่านไฟล์นี้
- แต่ละ "Workflow" = กระบวนการหลายขั้น (multiple prompts) ที่คนจริงใช้และบันทึกขั้นตอนไว้
- Prompt ยกมา verbatim (ภาษาอังกฤษคงเดิม, แนบคำแปลไทยสั้น) / ถ้าภาษาไทยคงเดิม (แนบ EN gloss)
- Dedupe note: หลีกเลี่ยงคอนเซปต์ใน `existing-concepts-dedupe.md` (คอนเซปต์ใบงาน/แฟลชการ์ด/อินโฟกราฟิกของตัวเองในโปรเจกต์)

---

## 1. 6 กลยุทธ์การเรียนรู้จากงานวิจัย → สร้างสื่อภาพด้วย Nano Banana — education/summary/steps
- **แหล่ง:** https://drphilippahardman.substack.com/p/beyond-infographics-how-to-use-nano (Substack, 4 ธ.ค. 2025)
- **บริบท:** Dr Philippa Hardman (นักวิทยาศาสตร์การเรียนรู้, 31k+ subscribers) แสดงวิธีใช้ Nano Banana (Gemini app) เปลี่ยน "image generation → instructional scaffolding" ด้วย 6 กลยุทธ์อิงงานวิจัย: Visualisation, Analogy, Worked Examples, Contrasting Cases, Elaboration, Generation เธอใช้ input หลายแบบ (process notes, course storyboard, scenario brief, module outline, วิดีโอ) ป้อนเข้ารูปภาพ แล้วสั่งให้เจนภาพต่อเนื่อง เช่น แผนภาพจากวิดีโอ "How a Bill Becomes Law", worked example 5 ขั้นจากวิดีโอผูกเงื่อน Bowline knot (ภาพในโพสต์)
- **Prompt (EN) ตามตัวอักษร (ยกมา 3 จาก 6 ตัวอย่าง):**
  - Visualization: *"Using these process notes and workflow screenshots, generate a structured visualisation (flowchart, swim lane map, or system diagram) that clarifies relationships, dependencies, and sequencing."*
  - Analogy: *"Using the relevant parts of this course storyboard, generate a side-by-side diagram explaining X using the analogy of Y. Ensure each element of X maps clearly to its counterpart in Y. Maintain consistent colour coding and aligned spatial structure to emphasise the shared deep principle. Never use the work "analogy" in the image."* (แปลไทย: ใช้ storyboard ของคอร์ส สร้างแผนภาพ side-by-side อธิบาย X ด้วยอุปมาอุปไมย Y ให้แต่ละส่วนของ X สัมพันธ์กับ Y สีและโครงสร้างคงที่ ห้ามใช้คำว่า "analogy" ในภาพ)
  - Worked Examples: *"Using the relevant parts of this course storyboard, create a 5-step visual worked example illustrating the solution process. Ensure each step highlights key information, with consistent visual scaffolding that fades in later steps."* (แปล: สร้างตัวอย่างเฉลย 5 ขั้น พร้อม scaffolding ที่จางหายในขั้นหลัง)
- **Tool:** Nano Banana (Gemini)
- **Takeaway สำหรับครู:** เทคนิค "ล็อกโครงสร้าง/สี/ตัวละครคงที่ แล้วเปลี่ยนเฉพาะตัวแปร" และ "สร้างภาพเวอร์ชัน incomplete ให้เด็กเติม" (Generation strategy) ใช้ทำใบงานแบบ gap-fill ได้จริง — prompt ตัวเต็ม 6 อันอยู่ในโพสต์

## 2. ซีรีส์ภาพ scenario ตัวละคร 2 คน (นักศึกษา-อาจารย์) ด้วย ChatGPT Image + Midjourney — other/scenario (role-play)
- **แหล่ง:** https://christytuckerlearning.com/frustrations-with-chatgpt-image-generation/ (Experiencing eLearning blog, พ.ค. 2025)
- **บริบท:** Christy Tucker (instructional designer) ต้องสร้างชุดภาพ scenario 2 ตัวละคร (นักศึกษาป.โท + อาจารย์ คุยกันในห้องประชุม) สำหรับ eLearning เธอบันทึก workflow เต็ม: เจนตัวละครเดี่ยว → เจนท่าทางคุย → เพิ่มตัวละครที่ 2 → แก้ตำแหน่ง → ใช้สเก็ตช์เป็น reference guide ผลลัพธ์: ChatGPT ตัวละครเพี้ยนเมื่อแก้หลายรอบ มีเทคนิคที่เวิร์กคือ "ร่างสเก็ตช์ layout แล้วอัปโหลดเป็น guide"
- **Prompt (EN) ตามตัวอักษร:**
  - แก้ตำแหน่ง: *"Change where they're sitting so they are on opposite sides of the table, directly facing each other, with more space between them. They should not be at the corner of the table like this. Make the image aspect ratio 16×9."*
  - ใช้สเก็ตช์: *"That's not quite right. I want the characters to be viewed from a profile view instead of a 3/4 view. The table should be between them, and they are sitting across from each other on opposite sides of the table. See this attached image for the layout. Use this sketch as a guide, and keep the realistic characters but rotate them to a profile view."*
  - (ในคอมเมนต์) รวมสองตัวละครจาก Midjourney: *"Create an image: A scene with the characters in these attached images. The characters are in a meeting in a library conference room. The woman is talking and explaining something. The man is listening to her, sitting across from her at a table. Keep the characters consistent, including their clothes, hair, and glasses. Aspect ratio 16:9"*
- **Tool:** ChatGPT Image เป็นหลัก + Midjourney (สร้าง base character) — workflow "หลายเครื่องมือต่อกัน"
- **Takeaway:** การใช้ reference image (สเก็ตช์/ภาพตัวละคร) ช่วยคุม layout มากกว่าพิมพ์อธิบายอย่างเดียว — ตรงกับบทเรียน "make one change at a time" เพื่อรักษา consistency

## 3. สร้างชุดสีหน้าอารมณ์ของตัวละครเดียวกันด้วย Nano Banana — education (character consistency)
- **แหล่ง:** https://christytuckerlearning.com/nano-banana-gemini-character-image-experiments/ (ต.ค. 2025)
- **บริบท:** Christy Tucker ทดสอบ Nano Banana สร้างภาพผู้หญิงคนเดิมหลายอิริยาบถ (ยิ้ม งง หงุดหงิด ฯลฯ) พบว่าต้อง "เตือน" ให้คงรายละเอียดทุกครั้ง และเมื่อภาพเริ่มเพี้ยนให้อัปโหลดภาพเดิมกลับเป็น reference
- **Prompt (EN) ตามตัวอักษร:** *"Keep the character details the same (hair, glasses, blouse, etc.) but change her expression to [a slight frown; a confused expression; a frustrated expression"]* (แปล: คงรายละเอียดตัวละครเดิม แต่เปลี่ยนสีหน้าเป็น...) และใน multi-scene: *"Use this as the reference image. Show this woman talking and gesturing with her hands. Keep the character and setting consistent"* (จากชื่อไฟล์ภาพในโพสต์)
- **Tool:** Nano Banana (Gemini)
- **Takeaway:** Nano Banana คงตัวละครได้ดีกว่า ChatGPT ในซีรีส์เดียวกัน แต่ต้องใส่คำว่า "keep ... the same" ทุก prompt และใช้ reference image เมื่อเกิด drift

## 4. ทดสอบ 10 Prompt เดียวกันบน Nano Banana 2 vs GPT Image 2 (ตัวละคร/คุกบุ๊กขั้นตอน/แบรนด์/คาโรเซลเพื่อการศึกษา/ฟิสิกส์ atlas) — education/promotion/steps
- **แหล่ง:** https://aiblewmymind.substack.com/p/nano-banana-2-vs-gpt-images-2 (Substack "AI blew my mind", Daria Cupareanu, 10 พ.ค. 2026)
- **บริบท:** ผู้สร้างคอนเทนต์ป้อน prompt เดียวกัน 10 ชุดให้ทั้งสองโมเดลเปรียบเทียบ—รวมงานที่ครูใช้ได้: selfie → ภาพ collage 6 แพนเนลตัวละครเดิม, สูตรอาหาร blog → คู่มือคุกบุ๊กทีละขั้น, บทความ → Instagram carousel เพื่อการศึกษา 8 สไลด์, หน้า physics atlas, โปสเตอร์ infographic CPU ผล: GPT Image 2 เก่ง realistic/ตัวละครอ้างอิง, Nano Banana 2 เก่งสไตล์เรียบ minimal เหมาะตำราเรียน
- **Prompt (EN) ตามตัวอักษร (3 ตัวอย่าง):**
  - ตัวละครจาก selfie: *"Use amplifiers to create a high-end portrait collage using a headshot I will upload as the identity reference. Maintain strong character consistency across all variations. The person must remain clearly recognizable in every frame with the same facial structure, skin tone, eye shape, hairstyle, and overall identity. Generate a cinematic multi-panel collage featuring the same person wearing different professional and modern headsets across multiple scenes and moods. Include a mix of: sleek corporate LinkedIn-style portraits, cinematic studio lighting, podcast/interview setup, Netflix character poster, dark moody cyberpunk lighting, Wired magazine portrait photography."*
  - สูตร → คุกบุ๊กขั้นตอน: *"Use Amplifiers to turn this recipe: https://iamafoodblog.com/fluffy-japanese-pancakes-souffle-pancake-recipe/ into a premium cookbook-style step-by-step visual guide for fluffy Japanese pancakes. Include elegant food photography, ingredient callouts, numbered cooking steps, clean editorial layout, soft natural lighting, and realistic pancake textures throughout."*
  - บทความ → คาโรเซลเพื่อการศึกษา: *"Analyze this article I wrote: [URL] and use the Image Generation Amplifier to create an educational Instagram carousel. ... Make it practical, clear, beginner-friendly for non-technical people, and outcome oriented for business owners and execs. Include my branding naturally somewhere on each slide ... Format it as a polished Instagram carousel with multiple 4:5 slides, consistent layout, readable typography, and a final CTA slide..."* (ตัดกลาง—prompt เต็มในโพสต์)
- **Tool:** ทั้งคู่ (NB2 + GPT Images 2) ผ่าน Claude Amplifiers
- **Takeaway:** workflow "บทความ → ชุดสไลด์ภาพเพื่อการศึกษา" ใช้ได้จริง แต่ผู้ทดสอบพบว่าทั้งสองโมเดลยังทำ footer/เลขขั้นไม่ consistent — ต้องตรวจแก้เอง

## 5. Nano Banana 2 Education Prompt Library: ชุดบทเรียน 3 ตอนด้วยตัวละครนักวิทยาศาสตร์คนเดิม + ขั้นตอนล้างมือ — education/steps
- **แหล่ง:** https://www.vofy.art/blog/nano-banana-2-education-storytelling-prompts (Vofy blog, ~ส.ค. 2026)
- **บริบท:** บทความสอนครู/instructional designer ใช้ Nano Banana 2 สร้างสื่อการศึกษา มีโครงสร้าง prompt 5 ส่วน `[Learning objective] + [Subject/Scene] + [Visual style] + [Educational constraints] + [Output format]` และมี "ชุดบทเรียน 3 ตอน" ที่ตัวละครนักวิทยาศาสตร์หญิงคนเดิมปรากฏใน 3 บทเรียน รวมถึง sequence ขั้นตอนล้างมือทีละ Step
- **Prompt (EN) ตามตัวอักษร (ตัวอย่าง):**
  - ชุด 3 บทเรียน (ล็อกตัวละคร):
    - *"Create a friendly female scientist character, age 30s, wearing a white lab coat, brown hair in ponytail, warm smile, standing in a laboratory, holding a beaker, educational illustration style, bright colors, 4:5."*
    - *"Same female scientist character from previous image, same lab coat and hairstyle, now pointing at a periodic table on the wall, same illustration style and colors, laboratory setting, engaging teaching pose, 4:5."*
    - *"Same female scientist character, same appearance and clothing, now conducting an experiment with colorful liquids, same illustration style, laboratory background, excited expression, 4:5."*
  - ขั้นตอน: *"Step 1 of hand-washing tutorial, hands under running water, close-up view, clean medical illustration style, clear lighting, simple background, educational poster aesthetic, easy to understand, 1:1."*
  - ตัวละครครู: *"Create a friendly cartoon teacher character, warm smile, professional attire, standing in a modern classroom, approachable expression, consistent character design for series, bright educational illustration style, clean background, 4:5."* + *"Same teacher character from previous image, now pointing at a whiteboard with diagrams, same clothing and facial features, same illustration style, classroom setting, engaging teaching pose, 4:5."*
- **Tool:** Nano Banana 2 (Gemini)
- **วิธีล็อกตัวละคร (จากบทความ):** 1) ล็อก descriptor ใน prompt แรก (อายุ เสื้อผ้า ทรงผม สีหน้า) 2) อ้าง "Same character from previous image..." ใน prompt ถัดไป 3) คงตัวแปรไว้ 1 ตัว 4) เจนทั้งซีรีส์ในเซสชันเดียว

## 6. Comic Strip ที่ไม่มีฝีมือวาดรูป: วิเคราะห์สไตล์ → วางแผนแพนเนล → เจนด้วย ChatGPT — other/comic (g)
- **แหล่ง:** https://www.geekmum.com.au/creating-a-comic-strip-with-chatgpt/ (GeekMum blog, มิ.ย. 2025)
- **บริบท:** เจ้าของบล็อก (ปูพื้นหลังสาย IT/ศิลปะ) กลับมาวาดการ์ตูนอีกครั้งโดยใช้ ChatGPT สร้างคอมมิก 2 เรื่อง: 4-panel แบบสุ่ม และ 6-panel แบบวางแผนเอง (วิเคราะห์สไตล์จากคอมมิกที่ชื่นชอบ → วางแผนแต่ละแพนเนล: ฉาก/ตำแหน่งตัวละคร/บทพูด → ป้อนสคริปต์+สไตล์ให้ GPT-4o) ผล: ใช้เวลา <2 ชม. จากไอเดียถึงภาพเสร็จ แต่จุดอ่อนคือคุมการออกแบบแต่ละแพนเนลไม่ได้
- **Prompt (EN) ตามตัวอักษร:** *"create a four panel comic that you think I'd enjoy based on what you know about me"* (bandwagon comic) — ส่วน 6-panel ใช้สคริปต์ที่เขียนเอง + คำสั่งรายละเอียด layout/mood/tone (ไม่ได้เผยแพร่ full prompt)
- **Tool:** ChatGPT Image (GPT-4o)
- **Takeaway:** workflow วิเคราะห์สไตล์อ้างอิงก่อนเจน (ให้ ChatGPT แตกเป็น color palette/panel layout/styling/linework) ช่วยให้ prompt ที่ใช้ซ้ำได้ — ครูทำการ์ตูนอธิบายบทเรียนได้ด้วยวิธีเดียวกัน

## 7. การ์ตูน 4 แพนเนลอธิบายคอนเซปต์ใน 15 นาที (Medium) — other/comic (g)
- **แหล่ง:** https://medium.com/prompt-that-works/how-i-create-viral-comic-strips-in-15-minutes-with-chatgpt-no-drawing-skills-needed-e5c01c1672db (Medium "Prompt That Works", Santosh Shelar, 22 ธ.ค. 2025 — member-only บางส่วน)
- **บริบท:** นักพัฒนา/ครีเอเตอร์อธิบาย workflow: 1) เลือก "ไอเดียเดียว" ที่จะสื่อ (เช่น "Caching vs database" ใช้ได้, "ทุกอย่างเกี่ยวกับ backend performance" ไม่ได้) 2) เลือกรูปแบบ 3–5 แพนเนล โครงสร้าง Setup → Confusion/ความเข้าใจผิด → Explanation 3) ให้ ChatGPT สร้างการ์ตูน 4) ปรับบทพูดให้เป็นธรรมชาติ 5) ปรับแต่ง
- **Prompt (EN) ตามตัวอักษร (จากส่วนที่อ่านได้ + search snippet):** *"Create a 4-panel comic strip that explains [topic]"* → ต่อด้วย *"Rewrite the comic to sound more conversational and realistic"* → *"Adjust the comic so the..."* (เนื้อหาส่วน Prompt เต็มอยู่หลัง paywall ของ Medium)
- **Tool:** ChatGPT Image
- **Takeaway:** เริ่มจาก "หนึ่งคอนเซปต์ต่อการ์ตูน" และโครงสร้าง 3 จังหวะ — ใช้ได้กับวิชาที่ยาก (เช่น อัตราดอกเบี้ย vs ดอกเบี้ยทบต้น)

## 8. แฟลชการ์ดภาพ 12 ใบสไตล์เดียวกัน (MagicSchool AI) — education/flashcards (f)
- **แหล่ง:** https://www.facebook.com/magicschoolai/posts/998147983276346/ (Facebook post, วันที่ไม่มีบนหน้า — อ้างอิงจาก search snippet, เข้าถึง 23 ส.ค. 2026)
- **บริบท:** MagicSchool AI (แพลตฟอร์ม AI เพื่อครู) โพสต์แนะนำการสร้าง picture flashcards ที่ "จำได้ดีกว่าเมื่อคู่กับภาพ" พร้อม prompt ระบุสไตล์เดียวกัน ไฟสม่ำเสมอ พื้นหลังเรียบ ไม่มีตัวหนังสือ
- **Prompt (EN) ตามตัวอักษร:** *"Generate 12 picture flashcards for [TOPIC] (Grade [X]). Same style, consistent lighting, plain background, no words."* (แปล: สร้างแฟลชการ์ดภาพ 12 ใบเรื่อง [หัวข้อ] (ชั้น [X]) สไตล์เดียวกัน ไฟสม่ำเสมอ พื้นหลังเรียบ ไม่มีตัวหนังสือ)
- **Tool:** ChatGPT Image (โพสต์อ้างถึงครูที่ใช้ ChatGPT)
- **หมายเหตุ:** Facebook ไม่ให้ extract เนื้อหาเต็ม — prompt ข้างต้นมาจากข้อความที่ปรากฏใน search index

## 9. Knowledge Cards 24–30 ใบจาก PDF ตำราเรียน (pipeline ตำรา→การ์ด→สไลด์→MP4) — education/flashcards (f)
- **แหล่ง:** https://2slides.com/blog/ai-knowledge-cards-educators-classroom (2Slides blog, Sarah Choy, 3 พ.ค. 2026)
- **บริบท:** workflow เต็มสำหรับครู: อัปโหลด PDF ตำรา → เลือกรูปแบบการ์ด (definition/process/concept/vocabulary/timeline) → prompt คุมโครงสร้าง → เจน 24–60 การ์ด → add narration → export PPTX/PDF/MP4 ตัวอย่าง: ครูชีววิทยา ม.4 (US) ส่ง prompt 24 การ์ดเรื่อง cellular respiration ได้เด็ค 65 สไลด์ใน 22 นาที
- **Prompt (EN) ตามตัวอักษร:** *"Generate 24 knowledge cards from the attached chapter on cellular respiration for a US 10th-grade biology class. One card per concept. Each card: term, plain-English definition, real-world analogy, an exam-style multiple-choice question with answer hidden on a follow-up slide. Use diagrams, not photographs."* (แปล: สร้างการ์ดความรู้ 24 ใบจากบทที่แนบ หนึ่งใบต่อคอนเซปต์ แต่ละใบ: ศัพท์ + นิยามภาษาง่าย + อุปมาอุปไมย + ข้อสอบ MCQ ที่เฉลยอยู่สไลด์ถัดไป ใช้ diagram ไม่ใช้ภาพถ่าย)
- **Tool:** 2Slides (ใช้ Nano Banana สำหรับเจนภาพสไลด์) — pipeline หลายขั้น
- **Takeaway:** "one card per concept" + "template คือ prompt เอง" — เลือกแพตเทิร์นเดียวทั้งเด็ค = ความสม่ำเสมออัตโนมัติ

## 10. ครูไทย (เก๋ไก๋ไฮเทค): Nano Banana 2 สำหรับใบงาน/นิทานตัวละครเดิม/โจทย์ภาพ — education (TH)
- **แหล่ง:** https://inspirelearner.com/nanobanana2/ (Inspire Learner — จารุณี สินชัยโรจน์กุล, Google Certified Trainer, 2 มี.ค. 2026)
- **บริบท:** ครู/ที่ปรึกษาด้านพัฒนาครูแนะนำวิธีใช้ Nano Banana 2 (Gemini app + บัญชี Workspace for Education) กับ use cases ห้องเรียน: ใบงานที่มีตัวละครประจำห้อง, นิทานประกอบภาพที่ "ตัวเอกคนเดิมในทุกๆ หน้า (Character Consistency)" สำหรับปฐมวัย, โจทย์คณิต/อังกฤษจากภาพสถานการณ์, แผนผังความคิดจากบันทึกการสอน แนะนำ workflow: เขียนคำสั่ง → ระบุสไตล์/อัตราส่วน → สั่งเพิ่มข้อความในภาพ → แก้เฉพาะจุด
- **Prompt (TH) ตามตัวอักษร:**
  - *"สร้างภาพห้องเรียนในอนาคตที่มีหุ่นยนต์ช่วยสอน สไตล์ภาพวาดสีน้ำ อัตราส่วน 16:9"* (EN gloss: create a futuristic classroom with robot teaching assistant, watercolor style, 16:9)
  - เพิ่มข้อความในภาพ: *"พร้อมข้อความบนกระดานว่า 'Welcome to the Future'"* (EN: with text on the board saying "Welcome to the Future")
- **Tool:** Nano Banana 2 (Gemini)
- **จุดเด่นที่ครูไทยควรรู้ (จากบทความ):** คุมตัวละครได้สูงสุด 5 ตัวในงานเดียว, text rendering ภาษาไทยอ่านง่าย, ระบุ aspect ratio เอง

## 11. iT24Hrs: วิธีใช้ Nano Banana Pro ทำอินโฟกราฟิกภาษาไทย (workflow 6 ขั้น) — summary/infographic (TH)
- **แหล่ง:** https://it24hrs.com/2025/nano-banana-pro-upgrade-thai/ (iT24Hrs, พ.ย. 2025)
- **บริบท:** สื่อไทยแนะนำ workflow ทำอินโฟกราฟิกด้วย Nano Banana Pro (Gemini 3 Pro Image): 1) เปิด Gemini 2) เลือก "สร้างภาพ" 3) เลือกโมเดล "Thinking with 3 Pro" 4) ใส่ prompt ภาษาไทยพร้อมข้อมูล/สถิติ 5) ส่งแล้วรอ 6) ระบุสไตล์เพิ่ม เช่น อัตราส่วนภาพ ฟอนต์ โทนสี — เน้นว่าตอนนี้ text rendering ภาษาไทย "ตัวอักษรไม่เพี้ยน ไม่รวน"
- **Prompt fragments (TH) ตามตัวอักษร (คำสั่งระบุสไตล์):** *"ใช้ฟอนต์ภาษาไทยแบบโมเดิร์น Sans-Serif"* และ *"โทนสีน้ำเงิน (#0055FF) และสีเทาอ่อน"* — และเคล็ดลับจากบทความ: *"ออกแบบเป็นอินโฟกราฟิกแนว flat design"*
- **Tool:** Nano Banana Pro (Gemini)
- **Takeaway:** prompt ไทยสั่งได้เลย + ระบุ hex สี/ฟอนต์ไทยเพื่อคุมความสม่ำเสมอ; ตรวจทานภาษาไทยก่อน final (โมเดลยังผิดได้)

## 12. Pantip: เทรนด์เปลี่ยนรูป/ภาพวาดเป็น "ฟิกเกอร์" ด้วย Nano Banana (LMArena) — other (TH)
- **แหล่ง:** https://pantip.com/topic/43700584 (Pantip ห้อง AI, สมาชิก Vortex, 23–28 ส.ค. 2025)
- **บริบท:** กระทู้ไทยต้นๆ ยุค Nano Banana แรกเปิดตัว (gemini-2.5-flash-preview-image) สอน workflow ผ่าน LMArena: อัปโหลดภาพอ้างอิง → พิมพ์ prompt → สุ่มเจอ Nano Banana → ปรับรายละเอียดต่อ (เช่น เติมขาที่ขาดให้ฟิกเกอร์) มีตัวอย่าง prompt เปลี่ยนภาพวาดเป็นฟิกเกอร์ PVC ซึ่งเป็นเทรนด์โซเชียลช่วงนั้น
- **Prompt (EN) ตามตัวอักษร:**
  - *"Draw a prospective model of the character in the picture, commercialized as a 1/7 scale full body figure. Please make this image into a real-life figure photo."*
  - *"A realistic photo of the 1/7 scale figure from the picture, in a desk next to a keyboard and monitor. Make it look like an anime character figure."* (เครดิต @merunote จาก X)
  - *"Please turn this photo into a figure. Behind it, there should be a partially transparent plastic paper box with the character from this photo printed on it. In front of the box, on a round plastic base, place the figure version of the photo I gave you. I'd like the PVC material to be clearly represented. It would be even better if the background is indoors."*
  - *"Generate a photo of a girl cosplaying this illustration, with the background set at Comiket."*
- **Tool:** Nano Banana (ผ่าน LMArena — ตอนนั้นยังไม่เปิดตัวทางการ)
- **Takeaway:** ตัวอย่างการใช้ reference image + "เพิ่มรายละเอียดในภาพเดิม" (inpainting-style) ซึ่งเป็นพื้นฐานเดียวกับเทคนิคทำสื่อที่มีตัวละคร/มาสคอตประจำห้องเรียน

## 13. YouMind: Image-to-Prompt ขั้นตอน 3 ข้อเพื่อชุดภาพแบรนด์ consistent (ใช้ข้ามโมเดลได้) — promotion/brand (d)
- **แหล่ง:** https://youmind.com/blog/image-to-prompt-brand-consistency (YouMind blog, 16 มิ.ย. 2026)
- **บริบท:** workflow ระบบ "brand DNA": 1) เลือก anchor image ที่แทนสไตล์แบรนด์ 2) ใช้ Image-to-Prompt สกัดเป็น structured description (สี แสง medium องค์ประกอบ อารมณ์) 3) แยก "constant" (สี/แสง/พื้นผิว/องค์ประกอบ) ที่ล็อกไว้ กับ "variable" (หัวข้อในแต่ละภาพ) ที่เปลี่ยนได้ → นำ prompt ไปใช้ซ้ำทุก touchpoint (cover โซเชียล PPT) และใช้ข้ามเครื่องมือได้ (Nano Banana Pro, GPT Image 2, Midjourney, Stable Diffusion)
- **Prompt:** ไม่มี prompt ที่เผยแพร่โดยตรง — output ของขั้นตอนคือ "structured prompt text" ที่เครื่องมือสร้างให้
- **Tool:** YouMind Image-to-Prompt → ส่งต่อให้ Nano Banana Pro / GPT Image 2
- **Takeaway:** ใช้กับงานโรงเรียนได้ (ชุดโปสเตอร์งานกีฬาสี/นิทรรศการวิชาการด้วยธีมสี+สไตล์เดียวกัน) — ทางเลือกแทนการจดจำสไตล์ในหัว

---

## สรุปแพตเทิร์นที่ข้ามแหล่ง (สำหรับ facilitator)
1. **Consistency = ย้ำ descriptor ทุกครั้ง** ("Same character from previous image", "Keep the character details the same") + reference image คุม drift
2. **Pipeline ที่พบบ่อย:** เอกสาร/บทเรียน → สรุปโครงสร้าง → prompt ภาพชุดเดียวทั้งกอง (คาโรเซล/การ์ด/โปสเตอร์)
3. **"Template คือ prompt เอง"** — กำหนดหนึ่งแพตเทิร์น (definition card/4:5 slide/16:9 poster) แล้วเจนทั้งชุด
4. **ภาพ "กึ่งสมบูรณ์" (incomplete diagram)** ใช้ทำใบงานให้เด็กเติม — ตรงกับกลยุทธ์ Generation
5. **ไทย:** สั่งภาษาไทยได้ (Nano Banana Pro รองรับ) แต่ควรระบุฟอนต์/hex สี + ตรวจทานตัวสะกด

*หมายเหตุความน่าเชื่อถือ: ทุก prompt ข้างต้นยกมาจากหน้าต้นทางที่เปิดอ่านได้ (บันทึก full text ไว้ใน cache ของ Hermes) ยกเว้น #8 ที่อ้างจาก search snippet เนื่องจาก Facebook บล็อกการดึงเนื้อหา*