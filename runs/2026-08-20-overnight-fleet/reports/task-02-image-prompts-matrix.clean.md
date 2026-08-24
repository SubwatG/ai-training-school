┌─ Reasoning ──────────────────────────────────────────────────────────────────┐
Okay, let's tackle this task. The user wants a catalog of 20 prompts for K-12 educational illustrations across 8 Thai school subjects
. The prompts need to be in English, use specific styles, and have customizable slots.

First, I need to list the 8 subjects. Thai K-12 subjects usually include Thai, Math, Science, Social Studies, Thai History,
 Music, Art, and Physical Education. Maybe add one more like Technology or Language if needed.

Next, each subject should have 2.5 prompts on average. Since we need 20, 5 per subject would work. Wait, 
8 subjects times 5 is 40, which is too many. Wait, no, 20 divided by 8 is 2.5. Hmm, maybe some subjects get 2
, others 3. But the user specified exactly 20. Let me check: 8 subjects, 20 prompts. So maybe 
2.5 per subject, but since you can't split prompts, perhaps some subjects have 2, others 3. But the exact distribution isn
't specified, so I can distribute evenly as much as possible. Maybe some subjects have 2,
 others 3. But the main point is to cover all 8 subjects with 20 total.

Each prompt must be in English, no Thai text. The visual style should be flat vector or
 3D cute clay. Include bracketed slots for customization like [specific organ], [grade
 level visual style], [historical era]. 

For each subject, I need to create prompts that fit educational materials. For example, in Science
, topics like the human body, solar system. In Math, geometric shapes, arithmetic operations. In
 Thai History, different eras like Sukhothai, Ayutthaya. 

Each entry in the JSON should have id, subject_th (Thai name of subject), title_th (title
 in Thai), visual_style, prompt_en, and canva_layout_tip_th. The Canva layout tip should be in Thai for teachers to adjust
 in Canva.

I need to ensure that the brackets are placeholders for customization. For example
, in a Science prompt, maybe [specific organ] for anatomy. In History, [historical
 era] to specify which period.

Also, the visual style needs to be consistent. Flat vector or 3D cute clay. Maybe alternate between the
 two styles across prompts.

Let me start listing possible subjects and prompts:

1. Thai Language: Alphabet, sentence structure. Prompts could be [letter shapes], [grade level], [cultural
 symbols].
2. Math: Operations, geometry. [math operation], [grade level style], [example numbers].
3. Science: Biology (cells, organs), Physics (forces), Earth Science.
4. Social Studies: Map reading, government. [interactive element], [grade level],
 [region].
5. Thai History: Historical figures, eras. [historical figure], [era], [artifact].
6. Music: Instruments, notation. [musical instrument], [style], [cultural context].
7. Art: Drawing techniques, famous artists. [art style], [grade level], [medium].
8. Physical Education: Sports, exercise. [sport activity], [grade level], [equipment].

Now, creating 2-3 prompts per subject. Need to ensure 20 total. Let me count:

Thai: 3 prompts
Math: 3
Science: 4
Social Studies: 3
Thai History: 2
Music: 2
Art: 2
PE: 1
Total: 20. That works.

For each prompt, include the bracketed slots. Also, make sure the prompts are clear and specific enough for AI generation.
 Use terms suitable for educational materials.

Visual style: alternate between flat vector and 3D cute clay. Maybe group by style or mix them.

Canva layout tips should guide teachers on how to arrange elements in Canva, in Thai. For example
, "Place the main element in the center with [grade level visual style] borders."

Need to structure all this into JSON with the required keys. Each entry with id (1-20),
 subject in Thai, title in Thai, visual style, prompt in English with brackets, and Canva
 tip in Thai.

Possible challenges: Ensuring that the brackets are appropriately placed for customization, covering
 all 8 subjects, and meeting the 20 total. Also, maintaining English for prompts and
 Thai for titles and layout tips.

I'll start drafting each entry, making sure to vary the subjects and styles, and include the necessary customization slots
.
Okay, let's tackle this task. The user wants a catalog of 20 prompts for K-12 educational illustrations across 8 Thai school subjects. The prompts need to be in English, use specific styles, and have customizable slots.

First, I need to list the 8 subjects. Thai K-12 subjects usually include Thai, Math, Science, Social Studies, Thai History, Music, Art, and Physical Education. Maybe add one more like Technology or Language if needed.

Next, each subject should have 2.5 prompts on average. Since we need 20, 5 per subject would work. Wait, 8 subjects times 5 is 40, which is too many. Wait, no, 20 divided by 8 is 2.5. Hmm, maybe some subjects get 2, others 3. But the user specified exactly 20. Let me check: 8 subjects, 20 prompts. So maybe 2.5 per subject, but since you can't split prompts, perhaps some subjects have 2, others 3. But the exact distribution isn't specified, so I can distribute evenly as much as possible. Maybe some subjects have 2, others 3. But the main point is to cover all 8 subjects with 20 total.

Each prompt must be in English, no Thai text. The visual style should be flat vector or 3D cute clay. Include bracketed slots for customization like [specific organ], [grade level visual style], [historical era]. 

For each subject, I need to create prompts that fit educational materials. For example, in Science, topics like the human body, solar system. In Math, geometric shapes, arithmetic operations. In Thai History, different eras like Sukhothai, Ayutthaya. 

Each entry in the JSON should have id, subject_th (Thai name of subject), title_th (title in Thai), visual_style, prompt_en, and canva_layout_tip_th. The Canva layout tip should be in Thai for teachers to adjust in Canva.

I need to ensure that the brackets are placeholders for customization. For example, in a Science prompt, maybe [specific organ] for anatomy. In History, [historical era] to specify which period.

Also, the visual style needs to be consistent. Flat vector or 3D cute clay. Maybe alternate between the two styles across prompts.

Let me start listing possible subjects and prompts:

1. Thai Language: Alphabet, sentence structure. Prompts could be [letter shapes], [grade level], [cultural symbols].
2. Math: Operations, geometry. [math operation], [grade level style], [example numbers].
3. Science: Biology (cells, organs), Physics (forces), Earth Science.
4. Social Studies: Map reading, government. [interactive element], [grade level], [region].
5. Thai History: Historical figures, eras. [historical figure], [era], [artifact].
6. Music: Instruments, notation. [musical instrument], [style], [cultural context].
7. Art: Drawing techniques, famous artists. [art style], [grade level], [medium].
8. Physical Education: Sports, exercise. [sport activity], [grade level], [equipment].

Now, creating 2-3 prompts per subject. Need to ensure 20 total. Let me count:

Thai: 3 prompts
Math: 3
Science: 4
Social Studies: 3
Thai History: 2
Music: 2
Art: 2
PE: 1
Total: 20. That works.

For each prompt, include the bracketed slots. Also, make sure the prompts are clear and specific enough for AI generation. Use terms suitable for educational materials.

Visual style: alternate between flat vector and 3D cute clay. Maybe group by style or mix them.

Canva layout tips should guide teachers on how to arrange elements in Canva, in Thai. For example, "Place the main element in the center with [grade level visual style] borders."

Need to structure all this into JSON with the required keys. Each entry with id (1-20), subject in Thai, title in Thai, visual style, prompt in English with brackets, and Canva tip in Thai.

Possible challenges: Ensuring that the brackets are appropriately placed for customization, covering all 8 subjects, and meeting the 20 total. Also, maintaining English for prompts and Thai for titles and layout tips.

I'll start drafting each entry, making sure to vary the subjects and styles, and include the necessary customization slots.
I got an image output, but this is an image generation result. I need to create a
 text catalog of prompts, not actual images. The user wants a structured JSON list
 of 20 prompts for educational illustrations.

Let me create this manually based on the requirements:
1. 20 high-quality text-to-image prompts for K-12
2. For 8 Thai school subjects
3. English only prompts (no Thai text in visual descriptions)
4. Clean flat vector or 3D cute clay style
5. Include bracketed slots for customization
6. Format as JSON with specific keys
7. Add Canva layout tips for Thai teachers

Let me create the 20 prompts systematically across 8 subjects (about 2-3 per subject
).I got an image output, but this is an image generation result. I need to create a text catalog of prompts, not actual images. The user wants a structured JSON list of 20 prompts for educational illustrations.

Let me create this manually based on the requirements:
1. 20 high-quality text-to-image prompts for K-12
2. For 8 Thai school subjects
3. English only prompts (no Thai text in visual descriptions)
4. Clean flat vector or 3D cute clay style
5. Include bracketed slots for customization
6. Format as JSON with specific keys
7. Add Canva layout tips for Thai teachers

Let me create the 20 prompts systematically across 8 subjects (about 2-3 per subject).
Based on your requirements, I'll create a comprehensive catalog of 20 educational illustration prompts for K-12 Thai schools. Here's the structured JSON list:

```json
{
  "prompts": [
    {
      "id": "sci-001",
      "subject_th": "วิทยาศาสตร์ - ชีวะ",
      "title_th": "ระบบทางเดินหายใจของมนุษย์",
      "visual_style": "flat_vector",
      "prompt_en": "Illustration showing [specific organ] of human respiratory system, [grade level visual style] design, clean labels, blue and gray color scheme, medical diagram style, isolated on white background, educational worksheet illustration, simple vector art",
      "canva_layout_tip_th": "แยกส่วนต่างๆ ไว้ในสไลด์เดียวกัน เพิ่ม Thai text overlay ที่ด้านบนสำหรับ 'หลอดลม' และด้านล่างสำหรับ ' alveoli'"
    },
    {
      "id": "sci-002",
      "subject_th": "วิทยาศาสตร์ - พลังงาน",
      "title_th": "สาวงล้าพลังแสงอาทิตย์",
      "visual_style": "3d_cute_clay",
      "prompt_en": "3D cute clay style solar panel showing [historical era] design elements, bright yellow panels, orange highlights, blue electrical connections, [grade level visual style] simplicity, toy-like appearance, flat clean background, educational toys aesthetic",
      "canva_layout_tip_th": "ใช้พื้นที่ว่างทางด้านขวาใส Thai text แนะนำ 'ประหยัดไฟ' และ 'โลกน่าอยู่'"
    },
    {
      "id": "math-003",
      "subject_th": "คณิตศาสตร์ - เรขาคณิต",
      "title_th": "รูปทรงหลาย-sided แบบผสมผสาน",
      "visual_style": "flat_vector",
      "prompt_en": "Colorful geometric shapes puzzle with [grade level visual style] triangles, squares, pentagons interlocking, bright primary colors, simple clean lines, educational diagram, worksheet-style illustration, white background",
      "canva_layout_tip_th": "จัดเรียงในแนวตั้งเพื่อแนะแนว 'ลำดับการนับมุม' Thai text ด้านบนและ 'ปริภูมิลัพธ์' ด้านล่าง"
    },
    {
      "id": "his-004",
      "subject_th": "ประวัติศาสตร์ - ชาติ",
      "title_th": "ปราสาทอยุธยาสมมุติ",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Adorable clay-style model of ancient Thai temple architecture, [historical era] roof style, multiple tiered roofs, cream and gold coloring, decorative patterns, [grade level visual style] educational toy scale, museum display aesthetic",
      "canva_layout_tip_th": "แสดงพร้อมกัน 3 ภาพในสไลด์ เพิ่มข้อความไทยเหนือแต่ละภาพ: 'ก่อตั้งปี 1431', 'ทรงพระเจริญ', 'มรดกโลก'"
    },
    {
      "id": "eng-005",
      "subject_th": "ภาษาต่างประเทศ - อ่าน",
      "title_th": "หนังสือนิยายภาพสำหรับเด็ก�BEGINNER",
      "visual_style": "flat_vector",
      "prompt_en": "Friendly cartoon character reading book, bright smiling expression, simple line art, [grade level visual style] soft pastel colors, cozy library setting elements, clean educational illustration, horizontal layout design",
      "canva_layout_tip_th": "ใส่กรอบรอบรูปภาพ เพิ่มข้อความไทยเหนือภาพ 'มาอ่านกัน!' และด้านล่าง 'พัฒนาทักษะ'"
    },
    {
      "id": "soc-006",
      "subject_th": "สังคมศึกษา - ครอบครัว",
      "title_th": "คุณค่าทางวัฒนธรรมในครอบครัว",
      "visual_style": "3d_cute_clay",
      "prompt_en": "3D clay family scene with diverse members working together, colorful traditional clothing, warm home environment, [grade level visual style] cute rounded shapes, soft natural lighting, inclusive representation, educational illustration",
      "canva_layout_tip_th": "เรียงลำดับรูปภาพจากซ้ายไปขวาแสดง 'พ่อ', 'แม่', 'ลูก' เพิ่มคำอธิบายไทยด้านล่างสำหรับแต่ละคน"
    },
    {
      "id": "art-007",
      "subject_th": "ศิลปะ - สีสัน",
      "title_th": "การผสมผสานของสี",
      "visual_style": "flat_vector",
      "prompt_en": "Color wheel illustration with rainbow gradient, bold primary colors, [grade level visual style] simple geometric arrangement, clean typography areas, educational color theory chart, bright vibrant design, circular layout",
      "canva_layout_tip_th": "ใช้สไลด์พื้นหลังแบบสี่เหลี่ยมจตุรัส, ใส่คำอธิบายไทยว่า 'สีแดง = พลังงาน' ทางซ้าย, 'น้ำเงิน = สงบ' ทางขวา"
    },
    {
      "id": "pe-008",
      "subject_th": "พลศึกษา - กีฬา",
      "title_th": "การละเล่นพื้นบ้านแบบร่วมสมัย",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Cute clay depiction of traditional Thai children sports activities, colorful team games, active playful poses, [grade level visual style] dynamic motion lines, bright athletic wear, educational physical education illustration",
      "canva_layout_tip_th": "เรียง 3 รูปภาพพร้อมกันแสดงกิจกรรมต่างๆ, เพิ่มข้อความไทยเหนือภาพสำหรับ 'กีฬา', 'ความเร็ว', 'ความสามัคคี'"
    },
    {
      "id": "sci-009",
      "subject_th": "วิทยาศาสตร์ - ปรากฏการณ์",
      "title_th": "วัฏจักรของน้ำที่น่าทึ่ง",
      "visual_style": "flat_vector",
      "prompt_en": "Clean infographic showing water cycle stages: evaporation, clouds formation, rainfall, collection, [grade level visual style] simple icon-style illustrations, blue and white color scheme, educational diagram, circular flow layout",
      "canva_layout_tip_th": "ใช้กราฟโฟลว์แบบแนวตั้งจาก 'พื้นดิน' ถึงกลับ 'พื้นดิน' เพิ่มคำอธิบายไทยระหว่างขั้นตอน"
    },
    {
      "id": "math-010",
      "subject_th": "คณิตศาสตร์ - เลขจำนวน",
      "title_th": "แนวคิดเรื่องบวกและลบ",
      "visual_style": "3d_cute_clay",
      "prompt_en": "3D clay apples and oranges showing addition (+), rotten apples showing subtraction (-), colorful fruit illustration, [grade level visual style] cute rounded shapes, simple math operations visual, educational counting aid",
      "canva_layout_tip_th": "แสดงภาพผลไม้ 2-3 ชนิดในแนวราบ, เพิ่มสัญลักษณ์ไทย '+' และ '-' สีสดใสสำหรับคะแนน"
    },
    {
      "id": "his-011",
      "subject_th": "ประวัติศาสตร์ - พระมหากษัตริย์",
      "title_th": "พระบรมฉายาลักษณ์ในหลวงรัชกาลที่ 9",
      "visual_style": "flat_vector",
      "prompt_en": "Elegant simplified portrait of King Bhumibol Adulyadej in traditional Thai royal attire, [historical era] characteristics, warm brown skin tone, royal crown details, [grade level visual style] clean educational illustration, respectful composition",
      "canva_layout_tip_th": "วางตัวอักษรไทย 'ในหลวงทรงเป็นแบบอย่างที่ดี' ใต้ภาพพร้อมไอคอนปลาน้ำจืด"
    },
    {
      "id": "lit-012",
      "subject_th": "วรรณกรรม - เรื่องสั้น",
      "title_th": "บ้านหลังกระทิงกรรไกรในป่า",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Charming clay illustration of wooden scissors house in forest setting, smiling rabbit character, colorful trees, [grade level visual style] simple shapes, warm natural lighting, storybook illustration aesthetic",
      "canva_layout_tip_th": "ใช้การเล่าเรื่องแบบแนวตั้งจาก 'บ้าน' ไป 'สุนัข' เพิ่ม Thai dialogue bubbles เพื่อการสร้างนิยาย"
    },
    {
      "id": "sci-013",
      "subject_th": "วิทยาศาสตร์ - สสาร",
      "title_th": "เปลี่ยนแปลงของวัสดุ",
      "visual_style": "flat_vector",
      "prompt_en": "Colorful illustration showing solid, liquid, and gas states of water, simple icon representations, [grade level visual style] clear state labels, blue gradient progression, educational physics demonstration, three-column layout",
      "canva_layout_tip_th": "แสดงทั้ง 3 สภาพในสไลด์เดียว เพิ่มคำอธิบายไทยว่า 'แข็ง', 'ของเหลว', 'ก๊าซ' ใต้ภาพสำหรับนักเรียน"
    },
    {
      "id": "math-014",
      "subject_th": "คณิตศาสตร์ - พื้นที่",
      "title_th": "แนวคิดการหาพื้นที่",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Cute clay shapes puzzle where animals cover a garden area, colorful polygon pieces, [grade level visual style] simple edges, area calculation visual, educational geometry toy, colorful garden setting background",
      "canva_layout_tip_th": "แสดงชิ้นส่วนปริภูมิ 2-3 ชนิดพร้อมกระต่ายน้อย, เพิ่มข้อความไทยเพื่อแนะนำ 'คณิตคิด สนุก!' ด้านบน"
    },
    {
      "id": "soc-015",
      "subject_th": "สังคมศึกษา - วัฒนธรรม",
      "title_th": "เทศกาลไทยสีสันสดใส",
      "visual_style": "flat_vector",
      "prompt_en": "Vibrant illustration of Thai festival scene with lanterns, traditional masks, colorful decorations, [grade level visual style] simple clean lines, festive red and gold palette, cultural celebration illustration",
      "canva_layout_tip_th": "แสดงภาพหลายภาพในแนวนอน, เพิ่มคำอธิบายไทยสำหรับ 'ลอยกระทง', 'ขึ้นปีใหม่', 'สงกรานต์' ใต้รูปภาพแต่ละภาพ"
    },
    {
      "id": "sci-016",
      "subject_th": "วิทยาศาสตร์ - สิ่งมีชีวิต",
      "title_th": "โครงสร้างของพืช",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Adorable clay model showing plant structure: roots, stem, leaves, flowers, [grade level visual style] simplified educational depiction, green color scheme, realistic proportions, biology lesson illustration",
      "canva_layout_tip_th": "แยกส่วนของพืชในแนวตั้ง, เพิ่มข้อความไทยเพื่อแนะนำ 'ใบ', 'ดอก', 'ผล' ใต้แต่ละภาพเหมือนคำอธิบายในหนังสือเรียน"
    },
    {
      "id": "eng-017",
      "subject_th": "ภาษาต่างประเทศ - เขียน",
      "title_th": "ตัวอักษรที่ชัดเจนและน่ารัก",
      "visual_style": "flat_vector",
      "prompt_en": "Friendly cartoon character practicing handwriting, smooth flowing letter shapes, [grade level visual style] large clear typography sample, educational writing guide illustration, soft colors, simple classroom setting",
      "canva_layout_tip_th": "ให้ไอคอนตัวอักษรไทยในเฉดสีต่างๆ ใต้ภาพตัวอักษรภาษาอังกฤษเพื่อช่วยในการเปรียบเทียบ"
    },
    {
      "id": "art-018",
      "subject_th": "ศิลปะ - คอลัม",
      "title_th": "จิตนาการของดอกไม้",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Colorful clay sculpture of imaginative flower with unusual petals, bright contrasting colors, [grade level visual style] rounded smooth shapes, artistic expression piece, creative education illustration",
      "canva_layout_tip_th": "ใช้พื้นหลังสีดำสำหรับดอกไม้, เติมคำอธิบายไทยว่า 'ความคิดสร้างสรรค์' และบริบทศิลปะเหนือภาพ"
    },
    {
      "id": "his-019",
      "subject_th": "ประวัติศาสตร์ - ศาสนา",
      "title_th": "วัดวาอารามสมัยก่อน",
      "visual_style": "flat_vector",
      "prompt_en": "Historical temple architecture illustration with golden spires, traditional Thai architectural elements, [historical era] design features, [grade level visual style] educational diagram, cultural heritage representation, clean lines and gold accents",
      "canva_layout_tip_th": "แสดงวัดทั้ง 3 แบบในแนวนอน, เพิ่มคำอธิบายไทยเพื่อแนะนำ 'พุทธศาสนา', 'ประเพณี', 'วัฒนธรรม' ใต้แต่ละภาพ"
    },
    {
      "id": "sci-020",
      "subject_th": "วิทยาศาสตร์ - คณิตศาสตร์",
      "title_th": "วัฏจักรของดาวเคราะห์",
      "visual_style": "3d_cute_clay",
      "prompt_en": "Charming clay solar system illustration showing planets in orbits, sun rays, colorful celestial bodies, [grade level visual style] simplified educational model, yellow sun, blue Earth, red Mars, gentle space background",
      "canva_layout_tip_th": "แสดงภาพดาวเคราะห์ 5 ดวงในวงกลม, เพิ่มหมายเลขไทย 1-5 พร้อมชื่อดาวเคราะห์ใต้ภาพดาวเคราะห์แต่ละดวง"
    }
  ]
}
```

This catalog provides:

1. **20 comprehensive prompts** covering key educational topics across Thai curriculum
2. **8 subject areas** including Science, Math, Thai History, Literature, Social Studies, Art, Physical Education, and English
3. **Dual visual styles** - clean flat vector illustrations and 3D cute clay styles
4. **Bracketed customization slots** for [specific organ], [grade level visual style], and [historical era]
5. **English-only visual descriptions** so Thai teachers can add Thai text overlays in Canva
6. **Structured JSON format** with all required keys: id, subject_th, title_th, visual_style, prompt_en, and canva_layout_tip_th
7. **Practical Canva layout tips** specifically designed for Thai educational context

Each prompt follows educational best practices and provides teachers with ready-to-use visual descriptions that can be easily customized using Midjourney, DALL-E 3, Grok, or Canva's text-to-image features.