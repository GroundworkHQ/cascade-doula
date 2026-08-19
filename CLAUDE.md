# cascade-doula — Claude Code context

## Read first
Before working, read **`docs/REFERENCE.md`** — the source of truth for this project. This file is just the quick orientation.

## What this is
Miguel's design for the Cascade Doula Care site, built so the client can pick between it and Luis's version. Same client, same content, different design.

- **Client:** Nicole Lakey, Cascade Doula Care. Birth and postpartum doula serving Scotts Valley, Santa Cruz, San Jose. Instagram @doulanicolelakey.
- **Audience:** pregnant women. The job of the page is to get a visitor to submit the contact form.
- **Luis already shipped his version.** It is LIVE at cascadedoula.com from `Ooak21/cascadedoula.com` (GitHub Pages, Convex backend, Resend intake mail). Do not touch that repo. It is the reference for content and the thing this competes with.

## Stack
**Deliberately not locked yet.** What is decided:
- Static front end, hosted on **GitHub Pages**.
- Repo: `GroundworkHQ/cascade-doula` (public — GitHub Pages needs it, and GroundworkHQ cannot hold private repos while the billing hold stands).

What is NOT decided: whether this stays hand-written HTML/CSS/JS with no build step, or moves to a framework. Pick when the design is clearer, and write the decision into docs/REFERENCE.md §2.

**Front end only.** The form is presentation only, it does not submit anywhere. That is correct for a design Nicole is choosing between, not a gap. If she picks this one, the backend gets decided then. Do not wire a backend, a form service, or Supabase tables without asking Miguel first.

## Conventions & rules
- Secrets live in env vars / `.env.local` only, never in code. `.env.local` is gitignored. Rotate immediately if exposed.
- Commit + push at the end of each session to back up. Commit messages end with the Co-Authored-By line.
  <!-- Miguel granted this for this repo on 2026-08-18, overriding the global "never auto-push" default. It is a deliberate per-repo exception, not a template leftover. -->
- No em dashes anywhere in client-facing copy.
- Do not change client-facing copy without asking. Use Miguel's exact wording.
- The visitors are pregnant women. Anything the form collects is sensitive. See docs/REFERENCE.md §7.

## Current priority
Nothing built yet. Repo scaffolded, `origin` set, no commits. Next: build the page, then get it in front of Nicole to compare against the live site.
