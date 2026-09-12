# Invite links: the contract between the website and the iOS apps

This describes **both halves** of the invite flow. Half of it lives in the
website repo (`lendewugh.github.io`) and half lives in each Xcode project.
Neither half works alone.

Keep a copy of this file in each app repo as well as the website repo. If you
change anything here, change it in every copy.

## The flow

```
  User taps Share in the app
        │  app builds:  https://lendewugh.github.io/susspend/join?s=<payload>
        ▼
  Recipient taps the link
        │
   ┌────┴─────────────────────────────┐
   │                                  │
 universal link fires            it doesn't fire
 (AASA accepted, app installed)  (not installed, AASA not cached,
   │                              or served with a bad Content-Type)
   ▼                                  ▼
 app opens straight             join page loads → its inline script
 to the group/schedule          redirects to moneyplease://join?s=<payload>
 (join page never seen)         → app opens, or the Get button is offered
```

## Frozen identifiers — never change these

|  | Sus Spend | Sus Pay |
|---|---|---|
| Bundle ID | `com.LewDew.MoneyPlease` | `com.lendew.PayTracker` |
| Team ID | `TUUXPZ34Z8` | `TUUXPZ34Z8` |
| Link path | `/susspend/join` | `/paytracker/join` |
| URL scheme | `moneyplease://` | `paytracker://` |
| App Store ID | `6761013799` | `6763399577` |
| App Store name | Suspicious Spending | Suspicious Pay |

`LewDew` is a typo that shipped; Apple does not allow changing a bundle ID
after publication. `MoneyPlease` and `PayTracker` are the apps' original
names. All of these are load-bearing — changing any one breaks invite links
for users who already have the app.

## Website side (this repo)

- `.well-known/apple-app-site-association` — no file extension, no `.json`,
  valid JSON, no BOM. Its `appIDs` are `<TeamID>.<BundleID>` and its
  `components` paths must match the folders exactly.
- `.nojekyll` at the repo root, or GitHub Pages hides any dot-folder,
  including `.well-known`.
- `susspend/join/index.html`, `paytracker/join/index.html` — self-contained
  fallback pages. Their inline script reads `?s=` and redirects to the app's
  URL scheme. Do not remove that script; it is what makes invites work when
  universal links don't.

**Known limitation:** GitHub Pages cannot set a `Content-Type`, and Apple
wants `application/json` for the AASA file. If Apple rejects it, universal
links never fire and every invite goes through the fallback page instead.
The flow still works — it is just less seamless. This is the main reason the
fallback exists.

## App side (each Xcode project)

The app must have all three of these compiled in. None can be fixed from the
website:

1. **Associated Domains** capability listing `applinks:lendewugh.github.io`
   (Signing & Capabilities). Without it, universal links can never fire.
2. **URL scheme** registered under Info.plist → URL Types
   (`moneyplease` or `paytracker`). Without it, the fallback page has nothing
   to hand the invite to.
3. **Handling code** for both entry points: a universal link arriving at
   `/susspend/join?s=…` and a scheme URL arriving at `moneyplease://join?s=…`.
   Both carry the same `s=` payload and should be treated identically.

The app must generate links in exactly the form
`https://lendewugh.github.io/<path>/join?s=<payload>`, URL-encoded.

## The caching gotcha

iOS fetches the AASA file **when the app is installed**, not when the link is
tapped. An app installed before the file existed has cached "this site has no
app association" and will keep believing that.

The cache refreshes on **app update or reinstall**. Apple also refreshes
periodically, but don't rely on the timing.

Consequences:

- **Suspicious Spending** shipped before this file existed, so every existing
  install has the stale answer. Those users get the fallback page until they
  update or reinstall. That is not a bug.
- **Suspicious Pay** has not shipped, so its first install fetches the file
  fresh. Make sure Associated Domains is in the build before submitting.

## Status

**Suspicious Spending's URL scheme is confirmed registered.** Verified on a
real device (12 Sep 2026): `moneyplease://join?s=test` typed into Safari
opened the app. So the fallback path works, and **invites function today** —
a recipient lands on the join page for a moment and is handed into the app.

Universal links (the seamless path) are unverified and are a polish
improvement, not a requirement. Nothing is broken while they are off.

## Testing

Test on a real device; the Simulator is unreliable for universal links.

**Is the URL scheme registered?** Type `<scheme>://join?s=test` into Safari's
address bar. The app opening proves the fallback works. Safe — installs
nothing, changes nothing.

**Do universal links fire?** The obvious test is to delete and reinstall the
app, because that forces a fresh AASA fetch. **Don't do this on a device
holding real data.** Deleting the app deletes its on-device data, and whether
it comes back depends on iCloud sync actually working — which is not worth
betting a real ledger on to verify a convenience feature.

Safer options, in order of preference:

1. **Wait.** The AASA cache refreshes on the next App Store update, for any
   reason. Universal links will likely start working on their own.
2. Test on a second device, or a device without real data in the app.
3. Use a TestFlight or development build rather than the live app.

Once it is testable, the three outcomes are:

- Opens straight into the app → universal links work.
- Join page appears, then bounces into the app → fallback is carrying it;
  Associated Domains is missing or the AASA file was rejected.
- Join page appears and stays → neither path is wired up.
