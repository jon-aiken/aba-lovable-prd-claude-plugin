# Masterplan Template

Use this template to generate the `masterplan.md` document. Fill every section with the user's project specifics. Sections marked [REQUIRED] must be completed; sections marked [IF APPLICABLE] can be omitted if they don't apply.

---

## Template Structure

```markdown
# [Project Name] — Masterplan

## Elevator Pitch
[2-3 sentences maximum. What is it, who is it for, why does it matter. This anchors every Lovable prompt — keep it tight and memorable.]

## Problem & Mission

### Problem
[Describe the specific pain point in 2-3 sentences. Be concrete — name the frustration, the inefficiency, or the gap. Avoid generic statements like "current solutions are inadequate."]

### Mission
[One sentence. What does the product do about the problem? Frame as: "Build [thing] that [solves problem] for [audience]."]

## Target Audience

### Primary Users
[Describe the main user persona. Include: role/title, technical comfort level, context of use (when/where they'd use this), and what they care about most.]

### Secondary Users [IF APPLICABLE]
[Any additional user types — admins, managers, collaborators, etc. Same format as primary.]

### User Needs Summary
| User Type | Primary Need | Key Frustration |
|-----------|-------------|-----------------|
| [Primary] | [What they need to accomplish] | [What makes current solutions painful] |
| [Secondary] | [What they need to accomplish] | [What makes current solutions painful] |

## Core Features (MVP)

List 3-7 features for the minimum viable product. Each feature gets:
- A clear name
- A one-sentence description of what it does
- Why it matters (the user value)

### 1. [Feature Name]
[What it does in one sentence.]
**Why**: [User value in one sentence.]

### 2. [Feature Name]
[What it does in one sentence.]
**Why**: [User value in one sentence.]

### 3. [Feature Name]
[What it does in one sentence.]
**Why**: [User value in one sentence.]

[Continue as needed, max 7 for MVP]

## Explicit Non-Goals (v1)

This section is critical for Lovable builds. AI coding agents will implement anything not explicitly excluded. Be direct and specific.

- **[Non-goal 1]**: [Why it's out of scope. e.g., "Native mobile app — this is a web-first product. Mobile responsiveness via Tailwind is sufficient for v1."]
- **[Non-goal 2]**: [Why it's out of scope.]
- **[Non-goal 3]**: [Why it's out of scope.]
- **[Non-goal 4]**: [Why it's out of scope.]

Common non-goals to consider:
- Native mobile apps
- Multi-language/i18n support
- Advanced analytics dashboards
- Payment processing
- Email notification system
- Public API
- Multi-tenancy
- Offline support
- Complex role hierarchies beyond basic admin/user

## Tech Stack

### Frontend
- **Framework**: React 18+ with TypeScript
- **Build**: Vite
- **Styling**: Tailwind CSS
- **Components**: shadcn/ui
- **Routing**: React Router v6
- **Forms**: React Hook Form + Zod validation
- **State**: React hooks (useState, useContext, custom hooks)

### Backend (Supabase)
- **Database**: PostgreSQL with Row Level Security
- **Auth**: Supabase Auth ([specify providers: email/password, Google OAuth, magic links, etc.])
- **Storage**: Supabase Storage ([specify if needed: profile images, file uploads, etc.])
- **Real-time**: Supabase Realtime ([specify if needed: live updates, presence, etc.])
- **Edge Functions**: Supabase Edge Functions ([specify if needed: third-party API calls, webhooks, etc.])

### External Integrations [IF APPLICABLE]
| Service | Purpose | Integration Method |
|---------|---------|-------------------|
| [Service name] | [What it does for your app] | [API call via Edge Function / client-side SDK / webhook] |

## Data Model

Define your core entities as Supabase/PostgreSQL tables. Include the table name, key columns, relationships, and access patterns.

### [Table: profiles]
Extends Supabase auth.users with application-specific data.
| Column | Type | Notes |
|--------|------|-------|
| id | uuid (PK) | References auth.users.id |
| [column] | [type] | [notes] |
| created_at | timestamptz | Default: now() |
| updated_at | timestamptz | Auto-updated |

**RLS Policy**: Users can read/update their own profile. Admins can read all.

### [Table: your_main_entity]
[Description of what this table stores.]
| Column | Type | Notes |
|--------|------|-------|
| id | uuid (PK) | Default: gen_random_uuid() |
| user_id | uuid (FK) | References profiles.id |
| [column] | [type] | [notes] |
| created_at | timestamptz | Default: now() |

**RLS Policy**: [Who can read? Who can write? Who can delete?]

[Continue for each table]

### Relationships
[Describe key relationships: one-to-many, many-to-many (via junction tables), etc.]

## UI Design Principles

[3-5 principles that guide the visual and interaction design. These should be actionable — not just "clean and modern" but specific enough for Lovable to execute.]

1. **[Principle]**: [What it means in practice. e.g., "Content-first layout — minimize chrome, maximize the user's content. Use shadcn/ui Card components to create clear content boundaries without heavy borders."]
2. **[Principle]**: [What it means in practice.]
3. **[Principle]**: [What it means in practice.]

## Security & Compliance

### Authentication
[Describe auth approach: email/password, OAuth providers, magic links, etc.]

### Authorization
[Describe role-based access: what each role can do. This maps directly to Supabase RLS policies.]

### Data Protection
- All data encrypted in transit (HTTPS) and at rest (Supabase default)
- [Specify any GDPR/CCPA requirements]
- [Specify data retention policies]
- [Specify if users can export/delete their data]

## Phased Roadmap

### MVP (Phase 1)
[What ships first. Map to the Core Features section above.]
**Success metric**: [How you know the MVP works — e.g., "10 users can complete the core workflow without assistance."]

### V1 (Phase 2) [IF APPLICABLE]
[What comes after MVP.]
**Unlocked by**: [What MVP learning triggers this phase.]

### V2 (Phase 3) [IF APPLICABLE]
[Longer-term vision.]
**Unlocked by**: [What V1 learning triggers this phase.]

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk description] | [What happens if it occurs] | [How to prevent or handle it] |
| Lovable credit consumption | Build takes more prompts than expected | Break tasks small, test frequently, use revert aggressively |
| Scope creep during build | Features expand beyond MVP | Reference non-goals list before every Lovable session |
| [Project-specific risk] | [Impact] | [Mitigation] |

## Future Expansion Ideas

[Brief list of ideas beyond the roadmap. These are not commitments — they're signals of where the product could go. Keep to 3-5 bullet points.]

- [Idea 1]
- [Idea 2]
- [Idea 3]
```

---

## Section-by-Section Guidance

### Elevator Pitch
The elevator pitch is the single most referenced piece of text across all documents. It should be tight enough to memorize. Test it: if someone reads only this, do they understand what the product is?

### Non-Goals
This section prevents Lovable from building features you didn't ask for. AI agents interpret ambiguity as license to build. Every feature you don't want in v1 needs to be explicitly called out. When in doubt, add it to non-goals.

### Data Model
Think in Supabase terms from the start. Every table needs:
- A UUID primary key (Supabase convention)
- A created_at timestamp
- An RLS policy description (who can CRUD)
- Foreign key relationships spelled out

Avoid abstract ERD language. Use actual PostgreSQL types: `uuid`, `text`, `timestamptz`, `boolean`, `jsonb`, `integer`, etc.

### Tech Stack
This section is mostly pre-filled for Lovable projects. The main decisions are:
- Which Supabase Auth providers to enable
- Whether you need Supabase Storage
- Whether you need Supabase Realtime
- Whether you need Edge Functions (for third-party APIs)
- Any external libraries beyond the default stack

### Risks
Always include two standard Lovable risks: credit consumption and scope creep. Then add 2-3 project-specific risks. Keep mitigations actionable, not aspirational.
