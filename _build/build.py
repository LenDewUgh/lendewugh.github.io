#!/usr/bin/env python3
"""Generates the LenDew site from the content below.

    python3 _build/build.py

Writes index.html, apps/<id>.html, support.html and privacy.html next to
this folder. No dependencies. To add an app: add one entry to APPS, drop its
icon in assets/icons/<id>.png and a screenshot in assets/shots/<id>-1.webp.
"""
import html, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://lendewugh.github.io"
SUPPORT_EMAIL = "lendewugh@icloud.com"

APPS = [
  dict(
    id="sus-spend", name="Sus Spend", store="Suspicious Spending",
    line="Accounts, trips, groups, investments.",
    head="Know the number. Skip the confetti.",
    tag="A budget you type yourself. Accounts, shared groups, trip itineraries and investments — five tabs, one running total, no bank login anywhere.",
    price="$9.99", price_note="once. No subscription.",
    status="live", store_url="https://apps.apple.com/us/app/suspicious-spending/id6761013799",
    sub="You type it. Nobody reads it.",
    shot_caption="September on the Accounts tab — total spending, by category, then every account on one line.",
    feats=[
      ("Accounts","Every account and card on one balance line, with subscriptions and recurring charges counted before they hit."),
      ("Groups","A standing home group for the people you live with, and a trip group for the ones you don't. Settlement does the awkward math."),
      ("Trips","Bookings, attachments and an itinerary that knows what the week costs before the week starts."),
      ("Invest","Holdings tracked by hand, month over month, with a dashboard that doesn't try to sell you anything."),
    ],
    faq=[
      ("Why manual entry?","Typing the number is how you notice it. It also means the app never asks for a bank credential, because there is nothing to connect."),
      ("Does it sync?","Across your own devices through your iCloud. Nothing reaches a LenDew server, because there isn't one."),
      ("Is there a subscription?","No. $9.99 once, every tab, forever."),
      ("Can I get my data out?","Yes — PDF export from any month, any time. It's your ledger."),
    ],
    privacy=[
      "Everything you enter is stored on your device and, if you have iCloud enabled, in your own private iCloud database. LenDew has no server and cannot see it.",
      "If you invite someone to a group, the group's records are shared with them through Apple's iCloud sharing. You choose who; you can stop sharing at any time from inside the app.",
      "The app contains no analytics, no advertising and no third-party SDKs. It makes no network requests of its own.",
      "The home-screen widget reads a summary that the app writes locally on your device.",
      "Deleting the app deletes its data from your device. Data in your iCloud can be removed from Settings → iCloud → Manage Storage.",
    ],
  ),
  dict(
    id="cloud-drink", name="Cloud Drink", store="Cloud Drink",
    line="Drink orders, seat by seat.",
    head="14C wanted the ginger ale.",
    tag="A drink pad for the cart. Tap the seat, build the order — mixer, mini, ice, garnish — and every open row stays in front of you. It never needed the Wi-Fi.",
    price="$4.99", price_note="once. No subscription.",
    status="live", store_url="https://apps.apple.com/us/app/cloud-drink/id6760086566",
    sub="Drink orders, seat by seat.",
    shot_caption="First cabin, rows 1–4. Tap a seat, build the pour, and the open list underneath keeps the row in front of you.",
    feats=[
      ("The seat map","Your cabin, your rows. Drag a passenger, tap a seat, see what's still owed."),
      ("The full pour","Cocktails, minis, mixers, ice, garnish, coffee and decaf — built the way it's actually asked for."),
      ("Meals & preorders","Food inventory, preorders, and a reconciliation screen for when the count doesn't match."),
      ("Parties","Travelling together, ordering together. Group the seats once and stop asking twice."),
    ],
    faq=[
      ("Which aircraft?","Any. You build the cabin once — rows, letters, cabins — and it stays built."),
      ("Does it need Wi-Fi?","No. Everything runs on the device, including the flight timer on your Lock Screen."),
      ("Is my airline okay with this?","It's a personal notepad, not a company system. It sends nothing anywhere."),
      ("Subscription?","No. $4.99 once."),
    ],
    privacy=[
      "Cloud Drink stores everything on your device only. It does not use iCloud, has no account, and makes no network requests.",
      "The app contains no analytics, no advertising and no third-party SDKs.",
      "The Live Activity flight timer runs on your device and shows only the timer you started.",
      "Deleting the app deletes all of its data.",
    ],
  ),
  dict(
    id="sus-pay", name="Sus Pay", store="Suspicious Pay",
    line="Check the roster against the paycheck.",
    head="Count the hours before they do.",
    tag="Import the roster, let it flag the reassignments, and see the month's credit before payroll closes. Free to keep the log; the pay engine is the part you subscribe to.",
    price="Free", price_note="$2.99/month for the pay engine.",
    status="soon", store_url=None,
    sub="Check the roster against the paycheck.",
    shot_caption="July's take-home at the top, then every trip with its awarded credit, layovers and the pay it actually produced.",
    feats=[
      ("Import the month","Pull trips straight from your roster PDF or your calendar — no retyping the pairing."),
      ("Reassignment detection","It notices when the trip you flew stopped being the trip you were given, and reprices it."),
      ("Your contract's rules","Rates, step increases, holidays, month splits and per-trip credit, calculated the way the contract reads them."),
      ("Take-home","401(k), ESPP and tax percentages entered once, so the number on screen is the number that lands."),
    ],
    faq=[
      ("Is it out yet?","Not yet. This page goes live with the listing."),
      ("What's free and what isn't?","Logging trips and keeping the record is free. The pay calculation is $2.99 a month."),
      ("Does it read my roster?","It imports your roster PDF and your calendar. Nothing is sent to us — the parsing happens on the phone."),
      ("Can I get my data out?","PDF report, any month."),
    ],
    privacy=[
      "Your trips, rates and pay settings are stored on your device and, if iCloud is enabled, in your own private iCloud database. Roster PDFs and calendar events are parsed on the device; nothing is uploaded to LenDew, because LenDew has no server.",
      "Calendar access is used only to read the trips you choose to import. You can revoke it at any time in Settings.",
      "If you share your schedule with a friend, that schedule is shared through Apple's iCloud sharing with the people you pick, and only with them.",
      "Weather and sunrise/sunset tiles fetch a forecast from Open-Meteo using the airport's coordinates. No personal data is sent — only a latitude, longitude and date.",
      "The pay-engine subscription is handled entirely by Apple through the App Store. LenDew never sees your payment details.",
      "The app contains no analytics, no advertising and no third-party SDKs.",
    ],
  ),
  dict(
    id="losa", name="LOSA", store="Cabin LOSA",
    line="Line observations, filed before you land.",
    head="The observation, not the paperwork.",
    tag="A cabin line-operations safety audit you can run from the jumpseat: threats, errors, countermeasures and turbulence, timed against the real milestones — pushback to landing — and out as one PDF.",
    price="Free", price_note="Issued to trained observers.",
    status="beta", store_url=None,
    sub="Line observations, filed before you land.",
    shot_caption="Departure and arrival, then go. Saved flights and the archive sit underneath.",
    feats=[
      ("Threats & errors","Coded as they happen, with room for the sentence that actually matters."),
      ("Milestones","Pushback, takeoff, top of climb, cruise, top of descent, landing — timed, so every note has a phase."),
      ("Turbulence log","The phone's own motion sensors record the event while you keep your hands free."),
      ("Export","Demographics, quick takes and the F/A poll, out as one clean PDF when you're ready. Not before."),
    ],
    faq=[
      ("Who can get it?","Trained cabin observers running LOSA-style line audits. It isn't on the public App Store — email us to be issued a TestFlight invite."),
      ("Does it send anything?","No. The observation stays on the device until you export the PDF yourself."),
      ("Is it an official form?","No. It's a notepad shaped like the method."),
      ("Price?","Free to the observers it's issued to."),
    ],
    privacy=[
      "Observations are stored on your device only. LOSA does not use iCloud, has no account, and makes no network requests.",
      "Motion-sensor data is used only while you are recording a turbulence event, and only the event log is kept — never raw sensor streams.",
      "Nothing leaves the device until you export a PDF yourself and choose where to send it.",
      "The app contains no analytics, no advertising and no third-party SDKs. Deleting the app deletes all of its data.",
    ],
  ),
]

STATUS = {"live":("On the App Store","live"), "soon":("Coming soon",""), "beta":("Beta · auditors only","")}
PILLARS = [
  ("We can't read it. That's the design.",
   "No account, no analytics, no server. Your data lives on your phone and in your own iCloud."),
  ("It says the number and gets out of the way.",
   "One screen, one answer. No streaks, no confetti, no tiers."),
  ("Pay once where we can.",
   "Sus Spend and Cloud Drink are one price, forever. Sus Pay's log is free; only the pay engine is a subscription."),
]

e = html.escape

def accent(a):
    return f'style="--accent:var(--app-{a["id"]});--accent-txt:var(--app-{a["id"]}-txt)"'

def page(title, body, *, desc, rel="", current=None, canonical):
    nav = f'<a href="{rel}index.html"{" aria-current=page" if current=="home" else ""}>Home</a>' + "".join(
        f'<a href="{rel}apps/{a["id"]}.html"{" aria-current=page" if current==a["id"] else ""}>{e(a["name"])}</a>' for a in APPS)
    foot_apps = " · ".join(f'<a href="{rel}apps/{a["id"]}.html">{e(a["name"])}</a>' for a in APPS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{rel}assets/icons/sus-spend.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sanchez:ital@0;1&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{rel}assets/site.css">
</head>
<body>
<nav class="nav" aria-label="Site">
  <div class="wrap nav-in">
    <a class="brand" href="{rel}index.html"><span class="mark" aria-hidden="true">L</span><b>LenDew</b></a>
    <div class="nav-links">{nav}</div>
  </div>
</nav>
<main>
{body}
</main>
<footer>
  <div class="wrap foot">
    <div class="col" style="min-width:220px"><b>LenDew</b><span>A house of quiet instruments for measuring, making, and mapping.</span></div>
    <div class="col"><b>Apps</b><span>{foot_apps}</span></div>
    <div class="col"><b>Help</b><span><a href="{rel}support.html">Support</a> · <a href="{rel}privacy.html">Privacy</a></span></div>
    <div class="col" style="margin-left:auto"><b>Independent</b><span>Made by one flight attendant.<br>© LenDew</span></div>
  </div>
</footer>
</body>
</html>
"""

def home():
    cards = ""
    for a in APPS:
        label, cls = STATUS[a["status"]]
        note = f'<span class="price-note">+ {e(a["price_note"])}</span>' if "/month" in a["price_note"] else ""
        cards += f"""
      <a class="card" href="apps/{a["id"]}.html" {accent(a)}>
        <div class="card-top">
          <span class="icon"><img src="assets/icons/{a["id"]}.png" alt="" width="60" height="60"></span>
          <div><div class="store">{e(a["store"])}</div><h2>{e(a["name"])}</h2><div class="line">{e(a["line"])}</div></div>
        </div>
        <p class="head">{e(a["head"])}</p>
        <div class="card-foot"><span class="price">{e(a["price"])}</span>{note}<span class="status {cls}">{e(label)}</span></div>
      </a>"""
    pillars = "".join(f'<div class="pillar"><div class="rule"></div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h,p in PILLARS)
    swatches = "".join(f'<i style="background:var(--app-{a["id"]})"></i>' for a in APPS)
    body = f"""
  <div class="wrap hero-home">
    <div class="swatches" aria-hidden="true">{swatches}</div>
    <p class="eyebrow" style="color:var(--text-muted)">Independent iOS apps</p>
    <h1 style="margin-top:16px">A house of quiet instruments.</h1>
    <p class="sub">Four small apps for measuring, making, and mapping. <em>You type it. Nobody else reads it.</em> Nothing syncs to us, because there is no us to sync to.</p>
  </div>
  <div class="wrap"><div class="grid">{cards}
  </div></div>
  <div class="wrap sec" style="margin-top:64px">
    <h2>Small apps that say the number and shut up.</h2>
    <div class="pillars">{pillars}</div>
  </div>"""
    return page("LenDew — independent iOS apps", body, desc="Sus Spend, Cloud Drink, Sus Pay and LOSA. Small iOS apps with no account, no analytics and no server.", current="home", canonical=SITE+"/")

def app_page(a):
    label, _ = STATUS[a["status"]]
    cta = (f'<a class="badge" href="{a["store_url"]}">Download on the App Store</a>' if a["store_url"]
           else f'<span class="badge ghost">{e(label)}</span>')
    feats = "".join(f'<div class="feat"><div class="rule"></div><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h,p in a["feats"])
    faq = "".join(f'<div><h3>{e(q)}</h3><p>{e(ans)}</p></div>' for q,ans in a["faq"])
    body = f"""
  <div class="wrap hero-app" {accent(a)}>
    <div>
      <div class="icon-row"><span class="icon"><img src="../assets/icons/{a["id"]}.png" alt="" width="44" height="44"></span><p class="eyebrow">{e(a["store"])} · {e(label)}</p></div>
      <h1>{e(a["head"])}</h1>
      <p class="tag">{e(a["tag"])}</p>
      <div class="cta">{cta}<span class="price-big">{e(a["price"])} <span>{e(a["price_note"])}</span></span></div>
    </div>
    <figure class="phone-field" style="margin:0">
      <div class="phone"><img src="../assets/shots/{a["id"]}-1.webp" alt="{e(a["name"])} screenshot" width="1206" height="2622" loading="eager"></div>
      <figcaption class="lede" style="font-size:14px;text-align:center;margin-top:16px">{e(a["shot_caption"])}</figcaption>
    </figure>
  </div>
  <div class="wrap sec" {accent(a)}>
    <p class="eyebrow">What it does</p><h2>{e(a["sub"])}</h2>
    <div class="feats">{feats}</div>
  </div>
  <div class="wrap sec" {accent(a)}>
    <p class="eyebrow">Questions</p><h2>Before you buy.</h2>
    <div class="faq">{faq}</div>
  </div>
  <div class="wrap" {accent(a)}>
    <div class="privacy-block">
      <p class="big">We can't read it.<br>That's the design.</p>
      <p class="lede">{e(a["privacy"][0])} <a href="../privacy.html#{a["id"]}">Read the full {e(a["name"])} privacy policy.</a></p>
    </div>
  </div>"""
    title = f'{a["store"]} — {a["line"].rstrip(".")} · LenDew'
    return page(title, body, desc=a["tag"], rel="../", current=a["id"], canonical=f'{SITE}/apps/{a["id"]}.html')

def support():
    rows = "".join(f'<dt>{e(a["store"])}</dt><dd>{e(STATUS[a["status"]][0])}</dd>' for a in APPS)
    body = f"""
  <div class="wrap doc">
    <p class="eyebrow" style="color:var(--text-muted)">Support</p>
    <h1 style="margin-top:12px">One person answers this.</h1>
    <p>Every LenDew app is made and supported by one person. Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> with the app's name and what happened, and you'll hear back — usually within a couple of days, sooner if it's broken.</p>
    <h2>Before you write</h2>
    <p><strong>Purchases and refunds</strong> are handled by Apple, not by us: open the App Store, tap your picture, then <em>Purchase History</em>. Refund requests go through <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
    <p><strong>Sync</strong> in Sus Spend and Sus Pay runs through your own iCloud. If devices disagree, check that both are signed into the same Apple Account with iCloud Drive on.</p>
    <p><strong>Invites</strong> from Sus Spend and Sus Pay are iCloud share links. They open in the app they came from; if the app isn't installed yet, the link shows an App Store button first.</p>
    <p><strong>LOSA</strong> isn't on the public App Store. Trained observers can email the address above to be issued a TestFlight invite.</p>
    <h2>The apps</h2>
    <dl>{rows}</dl>
    <p class="muted" style="margin-top:32px">LenDew is an independent studio. It isn't affiliated with any airline, and none of these apps are company systems.</p>
  </div>"""
    return page("Support · LenDew", body, desc="How to get help with Sus Spend, Cloud Drink, Sus Pay and LOSA.", canonical=SITE+"/support.html")

def privacy():
    toc = "".join(f'<a href="#{a["id"]}">{e(a["store"])}</a>' for a in APPS)
    secs = ""
    for a in APPS:
        secs += f'<h2 id="{a["id"]}">{e(a["store"])}</h2>' + "".join(f"<p>{e(p)}</p>" for p in a["privacy"])
    body = f"""
  <div class="wrap doc">
    <p class="eyebrow" style="color:var(--text-muted)">Privacy policy</p>
    <h1 style="margin-top:12px">We can't read it. That's the design.</h1>
    <p>LenDew apps have no accounts and no servers. There is no LenDew database anywhere that holds your data, so there is nothing for us to sell, leak or hand over. What follows is the specific version of that promise for each app.</p>
    <p class="muted">Effective 11 September 2026. Questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
    <div class="toc">{toc}</div>
    {secs}
    <h2>All apps</h2>
    <p>None of the apps contain analytics, advertising, tracking or third-party SDKs, and none collect data for any purpose. Where an app uses iCloud, the data is stored in your private iCloud database under Apple's <a href="https://www.apple.com/legal/privacy/">privacy policy</a>; LenDew has no access to it. Purchases and subscriptions are processed by Apple.</p>
    <p>If this policy changes, the date above changes with it, and the change will be described here.</p>
  </div>"""
    return page("Privacy · LenDew", body, desc="Privacy policy for Sus Spend, Cloud Drink, Sus Pay and LOSA: no account, no analytics, no server.", canonical=SITE+"/privacy.html")

def write(rel, content):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8"); print("wrote", rel, len(content.encode()) // 1024, "KB")

if __name__ == "__main__":
    write("index.html", home())
    for a in APPS: write(f"apps/{a['id']}.html", app_page(a))
    write("support.html", support())
    write("privacy.html", privacy())
