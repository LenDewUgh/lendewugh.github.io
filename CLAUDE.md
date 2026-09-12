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

## Hand-written exceptions: the app invite pages

These are **not** generated and `_build/build.py` must never write them:

- `.well-known/apple-app-site-association` — Apple universal-links file. No
  file extension, no `.json`, no BOM. Must stay valid JSON.
- `susspend/join/index.html`
- `paytracker/join/index.html`

`/susspend/join` and `/paytracker/join` are **hardcoded in the shipped iOS
apps** and in the AASA file. Renaming or moving them breaks invite links for
users who already have the apps installed. Don't "tidy" them into `apps/`.

Two things in these files look like mistakes and are not. Leave both alone:

- **`com.LewDew.MoneyPlease` is correct.** "LewDew" (not "LenDew") was a typo
  made when the app was first created and it shipped that way, so the bundle
  ID is frozen — Apple does not allow changing it after publication.
  "MoneyPlease" is likewise the app's original name; it is now Sus Spend.
  Correcting either spelling would break universal links for every existing
  user. The Pay Tracker entry, `com.lendew.PayTracker`, is correct as written.
- **Pay Tracker's App Store link (`id6763399577`) is dead until the app
  ships.** Known and accepted: the owner expects little traffic before launch
  and is reachable by email. Don't remove the link or gate the page on it.
- **The join pages deliberately disagree with their own folder names.**
  Each app carries three names, and they are not meant to match:

  | | Sus Spend | Sus Pay |
  |---|---|---|
  | Folder (fixed, app depends on it) | `susspend/join` | `paytracker/join` |
  | URL scheme (fixed) | `moneyplease://` | `paytracker://` |
  | Visible text = App Store listing | Suspicious Spending | Suspicious Pay |

  The folders and schemes keep the apps' original internal names because the
  shipped apps are wired to them. The *visible* wording must match the App
  Store listing, because the join page is the first thing a stranger sees and
  the next thing they see is that listing. Don't "fix" the wording to match
  the folder. If a listing name changes, update the visible text on that join
  page and the `store` field in `APPS` together.

  The short forms ("Sus Spend", "Sus Pay") are for the marketing site only —
  never on a join page.

They are deliberately self-contained (inline CSS and JS, no site stylesheet).
Their inline script is what hands the invite to the app when the universal
link doesn't fire. **Do not restyle them to match the site** until the invite
flow is confirmed working on a real device.

They are intentionally absent from `sitemap.xml` — they are invite landing
pages, not content.

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
