# LenDew site — how this repo works

Read this before changing anything.

## The pages are generated. Do not edit them by hand.

`index.html`, `apps/*.html`, `support.html`, `privacy.html`, `404.html`,
`sitemap.xml` and the redirect stubs are **output**, written by
`_build/build.py`. Editing them directly appears to work and is then silently
erased the next time anyone runs the script.

| To change | Edit | Then |
|---|---|---|
| Words, prices, FAQs, privacy text | `_build/build.py` (the `APPS` list) | `python3 _build/build.py` |
| Colours, fonts, spacing, layout | `assets/site.css` | nothing — it's hand-written |
| Support email | `SUPPORT_EMAIL` in `_build/build.py` | `python3 _build/build.py` |

Always re-run `python3 _build/build.py` after touching the script, and commit
the regenerated files together with the script change.

## Adding an app

One entry in `APPS`, plus `assets/icons/<id>.png` and
`assets/shots/<id>-1.webp`. Nav, footer, home cards, privacy section, support
list and sitemap all pick it up automatically. Never hand-write a new app page.

## Publishing

The repo is a GitHub Pages user site: **whatever lands on `main` is the live
website** at https://lendewugh.github.io. There is no build step on GitHub's
side and no staging. Push to `main` = publish.

`.nojekyll` must stay at the root; without it GitHub ignores `_build/`
inconsistently.

## Invariants worth keeping

- Every `.html` file contains exactly one `</html>`.
- `404.html` uses **root-relative** paths (`/assets/...`), because GitHub Pages
  serves that one file for missing paths at any depth. Relative paths break it.
- `sitemap.xml` deliberately has no `<lastmod>`: a build-time date would change
  on every run and make the output non-reproducible.
- Running `python3 _build/build.py` on a clean tree must produce **no** git
  diff. If it does, someone hand-edited generated output.
- The redirect stubs in `apps/` (`money-please`, `pay-tracker`, `cc-perks`)
  are old URLs kept alive for existing links. They are `noindex` and are not
  in the sitemap. Don't "tidy" them away.

## Owner

Lenny is not a programmer. Explain changes in plain language, avoid jargon,
and say plainly when something is unverified rather than implying it was
checked. The site is live and public — a bad push is visible immediately.
