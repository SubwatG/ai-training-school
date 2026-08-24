# AI Training School Platform Context

The web platform and interactive tools supporting AI literacy, prompt engineering, and EdTech workflow training for Thai educators and teachers.

## Language

### Core Prompt Concepts

**Prompt Template**:
The parameterized master text containing bracketed placeholders (e.g. `[ชื่อเนื้อหา]`, `[ระดับชั้น]`) designed to guide an LLM to generate classroom artifacts.
_Avoid_: Prompt string, raw prompt, prompt recipe

**Prompt Slot**:
A bracketed customizable variable token inside a prompt template (e.g. `[วิชา]`, `[จำนวนชั่วโมง]`) dynamically extracted via regex and intended to be replaced with teacher-specific inputs.
_Avoid_: Parameter, variable placeholder, dynamic tag

**Slot Auto-Extraction**:
The client-side regex engine that scans prompt templates for `\[(.*?)\]` tokens and automatically generates interactive input fields and contextual preset dropdowns.
_Avoid_: Template parser, token scanner

**Prompt Customizer**:
An in-browser interactive mechanism (inline card accordion or form) allowing teachers to populate prompt slots with their specific subject, grade level, and learning topic before copying.
_Avoid_: Prompt editor, prompt builder, prompt generator

**Role-Context-Condition (RCC)**:
The canonical 3-part framework used for structuring high-leverage educational prompts for Thai teachers (บทบาท–บริบท–เงื่อนไข).
_Avoid_: System prompt formula, 3-step prompt

### Design & Typography System

**Playful Modern EdTech Archetype**:
A human-centric, welcoming aesthetic tailored for K-12 educators combining warm pastel surfaces, generous rounded panels (`14px-18px`), and accessible typography.
_Avoid_: Generic SaaS UI, cold tech theme

**Typography Roles**:
- **Display & Headings**: `Mali` (Google Fonts, weights 600/700) — delivers warmth, handwritten charm, and playful readability.
- **Body & Instructional Prose**: `IBM Plex Sans Thai Looped` (Google Fonts, weights 400/500) — ensures highest legibility for complex pedagogical texts.
- **Code & Prompt Variables**: `JetBrains Mono` / Monospace — for exact token boundary distinction.

### Game & Simulation Concepts

**Learning Atom**:
The single, atomic curriculum objective or competency targeted by a specific educational mini-game (e.g. `อักษรสูง`, `คำควบกล้ำ`, `การรวมสิบ`).
_Avoid_: Micro-lesson, topic unit, skill point

**Game Mechanic**:
The core interactive rule and input action driving an educational mini-game (e.g. `Whack-a-Mole`, `Bubble Bond`, `AR Motion Tracking`).
_Avoid_: Game engine, game play type
