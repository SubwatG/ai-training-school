# Research Brief: NotebookLM Use Cases Deep Dive

## Mission
Deep-research **NotebookLM (Google)** use cases worldwide AND in Thailand. Output = Markdown files with full source URLs. This feeds an AI-teacher-training project (workshop 29 Aug 2026 covering Gemini / Canva / NotebookLM for Thai teachers).

## Hard rules
1. **Every claim MUST carry a traceable source URL** (user requirement: ทุกที่ต้องมีแจ้งแหล่งที่มาให้สืบต้นต่อได้).
2. No fabrication. If a source is inaccessible, say so and use an alternative.
3. Write output as ONE self-contained .md file at the exact path given in your task.
4. Write incrementally (write skeleton first, then patch/append sections) — avoid one giant write.
5. Language: Thai prose, English tool names/terms OK. Keep original English quotes where useful.
6. Include dates of posts/pages when known; flag anything possibly outdated.
7. Do NOT store secrets. Do not edit any other project files.

## What to collect
- Concrete use cases & workflows (step-level detail: what sources uploaded, what prompts/settings used, what output).
- Real user stories: Reddit threads (r/notebooklm, r/Teachers, r/professors, r/GradSchool…), blogs, YouTube tutorials (title+URL), GitHub repos/tools built on NotebookLM API or exports.
- Education-specific: teachers, professors, students, researchers; lesson planning, quiz generation, podcast/Audio Overview, study guides, mind maps.
- Thailand-specific: Thai teacher blogs, Pantip, Facebook groups indexed on web, Thai university/library adoption news, Thai tech media coverage. Search both English and Thai keywords (e.g. "NotebookLM การใช้งาน", "NotebookLM ครู", "NotebookLM สอน").
- Limitations/pitfalls users report (hallucination, upload limits, privacy concerns, language support for Thai).
- Notable official updates 2025–2026 (features like Audio Overview languages incl. Thai?, Video Overviews, Mind Maps, Nano Banana visuals, Gemini 3 upgrade).

## Output format (each file)
```markdown
---
topic: <assigned topic>
date: 2026-08-23
sources_count: N
---
# <Title>
## Executive summary (Thai)
## Findings (grouped by theme)
### <Theme> 
- finding … [Source](url) (date)
## Use-case table
| Use case | Who | Workflow | Source |
## Pitfalls / limitations
## Source list (numbered, full URLs)
```

## Useful search entry points
- site:reddit.com/r/notebooklm
- "NotebookLM" education use cases 2025..2026
- NotebookLM GitHub (API wrappers, notebook exporters)
- Google blog: notebooklm.google, blog.google/product/notebooklm
- Thai: "NotebookLM" ครู | การอบรม | ภาษาไทย | Pantip
