# cascade-doula — Reference

> Source-of-truth reference for cascade-doula. `CLAUDE.md` points every new
> session here. Last full update: 2026-08-19.

## 1. Overview

Miguel's design for the **Cascade Doula Care** site, built so the client can
choose between it and Luis's version. Same client, same content, different
design.

- **Client:** Nicole Lakey, Cascade Doula Care. Birth and postpartum doula.
- **Service area:** Scotts Valley, Santa Cruz, San Jose and surrounding areas.
- **Instagram:** @doulanicolelakey
- **Her intake email (on the live site):** cascadedoulanl@gmail.com
- **Audience:** pregnant women. **Conversion goal:** submit the contact form.

### Luis's version is live. Do not touch it.
`Ooak21/cascadedoula.com` serves cascadedoula.com today (GitHub Pages, `www`
CNAME to `ooak21.github.io`). Luis built it and cut over 2026-08-16, with a
Convex backend for the intake form and branded Resend mail. **This repo is a
separate proposal, not a fork and not a replacement.** Never push to Ooak21.

## 2. Where it lives

| | |
|---|---|
| Repo | `GroundworkHQ/cascade-doula` (public) |
| Preview URL | https://cascade-doula.miguelloza.com/ |
| Hosting | GitHub Pages, built from `main` |
| DNS | repo `CNAME` file + Cloudflare `CNAME cascade-doula -> groundworkhq.github.io`, grey cloud |
| Vercel | **None.** Miguel declined a Vercel project 2026-08-18, so `/preview`'s Vercel path does not apply |

**Workflow: push to `main` → live.** Not a `preview` branch; Pages serves one
branch only.

⚠️ **Bump the `?v=` on the CSS and JS links in all ten pages after any asset
change.** Pages sends `cache-control: max-age=600`, so without it browsers pair
new HTML with a ten-minute-old stylesheet. This has caused real "it's broken"
reports. One-liner:

```bash
python3 - <<'PY'
import pathlib, re, subprocess
v = subprocess.run(["date","+%Y%m%d%H%M%S"], capture_output=True, text=True).stdout.strip()
root = pathlib.Path.home()/"Documents/code/cascade-doula"
for f in [root/"index.html"] + sorted(root.glob("*/index.html")):
    s = f.read_text(); f.write_text(re.sub(r'(assets/(?:css/site\.css|js/site\.js))\?v=\d+', rf'\1?v={v}', s))
PY
```

## 3. Stack

Static HTML, one shared stylesheet, one small JS file. No framework, no build
step at runtime, no backend.

```
index.html              about/  services/  services-packages/  testimonials/
consultation/  contact/  creative-funding/  body-ready-method/  resources-for-mamas/
assets/css/site.css     the whole design system
assets/js/site.js       mobile nav, demo-form intercept, review + pillar modals
assets/img/             photos, line drawings, header mark
scripts/generate-pages.py   emitted the ten pages; see §7 before running it
.nojekyll               Jekyll processing failed builds on ordinary markdown in docs/
```

Directory-per-page so URLs match Nicole's existing slugs exactly. Links are
relative, so it also serves correctly from a subpath.

## 4. Design system

### Palette (tokens at the top of site.css)
| Token | Value | Role |
|---|---|---|
| `--ink` | `#3d2b35` | deep plum, dark bands, footer is a step darker at `#33232c` |
| `--ink-soft` | `#5b4552` | body copy |
| `--cream` | `#fbf7f1` | page background |
| `--sand` | `#f2e9dd` | alternating section band, trust strip |
| `--clay` | `#a04d63` | deep rose accent: buttons, numerals, eyebrows, bullets, brackets |
| `--muted` | `#7c6d75` | captions, attributions |

Lineage, so nobody re-litigates it: evergreen → warm espresso → **deep plum**.
Accent was clay orange, changed to deep rose because orange fought the plum.
No green values remain anywhere.

### Type
**Cormorant Garamond** (headings) + **Karla** (body), Google Fonts.

Cormorant is the face Nicole already uses on her own Marriage Health Score
page, so it is her choice rather than one imposed. It runs small and light for
its point size, which is why heading weight is 600 and the display sizes were
retuned. Predecessors: Fraunces + Inter, then Fraunces + Karla.

- `h1` `clamp(2.5rem, 5.2vw, 4rem)` weight 600
- `h2` `clamp(1.85rem, 3.4vw, 2.6rem)`
- Interior hero `h1` `clamp(2.1rem, 4vw, 3.15rem)` — its own smaller scale
- Closing CTA `h2` `clamp(1.7rem, 2.9vw, 2.3rem)`, its lede smaller again
- Body 17px, per the 16-18px floor for tired readers on phones

⚠️ **Numerals need `font-variant-numeric: lining-nums`.** Cormorant defaults to
oldstyle figures, whose 3 4 5 7 9 drop below the baseline and collide with
anything underneath.

### Shape and treatment
- 6px radius on buttons, cards, photo frames. Buttons were pills; squared off
  so they match everything else.
- **Cards** (`.card--feature`): warm vertical wash, hairline border, corner
  bracket in clay, one of Nicole's drawings watermarked in the corner, hover
  lift. Numbered variant `.card--num` adds `01`-style numerals.
- **Photos**: `saturate(.78) contrast(.95) brightness(1.05)` plus a light blush
  wash multiplied over them, so they sit in the palette. Each has an offset
  hairline frame behind it, like a matted print.
- **Home hero**: full-bleed photograph with a blush duotone. Blush is
  *multiplied into* a desaturated image rather than laid over it — that is the
  only way to get a real pink cast and keep the photo visible at the same time.
  A left-right split version was built and rejected 2026-08-19.
- **Interior heroes** (`.hero--art`): flat pink field fading soft to full,
  copy left, one line drawing right, band ~248px. Photos behind interior
  headings needed so much tint they stopped reading, and cost ~500KB each.

## 5. Nicole's assets (all borrowed)

Everything in `assets/img/` came off her live site for the mockup.

- `nicole.jpg`, `photo-boardwalk`, `photo-coast`, `photo-couple`, `photo-garden`
- `line-1/2/3.png` — her line drawings. Originals were WebP misnamed `.png`
  with **no alpha**, white art baked onto blush. Keyed to transparency here,
  so they are tintable. `-soft` = dusty mauve, `-sage` = older green (unused),
  `mark-clay.png` = the header mark in rose.

**Replace with originals from her before this goes anywhere real.** Ideally get
the drawings as SVG. One photo appears on two pages (`photo-garden`); the rest
are used once.

## 6. What's built

All ten pages, using Nicole's real copy throughout.

- **Home** — hero, trust strip, plum band with tagline + Connect/Empower/Prepare,
  Meet Nicole, package summary + Ways to Pay panel, three expandable reviews,
  Body Ready Method teaser, contact form, closing CTA.
- **Testimonials** — all **29 full reviews**, real text pulled from her live
  site, ~4,500 words. Card shows headline + truncated preview; click or Enter
  opens the full review in a modal. Escape/backdrop closes, focus returns.
- **Body Ready Method** — five pillar cards that open the same modal, plus her
  real pricing table. **Pillar descriptions are placeholders, see §8.**
- **Birth Doula** — full 7-item package, three stages, dark trust strip.
- **Contact / Consultation / Services / Creative Funding / Resources** — her
  copy, her Calendly links.

The contact form is **presentation only**. Submitting shows an inline note
saying so. That is correct for a design being chosen between.

Every page carries `<meta name="robots" content="noindex, nofollow">`. Pages
cannot set headers, so that tag is the only thing keeping this out of search.
**Do not remove it while the site lives at the preview URL.**

## 7. Gotchas that have already bitten

- **The `padding` shorthand silently overrides an earlier `padding-top`.** This
  caused the corner bracket to cut through the card numerals for three rounds.
- **Source order beats intent.** An override placed *before* the rule it means
  to beat does nothing at equal specificity. Cost a broken dark trust strip
  (plum text on plum) and an overflowing hero drawing.
- **`backdrop-filter` kills subpixel antialiasing** for everything inside the
  element. It made the whole nav render soft. Removed; also removed the
  site-wide `-webkit-font-smoothing: antialiased`.
- **A gradient clipped mid-fade is a hard edge.** A radial halo anchored to a
  too-small element produced a visible vertical seam across the hero.
- **Card gradients must not end at the page background colour**, or cards
  dissolve at the bottom.
- **`scripts/generate-pages.py` is behind the hand-edited pages.** It was used
  to emit the original ten and has been kept roughly in sync, but the pages are
  the source of truth now. Re-running it will overwrite hand work. Read it and
  diff before ever running it again.

## 8. Needs Nicole before this is real

1. **The five Body Ready Method pillar descriptions are Miguel's placeholder
   copy.** Neutral by design — they describe the body region and why it matters
   in pregnancy, with no BRM method claims. She is the certified BRM Pro and
   must approve or rewrite all five. She may have licensed marketing language
   from BRM, which would be the better source. Copying bodyreadymethod.com is
   not an option.
2. **"Every birth is different. The support should be too."** is Miguel's line,
   not hers.
3. **Original photos and drawings**, replacing the borrowed ones.
4. **One inconsistency in her own content:** her Services page says Central
   California Alliance and Medi-Cal; her Creative Funding page says Kaiser and
   Medi-Cal. Each page here uses its own page's wording. One is probably stale.
5. **Where the form posts**, only if she picks this design. Options are a form
   service or a Supabase Edge Function writing to a `doula_leads` table, the
   same shape as Rekindle's `rekindle-reserve`.
6. **Sensitive data.** Visitors are pregnant women and the form asks for a due
   date. If she is in California, CMIA is broader than HIPAA. Ask for the
   minimum, keep notifications as pointers not content. The rails in
   `clinic-receptionist/CLAUDE.md` §7 are the reference.

## 9. Conventions

- No em dashes in client-facing copy.
- Client copy is hers. Do not reword without asking Miguel. **Do not expand her
  contractions** — that was done once and had to be reverted; it is the single
  strongest tell that copy was machine-written.
- Title case for h1–h4 and price names. Sentence case for anything ending in a
  period.
- Commit + push at the end of each session (per-repo exception Miguel granted
  2026-08-18; the global default is never auto-push).
- Verify layout claims by measuring in the DOM, not by eye. Several rounds were
  lost to fixing the wrong element.

## 10. Open decisions

- **Repo account.** Client domain repos live under `Ooak21`. This stays under
  GroundworkHQ because it is a proposal. Revisit only if she picks it.
- **Public repo names the client.** Miguel approved that tradeoff 2026-08-18.
- **Interior pages all open identically.** Consistent, but nothing distinguishes
  them except the words and which drawing appears.
