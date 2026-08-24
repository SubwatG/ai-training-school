# Parent Cross-check Notes (base facts ที่ Hermes หาเอง)

## Critical finding: rebrand
- **NotebookLM → "Gemini Notebook" ตั้งแต่ July 2026** — notebooklm.google ตอนนี้ branding "Gemini Notebook | AI Research Tool & Thinking Partner" [Source](https://notebooklm.google/)
- Elephas blog: "as of July 2026 it carries a new name: Google now calls it Gemini Notebook"; one notebook syncs across standalone app + Notebooks section inside Gemini app + soon AI Mode in Search; new feature = secure cloud computer per notebook (runs code on your sources, Ultra first then Pro) [Source](https://elephas.app/blog/what-is-notebooklm)

## Thai language support (สำคัญต่อ workshop)
- Audio Overviews รองรับ **50+ languages** รวมภาษาไทย — เปิด Settings > Output Language [Source](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-audio-overviews-50-languages/) + [Workspace update Apr 2025](https://workspaceupdates.googleblog.com/2025/04/language-expansion-audio-overviews-notebooklm.html)
- spin9.me (FB): ขยายจาก 50 → **76 ภาษา** รวมไทย [Source](https://www.facebook.com/spin9.me/posts/1246589493504553) (verify date)
- YouTube: "Audio Overviews ภาษาไทย บน NotebookLM พร้อมใช้งานแล้ว!" [Source](https://www.youtube.com/watch?v=cJu2Y5bdr68)
- Tangerine (Thai tech blog): how-to ตั้งค่าภาษาไทย step-by-step [Source](https://www.tangerine.co.th/blogs/data-analytics-artificial-intelligence/notebooklm-audio-50-languages/)

## Limits (support page, current)
Free / Plus(Pro?) tiers table — Free: 100 notebooks, **50 sources/notebook**, 50 chats/day, 3 Audio Overviews/day, 3 Video Overviews/day, Reports/Flashcards/Quizzes/Mind Maps 10/day, Deep Research 10/month. Paid tiers scale up to 500 notebooks/600 sources/5K chats [Source](https://support.google.com/gemininotebook/answer/16213268?hl=en)
- Workspace for Education: uploads NOT used to train models, no human review — good for teachers' privacy pitch

## Feature timeline anchors
- Video Overviews + Studio multi-output upgrade: **Jul 29, 2025** [Source](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/)
- 2025-2026: Cinematic Video Overviews (styles: Scientific/Professional/Editorial/Sketch Note, Ultra), Deep Research mode, Flashcards & Quizzes, Gemini 3 engine, Data Tables, ~1M token context, saved chat history
- Official edu case study: **FSU (Florida State University), Jun 22, 2026** — NotebookLM as "24/7 study partner", custom quizzes + study guides grounded in professors' course materials only, frees faculty time for mentoring; video case study embedded [Source](https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/)

## TODO after subagents return
1. Verify each subagent file exists on disk + spot-check URLs
2. Reconcile conflicts (esp. Thai language dates, source limits which changed over time)
3. Write 00-README.md synthesis + summary.csv
