Lovable PRD Builder
A Claude Cowork plugin that guides you through building a complete, Lovable.dev-ready Product Requirements Document. It generates five structured documents — Masterplan, Implementation Plan, Design Guidelines, App Flow (Pages & Roles), and a condensed Knowledge Base — all optimized for Lovable's React/Vite/Tailwind/shadcn/Supabase stack.
Built by Agent Builder Academy.

What It Does
When you tell Claude to "build a PRD", "plan my Lovable project", or "create a masterplan", this plugin activates a guided workflow:

Discovery Interview — Claude asks focused questions about your product concept, users, scope, design direction, and technical needs.
Masterplan — Strategic foundation: elevator pitch, features, non-goals, data model, and phased roadmap.
Implementation Plan — Prompt-by-prompt build sequence organized into 7 phases, each step sized for a single Lovable prompt.
Design Guidelines — Visual contract with colors, typography, and components mapped directly to Tailwind classes and shadcn/ui components.
App Flow, Pages & Roles — Every route wireframed, user roles mapped to Supabase RLS policies, component architecture defined.
Knowledge Base Summary — A condensed version (under 2,000 words) you paste directly into Lovable's Knowledge Base settings.

The five output files are cross-referenced and consistent — same color hex values, same table names, same route paths, same component names across every document.

Installation
Option 1: Install from GitHub (recommended)
Open a terminal and run:
bashclaude plugin add jon-aiken/aba-lovable-prd-claude-plugin
That's it. The plugin is now available in Claude Cowork.
Option 2: Manual installation

Clone the repository into your Claude plugins directory:

bashgit clone https://github.com/jon-aiken/aba-lovable-prd-claude-plugin.git ~/.claude/plugins/lovable-prd-builder

Restart Claude Cowork (or start a new session) to pick up the plugin.

Verify installation
In a Claude Cowork session, type:
Build me a PRD for a Lovable project
If the plugin is installed correctly, Claude will begin the Discovery Interview workflow.

Usage
Starting a new PRD
Say any of the following to activate the plugin:

"Build a PRD for my app"
"Plan my Lovable project"
"Create a masterplan"
"Prepare my build docs"
"Start a new project for Lovable"
"Lovable knowledge base"

Claude will walk you through the Discovery Interview, then generate all five documents.
What you get
FilePurposeWhere to use itmasterplan.mdStrategic foundationReference doc; feed sections into Lovable prompts as neededimplementation-plan.mdBuild sequenceYour prompt-by-prompt guide for the Lovable builddesign-guidelines.mdVisual contractPaste key sections into Lovable's Knowledge Baseapp-flow-pages-and-roles.mdStructural blueprintReference for routes, roles, and componentslovable-knowledge-base.mdCondensed summaryPaste directly into Lovable's Project Settings > Knowledge
After generating

Open your Lovable project at lovable.dev
Go to Project Settings > Knowledge
Paste the contents of lovable-knowledge-base.md
Open implementation-plan.md and follow it phase by phase — each step is a single Lovable prompt


Plugin Structure
lovable-prd-builder/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest (name, version, metadata)
├── SKILL.md                     # Main skill — orchestrates the 6-phase workflow
├── references/
│   ├── api_reference.md         # Index of all reference files
│   ├── lovable-platform.md      # Lovable.dev platform reference (stack, constraints, KB system)
│   ├── masterplan-template.md   # Masterplan document template with guidance
│   ├── implementation-plan-template.md  # Implementation plan template
│   ├── design-guidelines-template.md    # Design guidelines template
│   └── app-flow-template.md     # App flow, pages & roles template
├── scripts/
│   └── example.py               # Assembly script to combine all docs into one file
├── assets/
│   └── example_asset.txt        # Placeholder for future assets
└── README.md

What's in the Reference Files
The references/ directory contains the templates and platform knowledge that power the plugin:
lovable-platform.md — Everything you need to know about Lovable.dev: the fixed tech stack (React 18+ / Vite / Tailwind CSS / TypeScript / shadcn/ui / Supabase), hard constraints (no SSR, no native mobile, no Python backends), the Knowledge Base system, prompting best practices, and supported shadcn/ui components.
masterplan-template.md — Full template for the strategic document: elevator pitch, problem/mission, target audience, core features (3-7 for MVP), explicit non-goals, Supabase-native data model, UI design principles, security model, phased roadmap, and risks.
implementation-plan-template.md — 7-phase build template: Foundation, Database & Auth, Page Layouts, Data Layer, Core Behavior, Enhanced Features, and Polish & QA. Each step is formatted as a single Lovable prompt with verification steps and checkpoint markers.
design-guidelines-template.md — Visual system template: color system as tailwind.config.ts extensions, typography scale mapped to Tailwind classes, spacing scale, responsive breakpoints, shadcn/ui component usage table, button hierarchy, card/form patterns, motion guidelines, voice & tone, and accessibility requirements.
app-flow-template.md — Structural blueprint template: site map with React Router paths, page specifications with ASCII wireframes, user roles mapped to Supabase RLS policies (with SQL examples), user journeys mapped to build phases, component architecture tables, and navigation structure.

For Agent Builder Academy Students
This plugin is designed for use across all three ABA courses:
Foundation Course — Use the Discovery Interview to practice thinking through a product before building. The four documents teach you the discipline of planning that separates good vibe coders from great ones.
Practitioner Course (Certified Agent Builder) — Generate all four documents for your capstone project. The Implementation Plan becomes your literal build script — each phase maps to a Lovable session.
Professional Vibe Coder Bootcamp — Use the Implementation Plan as a speed challenge. Time yourself through each phase. This teaches prompt efficiency and helps you understand Lovable's credit economics.
The Knowledge Base summary is also your "project handoff" document — anyone with it can pick up your Lovable build and maintain full context.

Tech Stack Covered
This plugin generates documentation specifically for Lovable.dev's fixed stack:

Frontend: React 18+ / TypeScript / Vite / Tailwind CSS / shadcn/ui / React Router v6
Backend: Supabase (PostgreSQL + Auth + Storage + Real-time + Edge Functions)
Forms: React Hook Form + Zod validation
Data Fetching: TanStack Query (React Query)
Icons: Lucide React


Contributing
Found a bug or want to improve a template? Pull requests are welcome.

Fork the repository
Create a feature branch (git checkout -b improve-template)
Commit your changes (git commit -m "Improve masterplan template guidance")
Push to the branch (git push origin improve-template)
Open a Pull Request


License
MIT License. See LICENSE for details.

Built with care by Agent Builder Academy — teaching students to build products with AI tools.
