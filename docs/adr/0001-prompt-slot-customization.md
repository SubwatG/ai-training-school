# ADR 0001: Client-Side Interactive Prompt Slot Customization

Status: accepted

## Context & Decision
Teachers frequently copy prompt templates with unreplaced brackets (e.g. `[ชื่อเนื้อหา]`, `[ระดับชั้น]`), leading to generic or failed LLM completions. 

We decided to implement an in-browser **Prompt Customizer** in `site/assets/js/app.js` using an **In-Card Interactive Slot Form** with live reactive previews.

## Why this approach over alternatives
1. **Low cognitive friction:** Teachers see immediate slot inputs (subject dropdown, grade selector, topic input) directly on the prompt card without opening a disruptive modal or navigating away.
2. **Zero backend dependency:** Variable substitution runs 100% in client-side Vanilla JavaScript, preserving our static single/multi-page architecture for GitHub Pages deployment.
3. **Preserved Raw Copy fallback:** Teachers who want the raw template can still copy immediately, while teachers wanting personalized prompts get their tailored version in one click.
