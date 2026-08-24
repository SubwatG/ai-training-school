# Parent Cross-Check Notes — Image Prompts Research

## Base facts ที่ Hermes หาเอง (สำหรับ cross-check subagents)

### Official Google: Nano Banana Pro (blog.google, 20 พ.ย. 2025)
- URL: https://blog.google/innovation-and-ai/products/nano-banana-pro/
- Nano Banana Pro = **Gemini 3 Pro Image** จาก Google DeepMind; Nano Banana เดิม = Gemini 2.5 Flash Image
- ขายจุดหลัก: text rendering ถูกต้องหลายภาษา, infographics, แปลงโน้ตมือเขียนเป็น diagram, Search grounding (real-time weather/sports), SynthID watermark
- Prompt ตัวอย่างในบทความ (official):
  - "Create an infographic about this plant focusing on interesting information." (plant infographic)
  - "Create an infographic that shows how to make elaichi chai" (step-by-step recipe infographic)
- ลิงก์ prompting tips official: https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/
- Storyboard prompt: "Create a storyboard for this scene" (4 panels)
- Text-in-image prompt: คำว่า BERLIN เป็นตัวอาคาร; "make 8 minimalistic logos..." (expressive typography)
- Translate prompt: "translate all the English text on the three yellow and blue cans into Korean, while keeping everything else the same" ← รูปแบบ edit-preserve ที่ดีมาก

### Official Google (dev.to/googleai): Nano Banana Pro Prompting Guide & Strategies
- URL: https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n
- Golden Rules: (1) Edit don't re-roll (2) Natural language full sentences ไม่ใช่ tag soup (3) Specific+descriptive (subject/materiality) (4) Provide context "why / for whom"
- ตัวอย่าง prompts ตรงธีมเรา:
  - Earnings infographic: "Generate a clean, modern infographic summarizing the key financial highlights from this earnings report. Include charts for 'Revenue Growth' and 'Net Income'..."
  - Retro infographic: "Make a retro, 1950s-style infographic about the history of the American diner. Include distinct sections for 'The Food,' 'The Jukebox,' and 'The Decor.' Ensure all text is legible..."
  - Technical diagram: "Create an orthographic blueprint that describes this building in plan, elevation, and section. Label the 'North Elevation' and 'Main Entrance' clearly... Format 16:9."
  - Whiteboard summary (educational!): "Summarize the concept of 'Transformer Neural Network Architecture' as a hand-drawn whiteboard diagram suitable for a university lecture. Use different colored markers for Encoder and Decoder blocks..."
  - Viral thumbnail w/ identity lock: "Design a viral video thumbnail using the person from Image 1. Face Consistency: Keep the person's facial features exactly the same as Image 1..." (+14 reference images, 6 high fidelity)
- Full text saved: ~/.hermes/profiles/teaching-orchestrated/cache/web/dev.to-1bff616e03.md

### OpenAI: GPT-4o native image generation (openai.com, 25 มี.ค. 2025)
- URL: https://openai.com/index/introducing-4o-image-generation/
- จุดเด่น: accurate text rendering, precise instruction following, multi-turn conversational editing, chat context awareness
- Prompt Engineering Guide มี guide เฉพาะ: https://www.promptingguide.ai/guides/4o-image-generation

### Third-party guides ที่น่าเชื่อ
- Leonardo.ai Nano Banana Prompt Guide: https://leonardo.ai/news/nano-banana-prompt-guide/
  - Infographic layout tips: S-curve/zigzag pattern สำหรับ step-by-step, Bento grid สำหรับ modular overview, white space + 3-level text hierarchy, sequential palette สำหรับ magnitude
  - ตัวอย่าง S-curve prompt: "Create a professional process infographic showing 'How to Brew the Perfect Espresso.' Use an S-curve pattern to guide the eye from the top-left to the bottom-right. Include five steps, each with a small icon and a short label. Style the image with a 'Mocha Mousse' warm neutral palette for a high-end feel."
- Dr Philippa Hardman (Substack) "How to Use Nano Banana to Actually Support Learning": https://drphilippahardman.substack.com/p/beyond-infographics-how-to-use-nano
  - 6 use cases เชิง pedagogy: Visualisation, Analogy ("generate a side-by-side diagram explaining X using the analogy of Y"), ... Generation (intentionally incomplete diagrams ให้ learner เติม — "create an unlabelled or partially revealed diagram of X that requires learners to generate missing steps or labels")

### Official Google: "7 tips to get the most out of Nano Banana Pro" (blog.google, 20 พ.ย. 2025)
- URL: https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/
- Prompt anatomy official: **Subject / Composition / Action / Location / Style / Editing Instructions** + advanced: aspect ratio ("A 9:16 vertical poster"), camera+lighting ("Golden hour backlighting creating long shadows"), text integration ("The headline 'URBAN EXPLORER' rendered in bold, white, sans-serif font at the top"), factual constraints สำหรับ diagram ("A scientifically accurate cross-section diagram", "Ensure historical accuracy for the Victorian era")
- Input ได้สูงสุด 14 images per composition

### แหล่งไทย: MarketingOops (พ.ย. 2025) — Nano Banana Pro เจนภาพโฆษณา text ไทยไม่เพี้ยน
- URL: https://www.marketingoops.com/how-to-4/nano-banana-pro-gemini-how-to/
- Prompt ไทยเต็ม (verbatim) — product poster จากรูปถ่ายจริง:
  "สร้างโปสเตอร์โฆษณาสวยๆ ให้กับผลิตภัณฑ์ "น้ำปลาแท้ตราทิพรส" / องค์ประกอบภาพ: ขวดน้ำปลาทิพรสวางเด่นอยู่บนโต๊ะอาหารไม้สีเข้ม จัดแสงแบบ Cinematic Warm Light... / การวางข้อความ: ด้านบนใช้ฟอนต์ภาษาไทยแบบมีหัว ตัวหนา เขียนว่า "น้ำปลาแท้ตราทิพรส" ด้านล่างมีคำโปรยตัวเล็กกว่า "รสไทยแท้ คู่ครัวไทย" ขอให้ตัวสะกดภาษาไทยถูกต้องและอ่านง่าย"
- Pattern: Context + Text ในเครื่องหมายคำพูด + ระบุฟอนต์ไทย (แบบมีหัว/loopless) + สั่ง "ตัวสะกดถูกต้อง"
- แหล่งไทยอื่น seed: flowaccount.com/blog/how-to-create-image-by-using-gemini-ai/ (70 prompts), YouTube "แจกสูตรสร้างภาพด้วย Google Gemini ... Nano Banana Pro" (#สื่อการสอนครู), gemini.google/th image-generation page

## USER STEERING (2026-08-23 ระหว่างทำงาน)
- **ChatGPT Image: เน้นของใหม่ปี 2025 → ปัจจุบัน (ส.ค. 2026)** — ไม่ใช่แค่กระแส launch มี.ค. 2025; ให้ประเมิน timeline update ล่าสุดด้วย
- ทุก entry ต้องมีวันที่โพสต์ชัดเจน

## TODO หลัง subagents กลับ
- [ ] ตรวจว่า international-en.md มี prompts ซ้ำกับ official examples ไหม (ถ้าซ้ำ ให้ mark เป็น "official example" ไม่ใช่ community)
- [ ] ตรวจ thailand-th.md ว่า viral trends (3D figurine ฯลฯ) ผูกกับ educational angle จริง
- [ ] ตรวจ github-official.md ว่า repos จริง + stars + README prompts verbatim
- [ ] ตรวจ use-case-workflows.md ว่า workflow 8+ อัน แต่ละอันมี prompts ครบ + URL
- [ ] QA: leftover markers, unclosed quotes in prompt blocks, source counts per file
- [ ] สังเคราะห์ 00-README.md master index + dedupe across files
