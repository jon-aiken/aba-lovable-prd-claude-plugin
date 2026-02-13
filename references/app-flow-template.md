# App Flow, Pages & Roles Template

Use this template to generate the `app-flow-pages-and-roles.md` document. Every page maps to a React Router route, every role maps to a Supabase RLS policy, and every component maps to a file in the project structure.

This document is the architectural blueprint that tells Lovable exactly what to build and where to put it.

---

## Template Structure

```markdown
# [Project Name] — App Flow, Pages & Roles

## Site Map

A flat list of every top-level page with its React Router path:

| # | Page Name | Route | Auth Required | Purpose (one line) |
|---|-----------|-------|:------------:|-------------------|
| 1 | Landing | `/` | No | Explain value and drive signup |
| 2 | Login | `/login` | No | User authentication |
| 3 | Signup | `/signup` | No | Account creation |
| 4 | Dashboard | `/dashboard` | Yes | Main workspace after login |
| [N] | [Page] | [/route] | [Yes/No] | [Purpose] |
| — | Not Found | `*` | No | 404 error page |

**Total pages**: [N]
**Authenticated pages**: [N]
**Public pages**: [N]

## Page Specifications

For each page, define its layout, components, data needs, and behavior.

### 1. Landing Page (`/`)

**Purpose**: [One sentence — what this page accomplishes]
**Auth state**: Public (no login required)
**Redirect logic**: If user is already logged in, redirect to `/dashboard`

**Layout**:
```
┌─────────────────────────────────────────┐
│  Header: Logo + Nav (Login / Signup)    │
├─────────────────────────────────────────┤
│  Hero Section:                          │
│  - Headline (H1)                        │
│  - Subheadline (Body)                   │
│  - CTA Button → /signup                 │
├─────────────────────────────────────────┤
│  Features Section:                      │
│  - 3-column card grid                   │
│  - Icon + Title + Description per card  │
├─────────────────────────────────────────┤
│  [Additional sections as needed]        │
├─────────────────────────────────────────┤
│  Footer: Links + Copyright              │
└─────────────────────────────────────────┘
```

**Components used**:
- `Button` (CTA) → variant: `default`, size: `lg`
- `Card` → for feature cards
- `NavigationMenu` → top navigation

**Data needs**: None (static content)
**Key interactions**: CTA click → navigate to `/signup`

---

### 2. Login Page (`/login`)

**Purpose**: Authenticate existing users
**Auth state**: Public (redirect to `/dashboard` if already authenticated)

**Layout**:
```
┌─────────────────────────────────────────┐
│  Centered card (max-w-md mx-auto):      │
│  ┌─────────────────────────────────┐    │
│  │  Logo                           │    │
│  │  "Welcome back" (H2)            │    │
│  │                                 │    │
│  │  Email input                    │    │
│  │  Password input                 │    │
│  │  [Login] button                 │    │
│  │                                 │    │
│  │  "Forgot password?" link        │    │
│  │  Divider "or"                   │    │
│  │  [Continue with Google] button  │    │
│  │                                 │    │
│  │  "Don't have an account? Sign up" │  │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

**Components used**:
- `Card`, `CardHeader`, `CardContent`, `CardFooter`
- `Form`, `FormField`, `FormItem`, `FormLabel`, `FormMessage`
- `Input` (email, password)
- `Button` (submit + OAuth)
- `Separator` (divider)

**Data needs**: Supabase Auth (signInWithPassword, signInWithOAuth)
**Validation**: Email required + valid format, password required + min 8 chars
**Error handling**: Invalid credentials → inline error message
**Success**: Redirect to `/dashboard`

---

### 3. [Dashboard / Main Page] (`/dashboard`)

**Purpose**: [Primary workspace — what users see after login]
**Auth state**: Protected (redirect to `/login` if not authenticated)

**Layout**:
```
┌──────────┬──────────────────────────────┐
│          │  Page Header:                │
│  Sidebar │  Title + Action buttons      │
│  Nav     ├──────────────────────────────┤
│          │  Content Area:               │
│  - Link  │  [Main content — cards,      │
│  - Link  │   table, or custom layout]   │
│  - Link  │                              │
│  - Link  │                              │
│          │                              │
│  ────────│                              │
│  User    │                              │
│  menu    │                              │
└──────────┴──────────────────────────────┘
```

**Components used**:
- [List specific shadcn/ui components]

**Data needs**: [Which Supabase tables/queries]
**Key interactions**: [What users can do on this page]
**Loading state**: [Skeleton layout description]
**Empty state**: [What shows when no data exists]

---

### [N. Additional Pages]

[Follow the same pattern for each page:
- Purpose
- Auth state
- Layout (ASCII wireframe)
- Components used
- Data needs
- Key interactions
- Loading state
- Empty state]

## User Roles & Access Control

### Role Definitions

| Role | Description | Auth State | Supabase Implementation |
|------|------------|-----------|------------------------|
| Guest | Unauthenticated visitor | No session | No Supabase user record |
| User | Registered, logged-in user | Active session | `auth.users` record exists |
| Admin | System administrator | Active session + admin flag | `profiles.role = 'admin'` |
| [Custom role] | [Description] | [Auth state] | [How to identify in Supabase] |

### Access Matrix

Map which roles can access which pages and perform which actions:

| Page / Action | Guest | User | Admin |
|--------------|:-----:|:----:|:-----:|
| View landing page | ✓ | ✓ | ✓ |
| Login / Signup | ✓ | Redirect to dashboard | Redirect to dashboard |
| View dashboard | ✗ → /login | ✓ | ✓ |
| Create [item] | ✗ | ✓ (own only) | ✓ (any) |
| Edit [item] | ✗ | ✓ (own only) | ✓ (any) |
| Delete [item] | ✗ | ✓ (own only) | ✓ (any) |
| View admin panel | ✗ | ✗ | ✓ |
| Manage users | ✗ | ✗ | ✓ |

### Supabase RLS Policies

Translate the access matrix into RLS policy descriptions:

**Table: [main_entity]**
```sql
-- Users can view their own records
CREATE POLICY "Users read own records"
  ON public.[table] FOR SELECT
  USING (auth.uid() = user_id);

-- Users can insert their own records
CREATE POLICY "Users insert own records"
  ON public.[table] FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Users can update their own records
CREATE POLICY "Users update own records"
  ON public.[table] FOR UPDATE
  USING (auth.uid() = user_id);

-- Users can delete their own records
CREATE POLICY "Users delete own records"
  ON public.[table] FOR DELETE
  USING (auth.uid() = user_id);

-- Admins can do everything
CREATE POLICY "Admins full access"
  ON public.[table] FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM public.profiles
      WHERE profiles.id = auth.uid()
      AND profiles.role = 'admin'
    )
  );
```

[Repeat for each table with different access patterns]

## User Journeys

Define the primary paths users take through the app. Each journey is 3-5 steps max and maps to a sequence of Lovable prompts.

### Journey 1 — First-Time User

| Step | User Action | System Response | Route |
|------|------------|-----------------|-------|
| 1 | Lands on homepage | Show value proposition + CTA | `/` |
| 2 | Clicks "Get Started" | Show signup form | `/signup` |
| 3 | Submits signup form | Create account, create profile, redirect | `/dashboard` |
| 4 | Sees empty dashboard | Show welcome message + empty state with CTA | `/dashboard` |
| 5 | Creates first [item] | Save to Supabase, show in list | `/dashboard` |

**Lovable build sequence**: This journey spans Phase 0 (landing), Phase 1 (auth), Phase 2 (dashboard layout), Phase 3 (data), Phase 4 (create behavior).

### Journey 2 — Returning User

| Step | User Action | System Response | Route |
|------|------------|-----------------|-------|
| 1 | Opens app | Check auth state, redirect to dashboard | `/dashboard` |
| 2 | Views existing [items] | Fetch from Supabase, display in list/grid | `/dashboard` |
| 3 | [Core action] | [Response] | [Route] |

### Journey 3 — [Power User / Admin / Custom]

| Step | User Action | System Response | Route |
|------|------------|-----------------|-------|
| 1 | [Action] | [Response] | [Route] |
| 2 | [Action] | [Response] | [Route] |
| 3 | [Action] | [Response] | [Route] |

## Component Architecture

### Shared Components

Components used across multiple pages:

| Component | Location | Used On | Props |
|-----------|----------|---------|-------|
| `Layout` | `src/components/Layout.tsx` | All authenticated pages | `children` |
| `Header` | `src/components/Header.tsx` | Inside Layout | `title`, `actions` |
| `Sidebar` | `src/components/Sidebar.tsx` | Inside Layout | `items`, `activeItem` |
| `EmptyState` | `src/components/EmptyState.tsx` | Any page with data | `icon`, `title`, `description`, `action` |
| `LoadingSkeleton` | `src/components/LoadingSkeleton.tsx` | Any page with data | `variant` |

### Page Components

Each route maps to a page component:

| Route | Component | Location |
|-------|-----------|----------|
| `/` | `Landing` | `src/pages/Landing.tsx` |
| `/login` | `Login` | `src/pages/Login.tsx` |
| `/signup` | `Signup` | `src/pages/Signup.tsx` |
| `/dashboard` | `Dashboard` | `src/pages/Dashboard.tsx` |
| [/route] | [Component] | [src/pages/Component.tsx] |
| `*` | `NotFound` | `src/pages/NotFound.tsx` |

### Feature Components

Components specific to a feature area:

| Component | Location | Purpose |
|-----------|----------|---------|
| `[ItemCard]` | `src/components/[feature]/ItemCard.tsx` | Display single item |
| `[ItemForm]` | `src/components/[feature]/ItemForm.tsx` | Create/edit item |
| `[ItemList]` | `src/components/[feature]/ItemList.tsx` | List/grid of items |

### Custom Hooks

| Hook | Location | Purpose |
|------|----------|---------|
| `useAuth` | `src/hooks/useAuth.ts` | Current user + auth state |
| `use[Items]` | `src/hooks/use[Items].ts` | Fetch [items] from Supabase |
| `useCreate[Item]` | `src/hooks/useCreate[Item].ts` | Create mutation |
| `useUpdate[Item]` | `src/hooks/useUpdate[Item].ts` | Update mutation |
| `useDelete[Item]` | `src/hooks/useDelete[Item].ts` | Delete mutation |

## Navigation Structure

### Desktop Navigation

[Sidebar or top nav — describe the hierarchy]

```
├── Dashboard (icon: LayoutDashboard)
├── [Section 1] (icon: [Lucide icon name])
│   ├── [Sub-page 1]
│   └── [Sub-page 2]
├── [Section 2] (icon: [Lucide icon name])
├── Settings (icon: Settings)
└── User menu (avatar dropdown)
    ├── Profile
    ├── Settings
    └── Sign out
```

### Mobile Navigation

[How navigation adapts on mobile — typically a Sheet component triggered by hamburger icon]

## Structural Principles

- **3-click rule**: Any core action is reachable within 3 clicks from dashboard
- **Persistent input**: Chat/form input always visible on relevant pages
- **History accessible but not distracting**: Past items available via sidebar, not cluttering the main view
- **Settings tucked away**: Accessible via user menu, not competing with primary actions
- **Empty states are encouraging**: Never show a blank page — always guide the user toward their first action
```

---

## Guidance for Generating the Document

### Wireframes in ASCII

The ASCII wireframes don't need to be pixel-perfect — they need to communicate the layout structure unambiguously. Use box-drawing characters (┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼) for clean wireframes. Show:

- Where major sections are positioned
- Relative sizing (sidebar narrower than content)
- What content goes in each section
- Which shadcn/ui components are used where

### From the User's Masterplan to This Document

Map Masterplan sections to App Flow sections:

- **Core Features** → Pages and their content areas
- **Target Audience roles** → User Roles & Access Control
- **Data Model** → Data needs per page + RLS policies
- **Non-Goals** → Pages NOT to build (reference what's excluded)
- **UI Design Principles** → Structural Principles

### Component Naming Conventions

Follow Lovable's file structure conventions:

- Page components: PascalCase, e.g., `Dashboard.tsx`, `UserSettings.tsx`
- Feature components: PascalCase in feature folders, e.g., `components/projects/ProjectCard.tsx`
- Hooks: camelCase with `use` prefix, e.g., `useProjects.ts`, `useAuth.ts`
- Utilities: camelCase, e.g., `formatDate.ts`, `validateEmail.ts`

### RLS Policy Patterns

Common patterns to use:

- **Own records only**: `auth.uid() = user_id`
- **Admin override**: Check `profiles.role = 'admin'`
- **Public read, owner write**: SELECT for all, INSERT/UPDATE/DELETE for owner
- **Team-based access**: Join through a team_members junction table
