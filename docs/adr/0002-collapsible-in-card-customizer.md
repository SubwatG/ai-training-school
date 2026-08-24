# ADR 0002: Collapsible In-Card Slot Customizer UX

Status: accepted

## Context & Decision
With 260+ prompts in the catalog, rendering persistent input fields on every card would drastically clutter the feed and overwhelm teachers visually.

We decided to implement a **Collapsible In-Card Slot Customizer** (`<details>` or animated toggle) labeled **"ปรับแต่งตัวแปรก่อนคัดลอก ⚙️"**:
1. Default state is collapsed: maintains clean, readable prompt cards with fast raw copying.
2. Expanded state: reveals auto-extracted slot inputs, smart presets, and a reactive live preview with an instant "คัดลอกแบบปรับแต่งแล้ว" action button.
