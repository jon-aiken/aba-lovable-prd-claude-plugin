# Lovable.dev Platform Reference

This document captures everything you need to know about Lovable.dev's capabilities and constraints before writing PRD documents. Read this first — it shapes every decision in the other four documents.

## Tech Stack (Fixed — Not Negotiable)

Lovable generates code in a specific stack. You cannot change these choices:

| Layer | Technology | Notes |
|-------|-----------|-------|
| **Framework** | React 18+ | No Angular, Vue, Svelte, or Next.js |
| **Build Tool** | Vite | Fast HMR, ESM-native |
| **Styling** | Tailwind CSS | Utility-first, all styling via classes |
| **Components** | shadcn/ui | 40+ pre-built components (Button, Card, Dialog, etc.) |
| **Language** | TypeScript | Strict mode, all code is typed |
| **Backend** | Supabase | PostgreSQL database, auth, storage, real-time, edge functions |
| **Routing** | React Router | Client-side routing with nested layouts |
| **State** | React hooks | useState, useEffect, useContext, custom hooks |
| **Deployment** | Lovable hosting | One-click deploy, custom domains available |

### What Lovable Cannot Do

These are hard constraints — do not plan for these in your PRD:

- **No server-side rendering (SSR)** — It's a client-side SPA
- **No native mobile apps** — Web only, responsive design via Tailwind
- **No Python, Ruby, Node.js backends** — Backend logic goes through Supabase Edge Functions (Deno/TypeScript)
- **No custom webpack/build configs** — Vite config is managed by Lovable
- **No direct server access** — No SSH, no file system, no cron jobs outside Supabase
- **No other CSS frameworks** — No Bootstrap, Material UI, or Chakra alongside Tailwind
- **No complex multi-service architectures** — Single Supabase project per app

### What Lovable Does Well

Play to these strengths in your PRD:

- **Rapid UI generation** — Describe a layout and get pixel-perfect React + Tailwind
- **shadcn/ui integration** — Reference components by name and they work immediately
- **Supabase scaffolding** — Auth flows, database tables, RLS policies, storage buckets
- **Responsive design** — Tailwind breakpoints work out of the box
- **Real-time features** — Supabase subscriptions for live updates
- **Form handling** — React Hook Form + Zod validation patterns
- **Data tables** — TanStack Table integration

## Supabase Backend Model

All backend functionality runs through Supabase. Your data model should think in these terms:

**Database**: PostgreSQL with Row Level Security (RLS)
- Tables map to your data entities
- RLS policies control who can read/write what
- Foreign keys define relationships
- Views for complex queries
- Database functions for business logic

**Authentication**: Built-in auth with multiple providers
- Email/password, magic links, OAuth (Google, GitHub, etc.)
- Session management handled automatically
- User metadata stored in `auth.users`
- Custom user profiles in a `public.profiles` table

**Storage**: File storage with access policies
- Buckets for organizing files
- Storage policies (similar to RLS) for access control
- Public and private buckets
- Image transformations available

**Edge Functions**: Serverless TypeScript/Deno functions
- For third-party API calls
- Webhook handlers
- Complex business logic that shouldn't be client-side
- Scheduled via Supabase cron (pg_cron)

**Real-time**: Live data subscriptions
- Subscribe to database changes
- Presence (who's online)
- Broadcast (custom events)

## Knowledge Base System

Lovable's Knowledge Base is a text field in Project Settings → Knowledge → Manage Knowledge. Everything you put there gets sent with every prompt.

### How It Works

- The Knowledge Base content is prepended to every prompt you send
- It persists across all sessions for that project
- It has no formal structure requirement — it's freeform text
- Lovable references it to maintain consistency

### What to Put In

The Knowledge Base is most effective when it contains:

1. **Project identity** — One-paragraph description of what you're building
2. **Design tokens** — Colors, fonts, spacing expressed as Tailwind values
3. **Component conventions** — Which shadcn/ui components to prefer, naming patterns
4. **Data model summary** — Key tables, relationships, access patterns
5. **Scope boundaries** — What the app does NOT do (explicit non-goals)
6. **Coding conventions** — File naming, folder structure, import patterns

### What NOT to Put In

- Long narratives or backstory (wastes token budget)
- Information that changes frequently (update friction)
- Implementation details for features not yet built (confuses context)
- Duplicate information across sections (token waste)

### Size Guidance

Keep the Knowledge Base under 2000 words. Lovable sends it with every prompt, so bloated knowledge bases slow responses and dilute focus. Be concise and precise.

## Prompting Best Practices

### The Golden Rule: One Prompt, One Task

Lovable works best when each prompt does one thing. Instead of "Build the entire settings page with form validation, dark mode toggle, and profile picture upload," break it into:

1. "Create the Settings page layout with a sidebar navigation and content area"
2. "Add a profile form with name, email, and bio fields using shadcn/ui Form components"
3. "Add form validation using Zod schema — name required, email must be valid"
4. "Add a dark mode toggle using shadcn/ui Switch component"
5. "Add profile picture upload connected to Supabase Storage"

### Layout First, Behavior Second

Get the visual structure right before adding interactivity. Fixing layout after you've wired up state and API calls is painful — Lovable may break the behavior while fixing the layout.

Sequence: Structure → Styling → Data → Behavior → Polish

### The ~150 Instruction Ceiling

Research suggests AI coding agents maintain quality with roughly 150-200 instructions per context. Beyond that, quality degrades. This means:

- Keep Knowledge Base concise (it counts toward the ceiling)
- Don't stack too many requirements in a single prompt
- Use the Implementation Plan to stay focused per session

### Revert Is Your Safety Net

Lovable has a revert feature in the chat history. Use it aggressively:

- Test after every significant change
- If something breaks, revert immediately rather than trying to fix forward
- Revert is cheaper than debugging loops (which waste credits)

### Reference shadcn/ui Components by Name

Lovable knows shadcn/ui natively. When you reference components by their exact names, you get consistent, high-quality output:

- `Button`, `Card`, `Dialog`, `Sheet`, `Popover`
- `Form`, `Input`, `Select`, `Textarea`, `Checkbox`, `Switch`
- `Table`, `Tabs`, `Accordion`, `Alert`, `Badge`
- `Avatar`, `Skeleton`, `Tooltip`, `Toast`
- `DropdownMenu`, `NavigationMenu`, `Command`, `Calendar`

### Reference Tailwind Classes Directly

Instead of describing styles abstractly, use Tailwind class names:

- "Add `p-6 space-y-4` to the card container"
- "Make the heading `text-2xl font-semibold tracking-tight`"
- "Use `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6` for the card grid"

## File Structure Convention

Lovable generates projects with this structure:

```
src/
├── components/          # Reusable UI components
│   └── ui/             # shadcn/ui components (auto-managed)
├── hooks/              # Custom React hooks
├── lib/                # Utilities, Supabase client, helpers
├── pages/              # Route-level page components
├── types/              # TypeScript type definitions
├── integrations/       # Supabase client config, auto-generated types
└── App.tsx             # Root component with router
```

Reference this structure in your PRD so component placement is unambiguous.
