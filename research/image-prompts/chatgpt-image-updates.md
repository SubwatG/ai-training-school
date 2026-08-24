# ChatGPT Image Generation — Model Timeline & Fresh Prompts (2025 → Aug 2026)

> Deep-research note for the AI Training School workshop (Thai teachers, Aug 29 2026).
> Focus: what "ChatGPT Image" means TODAY (Aug 2026), dated model milestones, and
> fresh, citable prompts — with emphasis on material from Oct 2025 onward.

---
topic: ChatGPT Image progress and prompts 2025-2026
date: 2026-08-23
model: GPT-4o / gpt-image-1 / gpt-image-1-mini / gpt-image-1.5 / gpt-image-2 (ChatGPT Images 2.0)
provider: OpenAI
sources_count: 32
---

## How to read this file
- **Section 1 — Model timeline**: every dated milestone with official URL(s).
- **Section 2 — Prompt trends**: what went viral / proved useful, with source + date.
- **Section 3 — Copy-paste prompts by theme** (education / communication-PR / promotion / summary visuals / step-by-step), verbatim where possible, with who used it and the result.
- All claims carry a working URL. Nothing here is fabricated; where a number is approximate it is flagged.

## 1. Model / update timeline

| # | Date | Milestone | Model name | Official source |
|---|------|-----------|-----------|-----------------|
| 1 | **Mar 25, 2025** | Native image generation arrives in ChatGPT — the natively multimodal 4o can render text, follow long instructions, and edit uploaded photos. Demand was so high OpenAI briefly capped requests ("our GPUs are melting"). | GPT-4o (image generation) | [OpenAI blog — Introducing 4o Image Generation](https://openai.com/index/introducing-4o-image-generation/) · [The Verge — GPU limits, Mar 27 2025](https://www.theverge.com/news/637542/chatgpt-says-our-gpus-are-melting-as-it-puts-limit-on-image-generation-requests) |
| 2 | **Apr 23, 2025** | Same model ships to developers as **`gpt-image-1`** in the Images API (Canva announced as a launch partner). High-fidelity edits + text generation for B2B workflows. | gpt-image-1 | [OpenAI blog — latest image generation model in the API](https://openai.com/index/image-generation-api/) |
| 3 | **Aug 7, 2025** — plus Aug 18, 2025 | GPT-5 arrives in ChatGPT (image creation/editing is part of the multimodal toolbox); a week later **ChatGPT Go** adds "expanded image generation" on its low-cost plan. | GPT-5 / ChatGPT Go | [ChatGPT Release Notes — Aug 7 & Aug 18 2025](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [ZDNet — GPT-5 free for all](https://www.zdnet.com/article/openais-gpt-5-is-now-free-for-all-how-to-access-and-everything-else-we-know/) |
| 4 | **Sep 30, 2025** | **Sora 2** launches — a *video + audio* model (synchronized dialogue, sound effects), **no separate image model**. Image creation stayed in ChatGPT. Sora the product was later discontinued on **Apr 26, 2026** (API Sep 24, 2026); OpenAI explicitly says image creation continues in ChatGPT. | Sora 2 (video) | [OpenAI — Sora 2 is here](https://openai.com/index/sora-2/) · [Sora discontinuation, Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) |
| 5 | **Oct 6, 2025** | DevDay 2025 quietly adds **`gpt-image-1-mini`** — "80% less expensive than the large model" (≈ $0.005–0.015/image at low/medium quality). Independent verification by Simon Willison the same day. | gpt-image-1-mini | [OpenAI DevDay 2025 announcements](https://openai.com/devday/) · [Simon Willison, Oct 6 2025](https://simonwillison.net/2025/Oct/6/gpt-image-1-mini/) |
| 6 | **Dec 16, 2025** | **"The new ChatGPT Images is here"** — flagship **GPT Image 1.5** rolls out to all ChatGPT users + API: 4x faster, precise edits that preserve faces/logos/lighting, new dedicated **Images tab** (preset styles, trending prompts), and a **"My images"** library at chatgpt.com/images. | GPT Image 1.5 | [OpenAI blog — The new ChatGPT Images is here](https://openai.com/index/new-chatgpt-images-is-here/) · [Release Notes — Dec 16 2025](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [The Verge, Dec 16 2025](https://www.theverge.com/ai-artificial-intelligence/845558/openais-new-flagship-image-generation-model-gpt-image-1-5) |
| 7 | **Apr 21, 2026** | **ChatGPT Images 2.0** / **`gpt-image-2`** — a *reasoning* image model: "thinking capabilities" (plans and refines before generating; can search the web in thinking mode), up to **2K resolution**, up to **8 images per prompt** (paid), dramatically better text rendering incl. **multilingual** (Japanese, Korean, Hindi, Bengali), knowledge cutoff Dec 2025. API on Apr 21, all ChatGPT plans Apr 22. Top of Image Arena leaderboard (+242 Elo per third-party trackers). | gpt-image-2 / ChatGPT Images 2.0 | [OpenAI blog — Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) · [TechCrunch, Apr 21 2026](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/) · [Release Notes — Apr 21 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · [AIMLAPI tracker (third-party)](https://aimlapi.com/blog/gpt-image-2-release-date-features-and-everything-you-need-to-know) |
| 8 | **May 12, 2026** | **DALL·E 2 and DALL·E 3 removed from the API** (developers notified Nov 14, 2025); gpt-image models are the recommended replacements. | end of DALL·E API era | [OpenAI API — Deprecations](https://developers.openai.com/api/docs/deprecations) |
| 9 | **Jul–Aug 2026** | The official **DALL·E GPT in the ChatGPT UI is retired on Aug 30, 2026** — "To continue creating or editing images, use ChatGPT Images." | DALL·E → ChatGPT Images | [ChatGPT Release Notes (July 2026 entry)](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |

**What "ChatGPT Image" means today (Aug 2026):** image generation is a built-in core capability of ChatGPT, not a side product — powered by **ChatGPT Images 2.0 (gpt-image-2)** on all plans, with "images with thinking" on paid plans, logged under one "My images" library. The Sora app and DALL·E branding are gone; the DALL·E GPT is being retired Aug 30, 2026. Frontier text models (currently GPT-5.6 Sol/Luna/Terra family) keep image generation as a separately limited tool inside the same chat. Overview: [Wikipedia — GPT Image](https://en.wikipedia.org/wiki/GPT_Image) · [Help Center — GPT-5.6 in ChatGPT (image-generation limits)](https://help.openai.com/en/articles/11909943) · [Images in ChatGPT FAQ](https://help.openai.com/en/articles/11084440).

## 2. Prompt trends 2025 → 2026 (what worked, with sources + dates)

### 2.1 Studio Ghibli wave & the policy aftermath (Mar–Apr 2025)
The launch trend that set the rules. OpenAI CEO Sam Altman publicly joined in on Mar 26, 2025 ([Variety, Mar 26 2025](https://variety.com/2025/digital/news/openai-ceo-chatgpt-studio-ghibli-ai-images-1236349141/)); within days OpenAI added a **"refusal which triggers when a user attempts to generate an image in the style of a living artist"** while still permitting "broader studio styles" ([Business Insider, Mar 27 2025](https://www.businessinsider.com/openai-studio-ghibli-style-images-violate-copyright-or-not-2025-3); official addendum: [GPT-4o Image Generation System Card Addendum](https://openai.com/index/gpt-4o-image-generation-system-card-addendum/)). A follow-up policy update restricted restyling *real people's photos* into such styles ([Times of India, c. Apr 2025 — date approximate](https://timesofindia.indiatimes.com/technology/tech-news/openais-chatgpt-has-just-updated-its-ghibli-style-photos-policy-now-you-cannot-modify-alter-to-transform-these-photos/articleshow/119597831.cms)). **Workshop takeaway:** style imitation of *studios* is usually OK; living artists and real-person likenesses are protected.

### 2.2 Text-heavy graphics: menus, infographics, posters (Dec 2025 → 2026)
The single biggest capability leap. GPT Image 1.5 (Dec 16, 2025) handles dense small text ([OpenAI launch post](https://openai.com/index/new-chatgpt-images-is-here/)); Images 2.0 renders entire menus, posters and ads that "could immediately be used in a restaurant" ([TechCrunch, Apr 21 2026](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)). Perfect for Thai teachers: posters, worksheets and slides with long Thai text now render far more reliably (multilingual support is a headline Images 2.0 feature — [OpenAI blog](https://openai.com/index/introducing-chatgpt-images-2-0/)).

### 2.3 Education: worksheets, coloring pages, "make this a coloring page" (2025 → 2026)
A year-round teacher trend: upload a photo → "Make this image a coloring page" ([Frugal Fun 4 Boys](https://frugalfun4boys.com/use-chatgpt-to-make-custom-coloring-pages/)); back-to-school coloring pages with the teacher's own picture ([Instagram](https://www.instagram.com/p/DMtoTNHxxz-/)); printable-worksheet prompting tutorials ([YouTube](https://www.youtube.com/watch?v=XOdxcbEw-Aw)); and OpenAI's own education newsletter now publishes classroom image prompts ([The Edu Prompt, Jun 18 2026](https://edunewsletter.openai.com/p/the-edu-prompt-from-ideas-to-images)).

### 2.4 Profile-picture & "me" mashups: fisheye anime selfie, Pixar-ify, caricature (Nov 2025 → Feb 2026)
The fisheye-anime-character selfie format generated **50M+ collective TikTok views**; Pixar-3D-style family portraits and the "caricature trend" (draw me like a cartoon character) swept Instagram/TikTok into early 2026 ([PXZ AI prompt guide, updated Feb 12 2026](https://pxz.ai/blog/viral-chatgpt-image-prompts); [Mashable — 9 more viral prompts](https://sea.mashable.com/tech/42021/love-the-caricature-trend-9-more-viral-chatgpt-image-prompts-to-try)).

### 2.5 "New year, new me" — vision boards & opposite-versions (Dec 2025 → Jan 2026)
2026 vision boards were one of the biggest Dec-Jan trends, with dedicated prompt walkthroughs ([Shilpa Goel, Dec 2025](https://www.shilpagoel.com/2025/12/how-to-create-your-2026-vision-board.html); [Fello AI](https://felloai.com/vision-board-chatgpt/)). The split-frame **"opposite versions"** composition (casual self vs. elevated self, side by side) started late Dec 2025 and peaked in Jan 2026 ([PXZ AI](https://pxz.ai/blog/viral-chatgpt-image-prompts)).

### 2.6 Photo restoration — the "sentimental AI" duty (2025 → May 2026)
Restoring old family photos is now a top everyday use; OpenAI itself noted Images 2.0 users in India are "using the AI tool to restore older photos" ([TechCrunch, Apr 30 2026](https://techcrunch.com/2026/04/30/chatgpt-images-2-0-is-a-hit-in-india-but-not-a-big-winner-elsewhere-yet/)). Complete copy-paste restoration prompt suites: [eWEEK, May 6 2026](https://www.eweek.com/news/ai-prompts-restore-old-photos/).

### 2.7 Micro-business promo assets (Apr 2026)
OpenAI's own Images 2.0 showcase is built around ads: a matcha-café launch poster, a Korean hanok hospitality campaign, product-grid merch mockups, print-ready bookmark with bleed/trim guides ([OpenAI blog, Apr 21 2026](https://openai.com/index/introducing-chatgpt-images-2-0/)). Adoption data: India downloaded ~5M ChatGPT copies in launch week, users making avatars, stylized portraits, fantasy newspaper covers, tarot visuals, fashion moodboards ([TechCrunch, Apr 30 2026](https://techcrunch.com/2026/04/30/chatgpt-images-2-0-is-a-hit-in-india-but-not-a-big-winner-elsewhere-yet/)).

### 2.8 Comics, manga & motion explainers (Dec 2025 → Apr 2026)
Multi-panel comic strips are now a headline capability ("multi-paneled comic strips" per [TechCrunch, Apr 21 2026](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)); OpenAI demos include a Miami museum trip as a vintage comic, an indie rooftop comic, a seinen manga page, and a frame-by-frame basketball dunk breakdown in manga style ([OpenAI blog](https://openai.com/index/introducing-chatgpt-images-2-0/)).

### 2.9 Data & summary visuals (2025 → 2026)
Infographics from dense content: a wolf-species magazine spread with maps and "myth vs. fact" callouts, a Cantor diagonalization proof infographic, a 2025 design-trends poster, the original GPT-1 paper as a conference poster, and a math proof drawn on a classroom blackboard ([OpenAI blog, Apr 21 2026](https://openai.com/index/introducing-chatgpt-images-2-0/)).

## 3. Copy-paste prompts by theme (verbatim + who used it + result)

### 3.1 Education

**E1 — Concept → lecture-slide infographic**
> Source: OpenAI Education newsletter, "The Edu Prompt: From Ideas to Images," **Jun 18, 2026** ([URL](https://edunewsletter.openai.com/p/the-edu-prompt-from-ideas-to-images)). Written by OpenAI Education for teachers.
```
Create a professional educational infographic explaining photosynthesis for first-year college students.
Include labeled diagrams, key vocabulary, visual callouts, a clean academic design, and a color palette appropriate for science education.
Make it suitable for a lecture slide.
```
**Result described:** a full-blown class visual ("Turn a concept for your class into a full-blown visual"), posted with a ready-to-open ChatGPT link so teachers can swap in their own concept.

**E2 — Custom coloring pages from a photo**
> Source: Frugal Fun 4 Boys blog (parenting/education site) — [URL](https://frugalfun4boys.com/use-chatgpt-to-make-custom-coloring-pages/) · also teacher trend posts: [Instagram back-to-school coloring page](https://www.instagram.com/p/DMtoTNHxxz-/) · [YouTube worksheet tutorial](https://www.youtube.com/watch?v=XOdxcbEw-Aw).
```
Make this image a coloring page.
```
**Result described:** an uploaded photo converted into a clean, printable black-line coloring page for kids ("turning your own photos into coloring sheets!"). Worksheet tutorials add: request *bold outlines, no shading, lots of whitespace* for printable results.

**E3 — Math visual on a blackboard (model demo, describes intent not verbatim prompt)**
> Source: OpenAI official Images 2.0 gallery, Apr 21 2026 ([URL](https://openai.com/index/introducing-chatgpt-images-2-0/)) — demo image: "a classroom blackboard into a visual math proof — showing how the sum of consecutive odd numbers forms perfect squares… structured reasoning, symbolic accuracy, and pedagogical layout." Exact prompt not published; use as a goal description for your own prompt.

**E4 — Teacher's whole lesson package + 16:9 LinkedIn card (agents/Codex)**
> Source: same OpenAI Education newsletter, Jun 18 2026 ([URL](https://edunewsletter.openai.com/p/the-edu-prompt-from-ideas-to-images)). Full verbatim prompt is long — key image-relevant excerpt:
```
…After both files are complete, ask whether I want a unique 16:9 LinkedIn image. If yes,
create `lesson-package/linkedin-summary-card.png` with specific details from my lesson
package and the hashtag `#createdwithcodex`.
```
**Result described:** lesson plan + Google-Docs-ready DOCX + a generated social image in one flow ("Codex will walk you through step by step").

### 3.2 Communication / PR

**C1 — Story of an outing as a comic strip**
> Source: OpenAI Images 2.0 gallery demo (Miami museum trip as a vintage comic: "cohesive narrative sequence — retro print texture, panel storytelling, consistent characters, readable lettering, destination branding"), Apr 21 2026 ([URL](https://openai.com/index/introducing-chatgpt-images-2-0/)). Exact prompt unpublished; pattern = *scene-by-scene story, characters stay consistent, one style, readable speech balloons*.

**C2 — "Opposite versions" split image (trend, Jan 2026)**
> Source: PXZ AI viral-prompt guide, updated Feb 12 2026; trend noted "started late December 2025, peak engagement" ([URL](https://pxz.ai/blog/viral-chatgpt-image-prompts)).
```
Create a split vertical composition showing contrasting versions of the same person. Left side: casual everyday look (relaxed clothes, natural lighting, ordinary setting). Right side: elevated transformation (formal/stylish attire, dramatic cinematic lighting, upscale setting). Clean vertical split down the center. Different color grading on each side left more natural, right more saturated and dramatic. 1:1 ratio.
```
**Result described:** before/after storytelling that "performs" on Instagram/TikTok — transformation content with the split making it instantly readable (author's engagement notes).

**C3 — Fisheye anime selfie (viral, engaged 50M+ views)**
> Source: PXZ AI guide, Feb 12 2026 ([URL](https://pxz.ai/blog/viral-chatgpt-image-prompts)); format credit: TikTok/Instagram creators.
```
Create a 9:16 vertical fisheye selfie of me with [CHARACTER NAME - Naruto/Goku/Doraemon/Luffy/Satoru Gojo]. We're both making exaggerated silly faces and peace signs. Set in a bright, modern living room with cream and white tones, natural daylight. High camera angle with extreme fisheye lens distortion. The anime character should maintain their cartoon style but with realistic lighting and shadows that match the room. Warm, cheerful atmosphere, ultra-detailed human subject.
```
**Result described:** "This format has generated over 50M+ collective views on TikTok" (guide author's reported aggregate). Caution for teachers: character likeness rules apply; use generic "anime character" for classroom work.

### 3.3 Promotion

**P1 — Restaurant menu that prints**
> Source: Amanda Silberling, TechCrunch senior writer, Apr 21 2026 ([URL](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)).
```
…ask the brand new ChatGPT Images 2.0 model for a menu of Mexican food…
```
(short prompt in the article: "ask… for a menu of Mexican food" on Images 2.0.)
**Result described:** "it creates something that could immediately be used in a restaurant without customers noticing that something's off" — vs. DALL-E 3 in 2024 inventing "enchuita / churiros / burrto / margartas."

**P2 — Product lifestyle photography (e-commerce / small business)**
> Source: PXZ AI, Feb 12 2026 ([URL](https://pxz.ai/blog/viral-chatgpt-image-prompts)) — "measured in conversion, not likes."
```
Create professional product photography showing [product] in a lifestyle setting. Natural, soft lighting with gentle shadows that add depth. Composition follows rule of thirds with product as hero element. Include supporting props that complement without competing books, plants, neutral accessories. Clean, bright color grading with high clarity. Aspirational but accessible mood. Slightly blurred background maintains product focus. 4:5 ratio for social media.
```
**Result described:** "Lifestyle product shots dramatically outperform white-background images on social media."

**P3 — Café launch poster (official OpenAI demo — pattern, not verbatim)**
> Source: OpenAI Images 2.0 gallery: "polished café launch poster introduces Kizuna Matcha in Brooklyn Heights… branding, soft editorial typography, lifestyle product photography" — [URL](https://openai.com/index/introducing-chatgpt-images-2-0/). Use the pattern: *name, location, hero product, brand mood, typography + lifestyle photography in one poster*.

**P4 — LinkedIn-grade headshot**
> Source: PXZ AI guide ([URL](https://pxz.ai/blog/viral-chatgpt-image-prompts)).
```
Create a professional corporate headshot with studio-quality lighting. Clean, neutral background (soft gray or subtle gradient). Even, flattering illumination with fill light to soften shadows. The subject has a confident, approachable expression. Enhance clarity and sharpness while preserving natural skin texture. Avoid over-smoothing. Soft catchlights in eyes. Corporate professional quality. 1:1 or 4:5 ratio.
```
**Result described:** "Professional headshots cost $200–500. This delivers comparable quality instantly" — used for LinkedIn, conference bios, school/parent-committee profiles.

### 3.4 Summary visuals

**S1 — Layout torture-test: the 6×6 grid (official, instruction-following benchmark)**
> Source: OpenAI launch post, Dec 16 2025 ([URL](https://openai.com/index/new-chatgpt-images-is-here/)) — shown "New" vs "Previous" model behavior.
```
Make a 6 (columns) by 6 (rows) grid grid of:
Row 1: the Greek letter beta, a beach ball, a lemon, a robot, a fish tank, a frog
Row 2: a praying mantis, an expensive watch, a baththub, a pair of sunglasses, a colorful butterfly, an envelope
Row 3: a stamp, a picture frame, a steaming dumpling, the word "miracle", a pair of skis, the letter Z
Row 4: a toilet, a subway token, a mute icon, a bottle of perfume, a dragonfly, a skateboard helmet
Row 5: a Bluetooth icon, the number 13, a green heart, a rubik's cube, a Canada goose, a soldier's helmet
Row 6: a white dog, a life jacket, a knot, a keyboard, a tissue box, the number 14
```
**Result described:** the old model scrambled cells; GPT Image 1.5 places all 36 items exactly (OpenAI's side-by-side demo). Great warm-up exercise for a workshop.

**S2 — Turn any markdown into a real newspaper page (dense text rendering)**
> Source: OpenAI launch post, Dec 16 2025 ([URL](https://openai.com/index/new-chatgpt-images-is-here/)) — officially demonstrated by feeding the GPT-5.2 announcement markdown:
```
There is a newspaper on a desk. The newspaper shows the markdown below laid out as a **natural** newspaper article. Preserve all content, formatting, and numbers exactly. The image should be tall.
```
**Result described:** full newspaper layout with headline, byline and benchmark tables intact (screenshot in the post). Works for turning a school announcement or test summary into a "newspaper" poster.

**S3 — Magazine-style infographic spread (official Images 2.0 example — pattern)**
> Source: OpenAI gallery: "magazine-style infographic spread about wolves… bold editorial headlines, myth-versus-fact callouts, maps, statistics" — [URL](https://openai.com/index/introducing-chatgpt-images-2-0/). Pattern: *topic + "magazine-style infographic spread" + "myth vs fact callouts, maps, statistics, clean editorial layout."*

**S4 — One-shot photo restoration (result: professional-grade repair)**
> Source: eWEEK, May 6 2026 — reporter Aminu Abdullahi, "6 AI Prompts That Can Restore Old Photos in Seconds" ([URL](https://www.eweek.com/news/ai-prompts-restore-old-photos/)).
```
Restore this photograph comprehensively and professionally. Analyze every visible form of damage or degradation, including scratches, tears, creases, stains, fading, discoloration, blur, noise, and grain and correct each one carefully. Sharpen soft edges and facial features naturally, without over-processing. Repair or reconstruct any missing areas by intelligently matching the surrounding textures, colors, and tones. Where colors have faded, restore them to vibrant, realistic values that suit the original era of the photo. Adjust brightness and contrast so that all areas of the image are clearly visible, with no blown-out highlights or lost shadow detail. Preserve the complete facial identity and natural likeness of every person in the image without alteration. Upscale the final output to the highest possible resolution — Full HD or above — with a clean, photo-realistic finish that looks like a professionally restored print.
```
**Result described:** "I designed the Complete One-Shot Restoration prompt to address every common problem… in a single instruction"; demo photos show restored results "via ChatGPT."

### 3.5 Step-by-step process

**T1 — Frame-by-frame motion breakdown (manga "how a dunk works")**
> Source: OpenAI Images 2.0 gallery, Apr 21 2026 ([URL](https://openai.com/index/introducing-chatgpt-images-2-0/)) — "manga-style motion breakdown illustrates a basketball player's full dunk sequence frame by frame — from dribble approach and gather steps to leap, hang time, and slam finish — like an animation keyframe study." Exact prompt unpublished; pattern: *describe the process in stages, ask for "frame-by-frame / keyframe study" panels in one page* — directly reusable for "how photosynthesis works" / "how a bill becomes law."

**T2 — Staged archival restoration (6-stage process)**
> Source: eWEEK, May 6 2026 ([URL](https://www.eweek.com/news/ai-prompts-restore-old-photos/)); for badly damaged photos.
```
Perform a full, multi-stage deep restoration of this photograph, treating it as a professional archival restoration project. Work through the following stages systematically:
Stage 1 — Damage Assessment: Analyze the entire image and identify every form of degradation present, including physical damage (tears, scratches, folds, stains), chemical deterioration (fading, yellowing, discoloration), optical issues (blur, grain, noise), and resolution limitations.
Stage 2 — Structural Repair: Reconstruct all physically damaged or missing areas using intelligent context-aware inpainting, ensuring all repairs are completely seamless and match the surrounding visual content.
Stage 3 — Tonal and Color Restoration: Restore the full dynamic range of the image — recover shadow detail, reduce blown-out highlights, and rebalance the overall exposure. Correct all color casts and restore accurate, natural colors throughout, particularly for skin tones, foliage, sky, and fabrics.
Stage 4 — Detail Enhancement: Apply targeted sharpening to all areas of the image, with greatest precision on human faces. Restore fine details including hair, eyelashes, skin texture, clothing weave, and background elements. Reduce all noise and grain while preserving natural photographic texture.
Stage 5 — Super-Resolution Upscaling: Upscale the fully restored image to the highest resolution available — targeting 4K or above — using AI super-resolution to reconstruct fine detail consistent with the image content.
Stage 6 — Final Finishing: Apply a warm, natural finishing grade that makes the image feel beautiful and lifelike. Introduce a very subtle vignette and ensure color richness and tonal depth throughout. Throughout all stages, preserve the complete identity and likeness of every person in the photograph without alteration. Deliver the final result as a pristine, print-quality image that looks professionally restored.
```
**Result described:** layered restoration pipeline with before/after examples ("Original photo via Unsplash … Restoration via ChatGPT").

**T3 — Sequential photo edits on one image (official GPT Image 1.5 demo, verbatim sequence)**
> Source: OpenAI launch post, Dec 16 2025 ([URL](https://openai.com/index/new-chatgpt-images-is-here/)) — edit chain on one uploaded photo; each step is a follow-up message:
```
Combine the two men and the dog in a 2000s film camera-style photo of them looking bored at a kids birthday party.
Add chaotic kids in the background throwing things and screaming.
Change the man on the left to a hand-drawn retro anime style, the dog to plushie style, keep the man on the right and background scenery the way they are.
Put them all in OpenAI sweaters that look like this.
Now remove the two men, just keep the dog, and put them in an OpenAI livestream that looks like the attached image.
```
**Result described:** each edit keeps "what matters" (lighting, composition, people) while changing only what was asked — OpenAI's flagship demonstration of iterative, step-by-step editing; the model "adheres to your intent more reliably… changing only what you ask for."

## 4. GPT Image 2.0 เพิ่มเติม (parent verification pass — 2026-08-23)

### 4.1 ตัวอย่างทางการที่ครูไทยต้องรู้: OpenAI ใช้ "ภาพถนนไทย" เป็นภาพสาธิต
- **แหล่ง:** https://openai.com/index/introducing-chatgpt-images-2-0/ (gallery official)
- ภาพสาธิต panoramic กรุงเทพฯ: "...a busy urban street in Thailand with multi-lane traffic... and **Thai-language signage** under a bright daytime sky" — OpenAI ยกไทยเป็น showcase multilingual text rendering ของ Images 2.0 (ป้ายภาษาไทยอ่านได้) → ใช้เปิด workshop ได้ว่า "โมเดลนี้เขียนภาษาไทยในภาพได้จริง"

### 4.2 Spec สำคัญ Images 2.0 / gpt-image-2 (cross-check 2 แหล่ง)
- Text rendering accuracy ~99% · Thinking Mode (browse web + self-verify + multi-variant) · native 2K · knowledge cutoff Dec 2025 · แทนที่ DALL·E 3 (ปิด 12 พ.ค. 2026) และ GPT Image 1.5 [tosea.ai guide](https://tosea.ai/blog/gpt-image-2-complete-guide); Thinking/web search/multi-image = Plus/Pro/Business only [atlabs.ai](https://www.atlabs.ai/blog/the-ultimate-gpt-image-2-prompting-guide-how-to-use-openai%E2%80%99s-best-image-model-2026)
- จุดอ่อน (จาก hands-on review): tiny legal copy, brand-logo เป๊ะๆ, ฟอนต์ลิขสิทธิ์, transparent background ยังต้อง QA มือ [PixVerse 80-prompt guide](https://pixverse.ai/en/blog/gpt-image-2-review-and-prompt-guide)

### 4.3 Prompt formula เฉพาะ GPT Image 2 (PixVerse, 2026)
```
Create [type of image] for [use case].
Main subject: [specific subject and visible details].
Exact text, if any: "[copy that must appear]".
Composition: [framing, layout, negative space].
Style and lighting: [visual language, mood, light direction].
Constraints: [what must not change, no extra words, no watermark].
Output format: [aspect ratio / print-ready].
```
- หลักการ: **"Name the Job Before the Style"** — บอกว่าภาพนี้จะถูกตัดสินด้วยอะไร (layout/hierarchy/usability) ไม่ใช่ stack keyword
- 10 rules ย่อ (mavgpt.ai): quote ข้อความเป๊ะใน "" · ระบุ lens/lighting · reference real styles · image-to-image · specify what NOT to include · 7–8 constraints ต่อ prompt ไหว · iterate don't restart · mention aspect ratio — https://mavgpt.ai/resources/ultimate-chatgpt-image-prompting-guide-2026

### 4.4 เปรียบเทียบฝีมือล่าสุด (สำหรับตอบคำถามในห้อง)
- Nano Banana 2 นำที่ photorealism + 4K; **gpt-image-2 นำที่ text fidelity + prompt adherence + Thinking Mode** [tosea.ai] — เลือกเครื่องมือตามงาน: โปสเตอร์ตัวหนังสือเยอะ→GPT Image 2; ภาพสมจริง/ตัวละคร→Nano Banana

## 5. Practical notes for the workshop
- **Chronology to teach:** the March 2025 "4o image" launch is now *two generations old* — today it's **Images 2.0 / gpt-image-2** (Apr 2026), with 1.5 (Dec 2025) and mini (Oct 2025) as history. Free users have Images 2.0 with limits; "images with thinking" is paid ([Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)).
- **Expect edits to work**: piece-by-piece photo editing (T3) and text-heavy layouts (S1/S2) are the flagship capabilities — demo those, not Ghibli-style portraits.
- **Rules of thumb:** protect real people's likenesses; living-artist styles are refused; studio styles ("anime", "vintage comic", "watercolor storybook") are fine; DALL·E is deprecated everywhere ([API deprecations](https://developers.openai.com/api/docs/deprecations), [DALL·E GPT retirement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)).
- **Multilingual is a feature now**: Thai text rendering improved dramatically with Images 2.0's non-Latin push (official claim + [TechCrunch](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)); still, proofread Thai text after generation.
- Sources marked "(pattern, not verbatim)" are official demo images whose exact prompt OpenAI did not publish — the pattern text is safe to reuse.