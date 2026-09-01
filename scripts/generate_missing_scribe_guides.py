import json, base64, os
from PIL import Image, ImageDraw, ImageFont

def get_b64(img):
    out_p = '/tmp/_tmp_scribe.png'
    img.save(out_p)
    with open(out_p, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

def build_guide_html(meta_title, steps):
    with open('/home/kitti/Projects/local-scribe/extension/viewer.html', 'r', encoding='utf-8') as f:
        html = f.read()
    with open('/home/kitti/Projects/local-scribe/extension/viewer.js', 'r', encoding='utf-8') as f:
        js = f.read()

    bundle = {
        'meta': {'title': meta_title, 'startTime': 1787640000000},
        'session': steps
    }

    safe_bundle = json.dumps(bundle, ensure_ascii=False).replace('</script>', '<\\/script>')
    safe_js = js.replace('</script>', '<\\/script>')

    tag_s = '<' + 'script' + '>'
    tag_e = '<' + '/script' + '>'
    search_tag = '<' + 'script src=\"viewer.js\">' + '<' + '/script>'

    return html.replace(search_tag, f'{tag_s}\nwindow.__SCRIBE_DATA__ = {safe_bundle};\n{safe_js}\n{tag_e}')

# ==========================================
# GUIDE 1: Canva สำหรับครู: สร้างใบงานการศึกษา & โหลด PDF
# ==========================================
def make_canva_guide():
    w, h = 1280, 720
    steps = []
    
    # Step 1: Click "สร้างดีไซน์"
    img1 = Image.new('RGB', (w, h), color=(244, 246, 248))
    d1 = ImageDraw.Draw(img1)
    # Header
    d1.rectangle([0, 0, w, 64], fill=(255, 255, 255))
    d1.rectangle([0, 63, w, 64], fill=(226, 232, 240))
    d1.text((32, 22), 'Canva for Education — หน้าหลัก (ครูกิตติพงศ์)', fill=(30, 41, 59))
    # Button สร้างดีไซน์ (Top Right)
    bx, by, bw, bh = 1100, 14, 150, 38
    d1.rectangle([bx, by, bx+bw, by+bh], fill=(122, 111, 177), outline=(95, 84, 150))
    d1.text((bx+24, by+10), '+ สร้างดีไซน์', fill=(255, 255, 255))
    # Hero content
    d1.rectangle([80, 120, 1200, 300], fill=(255, 255, 255), outline=(226, 232, 240))
    d1.text((120, 160), 'วันนี้คุณครูต้องการออกแบบอะไรสำหรับห้องเรียน?', fill=(30, 41, 59))

    steps.append({
        'id': 'step_canva_1',
        'timestamp': 1787640001000,
        'action': 'click',
        'elementTag': 'button',
        'elementText': '+ สร้างดีไซน์',
        'description': 'ขั้นตอนที่ 1: คลิกที่ปุ่ม "+ สร้างดีไซน์" ที่มุมขวาบนของหน้าหลัก Canva',
        'tipText': 'เข้าผ่าน canva.com ด้วยบัญชีครู (Canva for Education) เพื่อปลดล็อกเทมเพลตและฟอนต์ฟรี 100%',
        'coords': {'xPercent': 91.8, 'yPercent': 4.6, 'box': {'left': 85.9, 'top': 1.9, 'width': 11.7, 'height': 5.3}},
        'screenshot': get_b64(img1)
    })

    # Step 2: Select "ใบงานการศึกษา (A4 แนวนอน/แนวตั้ง)"
    img2 = Image.new('RGB', (w, h), color=(244, 246, 248))
    d2 = ImageDraw.Draw(img2)
    d2.rectangle([0, 0, w, 64], fill=(255, 255, 255))
    d2.text((32, 22), 'Canva for Education — เมนูค้นหาขนาดกระดาษ', fill=(30, 41, 59))
    # Dropdown menu
    mx, my, mw, mh = 880, 60, 370, 450
    d2.rectangle([mx, my, mx+mw, my+mh], fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    d2.text((mx+20, my+20), 'ขนาดที่แนะนำสำหรับการศึกษา:', fill=(100, 116, 139))
    # Item: ใบงาน A4 (Education Worksheet)
    ix, iy, iw, ih = mx+10, my+60, mw-20, 50
    d2.rectangle([ix, iy, ix+iw, iy+ih], fill=(237, 233, 254), outline=(122, 111, 177))
    d2.text((ix+20, iy+15), '📄 ใบงานการศึกษา (A4 21 x 29.7 ซม.)', fill=(30, 41, 59))
    d2.text((ix+20, iy+80), '📊 พรีเซนเทชั่นเพื่อการศึกษา (16:9)', fill=(71, 85, 105))
    d2.text((ix+20, iy+140), '🃏 แฟลชการ์ด / บัตรคำศัพท์ (A4)', fill=(71, 85, 105))

    steps.append({
        'id': 'step_canva_2',
        'timestamp': 1787640002000,
        'action': 'click',
        'elementTag': 'item',
        'elementText': 'ใบงานการศึกษา A4',
        'description': 'ขั้นตอนที่ 2: เลือกขนาด "ใบงานการศึกษา (Worksheet A4)" เพื่อให้ได้สัดส่วนกระดาษพิมพ์พอดี',
        'tipText': 'เลือกขนาด A4 มาตรฐาน จะช่วยให้เวลาสั่งพิมพ์ที่โรงเรียนขอบกระดาษไม่ล้นและไม่ตกขอบ',
        'coords': {'xPercent': 82.5, 'yPercent': 20.0, 'box': {'left': 70.0, 'top': 16.5, 'width': 27.0, 'height': 7.0}},
        'screenshot': get_b64(img2)
    })

    # Step 3: Insert Image from Gemini & Text
    img3 = Image.new('RGB', (w, h), color=(241, 245, 249))
    d3 = ImageDraw.Draw(img3)
    # Left Toolbar
    d3.rectangle([0, 0, 72, h], fill=(30, 41, 59))
    d3.rectangle([72, 0, 360, h], fill=(255, 255, 255), outline=(226, 232, 240))
    d3.text((90, 25), 'อัปโหลดสื่อ (Uploads)', fill=(30, 41, 59))
    # Upload button
    ux, uy, uw, uh = 90, 70, 250, 40
    d3.rectangle([ux, uy, ux+uw, uy+uh], fill=(95, 169, 158))
    d3.text((ux+40, uy+10), '⬆ อัปโหลดภาพจาก Gemini', fill=(255, 255, 255))
    # Canvas Workspace A4
    cx, cy, cw, ch = 520, 40, 500, 640
    d3.rectangle([cx, cy, cx+cw, cy+ch], fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    d3.text((cx+120, cy+40), 'ใบงานวิทยาศาสตร์: วัฏจักรของน้ำ', fill=(38, 57, 74))
    # Image placeholder
    d3.rectangle([cx+80, cy+100, cx+cw-80, cy+320], fill=(248, 250, 252), outline=(148, 163, 184), width=1)
    d3.text((cx+120, cy+200), '[ รูปภาพ 2D Vector จาก Gemini/Banana ]', fill=(100, 116, 139))

    steps.append({
        'id': 'step_canva_3',
        'timestamp': 1787640003000,
        'action': 'click',
        'elementTag': 'button',
        'elementText': 'อัปโหลดสื่อ',
        'description': 'ขั้นตอนที่ 3: คลิกที่แท็บ "อัปโหลด" แล้วลากภาพประกอบพื้นขาวที่ได้จาก Gemini มาวางบนใบงาน',
        'tipText': 'ภาพที่สั่งแบบ isolated on white background จาก Gemini จะวางลงบนกระดาษขาวได้เนียนตา ไม่ต้องไดคัท',
        'coords': {'xPercent': 16.8, 'yPercent': 12.5, 'box': {'left': 7.0, 'top': 9.7, 'width': 19.5, 'height': 5.6}},
        'screenshot': get_b64(img3)
    })

    # Step 4: Export to PDF Print
    img4 = Image.new('RGB', (w, h), color=(241, 245, 249))
    d4 = ImageDraw.Draw(img4)
    # Header bar
    d4.rectangle([0, 0, w, 56], fill=(255, 255, 255), outline=(226, 232, 240))
    d4.text((30, 18), 'ใบงานวิทยาศาสตร์ ป.4 — บันทึกแล้ว', fill=(71, 85, 105))
    # Share Button (Top Right)
    sx, sy, sw, sh = 1130, 10, 120, 36
    d4.rectangle([sx, sy, sx+sw, sy+sh], fill=(232, 135, 122))
    d4.text((sx+25, sy+9), 'แชร์ (Share)', fill=(255, 255, 255))
    # Download Popover
    dx, dy, dw, dh = 900, 60, 350, 360
    d4.rectangle([dx, dy, dx+dw, dy+dh], fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    d4.text((dx+20, dy+20), 'ประเภทไฟล์สำหรับพิมพ์:', fill=(30, 41, 59))
    # Option: PDF สำหรับพิมพ์ (PDF Print)
    ox, oy, ow, oh = dx+15, dy+70, dw-30, 55
    d4.rectangle([ox, oy, ox+ow, oy+oh], fill=(236, 253, 245), outline=(95, 169, 158), width=2)
    d4.text((ox+15, oy+16), '🖨️ PDF สำหรับพิมพ์ (PDF Print - คุณภาพสูง)', fill=(15, 118, 110))
    # Download Button
    dbx, dby, dbw, dbh = dx+20, dy+280, dw-40, 45
    d4.rectangle([dbx, dby, dbx+dbw, dby+dbh], fill=(95, 169, 158))
    d4.text((dbx+90, dby+12), 'ดาวน์โหลด (Download)', fill=(255, 255, 255))

    steps.append({
        'id': 'step_canva_4',
        'timestamp': 1787640004000,
        'action': 'click',
        'elementTag': 'button',
        'elementText': 'ดาวน์โหลด PDF Print',
        'description': 'ขั้นตอนที่ 4: กดปุ่ม "แชร์" -> เลือกประเภทไฟล์เป็น "PDF สำหรับพิมพ์" แล้วกดดาวน์โหลด',
        'tipText': 'เลือก "PDF สำหรับพิมพ์ (PDF Print)" จะได้ความละเอียด 300 DPI คมชัดทุกตัวอักษรเมื่อสั่งปริ้นท์',
        'coords': {'xPercent': 82.5, 'yPercent': 45.0, 'box': {'left': 71.5, 'top': 38.8, 'width': 22.0, 'height': 6.2}},
        'screenshot': get_b64(img4)
    })

    return build_guide_html('คู่มือการใช้งาน Canva: สร้างใบงานการศึกษาและส่งออก PDF', steps)

# ==========================================
# GUIDE 2: NotebookLM: สรุปเอกสารราชการ & สร้าง Audio Podcast
# ==========================================
def make_notebooklm_guide():
    w, h = 1280, 720
    steps = []

    # Step 1: Create New Notebook
    img1 = Image.new('RGB', (w, h), color=(248, 250, 252))
    d1 = ImageDraw.Draw(img1)
    d1.rectangle([0, 0, w, 64], fill=(255, 255, 255), outline=(226, 232, 240))
    d1.text((40, 20), 'Google NotebookLM — สมุดบันทึก AI อิงเอกสารจริง', fill=(30, 41, 59))
    # New Notebook Card
    nx, ny, nw, nh = 80, 130, 320, 240
    d1.rectangle([nx, ny, nx+nw, ny+nh], fill=(255, 255, 255), outline=(232, 135, 122), width=2)
    d1.text((nx+130, ny+80), '+', fill=(232, 135, 122))
    d1.text((nx+60, ny+130), 'สร้างสมุดบันทึกใหม่ (New Notebook)', fill=(30, 41, 59))

    steps.append({
        'id': 'step_nlm_1',
        'timestamp': 1787640011000,
        'action': 'click',
        'elementTag': 'card',
        'elementText': '+ สร้างสมุดบันทึกใหม่',
        'description': 'ขั้นตอนที่ 1: เข้าสู่ notebooklm.google.com แล้วคลิกที่การ์ด "+ สร้างสมุดบันทึกใหม่"',
        'tipText': 'ล็อกอินด้วย Google Account เพื่อใช้งานฟรี NotebookLM ทำงานแบบ Grounded ตอบเฉพาะเอกสารที่ใส่เท่านั้น',
        'coords': {'xPercent': 18.8, 'yPercent': 34.7, 'box': {'left': 6.2, 'top': 18.0, 'width': 25.0, 'height': 33.3}},
        'screenshot': get_b64(img1)
    })

    # Step 2: Upload Sources (PDF, Docs, CSV)
    img2 = Image.new('RGB', (w, h), color=(248, 250, 252))
    d2 = ImageDraw.Draw(img2)
    d2.rectangle([0, 0, w, 64], fill=(255, 255, 255), outline=(226, 232, 240))
    d2.text((40, 20), 'เพิ่มแหล่งที่มา (Add Sources) — ป้อนความรู้ให้ AI', fill=(30, 41, 59))
    # Modal Upload Dialog
    mx, my, mw, mh = 240, 110, 800, 500
    d2.rectangle([mx, my, mx+mw, my+mh], fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    d2.text((mx+40, my+40), 'เลือกประเภทเอกสารที่ต้องการอัปโหลด:', fill=(30, 41, 59))
    # Sources buttons
    # 1. Google Docs / Drive
    d2.rectangle([mx+40, my+100, mx+360, my+200], fill=(241, 245, 249), outline=(148, 163, 184))
    d2.text((mx+80, my+140), '📄 Google Docs / Drive', fill=(30, 41, 59))
    # 2. PDF & CSV Files
    d2.rectangle([mx+400, my+100, mx+720, my+200], fill=(236, 253, 245), outline=(95, 169, 158), width=2)
    d2.text((mx+440, my+140), '📂 อัปโหลด PDF / Word / CSV', fill=(15, 118, 110))

    steps.append({
        'id': 'step_nlm_2',
        'timestamp': 1787640012000,
        'action': 'click',
        'elementTag': 'button',
        'elementText': 'อัปโหลด PDF / Word / CSV',
        'description': 'ขั้นตอนที่ 2: เลือกอัปโหลดไฟล์หลักสูตร, แผนการสอน, หรือระเบียบ ก.ค.ศ. ที่ต้องการใช้อ้างอิง',
        'tipText': 'รองรับทั้งไฟล์ PDF, Google Docs และไฟล์ตาราง CSV แนะนำให้ตัดตารางที่ Merge ช่องออกก่อนอัปโหลด',
        'coords': {'xPercent': 56.2, 'yPercent': 21.0, 'box': {'left': 50.0, 'top': 13.8, 'width': 25.0, 'height': 13.8}},
        'screenshot': get_b64(img2)
    })

    # Step 3: Generate Deep Dive Audio Podcast
    img3 = Image.new('RGB', (w, h), color=(241, 245, 249))
    d3 = ImageDraw.Draw(img3)
    d3.rectangle([0, 0, w, 60], fill=(255, 255, 255), outline=(226, 232, 240))
    d3.text((40, 20), 'สมุดบันทึก: ประวัติองค์พระปฐมเจดีย์และวรรณกรรมท้องถิ่น (แหล่งข้อมูล: 1 ไฟล์)', fill=(30, 41, 59))
    # Studio Panel on Right
    rx, ry, rw, rh = 840, 80, 400, 600
    d3.rectangle([rx, ry, rx+rw, ry+rh], fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    d3.text((rx+20, ry+25), 'Audio Overview (พอดแคสต์เสียง)', fill=(30, 41, 59))
    # Audio Card
    ax, ay, aw, ah = rx+20, ry+70, rw-40, 160
    d3.rectangle([ax, ay, ax+aw, ay+ah], fill=(245, 243, 255), outline=(122, 111, 177), width=2)
    d3.text((ax+20, ay+20), '🎙️ สนทนาเชิงลึก (Deep Dive Conversation)', fill=(92, 82, 142))
    d3.text((ax+20, ay+50), 'AI 2 คนสนทนาสรุปประเด็นจากเอกสารของคุณ', fill=(100, 116, 139))
    # Generate Button
    d3.rectangle([ax+20, ay+95, ax+aw-40, ay+140], fill=(122, 111, 177))
    d3.text((ax+60, ay+110), '⚡ สร้างเสียงพอดแคสต์ (Generate)', fill=(255, 255, 255))

    steps.append({
        'id': 'step_nlm_3',
        'timestamp': 1787640013000,
        'action': 'click',
        'elementTag': 'button',
        'elementText': 'สร้างเสียงพอดแคสต์ (Generate)',
        'description': 'ขั้นตอนที่ 3: คลิกที่ปุ่ม "สร้างเสียงพอดแคสต์ (Generate)" เพื่อให้ AI แปลงเอกสารเป็นรายการสนทนา 2 คน',
        'tipText': 'ใช้เวลาประมวลผลประมาณ 3-5 นาที จะได้คลิปเสียงความยาว 8-12 นาที ใช้เป็นสื่อการสอนกระตุ้นเด็กก่อนเข้าบทเรียน',
        'coords': {'xPercent': 80.0, 'yPercent': 32.5, 'box': {'left': 68.0, 'top': 24.3, 'width': 25.0, 'height': 6.2}},
        'screenshot': get_b64(img3)
    })

    # Step 4: Ask Questions & Citations (Zero Hallucination)
    img4 = Image.new('RGB', (w, h), color=(241, 245, 249))
    d4 = ImageDraw.Draw(img4)
    d4.rectangle([0, 0, w, 60], fill=(255, 255, 255), outline=(226, 232, 240))
    d4.text((40, 20), 'แชทถาม-ตอบจากเอกสาร พร้อมเลขอ้างอิง (Citations)', fill=(30, 41, 59))
    # Chat Area
    cx, cy, cw, ch = 80, 80, 720, 600
    d4.rectangle([cx, cy, cx+cw, cy+ch], fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    # Chat Bubble
    d4.rectangle([cx+30, cy+40, cx+cw-30, cy+180], fill=(248, 250, 252), outline=(226, 232, 240))
    d4.text((cx+50, cy+60), 'สรุปตัวชี้วัดและคำถามชวนคิด 3 ข้อสำหรับนักเรียน:', fill=(30, 41, 59))
    d4.text((cx+50, cy+95), '1. ความเป็นมาขององค์พระปฐมเจดีย์ในสมัยทวารวดี [หน้า 3]', fill=(15, 118, 110))
    d4.text((cx+50, cy+130), '2. อิทธิพลทางศิลปะและสถาปัตยกรรมระฆังคว่ำ [หน้า 7]', fill=(15, 118, 110))
    # Input box
    d4.rectangle([cx+30, cy+ch-70, cx+cw-30, cy+ch-20], fill=(255, 255, 255), outline=(95, 169, 158), width=2)
    d4.text((cx+50, cy+ch-50), 'พิมพ์คำถาม เช่น "ช่วยออกแบบคำถามท้ายบทเรียน 5 ข้อ"...', fill=(148, 163, 184))

    steps.append({
        'id': 'step_nlm_4',
        'timestamp': 1787640014000,
        'action': 'click',
        'elementTag': 'input',
        'elementText': 'ช่องป้อนคำถาม',
        'description': 'ขั้นตอนที่ 4: พิมพ์คำถามในช่องแชทด้านล่าง NotebookLM จะตอบพร้อมติดป้ายเลขหน้าอ้างอิงทุกจุด',
        'tipText': 'เมื่อคลิกที่ตัวเลข [1], [2] ในคำตอบ หน้าจอจะพาเปิดไปยังหน้าเอกสารต้นฉบับทันที การันตีไม่มีข้อมูลหลอน',
        'coords': {'xPercent': 34.4, 'yPercent': 92.5, 'box': {'left': 8.6, 'top': 87.5, 'width': 51.5, 'height': 6.9}},
        'screenshot': get_b64(img4)
    })

    return build_guide_html('คู่มือการใช้งาน NotebookLM: ปราบความหลอนด้วยเอกสารจริงและสร้าง Audio Podcast', steps)

out_dir = '/home/kitti/Projects/Activities-me/ai-training-school/site/Outputs-from-ai'
os.makedirs(out_dir, exist_ok=True)

with open(f'{out_dir}/Canva-สร้างใบงานการศึกษาและโหลดPDF.html', 'w', encoding='utf-8') as f:
    f.write(make_canva_guide())
print('Generated Canva-สร้างใบงานการศึกษาและโหลดPDF.html')

with open(f'{out_dir}/NotebookLM-ปราบความหลอนและสร้างAudioPodcast.html', 'w', encoding='utf-8') as f:
    f.write(make_notebooklm_guide())
print('Generated NotebookLM-ปราบความหลอนและสร้างAudioPodcast.html')
