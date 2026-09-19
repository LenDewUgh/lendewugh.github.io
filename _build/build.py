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
    tag="Sus Pay reads the trips in your CrewSchedule calendar and estimates what each one should pay under the contract — trip pay, boarding, per diem and A position. Free. First Class, with automatic trip updates, is coming later.",
    price="Free", price_note="First Class coming soon, $2.99/month.",
    status="soon", store_url=None,
    sub="Check the roster against the paycheck.",
    shot_caption="July's take-home at the top, then every trip with its awarded credit, layovers and the pay it actually produced.",
    feats=[
      ("Import from your calendar","Trips come straight from your CrewSchedule calendar — legs, positions, layovers and TFP. No retyping the pairing."),
      ("Pay that shows its work","Base, boarding, per diem and A pay, each line labelled with the part of the contract it comes from."),
      ("Honest about what's checked","Rules checked against real Alaska pay count toward your total. The rest are shown as not verified, or left out until they're right."),
      ("Take-home","401(k), ESPP and your last paycheck entered once, so you see roughly what lands."),
    ],
    faq=[
      ("Is it out yet?","Not yet. This page goes live with the listing."),
      ("What's free and what isn't?","Everything in the app today is free: calendar import, trip pay, weather and monthly summaries. First Class — automatic trip updates, delay pay and per diem that follows your actual times — is coming later at $2.99 a month. Features that are free now stay free."),
      ("Does it read my schedule?","Only the CrewSchedule calendar you pick, read-only, on your phone. Nothing is sent to LenDew or to Alaska."),
      ("How do I set it up?","Step by step in the Sus Pay guide — it's linked from the Support page."),
      ("Can I get my data out?","PDF report, any month."),
    ],
    privacy=[
      "Your trips, rates and pay history are stored on your device only. There is no account and no sign-in, and deleting the app deletes the data with it. Your pay is never uploaded anywhere.",
      "Calendar access is read-only and is used only to read the CrewSchedule calendar you pick. You can turn it off at any time in Settings.",
      "If you share your schedule, your trip names, dates and layover cities — never any pay — are stored in your own iCloud and shared through Apple's iCloud sharing with the people you invite, and only with them.",
      "Layover weather is fetched from Open-Meteo using an airport's latitude, longitude and date — nothing about you.",
      "Sunrise and sunset times use your own location, to about three kilometres, sent to that same service. It is not stored or shared.",
      "If a paid tier is offered later, it will be handled entirely by Apple through the App Store. LenDew never sees your payment details.",
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

def page(title, body, *, desc, rel="", current=None, canonical, icon="sus-spend", noindex=False):
    nav = f'<a href="{rel}index.html"{" aria-current=page" if current=="home" else ""}>Home</a>' + "".join(
        f'<a href="{rel}apps/{a["id"]}.html"{" aria-current=page" if current==a["id"] else ""}>{e(a["name"])}</a>' for a in APPS)
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
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
<link rel="icon" href="{rel}assets/icons/{icon}.png">{robots}
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
    return page(title, body, desc=a["tag"], rel="../", current=a["id"], canonical=f'{SITE}/apps/{a["id"]}.html', icon=a["id"])

def support():
    rows = "".join(f'<dt>{e(a["store"])}</dt><dd>{e(STATUS[a["status"]][0])}</dd>' for a in APPS)
    body = f"""
  <div class="wrap doc">
    <p class="eyebrow" style="color:var(--text-muted)">Support</p>
    <h1 style="margin-top:12px">One person answers this.</h1>
    <p>Every LenDew app is made and supported by one person. Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> with the app's name and what happened, and you'll hear back — usually within a couple of days, sooner if it's broken.</p>
    <h2>Before you write</h2>
    <p><strong>Setting up Sus Pay?</strong> The <a href="sus-pay-guide.html">step-by-step Sus Pay guide</a> walks through connecting your work calendar, importing trips and reading your pay.</p>
    <p><strong>Purchases and refunds</strong> are handled by Apple, not by us: open the App Store, tap your picture, then <em>Purchase History</em>. Refund requests go through <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
    <p><strong>Sync</strong> in Sus Spend and Sus Pay runs through your own iCloud. If devices disagree, check that both are signed into the same Apple Account with iCloud Drive on.</p>
    <p><strong>Invites</strong> from Sus Spend and Sus Pay are iCloud share links. They open in the app they came from; if the app isn't installed yet, the link shows an App Store button first.</p>
    <p><strong>LOSA</strong> isn't on the public App Store. Trained observers can email the address above to be issued a TestFlight invite.</p>
    <h2>The apps</h2>
    <dl>{rows}</dl>
    <p class="muted" style="margin-top:32px">LenDew is an independent studio. It isn't affiliated with any airline, and none of these apps are company systems.</p>
  </div>"""
    return page("Support · LenDew", body, desc="How to get help with Sus Spend, Cloud Drink, Sus Pay and LOSA.", canonical=SITE+"/support.html")

def sus_pay_guide():
    body = f"""
  <div class="wrap doc" style="--accent:var(--app-sus-pay);--accent-txt:var(--app-sus-pay-txt)">
    <p class="eyebrow">Suspicious Pay · Guide</p>
    <h1 style="margin-top:12px">Set up Sus Pay, step by step.</h1>
    <p>About ten minutes, once. You'll need your iPhone, your Alaska email and password, and your last paycheck. Sus Pay estimates your pay from your own schedule — it's not your paycheck, it's how you check it.</p>
    <div class="toc"><a href="#calendar">1 · Calendar</a><a href="#setup">2 · Pay setup</a><a href="#connect">3 · Connect</a><a href="#import">4 · Import</a><a href="#premium">5 · Premium</a><a href="#trades">Trades</a><a href="#reading">Reading your pay</a><a href="#help">Troubleshooting</a></div>

    <h2 id="calendar">1. Put your work calendar on your iPhone</h2>
    <p>Sus Pay reads your trips from the CrewSchedule calendar that comes with your Alaska email. If you already see your trips in Apple's Calendar app, skip to step 2.</p>
    <ol>
      <li>Open the iPhone <strong>Settings</strong> app.</li>
      <li>Tap <strong>Apps → Calendar → Calendar Accounts → Add Account</strong>.</li>
      <li>Choose <strong>Microsoft Exchange</strong> and sign in with your Alaska email and password.</li>
      <li>Make sure <strong>Calendars</strong> is switched on for that account.</li>
      <li>Open Apple's Calendar app and check that your trips appear. It can take a few minutes the first time.</li>
    </ol>

    <h2 id="setup">2. Open Sus Pay and set up your pay</h2>
    <p>The first time you open the app, a short tour explains how it works, then asks four things. You can change any of them later in <strong>≡ → Current Rate</strong>.</p>
    <ol>
      <li><strong>Seniority Date</strong> — sets your step on the pay scale, and every raise lands on the right date. Find it in Rainmaker: expand <strong>Crew Member Profile</strong> and look for <strong>Seniority Date</strong>. No Rainmaker handy? Use the year and date from your PeopleSoft “Step Progression Pay Increase” email instead.</li>
      <li><strong>401(k)</strong> — the percentage you contribute.</li>
      <li><strong>ESPP</strong> — the percentage you put into the stock purchase plan, if any.</li>
      <li><strong>Take-home</strong> — from the bottom of your last paycheck, enter <strong>Current Total Gross</strong> and <strong>Current Net Pay</strong>.</li>
    </ol>

    <h2 id="connect">3. Let Sus Pay read your calendar</h2>
    <ol>
      <li>Tap <strong>≡</strong> (top right) → <strong>Current Rate</strong> and scroll to <strong>Calendar</strong>.</li>
      <li>When iPhone asks, allow calendar access. Sus Pay only reads — it never changes your calendar.</li>
      <li>Pick your <strong>CrewSchedule</strong> calendar. If it's the only work calendar, Sus Pay picks it for you.</li>
    </ol>

    <h2 id="import">4. Import your trips</h2>
    <ol>
      <li>On your trips list, tap the <strong>calendar button with the plus</strong>.</li>
      <li>Sus Pay shows the trips it found from about three weeks back and months ahead. New ones are ticked.</li>
      <li>Tap <strong>Import</strong>. Each trip arrives with its legs, layovers, positions and TFP, and its pay underneath.</li>
    </ol>
    <p><strong>Import each trip before you fly it.</strong> If flying is taken away from a trip mid-sequence, the calendar simply stops showing it — only a copy saved beforehand remembers what you were scheduled to fly. Importing once the trip appears on your schedule keeps that record.</p>

    <h2 id="premium">5. Add premium, if the trip had it</h2>
    <p>The calendar doesn't show whether a trip is premium, so Sus Pay can't know.</p>
    <ol>
      <li>Open the trip.</li>
      <li>Tap <strong>Add</strong>.</li>
      <li>Set the multiplier to match your roster — 1.5×, 2×, 2.5× or 3×.</li>
    </ol>

    <h2 id="trades">Traded, dropped or canceled a trip?</h2>
    <p>If a trip leaves your calendar before it starts, it shows under <strong>No longer on your schedule</strong> the next time you open the import screen. Tap it and pick what happened:</p>
    <ul>
      <li><strong>Swap and Delete</strong> — you traded or dropped it. It comes off your month so it isn't counted twice.</li>
      <li><strong>Keep and Pay Protect</strong> — the company canceled it. It stays, marked Pay Protected, and pays the way a protected trip does (no boarding or per diem). Changed your mind? Undo is on the trip's pay card.</li>
      <li><strong>Keep for Now</strong> — not sure yet. Nothing changes, and it asks again next time.</li>
    </ul>
    <p>Once a trip has started, Sus Pay never offers to remove it — a trip that changes mid-sequence may be a reassignment, and the saved copy is your record of it.</p>

    <h2 id="reading">Reading your pay</h2>
    <p>Every pay line is one of three kinds:</p>
    <ul>
      <li><strong>In your total</strong> — checked against real Alaska pay and counted.</li>
      <li><strong>Not verified</strong> — shown so you know to look, but left out of the total until real pay confirms it.</li>
      <li><strong>Hidden</strong> — not right yet, so the app says nothing rather than something misleading.</li>
    </ul>
    <p>That makes a total here the conservative one — more likely low than high. <strong>≡ → What's Included</strong> lists exactly what the app covers today. Our contract is complex, and more rules are on the way.</p>
    <p>Where Sus Pay and your pay disagree, treat it as a question to look into, not proof. Sus Pay doesn't file anything — if you find a shortfall, you claim it the way you always have. It isn't made by, affiliated with or endorsed by Alaska Airlines or AFA.</p>

    <h2 id="help">Troubleshooting</h2>
    <h3>No trips show up</h3>
    <p>Check Apple's Calendar app first — if your trips aren't there, redo step 1. If they are, check iPhone <strong>Settings → Apps → Sus Pay → Calendars</strong> is allowed, and that CrewSchedule is picked in <strong>≡ → Current Rate</strong>.</p>
    <h3>A leg's TFP looks wrong</h3>
    <p>Tap the TFP figure on that leg to correct it. Sus Pay remembers the route for next time.</p>
    <h3>I got a new phone</h3>
    <p>Your trips live on your phone, so they move with an iPhone backup and restore. A fresh install without a backup starts empty.</p>
    <h3>Something else looks wrong</h3>
    <p>Tap <strong>≡ → Feedback</strong> — it opens an email with your app version attached. Or write to <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> with the trip number and what you expected to see.</p>
  </div>"""
    return page("Sus Pay guide · LenDew", body, desc="Step-by-step setup for Suspicious Pay: connect your work calendar, set your seniority date, import trips and read your pay.", current="sus-pay", canonical=SITE+"/sus-pay-guide.html", icon="sus-pay")

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
    <p class="muted">Effective 19 September 2026. Questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
    <div class="toc">{toc}</div>
    {secs}
    <h2>All apps</h2>
    <p>None of the apps contain analytics, advertising, tracking or third-party SDKs, and none collect data for any purpose. Where an app uses iCloud, the data is stored in your private iCloud database under Apple's <a href="https://www.apple.com/legal/privacy/">privacy policy</a>; LenDew has no access to it. Purchases and subscriptions are processed by Apple.</p>
    <p>If this policy changes, the date above changes with it, and the change will be described here.</p>
    <h3>Changes</h3>
    <p><strong>19 September 2026</strong> — Suspicious Pay: corrected to say trips and pay are stored on your device only (not in iCloud), that only schedule sharing uses iCloud, and that sunrise and sunset times send your approximate location to Open-Meteo. Removed references to importing roster PDFs, which the app no longer does.</p>
  </div>"""
    return page("Privacy · LenDew", body, desc="Privacy policy for Sus Spend, Cloud Drink, Sus Pay and LOSA: no account, no analytics, no server.", canonical=SITE+"/privacy.html")

REDIRECTS = {
  "apps/money-please.html": ("apps/sus-spend.html", "Sus Spend"),
  "apps/pay-tracker.html":  ("apps/sus-pay.html",   "Sus Pay"),
  "apps/cc-perks.html":     ("index.html",          "the LenDew home page"),
}

def not_found():
    """404. Uses rel="/" so it renders correctly from any depth, because
    GitHub Pages serves this one file for every missing path."""
    links = " · ".join(f'<a href="/apps/{a["id"]}.html">{e(a["name"])}</a>' for a in APPS)
    body = f"""
  <div class="wrap doc">
    <p class="eyebrow" style="color:var(--text-muted)">404</p>
    <h1 style="margin-top:12px">That page isn't here.</h1>
    <p>The link may be old, or the page may have moved. Everything LenDew makes is one tap away:</p>
    <p>{links}</p>
    <p class="muted" style="margin-top:32px">Still stuck? Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> and say what you were looking for.</p>
  </div>"""
    return page("Page not found · LenDew", body, desc="That page isn't here.",
                rel="/", canonical=SITE+"/404.html", noindex=True)

def sitemap():
    """No <lastmod>: a build-time date would change on every run and make the
    output non-reproducible, and crawlers ignore a lastmod they can't trust."""
    urls = [SITE + "/"] + [f'{SITE}/apps/{a["id"]}.html' for a in APPS] + \
           [SITE + "/support.html", SITE + "/sus-pay-guide.html", SITE + "/privacy.html"]
    body = "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'{body}</urlset>\n')

def redirect(dest, label):
    """Static hosting can't issue a real 301, so: instant meta refresh, a
    canonical pointing at the successor, noindex, and a visible link if the
    refresh is blocked."""
    url = "/" + dest
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={url}">
<meta name="robots" content="noindex">
<title>Moved — LenDew</title>
<link rel="canonical" href="{SITE}/{dest}">
<link rel="icon" href="/assets/icons/sus-spend.png">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <div class="wrap doc">
    <h1>This page moved.</h1>
    <p>It's now at <a href="{url}">{label}</a>. Taking you there.</p>
  </div>
</body>
</html>
"""

def write(rel, content):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8"); print("wrote", rel, len(content.encode()) // 1024, "KB")

if __name__ == "__main__":
    write("index.html", home())
    for a in APPS: write(f"apps/{a['id']}.html", app_page(a))
    write("support.html", support())
    write("sus-pay-guide.html", sus_pay_guide())
    write("privacy.html", privacy())
    write("404.html", not_found())
    write("sitemap.xml", sitemap())
    for src, (dest, label) in REDIRECTS.items(): write(src, redirect(dest, label))
