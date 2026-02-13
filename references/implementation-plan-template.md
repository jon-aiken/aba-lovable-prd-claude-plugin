# Implementation Plan Template

Use this template to generate the `implementation-plan.md` document. Every step in this plan is designed as a single Lovable prompt — one focused instruction that Lovable can execute cleanly.

The core philosophy: **Layout → Data → Behavior → Polish.** Get the structure right before wiring things up.

---

## Template Structure

```markdown
# [Project Name] — Implementation Plan

## Build Philosophy

This plan follows the Lovable-optimized build sequence:

1. **Foundation first** — Project setup, Supabase connection, global styles
2. **Layout before behavior** — Build every page's visual structure before adding interactivity
3. **Data layer next** — Connect Supabase tables, set up queries, wire data to components
4. **Behavior last** — Add form handlers, state management, real-time features
5. **Polish to finish** — Loading states, error handling, animations, responsive tweaks

Each step is a single Lovable prompt. Complete one, verify it works, then move to the next. Use Lovable's revert feature if anything breaks.

## Pre-Build Checklist

Before opening Lovable:

- [ ] Masterplan document complete and reviewed
- [ ] Design Guidelines document complete (colors, fonts, spacing defined)
- [ ] App Flow document complete (routes, roles, components named)
- [ ] Supabase project created at supabase.com
- [ ] Supabase project URL and anon key ready
- [ ] Knowledge Base content prepared (from lovable-knowledge-base.md)

## Phase 0 — Project Foundation

**Goal**: Establish the project skeleton, global configuration, and design system.
**Duration estimate**: 1 Lovable session (15-30 min)

### Step 0.1 — Create project and set Knowledge Base
**Prompt pattern**: Create a new Lovable project, then paste the Knowledge Base content into Project Settings → Knowledge.
**Verify**: Knowledge Base is saved and visible in settings.

### Step 0.2 — Configure global styles and theme
**Prompt**: "Set up the Tailwind config with these custom values: [paste design tokens from Design Guidelines — custom colors, fonts, spacing]. Update the global CSS to import [specified Google Fonts]. Set the default font to [primary font]."
**Verify**: Create a test page and confirm fonts and colors render correctly.

### Step 0.3 — Set up Supabase connection
**Prompt**: "Connect this project to Supabase using project URL [URL] and anon key [KEY]. Set up the Supabase client in src/integrations/supabase/client.ts."
**Verify**: Supabase connection status shows green in Lovable.

### Step 0.4 — Create shared layout components
**Prompt**: "Create a main layout component at src/components/Layout.tsx with: [describe header, sidebar/nav, main content area, footer based on App Flow document]. Use shadcn/ui [NavigationMenu/Sheet/etc.] for the navigation. Make it responsive — sidebar collapses to a hamburger menu on mobile."
**Verify**: Layout renders correctly at desktop and mobile breakpoints.

**CHECKPOINT**: Project foundation is solid. Global styles work, Supabase is connected, layout component exists. Take a screenshot for reference.

## Phase 1 — Database & Auth Setup

**Goal**: Create Supabase tables, RLS policies, and authentication flow.
**Duration estimate**: 1 Lovable session (20-40 min)

### Step 1.1 — Create database tables
**Prompt**: "Create these Supabase database tables: [paste table definitions from Masterplan data model — table names, columns, types, foreign keys]. Add created_at and updated_at timestamps to all tables."
**Verify**: Check Supabase dashboard — all tables exist with correct columns.

### Step 1.2 — Set up Row Level Security
**Prompt**: "Enable Row Level Security on all tables. Create these RLS policies: [paste RLS descriptions from Masterplan, expressed as rules]. For the profiles table: users can read and update their own profile. For [table]: [policy]."
**Verify**: Test RLS by querying as different user roles in Supabase SQL editor.

### Step 1.3 — Configure authentication
**Prompt**: "Set up Supabase Auth with [email/password, Google OAuth, magic links — as specified in Masterplan]. Create a login page at /login and a signup page at /signup using shadcn/ui Form, Input, and Button components. Include form validation with Zod. Redirect to /dashboard after successful login."
**Verify**: Can create an account and log in. Redirect works.

### Step 1.4 — Create user profile system
**Prompt**: "When a new user signs up, automatically create a profile row in the profiles table using a Supabase database trigger. Create a useAuth hook that provides the current user and their profile data throughout the app."
**Verify**: Sign up a test user, confirm profile row appears in Supabase.

**CHECKPOINT**: Auth works end-to-end. Users can sign up, log in, and their profile is created. RLS policies are active. Test with at least 2 accounts.

## Phase 2 — Page Layouts (Structure Only)

**Goal**: Build the visual structure of every page. No data, no behavior — just layout.
**Duration estimate**: 1-2 Lovable sessions (30-60 min)

### Step 2.1 — [Page 1 name] layout
**Prompt**: "Create the [Page 1] page at [/route]. Layout: [describe the structure — header area, content sections, sidebar if any, action buttons]. Use shadcn/ui [Card, Table, Tabs — whatever components fit]. Use placeholder/mock data for now — we'll connect real data later. Apply the design system: [reference key design tokens]."
**Verify**: Page looks correct with placeholder data. Responsive at all breakpoints.

### Step 2.2 — [Page 2 name] layout
[Same pattern — one page per step]

### Step 2.3 — [Page 3 name] layout
[Same pattern]

[Continue for each page in the App Flow document]

### Step 2.N — Set up routing
**Prompt**: "Configure React Router with these routes: [list all routes from App Flow]. Add route protection — routes that require authentication should redirect to /login if the user is not signed in. Use the Layout component as the parent wrapper for authenticated routes."
**Verify**: Navigate to each route. Protected routes redirect correctly. Layout wraps all pages.

**CHECKPOINT**: Every page exists and looks right with placeholder data. Navigation works. Routes are protected. This is the visual skeleton of the entire app.

## Phase 3 — Data Layer

**Goal**: Replace placeholder data with real Supabase queries. Connect forms to the database.
**Duration estimate**: 1-2 Lovable sessions (30-60 min)

### Step 3.1 — Create data hooks
**Prompt**: "Create custom hooks for data fetching: [useItems, useProjects, etc. — one hook per main entity]. Each hook should use Supabase client to query the [table] table. Include loading and error states. Use React Query (TanStack Query) for caching and refetching."
**Verify**: Hooks return data. Check browser devtools network tab.

### Step 3.2 — Connect [Page 1] to real data
**Prompt**: "Replace the placeholder data on the [Page 1] page with the [useItems] hook. Show a loading skeleton using shadcn/ui Skeleton component while data loads. Show an empty state with a call-to-action if no data exists."
**Verify**: Page shows real data from Supabase. Loading and empty states work.

### Step 3.3 — Connect [Page 2] to real data
[Same pattern for each page]

[Continue for each page that displays data]

**CHECKPOINT**: All pages display real data from Supabase. Loading states show during fetch. Empty states display when no data exists. No more placeholder content.

## Phase 4 — Core Behavior

**Goal**: Add interactivity — form submissions, create/update/delete operations, state changes.
**Duration estimate**: 1-2 Lovable sessions (30-60 min)

### Step 4.1 — [Feature 1] — Create functionality
**Prompt**: "Add a create [item] form to the [Page] page. Use shadcn/ui Dialog for the modal, Form + Input components for the fields. Validate with Zod: [specify validation rules]. On submit, insert into the [table] Supabase table and refresh the list."
**Verify**: Can create a new item. It appears in the list immediately. Validation prevents bad input.

### Step 4.2 — [Feature 1] — Edit functionality
**Prompt**: "Add edit capability to [items]. Clicking an item opens the same form pre-filled with existing data. On submit, update the row in Supabase and refresh."
**Verify**: Can edit an existing item. Changes persist.

### Step 4.3 — [Feature 1] — Delete functionality
**Prompt**: "Add delete capability to [items]. Show a confirmation dialog using shadcn/ui AlertDialog before deleting. On confirm, delete the row from Supabase and refresh the list."
**Verify**: Can delete an item after confirming. Item disappears from list.

### Step 4.4 — [Feature 2] — [Core behavior]
[Same pattern — break each feature into create/read/update/delete steps]

[Continue for each core feature]

**CHECKPOINT**: All CRUD operations work for all core features. Data persists in Supabase. Forms validate correctly. Error handling covers the basics.

## Phase 5 — Enhanced Features [IF APPLICABLE]

**Goal**: Add features beyond basic CRUD — search, filtering, real-time updates, file uploads, etc.
**Duration estimate**: 1-2 Lovable sessions (variable)

### Step 5.1 — [Enhanced Feature: Search/Filter]
**Prompt**: "[Describe the specific enhanced feature and how it should work within the existing UI]"
**Verify**: [Specific verification criteria]

### Step 5.2 — [Enhanced Feature: Real-time]
**Prompt**: "[Describe real-time subscription setup]"
**Verify**: Open in two browser tabs, verify changes appear in real-time.

[Continue for each enhanced feature]

**CHECKPOINT**: Enhanced features work correctly alongside core functionality. No regressions in existing features.

## Phase 6 — Polish & QA

**Goal**: Loading states, error handling, responsive refinements, animations, and accessibility.
**Duration estimate**: 1 Lovable session (20-40 min)

### Step 6.1 — Error handling
**Prompt**: "Add error handling throughout the app: show shadcn/ui Toast notifications for all failed operations (create, update, delete, fetch errors). Use a friendly tone — e.g., 'Something went wrong. Please try again.' Add a generic error boundary component that catches unhandled errors."
**Verify**: Disconnect internet and trigger operations — errors show gracefully.

### Step 6.2 — Loading states
**Prompt**: "Add loading states to all data-dependent pages using shadcn/ui Skeleton components. Add loading spinners to submit buttons while operations are in progress. Disable buttons during loading to prevent double-submits."
**Verify**: Throttle network in devtools and verify loading states appear.

### Step 6.3 — Responsive polish
**Prompt**: "Review all pages at mobile (375px), tablet (768px), and desktop (1280px) widths. Fix any layout issues: [list specific problems found during testing]. Ensure touch targets are at least 44px on mobile."
**Verify**: Test at all three breakpoints. No horizontal scrolling. No overlapping elements.

### Step 6.4 — Micro-interactions [IF APPLICABLE]
**Prompt**: "Add subtle animations: fade-in for page transitions, hover effects on interactive cards (slight shadow lift), smooth skeleton-to-content transitions. Keep all animations under 200ms. Use Tailwind's transition utilities."
**Verify**: Animations feel smooth and intentional, never distracting.

### Step 6.5 — Accessibility audit
**Prompt**: "Audit the app for accessibility: ensure all images have alt text, all form inputs have labels, focus states are visible on all interactive elements, heading hierarchy is correct (h1 → h2 → h3, no skipped levels), color contrast meets WCAG AA. Add aria-labels to icon-only buttons."
**Verify**: Tab through the entire app using keyboard only. Use browser accessibility inspector.

**CHECKPOINT**: App is polished and production-ready. All error states handled. Responsive at all breakpoints. Accessible via keyboard.

## Deployment

### Step 7.1 — Deploy to Lovable hosting
**Prompt**: "Deploy this project to Lovable hosting."
**Verify**: Access the deployed URL. Test core features in production.

### Step 7.2 — Custom domain [IF APPLICABLE]
**Prompt**: Configure custom domain in Lovable project settings.
**Verify**: Domain resolves and app loads.

## Timeline Estimate

| Phase | Estimated Duration | Lovable Sessions |
|-------|-------------------|-----------------|
| Phase 0 — Foundation | 15-30 min | 1 |
| Phase 1 — Database & Auth | 20-40 min | 1 |
| Phase 2 — Page Layouts | 30-60 min | 1-2 |
| Phase 3 — Data Layer | 30-60 min | 1-2 |
| Phase 4 — Core Behavior | 30-60 min | 1-2 |
| Phase 5 — Enhanced Features | Variable | 1-2 |
| Phase 6 — Polish & QA | 20-40 min | 1 |
| **Total** | **3-6 hours** | **7-11 sessions** |

Note: These estimates assume well-written PRD documents and focused prompting. Budget 2x for learning projects or complex apps.
```

---

## Guidance for Generating the Plan

### Customizing the Template

When generating a project-specific implementation plan:

1. **Replace all bracketed placeholders** with project-specific names, routes, features, and descriptions from the Masterplan and App Flow documents.
2. **Adjust the number of steps per phase** based on the project's complexity. Simple apps might have 2-3 pages; complex ones might have 8-10.
3. **Add or remove Phase 5** based on whether enhanced features exist in the Masterplan.
4. **Adjust timeline estimates** based on project complexity and student experience level.

### Writing Effective Prompt Patterns

Each step's "Prompt" field should be a near-ready-to-paste instruction for Lovable. Good prompts:

- Start with a clear action verb (Create, Add, Configure, Connect, Replace)
- Name specific shadcn/ui components to use
- Reference specific Tailwind classes for styling
- Specify exact file paths when relevant (src/pages/Dashboard.tsx)
- Include validation rules and error messages
- Describe the expected outcome

### Checkpoint Strategy

Checkpoints are non-negotiable pauses. At each checkpoint:

1. Test everything that was just built
2. Verify in Supabase dashboard that data is correct
3. Test at mobile and desktop breakpoints
4. Take a mental snapshot of the working state (in case you need to revert)

If something is broken at a checkpoint, fix it before proceeding. Accumulating technical debt in a Lovable build is expensive — future prompts compound on the current state.
