# cascade-doula — Reference

> Source-of-truth reference for cascade-doula. Keep it current; `CLAUDE.md` points every new session here.

## 1. Overview
Miguel's design for the **Cascade Doula Care** site. Built as an alternative so the client can pick between this and Luis's version.

- **Client:** Nicole Lakey, Cascade Doula Care. Birth and postpartum doula.
- **Service area:** Scotts Valley, Santa Cruz, San Jose and surrounding areas.
- **Instagram:** @doulanicolelakey
- **Intake email on the live site:** cascadedoulanl@gmail.com
- **Audience:** pregnant women. **Conversion goal:** submit the contact form.

### Luis's version is live, do not touch it
`Ooak21/cascadedoula.com` serves cascadedoula.com today (GitHub Pages, `www` CNAME to `ooak21.github.io`). Luis built it and cut over 2026-08-16. It has a Convex backend for the intake form and branded Resend mail. **This repo is a separate design proposal, not a fork and not a replacement.** Never push to Luis's repo.

### The live site as reference
Ten pages: home, about, services, services-packages, testimonials, consultation, contact, creative-funding, body-ready-method, resources-for-mamas.

Visual direction on the live version: soft blush/mauve background, serif display type, muted sage green accent bands, black-and-white and desaturated maternity photography, line-drawing logo mark, very sparse homepage (tagline plus a four-photo grid).

Content available to reuse (it is Nicole's own copy, from her live site):
- **Tagline:** "Providing unbiased, unwavering birth and postpartum support for birthing mothers and families in Scotts Valley, Santa Cruz, San Jose and surrounding areas."
- **Services:** one-on-one support for expecting families (childbirth education, setting birth intentions, emotional and mental preparation, partner involvement); insurance billing guidance for birth workers; the Birth Doula Package (two 2-hour prenatal visits, continuous labor support, initial breastfeeding support, two postpartum follow-ups, unlimited phone and chat support, optional extra visits and birth photography).
- **Payment:** contracted with Central California Alliance for Health and Medi-Cal, plus private pay / sliding scale.
- **Office hours:** labor service 24/7, doula hours Monday to Friday 9am to 4pm.
- **Consultations:** two Calendly links, Santa Cruz and Los Gatos.
- **Live form fields:** first name, last name, email, phone, estimated due date, who is your provider, planned place of delivery, tell me about yourself, what are you looking for (Birth Doula / One on One Virtual Support / Childbirth Education Classes / Doula to Doula mentorship). Submit label "Send a note."

Assets are NOT in hand. Nicole's photos and logo belong to her and are on the live site; get proper copies rather than scraping, or use placeholders until she provides them.

## 2. Stack & accounts
**Decided:**
- **Static front end** — plain HTML/CSS/JS to start, no build step.
- **Hosting: GitHub Pages.** No Vercel. Miguel declined a Vercel project for this one on 2026-08-18, so the `/preview` skill's Vercel path does not apply here.
- **Preview URL: https://cascade-doula.miguelloza.com/** — served by GitHub Pages from `main` (not a `preview` branch), via the repo's `CNAME` file plus a Cloudflare `CNAME cascade-doula -> groundworkhq.github.io` on miguelloza.com, grey cloud. To update the preview, push to `main`.
- **noindex** comes from the `<meta name="robots">` tag in every page. GitHub Pages cannot set `X-Robots-Tag` headers, so the meta tag is the whole defense. Do not remove it while this is a proposal.
- **Repo:** `GroundworkHQ/cascade-doula` (public). Created 2026-08-18, `origin` set. Public is required: Pages on a private repo needs a paid plan, and GroundworkHQ cannot hold a private repo at all while the account-wide billing hold stands.

**Open (see §7):**
- Whether to stay no-build or adopt a framework.
- Where the form eventually posts. Only matters if Nicole picks this design.
- Domain and DNS. No CNAME yet, so the site serves from `groundworkhq.github.io/cascade-doula/` until a custom domain is pointed at it.
- Whether this repo eventually moves to Ooak21, where client domain repos normally live.

**Not wired yet:** database, email, analytics, payments, auth.

If a database is added later, prefix tables `doula_` (NOT `cascade-doula_`, the hyphen is awkward in Postgres identifiers). Checked 2026-08-18: `internal-prod` holds `mc_state`, `ironlog_data`, `church_*` (7 tables), `clinic_*` (10 tables). No collision with `doula_`.

## 3. Architecture
Ten static pages sharing `assets/css/site.css` and `assets/js/site.js`. Directory-per-page (`about/index.html`) so URLs match Nicole's existing slugs exactly. Links are relative, so it serves correctly from a subpath like `groundworkhq.github.io/cascade-doula/` as well as from a domain root.

## 4. What's built
All ten pages, static, no build step at runtime:

`/` `about/` `services/` `services-packages/` `testimonials/` `consultation/` `contact/` `creative-funding/` `body-ready-method/` `resources-for-mamas/`

- `assets/css/site.css` — the whole design system in one stylesheet (tokens at the top).
- `assets/js/site.js` — mobile nav toggle, and the intercept that keeps the demo form from looking broken.
- `assets/img/` — five photos pulled from Nicole's live site for the mockup. **Hers, used to show her a proposal. Replace with originals from her before this goes anywhere real, and do not treat them as ours.**
- `scripts/generate-pages.py` — emitted the ten pages so the shared header and footer stayed identical. Pages are plain HTML and fine to hand-edit; only re-run this if the header, footer, or nav changes, and it overwrites the pages when you do.

Design decisions worth knowing:
- Evergreen ink, warm cream, clay accent. Deliberately warmer and higher contrast than Luis's blush and sage, so the two read as real alternatives.
- Cormorant Garamond + Karla from Google Fonts.
- Conversion-first: a real hero with a CTA above the fold, a trust strip naming Medi-Cal / Alliance / FSA-HSA / sliding scale, a consult CTA in the header on every page, a sticky bottom CTA bar on mobile, and the form reachable from home, contact, and the birth doula page.
- Every page carries `noindex, nofollow`. The visible "design proposal" banner was removed on Miguel's instruction 2026-08-18; the meta tag is now the only thing keeping this out of search, so do not remove it while the site lives at the preview URL.
- The form posts nowhere. Submitting shows an inline note saying it is a proposal.

## 5. What's next
1. Miguel reviews locally: `python3 -m http.server 8931` from the repo root.
2. Commit and push (this repo has Miguel's standing OK for end-of-session pushes).
3. ~~Publish a shareable preview.~~ Done: https://cascade-doula.miguelloza.com/ (Pages, from `main`). cascadedoula.com is untouched and stays that way.
4. Get original photos from Nicole and swap out the borrowed ones.
5. Show her both, let her choose.

Deferred unless she picks this one: the form backend and the data-handling notes in §7.

## 6. Conventions
- No em dashes anywhere in client-facing copy.
- Client-facing copy is the client's, not ours. Do not reword without asking Miguel.
- Secrets in env only, never committed.
- Commit + push at the end of each session (per-repo exception Miguel granted 2026-08-18; the global default is never auto-push).
- One shared stylesheet, not per-page inline CSS. Ten pages sharing a design system made the self-contained-per-file rule the wrong call here.

## 7. Open decisions

### Body Ready Method pillar copy is PLACEHOLDER
The five pillar cards on `body-ready-method/` open a modal with a one-line
description each. **Those descriptions are mine, not Nicole's and not Body
Ready Method's.** They are deliberately neutral: they describe the body region
and why it matters in pregnancy, and make no BRM method claims.

Nicole is a certified BRM Pro and must approve or rewrite all five before this
goes anywhere real. She may also have approved marketing language from BRM that
she is licensed to use, which would be the better source. Copying the
descriptions off bodyreadymethod.com is not an option; that is their copyrighted
marketing copy and the liability would land on her.

### Where the form posts (deferred)
Not needed while this is a template. When it does go live, GitHub Pages cannot process a POST, so the form needs an external destination. Realistic options are a form service (Formspree, Basin, Getform; note Netlify Forms only works on Netlify hosting) or a Supabase Edge Function writing to a `doula_leads` table, the same shape as Rekindle's `rekindle-reserve`.

### Sensitive information (revisit before the form goes live)
The visitors are pregnant women, and a name next to a due date is health-adjacent personal information. If the client is in California, CMIA is broader than HIPAA. When the form becomes real: ask for the minimum, avoid a free-text "tell us about your pregnancy" field, and keep client notifications as pointers rather than content. The rails in `clinic-receptionist/CLAUDE.md` §7 are the reference.

### Other
- **Stack.** Hand-written no-build vs a framework. Deferred. The no-build + Pages shape fits a brochure site well and matches Rekindle and clinic-receptionist, but nothing is committed.
- **Repo account.** Client domain repos live under `Ooak21`. This one stays under GroundworkHQ because it is Miguel's proposal, not the live site. If Nicole picks it, decide then whether it moves.
- **Public repo, named client.** The repo is public and names the client. Miguel approved this on 2026-08-18 with that tradeoff on the table.
