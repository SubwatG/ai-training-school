// Mock dataset for training day exercises (PDF & Mock Sources)

window.__TRAINING_MOCKUPS__ = {
  // Scenario 1: Primary School Science (ว 1.2 / ว 3.1)
  science_primary: {
    title: "ใบงานจำลอง: วัฏจักรน้ำและสิ่งมีชีวิต ป.4",
    type: "pdf_ocr_candidate",
    raw_text: `ใบงานกิจกรรมวิทยาศาสตร์ ป.4 เรื่อง วัฏจักรของน้ำ
คำชี้แจง: ให้นักเรียนสังเกตภาพและตอบคำถามต่อไปนี้
1. การระเหย (Evaporation) เกิดขึ้นได้อย่างไรเมื่อน้ำในแหล่งน้ำได้รับความร้อนจากดวงอาทิตย์
2. เมฆและฝนเกิดขึ้นจากกระบวนการใด (การควบแน่น และการตกตะกอน)
3. ให้นักเรียนยกตัวอย่างความสำคัญของน้ำต่อการดำรงชีวิตของสัตว์ในชุมชนคลองเจดีย์บูชา จังหวัดนครปฐม 2 ข้อ`,
    gemini_prompt: "นำข้อความจากใบงานนี้ ไปสร้างเป็นกิจกรรม Active Learning 3 ด่าน โดยให้นักเรียนแบ่งกลุ่มสวมบทบาทเป็นหยดน้ำผจญภัย",
    suggested_banana_prompt: "clean 2d vector illustration of water cycle, cute sun, clouds, rain drops, pure white background, flat design, no text, children storybook style --ar 16:9"
  },

  // Scenario 2: Local History & Culture (Nakhon Pathom)
  local_history: {
    title: "เอกสารจำลอง: ประวัติองค์พระปฐมเจดีย์และวรรณกรรมท้องถิ่น",
    type: "notebooklm_candidate",
    summary: "เอกสารประวัติศาสตร์องค์พระปฐมเจดีย์ สำหรับบูรณาการวิชาสังคมศึกษาและภาษาไทย",
    key_points: [
      "องค์พระปฐมเจดีย์เป็นปูชนียสถานสำคัญ มีความสูง 120.45 เมตร",
      "มีประวัติความเป็นมายาวนานตั้งแต่สมัยทวารวดี",
      "เรื่องเล่าตำนานพญากง พญาพาน"
    ],
    audio_podcast_prompt: "สร้างบทสนทนาพอดแคสต์ 2 คน เล่าเรื่องตำนานองค์พระปฐมเจดีย์ให้นักเรียน ม.1 ฟังแบบสนุกสนาน ตื่นเต้น"
  }
};
