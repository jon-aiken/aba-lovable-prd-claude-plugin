# Design Guidelines Template

Use this template to generate the `design-guidelines.md` document. Every design decision is expressed in terms Lovable can execute directly: Tailwind CSS utility classes, shadcn/ui component names, and Tailwind config values.

The goal is a document so precise that Lovable produces visually consistent output from the first prompt.

---

## Template Structure

```markdown
# [Project Name] — Design Guidelines

## Emotional Tone

[One paragraph describing how the app should feel. Be specific — not just "clean and modern" but the actual emotional experience. This guides every visual decision.]

**Personality keywords**: [3-5 adjectives that define the product's character]
**Design metaphor**: [A physical space or experience that captures the vibe. e.g., "A well-organized studio workspace" or "A calm library reading room"]

## Color System

### Tailwind Config Extension

Add these to `tailwind.config.ts` under `theme.extend.colors`:

```typescript
colors: {
  // Brand
  brand: {
    DEFAULT: '[hex]',    // Primary brand color — [Tailwind class: bg-brand]
    light: '[hex]',      // Lighter variant — [Tailwind class: bg-brand-light]
    dark: '[hex]',       // Darker variant — [Tailwind class: bg-brand-dark]
  },
  // Semantic
  surface: {
    DEFAULT: '[hex]',    // Main background — [Tailwind class: bg-surface]
    raised: '[hex]',     // Cards, modals — [Tailwind class: bg-surface-raised]
    sunken: '[hex]',     // Inset areas — [Tailwind class: bg-surface-sunken]
  },
  content: {
    DEFAULT: '[hex]',    // Primary text — [Tailwind class: text-content]
    secondary: '[hex]',  // Secondary text — [Tailwind class: text-content-secondary]
    muted: '[hex]',      // Disabled/hint text — [Tailwind class: text-content-muted]
  },
  border: {
    DEFAULT: '[hex]',    // Default borders — [Tailwind class: border-border]
    strong: '[hex]',     // Emphasized borders — [Tailwind class: border-border-strong]
  },
  // Status
  success: '[hex]',      // [Tailwind: text-success, bg-success]
  warning: '[hex]',      // [Tailwind: text-warning, bg-warning]
  error: '[hex]',        // [Tailwind: text-error, bg-error]
  info: '[hex]',         // [Tailwind: text-info, bg-info]
}
```

### Color Usage Rules

| Context | Token | Tailwind Class | Hex |
|---------|-------|---------------|-----|
| Page background | surface | `bg-surface` | [hex] |
| Card background | surface-raised | `bg-surface-raised` | [hex] |
| Primary text | content | `text-content` | [hex] |
| Secondary text | content-secondary | `text-content-secondary` | [hex] |
| Primary button | brand | `bg-brand text-white` | [hex] |
| Borders | border | `border-border` | [hex] |
| Success states | success | `text-success` | [hex] |
| Error states | error | `text-error` | [hex] |

### Contrast Compliance

All color pairings meet WCAG AA (4.5:1 for text, 3:1 for large text):
- [content] on [surface]: [ratio]:1 ✓
- [content-secondary] on [surface]: [ratio]:1 ✓
- [white] on [brand]: [ratio]:1 ✓

### Dark Mode [IF APPLICABLE]

Dark mode inverts the surface hierarchy. Add these values under `darkMode: 'class'` in Tailwind config:

```typescript
// Dark mode overrides — applied when <html class="dark">
surface: {
  DEFAULT: '[dark hex]',
  raised: '[dark hex]',
  sunken: '[dark hex]',
},
content: {
  DEFAULT: '[dark hex]',
  secondary: '[dark hex]',
  muted: '[dark hex]',
},
border: {
  DEFAULT: '[dark hex]',
}
// Note: Do not use pure black (#000000). Use a near-black like #0F172A.
```

## Typography

### Font Stack

**Primary font**: [Font name] — [purpose, e.g., "UI text, headings, body copy"]
- Google Fonts import: `@import url('https://fonts.googleapis.com/css2?family=[Font]+[weights]')`
- Tailwind config: `fontFamily: { sans: ['[Font]', 'system-ui', 'sans-serif'] }`

**Secondary font** [IF APPLICABLE]: [Font name] — [purpose]
- Google Fonts import: [import URL]
- Tailwind config: `fontFamily: { serif: ['[Font]', 'Georgia', 'serif'] }`

**Monospace**: [Font name or system default] — code blocks, data values
- Tailwind config: `fontFamily: { mono: ['[Font]', 'monospace'] }`

### Type Scale

Using a [ratio, e.g., 1.25] modular scale:

| Level | Size | Weight | Line Height | Tailwind Classes | Usage |
|-------|------|--------|-------------|-----------------|-------|
| Display | 48px | 700 | 1.1 | `text-5xl font-bold leading-tight` | Hero sections only |
| H1 | 36px | 600 | 1.2 | `text-4xl font-semibold leading-tight` | Page titles |
| H2 | 28px | 600 | 1.3 | `text-3xl font-semibold` | Section headers |
| H3 | 22px | 500 | 1.4 | `text-xl font-medium` | Subsections |
| H4 | 18px | 500 | 1.4 | `text-lg font-medium` | Card titles, labels |
| Body | 16px | 400 | 1.6 | `text-base` | Paragraphs, default text |
| Body Small | 14px | 400 | 1.5 | `text-sm` | Secondary info, metadata |
| Caption | 12px | 400 | 1.4 | `text-xs` | Timestamps, badges |

### Typography Rules

- Max line width for reading: `max-w-prose` (65 characters)
- Paragraph spacing: `space-y-4` between paragraphs
- Heading spacing: `mt-8 mb-4` above headings, `mb-4` below
- No decorative or script fonts
- No text smaller than 12px (accessibility)

## Spacing & Layout

### Spacing Scale

Using Tailwind's default 4px base unit:

| Token | Value | Tailwind | Usage |
|-------|-------|---------|-------|
| xs | 4px | `p-1` / `gap-1` | Tight groupings |
| sm | 8px | `p-2` / `gap-2` | Related elements |
| md | 16px | `p-4` / `gap-4` | Component padding |
| lg | 24px | `p-6` / `gap-6` | Section padding |
| xl | 32px | `p-8` / `gap-8` | Page sections |
| 2xl | 48px | `p-12` / `gap-12` | Major section breaks |

### Layout System

**Content width**: `max-w-[value]` — [specify: 768px for content-focused, 1280px for dashboards]
**Content centering**: `mx-auto px-4 sm:px-6 lg:px-8`
**Page padding**: `py-8` (top and bottom)

**Grid patterns**:
- Card grid: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`
- Two-column layout: `grid grid-cols-1 lg:grid-cols-[250px_1fr] gap-8`
- Sidebar layout: `flex min-h-screen` with `w-64 shrink-0` sidebar and `flex-1` content

### Responsive Breakpoints

Using Tailwind defaults (mobile-first):
- **Mobile**: Default (< 640px) — single column, full-width
- **Tablet**: `sm:` (≥ 640px) — two columns where appropriate
- **Desktop**: `lg:` (≥ 1024px) — full layout with sidebar
- **Wide**: `xl:` (≥ 1280px) — max-width constraint

Rule: No horizontal scrolling at any breakpoint.

## Component Patterns

### shadcn/ui Component Usage

Map your UI patterns to specific shadcn/ui components:

| UI Pattern | shadcn/ui Component | Variant | Notes |
|-----------|-------------------|---------|-------|
| Primary action | `Button` | `default` | `bg-brand` custom color |
| Secondary action | `Button` | `outline` | |
| Destructive action | `Button` | `destructive` | Confirm with AlertDialog |
| Text input | `Input` | default | Wrap in Form + FormField |
| Dropdown | `Select` | default | |
| Toggle | `Switch` | default | |
| Data display | `Card` | default | `bg-surface-raised` |
| Data table | `Table` | default | With sorting via TanStack |
| Navigation (top) | `NavigationMenu` | default | Desktop only |
| Navigation (mobile) | `Sheet` | default | Hamburger trigger |
| Modal dialog | `Dialog` | default | For forms, confirmations |
| Notifications | `Toast` | default | Via Sonner integration |
| Tabs | `Tabs` | default | |
| Badges/Tags | `Badge` | varies | |
| Tooltips | `Tooltip` | default | On icon-only buttons |

### Button Hierarchy

1. **Primary**: One primary action per view — `<Button>` with brand color
2. **Secondary**: Supporting actions — `<Button variant="outline">`
3. **Ghost**: Subtle actions — `<Button variant="ghost">`
4. **Destructive**: Delete/remove — `<Button variant="destructive">` always with confirmation

### Card Pattern

Standard card structure:
```
<Card className="bg-surface-raised">
  <CardHeader>
    <CardTitle className="text-lg font-medium">Title</CardTitle>
    <CardDescription className="text-content-secondary">Subtitle</CardDescription>
  </CardHeader>
  <CardContent>
    {content}
  </CardContent>
  <CardFooter className="flex justify-end gap-2">
    <Button variant="outline">Cancel</Button>
    <Button>Save</Button>
  </CardFooter>
</Card>
```

### Form Pattern

Standard form structure:
- Use shadcn/ui `Form`, `FormField`, `FormItem`, `FormLabel`, `FormMessage`
- Validation: Zod schema with clear error messages
- Layout: `space-y-4` between fields, `space-y-6` between sections
- Submission: Loading spinner in button, disable during submit

## Motion & Interaction

### Animation Principles

Motion should reassure, not distract. It communicates state changes and provides feedback.

| Interaction | Duration | Easing | Tailwind |
|------------|----------|--------|----------|
| Hover effects | 150ms | ease-out | `transition-all duration-150` |
| Page transitions | 200ms | ease-out | `transition-opacity duration-200` |
| Modal open/close | 200ms | ease-out | Handled by shadcn/ui Dialog |
| Toast entry | 200ms | ease-out | Handled by Sonner |
| Skeleton pulse | 1.5s | ease-in-out | `animate-pulse` (Tailwind default) |

### Interaction States

| State | Visual Treatment | Tailwind |
|-------|-----------------|----------|
| Hover | Subtle shadow lift | `hover:shadow-md transition-shadow` |
| Focus | Visible ring | `focus-visible:ring-2 focus-visible:ring-brand` |
| Active | Slight scale down | `active:scale-[0.98]` |
| Disabled | Reduced opacity | `disabled:opacity-50 disabled:cursor-not-allowed` |
| Loading | Skeleton or spinner | `animate-pulse` or `animate-spin` |

### Empty States

- Centered icon (from Lucide) + heading + description + call-to-action button
- Tone: Encouraging, never blaming — "No [items] yet. Create your first one."
- Use `text-content-muted` for the description

### Error States

- Tone: Gentle and helpful — "Something went wrong. Let's try that again."
- Always offer a recovery action (retry button, link to support)
- Use `text-error` for error messages, never large blocks of red
- Form errors: inline below the field using shadcn/ui FormMessage

## Voice & Tone in UI Copy

**Personality**: [Restate from Emotional Tone section — e.g., "Thoughtful, clear, supportive"]

### Microcopy Patterns

| Context | Pattern | Example |
|---------|---------|---------|
| Onboarding | Welcoming, sets expectations | "Welcome. Let's get you set up." |
| Empty state | Encouraging, action-oriented | "No projects yet. Create your first one." |
| Success | Brief, positive | "Saved successfully." |
| Error | Gentle, offers recovery | "Couldn't save. Check your connection and try again." |
| Loading | Calm, informative | "Loading your data..." |
| Destructive confirm | Clear about consequences | "This will permanently delete [item]. This cannot be undone." |
| Placeholder text | Guides without being precious | "Enter a title..." (not "Type your amazing title here!") |

## Accessibility Requirements

- **Semantic HTML**: Correct heading hierarchy (h1 → h2 → h3), no skipped levels
- **Keyboard navigation**: All interactive elements reachable via Tab, activatable via Enter/Space
- **Focus indicators**: Visible `focus-visible:ring-2` on all interactive elements
- **Color independence**: Never use color alone to convey meaning — pair with icons or text
- **Alt text**: All meaningful images have descriptive alt text
- **ARIA labels**: Icon-only buttons have `aria-label`
- **Contrast**: All text meets WCAG AA (4.5:1 normal text, 3:1 large text)
- **Touch targets**: Minimum 44x44px on mobile

## Design Integrity Checklist

Before finalizing, verify:

- [ ] Emotional tone is consistent across all UI copy
- [ ] All colors map to named Tailwind tokens (no raw hex in components)
- [ ] Typography follows the defined scale (no ad-hoc sizes)
- [ ] Spacing uses the defined scale (no magic numbers)
- [ ] All interactive elements have hover, focus, active, and disabled states
- [ ] shadcn/ui components are used consistently for the same UI patterns
- [ ] Dark mode works if specified (no broken contrast, no pure black)
- [ ] Responsive layout works at mobile, tablet, and desktop
- [ ] Accessibility requirements are met
```

---

## Guidance for Generating the Document

### Translating Brand Direction into Tailwind

When the user describes a visual direction ("I want it to feel like Linear" or "warm and friendly"), translate that into specific Tailwind tokens:

- **"Minimal/focused"** → Generous whitespace (`space-y-8`), limited color palette, `max-w-3xl`
- **"Bold/energetic"** → Saturated accent colors, larger type scale, `font-bold` headings
- **"Warm/friendly"** → Warm palette (amber, orange tones), rounded corners (`rounded-xl`), softer shadows
- **"Professional/serious"** → Neutral palette (slate, gray), sharp corners (`rounded-md`), minimal animation
- **"Playful"** → Bright accents, generous `rounded-2xl`, micro-animations on hover

### Color Selection Defaults

If the user hasn't chosen colors, suggest palettes that match their emotional tone. Always include:

1. A brand color (the main accent)
2. Surface colors (background, card, inset)
3. Content colors (primary text, secondary text, muted text)
4. Status colors (success, warning, error, info)

Use Tailwind's built-in color palette as a starting point (slate, blue, green, amber, red) — Lovable knows these natively without config changes.

### Font Selection Defaults

If the user hasn't chosen fonts, suggest based on tone:

- **Technical/precise**: Inter, JetBrains Mono (for code)
- **Friendly/approachable**: Plus Jakarta Sans, Nunito
- **Editorial/authoritative**: Playfair Display (headings) + Source Sans Pro (body)
- **Modern/geometric**: Outfit, Space Grotesk
- **Neutral/flexible**: Inter (the safe default — Lovable uses it well)
