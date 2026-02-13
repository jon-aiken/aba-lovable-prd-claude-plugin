---
name: lovable-prd-builder
description: >
  Build a complete Lovable.dev-ready PRD knowledge base by generating four structured documents:
  Masterplan, Implementation Plan, Design Guidelines, and App Flow (Pages & Roles).
  Use this skill whenever someone wants to plan a Lovable.dev project, create a PRD for vibe coding,
  prepare documentation for an AI app builder, scaffold a new product idea for Lovable,
  or says anything like "build a PRD", "plan my app", "Lovable knowledge base", "start a new project",
  "create a masterplan", or "prepare my build docs". Also use when students in the Agent Builder Academy
  need to assemble their project documentation. This skill is designed for the full Lovable.dev workflow
  and produces output that can be pasted directly into Lovable's Knowledge Base settings.
---

# Lovable PRD Builder

Generate a complete, Lovable.dev-optimized Product Requirements Document in four parts. Each document is crafted to work within Lovable's constraints (React + Vite + Tailwind + shadcn/ui + Supabase) and formatted so it can be used directly in Lovable's Knowledge Base settings.

## Why This Matters

Lovable.dev reads your Knowledge Base with every prompt. A well-structured PRD knowledge base means Lovable understands your project's architecture, design language, and scope boundaries from the first interaction — and maintains that understanding throughout the build. Poorly structured or vague docs lead to drift, rework, and wasted credits.

The four documents work together as a system:

1. **Masterplan** — The strategic brain. What you're building, why, for whom, and what's explicitly out of scope.
2. **Implementation Plan** — The tactical playbook. Prompt-sized build steps sequenced for Lovable's workflow.
3. **Design Guidelines** — The visual contract. Colors, typography, spacing, and components mapped to Tailwind classes and shadcn/ui.
4. **App Flow, Pages & Roles** — The structural blueprint. Routes, access control, user journeys, and component hierarchy.

## Before You Start

Read `references/lovable-platform.md` to understand Lovable.dev's tech stack, constraints, and how the Knowledge Base system works. This context shapes every document you'll produce.

## Workflow

### Phase 1: Project Discovery Interview

Before generating any documents, conduct a focused interview to understand the project. Ask about these areas (adapt based on what the user has already shared):

**Core Concept**
- What is the product in one sentence?
- What problem does it solve and for whom?
- What does success look like for the MVP?

**Target Users**
- Who are the primary users? (roles, technical level, context of use)
- Are there secondary users or admin roles?
- What's the most important thing a user should be able to do?

**Scope & Boundaries**
- What are 3-5 core features for the MVP?
- What should this explicitly NOT do in v1? (This is critical — Lovable can't infer boundaries from omission)
- Does it need authentication? What type?
- Does it need a database? What kind of data?

**Design Direction**
- What's the emotional tone? (e.g., playful, professional, minimal, bold)
- Any brand colors or fonts already decided?
- Any apps or websites whose aesthetic you admire?
- Does it need dark mode?

**Technical Needs**
- Any third-party API integrations?
- Real-time features needed? (chat, notifications, live updates)
- File uploads or media handling?
- Any data that needs to be pre-seeded?

Capture all answers before proceeding. If the user has already provided a project brief or partial PRD, extract answers from that context and confirm gaps.

### Phase 2: Generate the Masterplan

Read `references/masterplan-template.md` for the full template structure.

The Masterplan establishes the strategic foundation. Generate it by filling the template with the user's project specifics. Key principles:

- **Be explicit about non-goals.** Lovable will build whatever isn't explicitly excluded. If auth isn't in v1, say so. If mobile-native is never planned, say so.
- **Constrain the tech stack to Lovable's reality.** Always React + Vite + Tailwind CSS + shadcn/ui for frontend, Supabase for backend. Don't suggest alternatives.
- **Make the data model Supabase-native.** Think in PostgreSQL tables with Row Level Security. Include relationships and access patterns.
- **Keep the elevator pitch tight.** This gets referenced constantly — it should anchor every prompt Lovable receives.

Output as: `masterplan.md`

### Phase 3: Generate the Implementation Plan

Read `references/implementation-plan-template.md` for the full template structure.

The Implementation Plan translates the Masterplan into a build sequence optimized for Lovable's prompting workflow. Key principles:

- **One prompt, one task.** Each step should be a single, focused instruction that Lovable can execute without ambiguity.
- **Layout before behavior.** Get the visual structure right first, then add interactivity. Fixing layout after behavior is painful in Lovable.
- **Supabase setup early.** Database schema, auth config, and RLS policies should be established before building features that depend on them.
- **Stay under the instruction ceiling.** Research suggests AI coding agents handle ~150-200 instructions well before quality degrades. Keep each prompt focused.
- **Include checkpoint and revert strategy.** After each phase, test and verify before moving forward. Lovable's revert feature is your safety net.

Output as: `implementation-plan.md`

### Phase 4: Generate the Design Guidelines

Read `references/design-guidelines-template.md` for the full template structure.

The Design Guidelines create a visual contract that Lovable can execute precisely. Key principles:

- **Map everything to Tailwind utilities.** Don't just say "16px padding" — say `p-4`. Don't just say "#3B82F6" — say `bg-blue-500` / `text-blue-500`.
- **Reference shadcn/ui components by name.** If the button style should be "outline", say `<Button variant="outline">`. Lovable knows these components natively.
- **Include the Tailwind config values.** Custom colors, fonts, and spacing that extend the default theme should be expressed as `tailwind.config.ts` entries.
- **Design for the single-column constraint.** Lovable apps default to centered, max-width layouts. Work with this, not against it.

Output as: `design-guidelines.md`

### Phase 5: Generate the App Flow, Pages & Roles

Read `references/app-flow-template.md` for the full template structure.

The App Flow document maps the user experience to React Router routes, Supabase auth states, and component architecture. Key principles:

- **Every page is a route.** Map pages to `/path` patterns that React Router will use.
- **Every role maps to Supabase RLS.** Define who can access what and express it in terms Lovable can implement as Row Level Security policies.
- **User journeys are prompt sequences.** Each journey becomes a set of Lovable prompts that build the flow step by step.
- **Component hierarchy matters.** Name the layout components, shared elements, and page-specific components so Lovable creates a clean architecture.

Output as: `app-flow-pages-and-roles.md`

### Phase 6: Assemble & Deliver

Once all four documents are generated:

1. **Review for consistency.** Verify that tech choices, component names, color tokens, and feature scope align across all four documents.
2. **Generate a Knowledge Base summary.** Create a condensed version (under 2000 words) that combines the most critical information from all four docs — this is what gets pasted into Lovable's Knowledge Base settings panel. Save as `lovable-knowledge-base.md`.
3. **Package all files.** Save all five documents to the output directory.
4. **Brief the user.** Explain which document goes where:
   - `lovable-knowledge-base.md` → Paste into Lovable's Knowledge Base settings
   - The four full documents → Keep as reference, feed sections into Lovable prompts as needed
   - The Implementation Plan → Use as your prompt-by-prompt build sequence

## Output Files

All files are saved as markdown, ready for use:

| File | Purpose | Where It Goes |
|------|---------|---------------|
| `masterplan.md` | Strategic foundation | Reference doc, sections fed to Lovable as needed |
| `implementation-plan.md` | Build sequence | Your prompt-by-prompt guide for the Lovable build |
| `design-guidelines.md` | Visual contract | Paste key sections into Knowledge Base |
| `app-flow-pages-and-roles.md` | Structural blueprint | Reference for routes, roles, components |
| `lovable-knowledge-base.md` | Condensed knowledge base | Paste directly into Lovable's Knowledge Base settings |

## Tips for Students

If you're using this as part of the Agent Builder Academy curriculum:

- **Foundation & Practitioner courses**: Work through all four documents for your capstone project. The discipline of writing these docs is as valuable as the output — it forces you to think through your product before touching Lovable.
- **Professional Vibe Coder bootcamp**: Use the Implementation Plan as your literal build script. Each phase maps to a Lovable session. Time yourself — this teaches prompt efficiency.
- **Sharing with teammates**: The Knowledge Base summary is your "project handoff" document. Anyone with it can pick up your Lovable build and maintain context.

## Resources

### references/
- `lovable-platform.md` — Lovable.dev tech stack, constraints, Knowledge Base system, and prompting best practices
- `masterplan-template.md` — Full Masterplan template with section-by-section guidance
- `implementation-plan-template.md` — Full Implementation Plan template with prompt-sized task breakdown
- `design-guidelines-template.md` — Full Design Guidelines template with Tailwind/shadcn/ui mappings
- `app-flow-template.md` — Full App Flow template with route/role/component patterns
