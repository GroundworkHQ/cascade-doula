# cascade-doula — Claude Code context

## Read first
Before working, read **`docs/REFERENCE.md`** — the source of truth. It carries
the design system, the gotchas that have already cost real time, and what still
needs Nicole. This file is just the orientation.

## What this is
Miguel's design for the Cascade Doula Care site, built so the client can pick
between it and Luis's version. Client is **Nicole Lakey**, a birth and
postpartum doula in Scotts Valley / Santa Cruz / San Jose.

- **Live preview:** https://cascade-doula.miguelloza.com/
- **Workflow:** push to `main` → live via GitHub Pages. No Vercel.
- **Luis's version is the real live site** at `Ooak21/cascadedoula.com`.
  Never push there.

## Stack
Static HTML across ten pages, one stylesheet, one small JS file. No framework,
no build step, no backend. Cormorant Garamond + Karla. Deep plum, cream, sand,
deep rose. Full palette and type scale in docs/REFERENCE.md §4.

**The contact form is presentation only** and every page carries
`noindex, nofollow`. Both are deliberate while this is a proposal.

## Before you change anything
- **Bump the `?v=` on the css and js links across all ten pages** after any
  asset change, or Pages will serve a stale stylesheet for ten minutes.
- **Measure in the DOM before claiming a layout fix.** Several rounds were lost
  fixing the wrong element.
- **`scripts/generate-pages.py` is behind the pages.** Do not run it without
  diffing first; it will overwrite hand work.
- Three things on the site are placeholders, not approved copy. See
  docs/REFERENCE.md §8 before showing it to anyone as finished.

## Conventions & rules
- Secrets in env vars / `.env.local` only, never in code.
- Commit + push at the end of each session. Commit messages end with the
  Co-Authored-By line.
- No em dashes in client-facing copy. Do not reword Nicole's copy, and do not
  expand her contractions.
- Title case for headings and price names; sentence case for anything that ends
  in a period.

## Current priority
Design is complete and live at the preview URL. Next step is Nicole's review,
which is Miguel's call to initiate. Nothing has been sent to her.
