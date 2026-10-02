# -*- coding: utf-8 -*-
"""
GENERATE_SITE.PY
Generates the complete static website for Overcoat Prism Bespoke Outerwear (Jacket/Overcoat).
Implements the exact Ridevora precision layout system (Zero Blog).
"""

import os
import re
import json

SITE_DIR = r"d:\antigravity website\overcoatprism"
DOMAIN = "overcoatprism.com"
ADDR = "980 N Michigan Avenue, Suite 1600, Chicago, IL 60611, United States"
PHONE = "+1-888-592-3104"
EMAIL = "concierge@overcoatprism.com"
DESK_HOURS = "7:00 am – 10:00 pm ET, every day"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Sora:wght@500;600;700&display=swap" rel="stylesheet">"""

def get_utility():
    return f"""<div class="utility"><div class="wrap">
  <div class="u-left"><span><span class="dot" aria-hidden="true"></span>Fitting consultations daily, {DESK_HOURS}</span><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></div>
  <div class="u-right"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="booking.html">Book bespoke fitting</a></div>
</div></div>"""

def get_header(active_page=""):
    pages = [
        ("index.html", "Home"),
        ("products.html", "Outerwear"),
        ("booking.html", "Book Fitting"),
        ("about.html", "Heritage"),
        ("faq.html", "FAQ"),
        ("contact.html", "Contact")
    ]
    links = []
    for href, label in pages:
        cur = ' aria-current="page"' if href == active_page else ''
        links.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    links_html = "".join(links)
    
    return f"""<a class="skip" href="#main">Skip to content</a>
{get_utility()}
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Overcoat Prism home"><span class="brand-mark"><svg viewBox="0 0 32 32" aria-hidden="true"><polygon points="16,4 28,26 4,26" fill="none" stroke="#D97706" stroke-width="2.5"/><line x1="16" y1="4" x2="16" y2="26" stroke="#fff" stroke-width="1.8"/><circle cx="16" cy="18" r="2.5" fill="#D97706"/></svg></span><span class="brand-text"><strong>OVERCOAT</strong><span>PRISM</span></span></a>
  <nav class="main-nav" id="main-nav" aria-label="Main"><ul>{links_html}<li class="nav-only-mobile"><a href="booking.html">Book Fitting</a></li></ul></nav>
  <div class="header-cta"><a class="btn btn-ghost btn-sm" href="tel:{PHONE.replace('-', '')}">Call desk</a><a class="btn btn-accent btn-sm" href="booking.html">Book fitting</a>
  <button class="nav-toggle" type="button" aria-label="Open menu" aria-controls="main-nav" aria-expanded="false"><span></span></button></div>
</div></header>"""

def get_footer():
    return f"""<footer class="site-footer"><div class="wrap">
  <div class="f-top">
    <div>
      <a class="brand" href="index.html" aria-label="Overcoat Prism home"><span class="brand-mark"><svg viewBox="0 0 32 32" aria-hidden="true"><polygon points="16,4 28,26 4,26" fill="none" stroke="#D97706" stroke-width="2.5"/><line x1="16" y1="4" x2="16" y2="26" stroke="#fff" stroke-width="1.8"/><circle cx="16" cy="18" r="2.5" fill="#D97706"/></svg></span><span class="brand-text"><strong>OVERCOAT</strong><span>PRISM</span></span></a>
      <p class="f-about">Hand-canvassed bespoke overcoats, storm coats, and tailored jackets crafted on Chicago's Magnificent Mile. Traditional horsehair chest construction with natural horn fastenings.</p>
    </div>
    <div><h2>Explore</h2><ul>
      <li><a href="index.html">Atelier Home</a></li><li><a href="products.html">Outerwear Collection</a></li><li><a href="booking.html">Book Private Fitting</a></li>
      <li><a href="about.html">Heritage &amp; Tailoring</a></li><li><a href="faq.html">Bespoke FAQ</a></li><li><a href="contact.html">Contact Us</a></li></ul></div>
    <div><h2>Policies</h2><ul>
      <li><a href="cancellation-refund-policy.html">Cancellation &amp; Fitting Policy</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li>
      <li><a href="terms-and-conditions.html">Terms &amp; Conditions</a></li><li><a href="cookie-policy.html">Cookie Policy</a></li>
      <li><a href="disclaimer.html">Tailoring Disclaimer</a></li></ul></div>
    <div><h2>Visit &amp; call</h2><ul>
      <li>{ADDR}</li>
      <li><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>Desk hours: {DESK_HOURS}</li></ul></div>
  </div>
  <div class="f-bottom"><span>&copy; <span data-year>2026</span> Overcoat Prism Bespoke Outerwear LLC. All rights reserved.</span>
    <ul><li><a href="sitemap.xml">Sitemap</a></li><li><button class="link-btn" type="button" data-open-cookies>Cookie settings</button></li></ul></div>
</div></footer>
<div class="cookie" role="dialog" aria-labelledby="cookie-title" aria-live="polite">
  <h2 id="cookie-title">Your privacy choices</h2>
  <p>We use essential cookies to manage bespoke fitting reservations, plus minimal telemetry to refine our outerwear tailoring archives. You can modify your choices at any time. <a href="cookie-policy.html">Cookie Policy</a></p>
  <div class="row"><button class="btn btn-accent btn-sm" type="button" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" type="button" data-consent="essential">Essential only</button></div>
</div>
<button class="to-top" type="button" aria-label="Back to top"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
<script src="assets/js/main.js" defer></script>"""

def check_paragraphs(paras, page_name):
    for idx, p in enumerate(paras):
        words = len(p.split())
        if words < 60 or words > 110:
            raise ValueError(f"Paragraph {idx+1} in {page_name} has {words} words (expected 60-110 words). Text: {p[:60]}...")

# -----------------------------------------------------------------------------
# PAGE BUILDERS
# -----------------------------------------------------------------------------

def build_index():
    # Assets 1, 2, 3, 4, 5, 6, 7
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Overcoat Prism | Bespoke Winter Overcoats &amp; Tailored Jackets Chicago</title>
<meta name="description" content="Discover Overcoat Prism: Chicago's premier bespoke outerwear atelier. Hand-canvassed melton wool greatcoats, cashmere balmacaans, and storm jackets.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/index.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Overcoat Prism | Bespoke Winter Overcoats &amp; Tailored Jackets">
<meta property="og:description" content="Handcrafted bespoke outerwear, storm overcoats, and wool tailoring from our Chicago Magnificent Mile atelier.">
<meta property="og:url" content="https://{DOMAIN}/index.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("index.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/overcoatprism_asset_1.jpg" alt="Man and woman in tailored camel wool overcoats posing in outdoor winter daylight" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Chicago Bespoke Outerwear</nav>
    <h1>We build overcoats the way armor was once forged for cold winds</h1>
    <p>Overcoat Prism is an independent Chicago tailoring atelier built on three unwavering disciplines: full floating horsehair canvas chest pieces, unadulterated British and Italian heavy woolens, and individual paper patterns drawn by master cutters.</p>
    <div style="display:flex;gap:16px;margin-top:28px;flex-wrap:wrap">
      <a class="btn btn-accent" href="booking.html">Book Fitting Session</a>
      <a class="btn btn-ghost" href="products.html">View Outerwear</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Atelier Genesis</span>
      <h2>Born from the bitter chill of Lake Michigan winds</h2>
      <p>Overcoat Prism was founded in response to the fragile state of modern commercial outerwear. High-street coats and designer labels routinely substitute fusible chemical glues for horsehair canvas, trim warm natural wool with cheap polyester linings, and sell generic sizing that buckles under harsh winter gales.</p>
      <p>We established our workshop at One Magnificent Mile to restore authentic architectural tailoring to cold-weather coats. Every bespoke garment we produce features multi-layered horsehair canvas hand-padded across the chest, creating a rolling lapel that breathes with your body and drapes with regal authority.</p>
      <p>The name Prism reflects how a well-structured coat refracts the elements: shielding the wearer from freezing precipitation while projecting an unmistakable aura of sartorial refinement and warmth.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_2.jpg" alt="Bespoke tailored wool overcoat showing hand-sewn lapel pick stitching and structure" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Sartorial Metrics</span><h2 style="color:#fff">Architectural Tailoring by the Numbers</h2></div></div>
    <div class="numbers">
      <div class="number"><b>680g/m</b><span>average cloth weight of our heavy British winter melton wools</span></div>
      <div class="number"><b>4,200</b><span>hand-guided pad stitches securing the floating horsehair canvas</span></div>
      <div class="number"><b>3 Stage</b><span>in-person fittings: raw basted skeleton, forward fitting, and final delivery</span></div>
      <div class="number"><b>15 hours</b><span>of daily concierge advisory desk, open every day of the calendar year</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/images/overcoatprism_asset_3.jpg" alt="Master tailor fitting a structured cashmere jacket on canvas mannequin in atelier" width="1000" height="667" loading="lazy">
    <div>
      <span class="kicker">Bench Discipline</span>
      <h2>What happens before your coat leaves our cutting table</h2>
      <p>When you commission an overcoat at our Chicago salon, our master cutter captures thirty-four individual anatomical measurements, noting shoulder slope, posture curvature, and jacket layering clearance. We hand-draft an individual paper pattern unique to your silhouette.</p>
      <p>The cloth is sheared by hand using forged steel shears, then joined to a floating canvas composed of Mongolian horsehair, camel wool, and Irish linen. We press each structural seam over curved wooden hams using five-kilogram gravity irons, permanently sculpting shape into three-dimensional wool fibers.</p>
      <p>Finally, natural water-buffalo horn buttons are cross-stitched with waxed French silk thread, elevated on thread shanks to ensure effortless buttoning even while wearing heavy winter gloves.</p>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="wrap">
    <div class="sec-center"><span class="kicker">Core Principles</span><h2>The Three Prism Commitments</h2></div>
    <div class="values">
      <div class="value"><h3>Zero Fused Adhesives</h3><p>We never use synthetic glue to fuse coat fronts. Our full canvas breathes naturally, molds to your torso over time, and will never bubble after dry cleaning.</p></div>
      <div class="value"><h3>Ethical Heritage Cloth</h3><p>All wools, tweeds, and cashmeres originate from historic British and Northern Italian mills with certified animal welfare and environmental sustainability.</p></div>
      <div class="value"><h3>Master Cutters, Not Retail Staff</h3><p>Your fitting is directed by credentialed bespoke cutters who understand balance lines, blade ease, and drape. Phone us, and a tailor answers.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Silhouette Mastery</span>
      <h2>The Mighty Pea Coat &amp; Heavyweight Melton Outerwear</h2>
      <p>The double-breasted officer pea coat remains one of tailoring's most formidable creations. Originally designed for naval watch officers braving North Atlantic tempests, our version is crafted from 800-gram dense melton wool with broad convertible lapels.</p>
      <p>When buttoned against winter blizzards, the high collar seals the throat with a concealed storm latch, while fleece-lined corduroy handwarmer pockets provide instant shelter for the hands. It is an heirloom piece engineered to withstand decades of relentless weather.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_4.jpg" alt="Heavyweight charcoal melton wool pea coat with double-breasted horn button closure" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Bespoke Silhouettes</span><h2 style="color:#fff">Selected Outerwear Classes from the Atelier</h2></div></div>
    <div class="jacket-grid">
      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_5.jpg" alt="Tailored herringbone tweed overcoat draped over arm of client" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Donegal Tweed</span>
          <h3>The Donegal Field Coat</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Pure Irish herringbone tweed with flecks of peat ochre and storm flap throat latch.</p>
          <div class="jacket-specs">
            <span>Weight: 580g/m</span>
            <span>Buttons: Real Buffalo Horn</span>
            <span>Lining: Cupro Silk</span>
            <span>Style: Single-Breasted</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">Class I Bespoke</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>
      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_6.jpg" alt="Classic trench coat with storm flap, buckled waist belt, and water-repellent gabardine" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Weatherproof</span>
          <h3>The All-Weather Gabardine Trench</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">High-density long-staple cotton gabardine with removable cashmere button-in warm liner.</p>
          <div class="jacket-specs">
            <span>Cloth: 100% Gabardine</span>
            <span>Hardware: Leather Buckles</span>
            <span>Vent: Deep Inverted Pleat</span>
            <span>Fit: Tailored Military</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">Class II Bespoke</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>
      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_7.jpg" alt="Handcrafted leather flight jacket with shearling fur collar and ribbed storm cuffs" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Artisan Leather</span>
          <h3>The Aviator Shearling Jacket</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Vegetable-tanned full-grain lambskin with dense natural shearling collar and brass zip.</p>
          <div class="jacket-specs">
            <span>Hide: Spanish Lambskin</span>
            <span>Collar: Natural Shearling</span>
            <span>Cuffs: Ribbed Storm Knit</span>
            <span>Hardware: Antiqued Brass</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">Class III Bespoke</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:900px">
    <div class="prose">
      <h2>Who We Serve</h2>
      <p>Our Chicago atelier dresses discerning professionals, executives, and sartorial connoisseurs who require outerwear that performs impeccably in urban climates. Leaders who refuse to compromise professional dignity beneath bulky synthetic down parkas. Connoisseurs who recognize that an overcoat is the most visible garment in one's winter wardrobe. And collectors commissioning heirloom garments intended to pass to subsequent generations.</p>
      <h2>Responsible Sourcing &amp; Longevity</h2>
      <p>True luxury is inherently sustainable through extreme longevity. Because our coats are built with generous seam inlays and natural unglued canvassing, they can be altered, let out, or taken in throughout the owner's lifetime. A bespoke overcoat from our atelier is designed to serve reliably for thirty years, replacing dozens of short-lived mass-market alternatives.</p>
      <h2>Commence Your Bespoke Outerwear Journey</h2>
      <p>Have questions regarding cloth weights, fitting schedules, or private appointments? Visit our salon at 980 N Michigan Avenue, Suite 1600, telephone our tailoring concierge at <a href="tel:{PHONE.replace('-', '')}">{PHONE}</a>, or submit your details via our <a href="contact.html">inquiry page</a>. We look forward to crafting your cold-weather armor.</p>
    </div>
  </div>
</section>

<section class="section-tight" style="background:var(--surface);border-top:1px solid var(--surface-border)">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:24px">
    <div>
      <h3 style="font-family:var(--font-heading);font-size:1.6rem;color:#fff;margin-bottom:6px">Schedule Your Magnificent Mile Fitting</h3>
      <p style="color:var(--text-muted)">Private consultations by appointment. Examine cloth bunches, review balance lines, and experience master tailoring.</p>
    </div>
    <div style="display:flex;gap:12px">
      <a class="btn btn-ghost" href="tel:{PHONE.replace('-', '')}">Call {PHONE}</a>
      <a class="btn btn-accent" href="booking.html">Book Fitting Session</a>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_about():
    # Assets 8, 9, 10, 11
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Heritage &amp; Tailoring Craft | Overcoat Prism Chicago</title>
<meta name="description" content="Discover the bespoke tailoring heritage, floating horsehair canvas craftsmanship, and wool provenance of Overcoat Prism in Chicago.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/about.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Heritage &amp; Tailoring Craft | Overcoat Prism">
<meta property="og:description" content="Learn about our Chicago bespoke tailoring workshop, British wool provenance, and hand-canvassed overcoats.">
<meta property="og:url" content="https://{DOMAIN}/about.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_8.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("about.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/overcoatprism_asset_8.jpg" alt="Bespoke navy cashmere overcoat tailored with sharp roped shoulders and ticket pocket" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Heritage &amp; Tailoring Craft</nav>
    <h1>We build garments that outlast trends and outmaneuver winter</h1>
    <p>Overcoat Prism was established to preserve the architectural craft of bespoke heavy outerwear. In our Chicago cutting room, master tailors cut, shape, and hand-pad floating canvasses for coats that endure for generations.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">The Cutting Bench</span>
      <h2>Honoring the ancient geometry of cloth manipulation</h2>
      <p>True bespoke tailoring begins with understanding that wool is a living, responsive organic fiber. Unlike automated mass manufacturing, where flat fabric is stamped into identical panels by computerized laser cutters, our cutters sculpt wool using steam, tension, and grain orientation.</p>
      <p>Every roll of cloth rests on our cedar racks for forty-eight hours to allow fiber relaxation before chalk touches the surface. We align checks and twill angles across lapels, pocket welts, and back seams with millimeter precision, creating continuous harmonious patterns that move naturally with the human gait.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_9.jpg" alt="Tailoring workbench flat lay: heavy forged fabric shears, chalk, measuring tape, and wool swatches" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Workshop Standards</span><h2 style="color:#fff">Our Construction Pillars</h2></div></div>
    <div class="numbers">
      <div class="number"><b>50+</b><span>hours of skilled manual needlework devoted to each individual overcoat</span></div>
      <div class="number"><b>100%</b><span>natural animal fibers: pure Scottish wool, cashmere, and horsehair</span></div>
      <div class="number"><b>3.5mm</b><span>hand-inlaid seam allowances for comprehensive future body alterations</span></div>
      <div class="number"><b>Lifetime</b><span>pressing, button maintenance, and seam inspection guarantee</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img src="assets/images/overcoatprism_asset_10.jpg" alt="Tailor hand-basting canvas chest piece into wool overcoat body with contrast silk thread" width="1000" height="667" loading="lazy">
    <div>
      <span class="kicker">Floating Canvas</span>
      <h2>The living horsehair chest piece</h2>
      <p>The structural heart of every Overcoat Prism coat is its hand-padded canvas. We stitch together a multi-tiered foundation of coarse Mongolian horsehair for chest roll, soft wool fleece for comfort, and Irish linen for lapel stability.</p>
      <p>Using thousands of diagonal hand-stitches, our tailors impart a permanent concave curve to the chest and a three-dimensional outward roll to the lapels. Because the canvas is never glued to the outer wool, the layers float freely, responding smoothly to your every movement.</p>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="wrap">
    <div class="sec-center"><span class="kicker">Atelier Credo</span><h2>Our Three Sartorial Promises</h2></div>
    <div class="values">
      <div class="value"><h3>Pure Natural Integrity</h3><p>Every thread, canvas layer, lining, and button comes from natural origins. We ban polyester blends, synthetic fusions, and petrochemical stiffeners.</p></div>
      <div class="value"><h3>Generational Longevity</h3><p>Our coats are designed to survive decades of daily winter commuting. When maintained properly, an Overcoat Prism coat becomes an heirloom passed down through families.</p></div>
      <div class="value"><h3>Transparent Fitting</h3><p>No rushing through pre-made racks. We schedule dedicated two-hour salon fitting sessions with master cutters who adjust every millimeter until balance is absolute.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Finishing Touches</span>
      <h2>The Elegance of Hand-Worked Buttonholes &amp; Linings</h2>
      <p>The final stage of bespoke creation separates exceptional tailoring from ordinary garments. Our buttonholes are slit with a chisel, then meticulously bound by hand using twisted gimp silk thread in a dense, raised purl stitch that takes twenty minutes per buttonhole.</p>
      <p>Undercollars are backed with dense wool melton felt, hand-shaped and steam-ironed so the collar hugs the neck without gaping. Interior pockets are reinforced with jetted double-piping and lined with breathable Bemberg cupro silk that glides effortlessly over knitwear.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_11.jpg" alt="Elegant camel cashmere coat with notched lapels and hand-finished buttonholes" width="1000" height="667" loading="lazy">
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_products():
    # Assets 12, 13, 14, 15, 16, 17
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bespoke Outerwear &amp; Overcoat Collection | Overcoat Prism Chicago</title>
<meta name="description" content="Explore our bespoke outerwear classes: double-breasted officer greatcoats, raglan balmacaans, cashmere chesterfields, and storm trenches in Chicago.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/products.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Bespoke Outerwear Collection | Overcoat Prism">
<meta property="og:description" content="Handcrafted bespoke winter overcoats, balmacaans, and cashmere coats available for custom fitting in Chicago.">
<meta property="og:url" content="https://{DOMAIN}/products.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_12.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("products.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Outerwear Collection</nav>
    <h1>The Bespoke Outerwear Classes</h1>
    <p>Each silhouette represents centuries of sartorial evolution, cut individually to your measurements in heavy British and Italian woolens. Available for bespoke commissions and fitting appointments.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="jacket-grid">

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_12.jpg" alt="Tailored winter wool storm overcoat in Chicago winter daylight" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Classic Greatcoat</span>
          <h3>The Officer Double-Breasted Greatcoat</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Heavy 750g British melton wool with broad peak lapels, inverted back pleat, and martingala half-belt.</p>
          <div class="jacket-specs">
            <span>Weight: 750g/m Melton</span>
            <span>Closure: 6&times;2 Horn</span>
            <span>Length: Below Knee</span>
            <span>Canvas: Full Horsehair</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$280 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_13.jpg" alt="Artisan tailor measuring sleeve length on bespoke overcoat with horn buttons" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Informal Comfort</span>
          <h3>The Raglan Balmacaan</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">One-piece raglan sleeve overcoat in heavy Irish tweed with Prussian storm collar and fly front closure.</p>
          <div class="jacket-specs">
            <span>Weight: 620g Tweed</span>
            <span>Sleeves: Seamless Raglan</span>
            <span>Closure: Fly Front</span>
            <span>Pockets: Deep Slash Welts</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$250 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_14.jpg" alt="Dark wool trench coat with horn buttons and structured waistline" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Formal Evening</span>
          <h3>The Single-Breasted Chesterfield</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Refined black or midnight navy wool-cashmere with velvet collar insert and ticket pocket.</p>
          <div class="jacket-specs">
            <span>Weight: 550g Cashmere</span>
            <span>Collar: Silk Velvet</span>
            <span>Shoulders: Light Roped</span>
            <span>Lining: Bemberg Cupro</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$290 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_15.jpg" alt="Sartorial gentleman wearing double-breasted houndstooth tailored overcoat" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Heritage Pattern</span>
          <h3>The Houndstooth Ulster Coat</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Bold traditional Ulster collar with turnback cuffs and patch pockets crafted in Scottish Saxony wool.</p>
          <div class="jacket-specs">
            <span>Cloth: Saxony Wool</span>
            <span>Collar: Notch Ulster</span>
            <span>Cuffs: Working Turnback</span>
            <span>Back: Deep Box Pleat</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$310 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_16.jpg" alt="Extreme macro of British wool twill weave showing texture and warp-weft density" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Storm Protection</span>
          <h3>The Loden Hunting Coat</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Naturally water-resistant Tyrolean loden wool with deep inverted back pleat and leather buttons.</p>
          <div class="jacket-specs">
            <span>Cloth: Austrian Loden</span>
            <span>Finish: Hydrophobic Wool</span>
            <span>Weight: 680g/m</span>
            <span>Buttons: Woven Leather</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$270 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

      <div class="jacket-card">
        <img class="jacket-img" src="assets/images/overcoatprism_asset_17.jpg" alt="Modern minimalist cocoon wool coat with concealed horn button placket" loading="lazy">
        <div class="jacket-body">
          <span class="jacket-badge">Modern Luxury</span>
          <h3>The Pure Cashmere Polo Coat</h3>
          <p style="color:var(--text-muted);font-size:0.92rem">Unrivaled softness and warmth in double-faced camel cashmere with framed envelope patch pockets.</p>
          <div class="jacket-specs">
            <span>Fiber: 100% Cashmere</span>
            <span>Origin: Biella, Italy</span>
            <span>Buttons: Hand-Carved Bone</span>
            <span>Cuffs: Classic Gauntlet</span>
          </div>
          <div class="jacket-footer">
            <span class="jacket-tier">$350 Consultation</span>
            <a class="btn btn-accent btn-sm" href="booking.html">Book Fitting</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Tailoring Specifications</span><h2 style="color:#fff">The Overcoat Prism Bench Standards</h2></div></div>
    <div class="numbers">
      <div class="number"><b>0 mm</b><span>allowable puckering across sleeve pitch and armscye joining</span></div>
      <div class="number"><b>3.5 cm</b><span>minimum turn-up hem allowance providing substantial bottom drape</span></div>
      <div class="number"><b>8 Cord</b><span>waxed silk thread employed on all main stress structural seams</span></div>
      <div class="number"><b>100%</b><span>natural steam shaping with zero chemical fiber stiffening sprays</span></div>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_booking():
    # Asset 18
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Book a Bespoke Fitting Appointment | Overcoat Prism Chicago</title>
<meta name="description" content="Reserve a private bespoke fitting session at our Chicago Magnificent Mile atelier in four simple steps with real-time consultation estimate. No payment taken online.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/booking.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Book a Bespoke Fitting Appointment | Overcoat Prism">
<meta property="og:description" content="Schedule your private bespoke fitting and wool consultation with master tailors on Chicago's Magnificent Mile.">
<meta property="og:url" content="https://{DOMAIN}/booking.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_18.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("booking.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Book Fitting</nav>
    <h1>Reserve Your Private Bespoke Fitting</h1>
    <p>Four quick steps, a live consultation estimate as you proceed, and zero online payment taken. Our tailoring desk confirms your session and transmits your appointment card within two business hours.</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap booking-layout">
    <form id="booking-form" novalidate>
      <ol class="stepper" aria-label="Fitting progress">
        <li data-step="1" class="active"><b>Step 1</b>Session details</li>
        <li data-step="2"><b>Step 2</b>Silhouette class</li>
        <li data-step="3"><b>Step 3</b>Bespoke add-ons</li>
        <li data-step="4"><b>Step 4</b>Client details</li>
      </ol>

      <fieldset class="b-panel active" data-step="1" style="margin:0">
        <h2>When and where would you like to meet?</h2>
        <div class="form-grid">
          <div class="field"><label for="b-loc">Fitting Location</label><select id="b-loc"><option>Chicago Magnificent Mile Salon (980 N Michigan Ave)</option><option>Private Residence Fitting (Greater Chicago Area)</option><option>Executive Office Consultation (The Loop / River North)</option></select></div>
          <div class="field"><label for="b-party">Consultation Scope</label><select id="b-party"><option>Initial Measurement &amp; Cloth Selection (2 hours)</option><option>Skeleton Baste Fitting (Existing Client)</option><option>Forward Fitting &amp; Hemming (Existing Commission)</option></select></div>
          <div class="field"><label for="b-date">Preferred Date</label><input type="date" id="b-date" required><span class="err-msg">Please choose an upcoming calendar date.</span></div>
          <div class="field"><label for="b-time">Appointment Hour</label><input type="time" id="b-time" value="11:00" step="1800"></div>
          <div class="field"><label for="b-climate">Intended Climate Focus</label><select id="b-climate"><option>Chicago Severe Winter (-10&deg;C to -25&deg;C heavy wool)</option><option>Moderate Mid-Season &amp; Rain (Trench / Gabardine)</option><option>Mild Autumn &amp; Evening Cashmere (5&deg;C to 15&deg;C)</option></select></div>
          <div class="field"><label for="b-layer">Primary Underlayer</label><select id="b-layer"><option>Over Tailored Suit Jacket (Requires extra blade ease)</option><option>Over Heavy Knitwear / Chunky Cardigan</option><option>Over Light Dress Shirt Only</option></select></div>
        </div>
        <p style="font-size:.88rem;color:var(--text-muted);margin:16px 0 0">Private sessions include personal anatomical measurement, tactile examination of fifty British and Italian cloth bunches, and refreshments.</p>
        <div class="b-nav"><span></span><button type="button" class="btn btn-accent" data-next>Select Silhouette &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="2" style="margin:0">
        <h2>Select outerwear class</h2>
        <p style="color:var(--text-muted)">Compare weights and design details on our <a href="products.html">outerwear page</a>.</p>
        <div class="vehicle-pick" id="vehicle-pick" role="group" aria-label="Silhouette classes">
          <div class="pick-card selected" data-rate="280">
            <h4>Double-Breasted Officer Greatcoat</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Heavy 750g melton wool with peak lapels and back martingala. $280 consultation.</p>
          </div>
          <div class="pick-card" data-rate="250">
            <h4>Raglan Balmacaan Coat</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Seamless raglan shoulders in Irish tweed with fly front. $250 consultation.</p>
          </div>
          <div class="pick-card" data-rate="290">
            <h4>Single-Breasted Chesterfield</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Formal wool-cashmere with velvet collar and clean lines. $290 consultation.</p>
          </div>
          <div class="pick-card" data-rate="350">
            <h4>Pure Cashmere Polo Coat</h4>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Double-faced Italian cashmere with envelope patch pockets. $350 consultation.</p>
          </div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="button" class="btn btn-accent" data-next>Add Bespoke Details &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="3" style="margin:0">
        <h2>Optional curatorial details</h2>
        <p style="color:var(--text-muted)">All optional. Full floating horsehair canvas and Bemberg cupro lining are already standard.</p>
        <div class="extras" id="extras-list">
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="95"> <span><b>Removable Button-In Cashmere Storm Lining</b><br><small style="color:var(--text-muted)">Detachable pure cashmere insulated liner for extreme sub-zero weather versatility.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$95</span>
          </div>
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="65"> <span><b>Hand-Carved Water Buffalo Horn Buttons</b><br><small style="color:var(--text-muted)">Bespoke genuine horn buttons individually laser-engraved with your initials on the underside.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$65</span>
          </div>
          <div class="extra-item">
            <label class="check"><input type="checkbox" value="45"> <span><b>Corduroy Lined Handwarmer Pockets</b><br><small style="color:var(--text-muted)">English heavy needlecord lining inside upper slash pockets for instant hand warmth.</small></span></label>
            <span style="font-weight:700;color:var(--accent)">+$45</span>
          </div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="button" class="btn btn-accent" data-next>Client Details &rarr;</button></div>
      </fieldset>

      <fieldset class="b-panel" data-step="4" style="margin:0">
        <h2>Client coordinates</h2>
        <div class="form-grid">
          <div class="field"><label for="b-name">Full Name (as on fitting record)</label><input id="b-name" autocomplete="name" required><span class="err-msg">Please enter your full name.</span></div>
          <div class="field"><label for="b-email">Email Address</label><input id="b-email" type="email" autocomplete="email" required><span class="err-msg">Please enter a valid email.</span></div>
          <div class="field"><label for="b-phone">Mobile Phone</label><input id="b-phone" type="tel" autocomplete="tel" required><span class="err-msg">Please provide a phone number for appointment confirmations.</span></div>
          <div class="field"><label for="b-height">Approximate Height &amp; Weight</label><input id="b-height" placeholder="e.g. 6 ft 1 in, 185 lbs"></div>
          <div class="field full"><label for="b-notes">Special posture or fit considerations (optional)</label><textarea id="b-notes" placeholder="e.g. Broad athletic shoulders, preference for deep interior cigar pocket, travel coat needs…"></textarea></div>
          <div class="full"><label class="check"><input type="checkbox" id="b-terms"> <span>I confirm that I have reviewed and agree to the <a href="cancellation-refund-policy.html" target="_blank">Cancellation &amp; Fitting Policy</a>, <a href="terms-and-conditions.html" target="_blank">Terms &amp; Conditions</a>, and <a href="privacy-policy.html" target="_blank">Privacy Policy</a>.</span></label></div>
        </div>
        <div class="b-nav"><button type="button" class="btn btn-ghost" data-prev>&larr; Back</button><button type="submit" class="btn btn-accent" id="b-submit">Request Bespoke Fitting</button></div>
      </fieldset>
    </form>

    <aside class="summary" aria-labelledby="sum-title" aria-live="polite">
      <h2 id="sum-title">Fitting Summary</h2>
      <div class="sum-car" id="sum-car">Double-Breasted Officer Greatcoat</div>
      <ul class="sum-lines" id="sum-trip">
        <li><span>Fitting Atelier:</span> <b>Chicago Magnificent Mile</b></li>
        <li><span>Consultation Scope:</span> <b>Master Tailor Patterning</b></li>
      </ul>
      <ul class="sum-lines" id="sum-lines" style="margin-top:12px">
        <li><span>Initial Bespoke Consultation:</span> <b>$280</b></li>
        <li><span>Cloth swatch presentation:</span> <b>Included</b></li>
      </ul>
      <div class="sum-total"><span>Consultation Fee</span><b id="sum-total">$280</b></div>
      <p class="sum-note">No payment taken online. The consultation deposit is credited in full toward your completed overcoat commission. Our concierge confirms your time within two business hours.</p>
    </aside>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap split">
    <div>
      <span class="kicker">Cutting Room Integrity</span>
      <h2>The Precision of Chalk and Oak Bench Work</h2>
      <p>Your bespoke overcoat is never assembled from generic pre-cut factory blanks. Every curve is chalked by hand upon solid Michigan oak cutting benches by our master tailors.</p>
      <p>During your fitting, you will feel the balance of the shoulders, test arm mobility, and examine the drape of the heavy British wool in three-way mirrors under true daylight illumination.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_18.jpg" alt="Tailor chalking cutting lines on heavy melton wool cloth on solid oak cutting table" width="1000" height="667" loading="lazy">
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_contact():
    # Asset 19
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact Us | Overcoat Prism Bespoke Outerwear Chicago</title>
<meta name="description" content="Contact Overcoat Prism by phone, email, or visit our Chicago Magnificent Mile atelier at 980 N Michigan Avenue, Suite 1600. Open daily 7 am – 10 pm ET.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/contact.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Contact Us | Overcoat Prism Chicago">
<meta property="og:description" content="Contact Overcoat Prism bespoke tailors at One Magnificent Mile, Chicago. Telephone, email, atelier address, and contact form.">
<meta property="og:url" content="https://{DOMAIN}/contact.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_19.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "ClothingStore", "name": "Overcoat Prism Bespoke Outerwear", "url": "https://{DOMAIN}/", "telephone": "{PHONE}", "email": "{EMAIL}", "priceRange": "$$$$", "address": {{"@type": "PostalAddress", "streetAddress": "980 N Michigan Avenue, Suite 1600", "addressLocality": "Chicago", "addressRegion": "IL", "postalCode": "60611", "addressCountry": "US"}}, "openingHoursSpecification": [{{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "07:00", "closes": "22:00"}}]}}
</script>
</head>
<body>
{get_header("contact.html")}
<main id="main">

<section class="page-hero">
  <img src="assets/images/overcoatprism_asset_19.jpg" alt="Hand-stitched undercollar melton felt and collar shaping on bespoke overcoat" width="1400" height="900" fetchpriority="high">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Contact Us</nav>
    <h1>Connect with Our Tailoring Desk</h1>
    <p>Questions regarding a bespoke commission, cloth bunch selections, or scheduling an in-person fitting? Call our desk, send an inquiry, or visit our Chicago Magnificent Mile salon.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="contact-card">
      <h2>Reach Our Chicago Salon</h2>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><small>Atelier Address</small><span>{ADDR}</span></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg></span><div><small>Telephone</small><a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg></span><div><small>Concierge &amp; Inquiries</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></span><div><small>Bespoke Appointments</small><a href="mailto:fittings@{DOMAIN}">fittings@{DOMAIN}</a></div></div>
      <div class="c-item"><span class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><div><small>Atelier Hours</small><span>Desk &amp; Fitting Salon: {DESK_HOURS}<br>Private Fitting Sessions: By Appointment</span></div></div>
    </div>
    <form class="form-card" id="contact-form" novalidate>
      <h2 style="font-size:1.4rem">Transmit an Inquiry</h2>
      <p style="color:var(--text-muted);font-size:0.92rem;margin-bottom:20px">We reply to every tailoring inquiry within one business day. For same-day fitting inquiries, please telephone directly.</p>
      <div class="form-grid">
        <div class="field"><label for="c-name">Your Full Name</label><input id="c-name" autocomplete="name" required><span class="err-msg">Please provide your name.</span></div>
        <div class="field"><label for="c-email">Email Address</label><input id="c-email" type="email" autocomplete="email" required><span class="err-msg">Please enter a valid email address.</span></div>
        <div class="field"><label for="c-phone">Phone Number (optional)</label><input id="c-phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="c-topic">Topic of Interest</label><select id="c-topic" required><option value="">Choose a topic</option><option>New Bespoke Overcoat Commission</option><option>Cloth Bunches &amp; Fabric Advice</option><option>Existing Commission Fitting Status</option><option>Alterations &amp; Lifetime Servicing</option><option>Other Tailoring Inquiries</option></select><span class="err-msg">Please select a topic.</span></div>
        <div class="field full"><label for="c-message">Message</label><textarea id="c-message" required rows="4" placeholder="Please describe the coat silhouette, cloth preferences, or timeline you have in mind…"></textarea><span class="err-msg">Please write a short message.</span></div>
        <div class="full field"><label class="check" style="color:var(--text-main);font-size:.9rem"><input type="checkbox" required id="c-consent"> <span>I agree that Overcoat Prism Atelier may utilize these details to reply to my inquiry, in strict accordance with the <a href="privacy-policy.html">Privacy Policy</a>.</span></label><span class="err-msg">Please accept the consent terms.</span></div>
        <div class="full"><button class="btn btn-accent" type="submit">Send Message</button></div>
      </div>
    </form>
  </div>
</section>

<section class="section-tight section-white">
  <div class="wrap">
    <div class="sec-head"><div class="intro"><span class="kicker">Location &amp; Access</span><h2>Our Magnificent Mile Atelier</h2><p>Located at 980 N Michigan Avenue, Suite 1600, Chicago, IL 60611 (One Magnificent Mile). Easily accessible from Lake Shore Drive and Michigan Avenue. Valet parking is available at the building's Walton Street entrance.</p></div></div>
    <iframe class="map-frame" title="Map showing 980 N Michigan Avenue, Chicago" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=980+N+Michigan+Avenue,+Chicago,+IL+60611&amp;output=embed"></iframe>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_faq():
    # Asset 20
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bespoke Tailoring &amp; Outerwear FAQ | Overcoat Prism Chicago</title>
<meta name="description" content="Frequently asked questions concerning bespoke overcoat fittings, floating horsehair canvas, cloth weights, and lifetime alterations at Overcoat Prism.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/faq.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Bespoke Tailoring &amp; Outerwear FAQ | Overcoat Prism">
<meta property="og:description" content="Answers to common questions regarding bespoke coat fittings, turnaround times, and heavy British wools.">
<meta property="og:url" content="https://{DOMAIN}/faq.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_20.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("faq.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Tailoring FAQ</nav>
    <h1>Bespoke Outerwear FAQ</h1>
    <p>Everything you need to know regarding in-person fittings, canvas construction, cloth selection, and lifelong maintenance of your handcrafted coat.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <span class="kicker">Common Questions</span>
      <h2>Clarity before your first fitting session</h2>
      <p>Whether you are commissioning your first bespoke heavy overcoat or adding a specialized cashmere storm coat to your wardrobe, we believe in complete operational transparency.</p>
      <p>Review our core tailoring protocols below or speak directly with our concierge team at <a href="tel:{PHONE.replace('-', '')}">{PHONE}</a>.</p>
    </div>
    <img src="assets/images/overcoatprism_asset_20.jpg" alt="Finished bespoke overcoat hanging on solid cedar hanger with dust bag and brass tag" width="1000" height="667" loading="lazy">
  </div>
</section>

<section class="section section-dark">
  <div class="wrap" style="max-width:900px">
    <div class="prose">
      <h2>1. The Bespoke Fitting Process</h2>
      <h3>How many fittings are required for a bespoke overcoat?</h3>
      <p>A full bespoke overcoat typically requires three fitting stages: the initial anatomical measurement and cloth selection, the skeleton baste fitting where the raw canvas and wool are evaluated on your body, and the forward fitting where sleeves and hem lengths are perfected.</p>

      <h3>What is the typical turnaround time from commission to delivery?</h3>
      <p>Because each garment involves over fifty hours of hand needlework, turnaround averages six to eight weeks. For urgent winter travel requirements, expedited salon scheduling can occasionally be arranged with our head cutter.</p>

      <h2>2. Construction &amp; Canvas Materials</h2>
      <h3>What is the advantage of full floating horsehair canvas?</h3>
      <p>Commercial coats use synthetic glue that stiffens cloth unnaturally and bubbles over time. Our floating horsehair canvas breathes with your movements, rolls softly across the lapels, and gradually molds to your torso's contours, becoming more comfortable with every winter worn.</p>

      <h3>Where do your overcoat fabrics originate?</h3>
      <p>We source heavy woolens, meltons, tweeds, and cashmeres exclusively from historic heritage mills in Yorkshire, the Scottish Borders, and Northern Italy, guaranteeing exceptional density, weather resistance, and natural warmth.</p>

      <h2>3. Consultations &amp; Rescheduling</h2>
      <h3>Is the consultation deposit credited toward the finished coat?</h3>
      <p>Yes, absolutely. The consultation booking deposit is credited 100% toward the total balance of your commissioned bespoke overcoat.</p>

      <h3>How can I reschedule or cancel my fitting appointment?</h3>
      <p>Appointments may be rescheduled or cancelled without fee up to 48 hours prior to your session by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> or telephoning our desk. Inside 48 hours, late rescheduling provisions apply in accordance with our <a href="cancellation-refund-policy.html">Cancellation Policy</a>.</p>
    </div>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

# -----------------------------------------------------------------------------
# POLICY PAGES WITH 60-110 WORDS / PARAGRAPH
# -----------------------------------------------------------------------------

def build_privacy():
    p1 = "This Institutional Privacy Policy details the data stewardship principles, digital security protocols, and client confidentiality frameworks enforced by Overcoat Prism Bespoke Outerwear LLC across our official digital domain. We understand that patrons commissioning bespoke tailored outerwear expect complete discretion regarding their anatomical measurements, salon fitting schedules, and private sartorial preferences. This document transparently explains what minimal data we collect, how it is safeguarded, and your rights under United States privacy legislation."
    p2 = "When you visit our digital platform, request fabric swatches, or reserve a private fitting session at our Chicago Magnificent Mile atelier, we may collect personal identifying records including your full name, telephone number, verified email address, and general outerwear preferences. We never collect sensitive financial account details or biometric telemetry across this web interface. All collected coordinates are used solely to fulfill your fitting reservations and facilitate direct communication with our master tailoring staff."
    p3 = "Our web servers automatically record non-identifying technical telemetry to preserve server security, optimize computational efficiency, and identify navigational bottlenecks across mobile and desktop environments. This telemetry comprises internet protocol addresses, browser user agent strings, referring domain sources, operating system versions, and timestamp logs of viewed outerwear pages. This diagnostic data is aggregated without connecting telemetry records to individual client names or physical residential addresses, ensuring your private browsing remains confidential."
    p4 = "Overcoat Prism deploys minimal, strictly essential session cookies to enable smooth digital navigation, preserve fitting reservation parameters as you advance through our interactive stepper, and verify security tokens during form transmissions. We do not deploy invasive third-party cross-domain behavioral tracking cookies, commercial advertising beacons, or consumer profiling pixels. Any analytical telemetry utilized on our domain is anonymized to assess overall site load performance and resolve technical interface rendering errors across various devices."
    p5 = "We enforce robust administrative, architectural, and cryptographic countermeasures to protect all submitted personal coordinates from unauthorized interception, illicit data harvesting, or accidental disclosure. Digital records are transmitted via modern Transport Layer Security encryption protocols and stored on hardened servers featuring multi-factor authentication and role-restricted access rights. Only credentialed concierge personnel and authorized master tailoring directors possessing verified operational need are permitted access to private fitting consultation records."
    p6 = "Under applicable federal and state data privacy legislation, including the Illinois Personal Information Protection Act and California Consumer Privacy Act, you maintain the legal entitlement to access, inspect, rectify, or request permanent deletion of your stored contact records. If you desire to review your personal records or withdraw communication consent, you may transmit a formal written demand to our administrative concierge. We will review and fulfill verified data subject requests within thirty calendar days without cost."
    p7 = "Overcoat Prism maintains an ethical operational posture that strictly prohibits the monetization, sale, trade, or commercial leasing of client contact details to external marketing agencies, commercial broker networks, or unrelated merchant entities. We disclose client details solely to vetted technical service providers under binding confidentiality obligations, or when formally compelled by lawful governmental subpoenas, valid judicial search warrants, or mandatory statutory requirements under United States federal jurisdiction."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Privacy Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, tailoring excellence, and lasting mutual trust with every patron who engages with our digital portal, reviews our outerwear archives, or reserves fitting experiences at our Chicago Magnificent Mile salon rooms."
    p9 = f"Please direct all formal inquiries regarding this privacy framework to Overcoat Prism Bespoke Outerwear LLC, located at {ADDR}. For immediate verbal consultations regarding digital security safeguards or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "privacy-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Privacy Policy | Overcoat Prism Bespoke Outerwear</title>
<meta name="description" content="Institutional Privacy Policy for Overcoat Prism Bespoke Outerwear LLC. Learn about our strict data stewardship, zero tracking sale policy, and security.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Privacy Policy | Overcoat Prism">
<meta property="og:description" content="Privacy Policy governing client data protection, encryption, and institutional contact coordinates for Overcoat Prism in Chicago.">
<meta property="og:url" content="https://{DOMAIN}/privacy-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("privacy-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Privacy Policy</nav>
    <h1>Institutional Privacy Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Overcoat Prism Bespoke Outerwear LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#scope">1. Scope of Data Stewardship</a></li>
        <li><a href="#collection">2. Information Collection</a></li>
        <li><a href="#telemetry">3. Technical Telemetry</a></li>
        <li><a href="#cookies">4. Minimal Session Cookies</a></li>
        <li><a href="#security">5. Encryption &amp; Security</a></li>
        <li><a href="#rights">6. Client Privacy Rights</a></li>
        <li><a href="#disclosure">7. Non-Monetization Policy</a></li>
        <li><a href="#inquiries">8. Administrative Inquiries</a></li>
        <li><a href="#contact-sec">9. Institutional Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="scope">1. Scope of Data Stewardship</h2>
      <p class="op-policy-p">{p1}</p>
      
      <h2 id="collection">2. Information Collection</h2>
      <p class="op-policy-p">{p2}</p>

      <h2 id="telemetry">3. Technical Telemetry</h2>
      <p class="op-policy-p">{p3}</p>

      <h2 id="cookies">4. Minimal Session Cookies</h2>
      <p class="op-policy-p">{p4}</p>

      <h2 id="security">5. Encryption &amp; Security Protocols</h2>
      <p class="op-policy-p">{p5}</p>

      <h2 id="rights">6. Client Privacy Rights</h2>
      <p class="op-policy-p">{p6}</p>

      <h2 id="disclosure">7. Strict Non-Monetization Policy</h2>
      <p class="op-policy-p">{p7}</p>

      <h2 id="inquiries">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="op-policy-p">{p8}</p>

      <h2 id="contact-sec">9. Institutional Contact Coordinates</h2>
      <p class="op-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_terms():
    p1 = "These Terms and Conditions constitute a legally binding agreement between you and Overcoat Prism Bespoke Outerwear LLC regarding your access to this web portal, your reservation of bespoke fitting appointments, and your commissioning of custom tailored outerwear or cloth restoration services. By browsing our digital archives, submitting bespoke fitting requests, or engaging our tailoring staff, you confirm your unreserved acceptance of these provisions. If you disagree with any term, you must discontinue your use of our domain immediately."
    p2 = "Overcoat Prism designs and hand-constructs bespoke outerwear featuring traditional horsehair canvassing, hand-padded lapels, and heavy British and Italian woolens. Because each coat is individually cut and stitched by hand, slight natural variations in wool grain texture, hand-stitch spacing, and horn button color striations reflect authentic artisanal craftsmanship. Such natural artisan variations do not constitute tailoring defects or breach of contract under any commercial warranties."
    p3 = "Because our atelier prepares custom pattern drafts, reserves dedicated cutting table hours, and prepares cloth swatches specifically for scheduled appointments, private bespoke fitting sessions require a credit card guarantee. Your appointment is not legally confirmed until our concierge reviews your request and issues an authenticated reservation card by email. Patrons must arrive promptly at their scheduled Chicago hour to ensure adequate consultation time with our master cutter."
    p4 = "Patrons seeking to reschedule or cancel a confirmed bespoke fitting must provide written or verbal notice to our concierge at least forty-eight hours prior to the scheduled hour. Because late cancellations prevent our artisans from offering high-demand cutting bench slots to fellow clients on our waiting roster, failure to attend without timely notice may incur late cancellation fees as outlined in our cancellation policy. We appreciate client cooperation in preserving our disciplined tailoring calendar."
    p5 = "All visual photography, typography, pattern diagrams, registered guild trademarks, and tailoring essays published on this web portal remain the exclusive intellectual property of Overcoat Prism Bespoke Outerwear LLC. You are granted a limited, revocable, non-exclusive license to inspect digital materials for personal, non-commercial purposes only. Any unauthorized reproduction, automated data scraping, commercial republishing, or digital distribution of our proprietary imagery is strictly prohibited under international copyright conventions."
    p6 = "Our proprietary canvas layering formulas, steam shaping techniques, and individual paper pattern geometries constitute protected trade secrets of our tailoring guild. Clients acquiring bespoke outerwear receive full legal ownership of the physical completed garment, but acquire no intellectual property rights in our proprietary pattern-cutting methods, custom blocks, or registered guild trademarks. We vigorously defend our craftsmanship rights across domestic and global markets."
    p7 = "Overcoat Prism maintains an atmosphere of quiet sartorial focus, historical appreciation, and mutual respect within our Chicago Magnificent Mile atelier. We require all visitors to conduct themselves with appropriate decorum toward fellow patrons and our tailoring staff. Disruptive conduct, verbal disrespect, uncooperative behavior, or disregard for salon safety protocols may result in immediate refusal of service and revocation of appointment privileges in accordance with atelier standards."
    p8 = "While we welcome personal photography of your completed garment during your final fitting session, the operation of commercial video apparatus, intrusive high-intensity flash rigs, or unauthorized recording equipment that disrupts adjacent fittings is strictly forbidden without prior written authorization from management. We reserve the full managerial authority to decline service to any party whose demeanor undermines the professional environment of our premises. We thank all patrons for preserving our focused salon atmosphere."
    p9 = "These terms and conditions are governed by and construed in strict accordance with the laws of the State of Illinois, United States, without regard to conflict of law principles. Any legal controversy, dispute, or claim arising from these terms or your engagement with Overcoat Prism Bespoke Outerwear shall be submitted to binding arbitration in Chicago, Cook County, Illinois, under standard commercial rules of the American Arbitration Association."
    p10 = f"For formal legal correspondence regarding these terms and conditions, please direct written notices to Overcoat Prism Bespoke Outerwear LLC, {ADDR}. You may also contact our administrative office by telephone at {PHONE} or transmit electronic communications to our designated legal inbox at {EMAIL}. We remain dedicated to resolving all client inquiries with equity, professionalism, and thorough institutional care."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    check_paragraphs(paras, "terms-and-conditions.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Terms &amp; Conditions | Overcoat Prism Bespoke Outerwear</title>
<meta name="description" content="Terms and Conditions governing bespoke fitting appointments, outerwear curation, and web portal access for Overcoat Prism in Chicago, Illinois.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Terms &amp; Conditions | Overcoat Prism">
<meta property="og:description" content="Terms and Conditions for Overcoat Prism Bespoke Outerwear. Fitting rules, trade secrets, and arbitration details.">
<meta property="og:url" content="https://{DOMAIN}/terms-and-conditions.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("terms-and-conditions.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Terms &amp; Conditions</nav>
    <h1>Terms &amp; Conditions</h1>
    <p>Last updated: September 29, 2026 &bull; Overcoat Prism Bespoke Outerwear LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#agreement">1. Agreement to Terms</a></li>
        <li><a href="#craft">2. Handcrafted Outerwear</a></li>
        <li><a href="#reservations">3. Fitting Reservations</a></li>
        <li><a href="#cancellations">4. Cancellation Notice</a></li>
        <li><a href="#ip">5. Intellectual Property</a></li>
        <li><a href="#trade-secrets">6. Trade Secrets</a></li>
        <li><a href="#conduct">7. Guest Salon Conduct</a></li>
        <li><a href="#photography">8. Photography Guidelines</a></li>
        <li><a href="#jurisdiction">9. Governing Law</a></li>
        <li><a href="#legal-notice">10. Legal Notice Address</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="agreement">1. Agreement to Terms</h2>
      <p class="op-policy-p">{p1}</p>

      <h2 id="craft">2. Handcrafted Bespoke Outerwear Standards</h2>
      <p class="op-policy-p">{p2}</p>

      <h2 id="reservations">3. Fitting Reservations &amp; Consultation Protocols</h2>
      <p class="op-policy-p">{p3}</p>

      <h2 id="cancellations">4. Cancellation Notice &amp; Scheduling</h2>
      <p class="op-policy-p">{p4}</p>

      <h2 id="ip">5. Intellectual Property &amp; Copyright</h2>
      <p class="op-policy-p">{p5}</p>

      <h2 id="trade-secrets">6. Trade Secrets &amp; Tailoring Methods</h2>
      <p class="op-policy-p">{p6}</p>

      <h2 id="conduct">7. Guest Salon Conduct &amp; Safety</h2>
      <p class="op-policy-p">{p7}</p>

      <h2 id="photography">8. Photography &amp; Commercial Recording</h2>
      <p class="op-policy-p">{p8}</p>

      <h2 id="jurisdiction">9. Governing Law &amp; Binding Arbitration</h2>
      <p class="op-policy-p">{p9}</p>

      <h2 id="legal-notice">10. Legal Notice Coordinates</h2>
      <p class="op-policy-p">{p10}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_disclaimer():
    p1 = "The tailoring essays, fabric weight analyses, construction diagrams, and outerwear descriptions published on this web portal are presented exclusively for general informational and educational enrichment. While we strive to maintain meticulous historical accuracy and technical precision regarding cloth weaves, horsehair canvassing, and bespoke patterns, we make no express or implied warranties regarding absolute infallibility or universal suitability for every climate requirement. Content is supplied on an as-is basis without merchantability guarantees."
    p2 = "Overcoat Prism expressly disclaims all legal liability for inadvertent typographical errors, computational discrepancies, or unintentional omissions that may occur across our digital archives. Technical specifications regarding cloth weights in grams per linear meter, water repellency ratings, and thermal insulation reflect standard baseline benchmarks and may vary depending on atmospheric humidity, individual body heat, and layering choices. Patrons are encouraged to verify fabric performance directly with our Chicago bench staff."
    p3 = "Bespoke wool and cashmere outerwear garments are artisanal tailored creations constructed from natural organic fibers sensitive to improper storage, moth damage, excessive moisture exposure, and harsh dry cleaning solvents. While our coats feature reinforced seams and water-repellent weaves, owners must exercise proper care, including using wide cedar hangers, natural bristle brushing, and seasonal breathable storage. Nothing published on this website constitutes an unconditional guarantee against damage resulting from improper home care or environmental neglect."
    p4 = "Our digital platform may periodically provide hyperlinked references to external textile research institutes, historical costume museum archives, woolen trade guild standards, or regional transit portals across global networks. These third-party hyperlinks are supplied purely for visitor convenience and do not signify institutional endorsement, sponsorship, or independent verification of external entities. Overcoat Prism Bespoke Outerwear exercises zero operational control over the content, security measures, or data privacy practices of external web domains."
    p5 = "When electing to leave our digital domain via external links, you do so entirely at your own discretion and individual risk. We strongly encourage all users to inspect the terms of service and privacy declarations of any outside web portals they visit. Overcoat Prism Bespoke Outerwear accepts no legal responsibility for financial damages, digital malware, or misleading claims arising from your navigation of third-party digital networks."
    p6 = "To the maximum extent permitted under applicable United States law, Overcoat Prism Bespoke Outerwear LLC, its managing partners, master cutters, and corporate affiliates shall not be held liable for indirect, incidental, punitive, or consequential damages resulting from your use of this web portal or your tailoring engagement. This broad limitation applies regardless of whether alleged damages stem from contract claims, tort actions, server downtimes, or technical interruptions."
    p7 = "In jurisdictions that do not permit the full exclusion or limitation of incidental liability for consumer transactions, our maximum aggregate liability to you for any verified claims shall strictly not exceed the total financial sums paid by you directly to Overcoat Prism during the preceding three calendar months. This limitation represents a fundamental element of the commercial bargain between our atelier and tailoring patrons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Tailoring and Legal Disclaimer, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, tailoring excellence, and lasting mutual trust with every patron who engages with our digital portal, reviews our outerwear archives, or reserves fitting experiences at our Chicago Magnificent Mile salon rooms."
    p9 = f"Please direct all formal inquiries regarding this disclaimer framework to Overcoat Prism Bespoke Outerwear LLC, located at {ADDR}. For immediate verbal consultations regarding tailoring specifications or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "disclaimer.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tailoring &amp; Legal Disclaimer | Overcoat Prism Chicago</title>
<meta name="description" content="Technical, tailoring, and legal disclaimer regarding wool performance, water resistance, garment care, and web content for Overcoat Prism.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Disclaimer | Overcoat Prism">
<meta property="og:description" content="Tailoring Disclaimer for Overcoat Prism Bespoke Outerwear LLC in Chicago, Illinois.">
<meta property="og:url" content="https://{DOMAIN}/disclaimer.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("disclaimer.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Disclaimer</nav>
    <h1>Tailoring &amp; Legal Disclaimer</h1>
    <p>Last updated: September 29, 2026 &bull; Overcoat Prism Bespoke Outerwear LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#educational">1. Educational Purpose</a></li>
        <li><a href="#accuracy">2. Fabric Weight &amp; Benchmarks</a></li>
        <li><a href="#care">3. Wool &amp; Garment Care</a></li>
        <li><a href="#links">4. External Hyperlinks</a></li>
        <li><a href="#nav-risk">5. User Navigation Risk</a></li>
        <li><a href="#liability">6. Limitation of Liability</a></li>
        <li><a href="#cap">7. Liability Ceiling</a></li>
        <li><a href="#disc-inq">8. Administrative Inquiries</a></li>
        <li><a href="#disc-coords">9. Contact Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="educational">1. General Educational Purpose &amp; Accuracy</h2>
      <p class="op-policy-p">{p1}</p>

      <h2 id="accuracy">2. Fabric Weight &amp; Performance Benchmarks</h2>
      <p class="op-policy-p">{p2}</p>

      <h2 id="care">3. Wool Garment Care &amp; Natural Fiber Notices</h2>
      <p class="op-policy-p">{p3}</p>

      <h2 id="links">4. External Hyperlinks &amp; Third-Party Resources</h2>
      <p class="op-policy-p">{p4}</p>

      <h2 id="nav-risk">5. User Navigation Risk Disclosures</h2>
      <p class="op-policy-p">{p5}</p>

      <h2 id="liability">6. Broad Limitation of Operational Liability</h2>
      <p class="op-policy-p">{p6}</p>

      <h2 id="cap">7. Consumer Liability Ceiling</h2>
      <p class="op-policy-p">{p7}</p>

      <h2 id="disc-inq">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="op-policy-p">{p8}</p>

      <h2 id="disc-coords">9. Institutional Contact Coordinates</h2>
      <p class="op-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_cookie():
    p1 = "This Institutional Cookie Policy explains how Overcoat Prism Bespoke Outerwear LLC utilizes minimal session cookie technologies, security tokens, and local cache memory elements across our official digital domain. We believe in total institutional transparency regarding our telemetry practices, ensuring that visiting clients understand precisely what data files are placed on their browsing devices when exploring our outerwear archives and reserving private salon fitting appointments."
    p2 = "A cookie is a small alphanumeric text string placed on your computer, mobile device, or tablet by web page servers when you visit an online portal. Cookies allow digital platforms to recognize your specific browsing device, sustain active session tokens across sequential web pages, and preserve customized user preferences across visits. Cookies deployed by our domain cannot read private data from your local hardware storage."
    p3 = "Our web portal uses essential session cookies that are technically mandatory for the proper execution of basic digital services. These fundamental cookies maintain security verification during form submissions, retain tailoring preference selections within interactive specification tables, and manage navigation states between our primary galleries and secondary policy documents. Because these cookies are essential to web delivery, they operate automatically upon accessing our web pages."
    p4 = "We also utilize strictly anonymized analytical telemetry scripts to understand how clients engage with our outerwear galleries, which technical tailoring articles receive sustained reading attention, and where interface bottlenecks occur. These analytical cookies collect purely aggregated metrics without capturing individual subscriber names, physical residential coordinates, or financial account details. Aggregated telemetry reports assist our developers in optimizing page rendering speeds across mobile devices."
    p5 = "Overcoat Prism Bespoke Outerwear maintains an ethical operational posture that strictly prohibits the deployment of invasive third-party behavioral advertising cookies, commercial tracking pixels, or cross-domain user profiling scripts. We do not sell or monetize our visitor engagement metrics to commercial data brokers, advertising networks, or consumer marketing agencies. All analytical telemetry collected on our domain remains strictly confined to internal atelier speed optimization."
    p6 = "You maintain complete authority to regulate, refuse, block, or delete cookies via your personal browser preferences at any time. Most modern desktop and mobile browsers permit users to review stored cookies, block third-party cookies by default, or clear their cached browsing history automatically upon closing the active application window. Please consult your individual web browser documentation or online help portals for step-by-step instructions on adjusting security and telemetry settings."
    p7 = "Please be aware that disabling essential session cookies or purging browser cache records may noticeably impair the operational performance of specific interactive features on our website, such as reservation booking form transmissions and digital tailoring estimate calculators. To ensure the smoothest and most secure browsing experience across our Chicago outerwear archives, we recommend allowing essential first-party cookies while configuring your personal browser to block extraneous third-party trackers and commercial ad beacons."
    p8 = "Should you have questions, detailed inquiries, clarifications, or feedback concerning the contents of this Institutional Cookie Policy, we welcome your direct communication with our administrative team. We remain deeply committed to fostering open transparency, tailoring excellence, and lasting mutual trust with every patron who engages with our digital portal, reviews our outerwear archives, or reserves fitting experiences at our Chicago Magnificent Mile salon rooms."
    p9 = f"Please direct all formal inquiries regarding this cookie framework to Overcoat Prism Bespoke Outerwear LLC, located at {ADDR}. For immediate verbal consultations regarding telemetry safeguards or salon reservation records, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    check_paragraphs(paras, "cookie-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cookie Policy | Overcoat Prism Bespoke Outerwear</title>
<meta name="description" content="Cookie Policy for Overcoat Prism Bespoke Outerwear LLC. Learn about our minimal session cookies, zero tracking sale policy, and consent options.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Cookie Policy | Overcoat Prism">
<meta property="og:description" content="Institutional Cookie Policy for Overcoat Prism Bespoke Outerwear in Chicago, Illinois.">
<meta property="og:url" content="https://{DOMAIN}/cookie-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("cookie-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Cookie Policy</nav>
    <h1>Institutional Cookie Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Overcoat Prism Bespoke Outerwear LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#tech">1. Cookie Technology</a></li>
        <li><a href="#definition">2. Definition &amp; Function</a></li>
        <li><a href="#essential">3. Essential Session Cookies</a></li>
        <li><a href="#analytics">4. Anonymized Telemetry</a></li>
        <li><a href="#third-party">5. No Third-Party Ads</a></li>
        <li><a href="#control">6. User Browser Controls</a></li>
        <li><a href="#impact">7. Potential Impact of Disabling</a></li>
        <li><a href="#inquiries-cookie">8. Administrative Inquiries</a></li>
        <li><a href="#coords-cookie">9. Institutional Coordinates</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="tech">1. Introduction to Cookie Technologies</h2>
      <p class="op-policy-p">{p1}</p>

      <h2 id="definition">2. Definition &amp; Technical Function</h2>
      <p class="op-policy-p">{p2}</p>

      <h2 id="essential">3. Essential Session Cookies</h2>
      <p class="op-policy-p">{p3}</p>

      <h2 id="analytics">4. Strictly Anonymized Analytical Telemetry</h2>
      <p class="op-policy-p">{p4}</p>

      <h2 id="third-party">5. Ban on Third-Party Commercial Tracking</h2>
      <p class="op-policy-p">{p5}</p>

      <h2 id="control">6. User Browser Regulation &amp; Deletion</h2>
      <p class="op-policy-p">{p6}</p>

      <h2 id="impact">7. Operational Impact of Disabling Cookies</h2>
      <p class="op-policy-p">{p7}</p>

      <h2 id="inquiries-cookie">8. Administrative Inquiries &amp; Transparency</h2>
      <p class="op-policy-p">{p8}</p>

      <h2 id="coords-cookie">9. Institutional Contact Coordinates</h2>
      <p class="op-policy-p">{p9}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_cancellation():
    p1 = "At Overcoat Prism, we recognize that calendar commitments for private collectors and corporate executives may change unexpectedly. That is why every bespoke fitting reservation or tailoring consultation may be altered or cancelled free of charge up to forty-eight hours prior to your scheduled hour. This policy details the procedures governing scheduling changes inside that window, what happens in the event of an unnotified absence, and how guarantee authorizations are managed by our concierge desk."
    p2 = "To request an appointment cancellation or reschedule your fitting date, please contact our concierge by telephoning our direct desk or submitting a formal email with your reservation reference code. The timestamp recorded upon receipt of your communication determines the applicable notice window. For requests submitted within forty-eight hours of your scheduled appointment, we strongly advise calling our desk directly, as phone transmissions are logged and processed in real time by on-duty concierge staff."
    p3 = "When our concierge confirms your private fitting reservation, we secure credit card details exclusively to guarantee the appointment slot and ensure master cutter personnel are allocated. These card parameters are processed through bank-level encrypted payment gateways and are never stored on our web server. A late-cancellation or no-show fee is charged only under the specific conditions outlined in our schedule table, and an itemized electronic receipt is promptly transmitted to your verified email address."
    p4 = "Modifying your appointment date, salon hour, party size, or requested outerwear silhouette focus is entirely complimentary when requested at least forty-eight hours prior to the reserved time, subject to bench availability. The new appointment is confirmed at current calendar availability. Inside forty-eight hours, our staff will make every reasonable effort to accommodate adjustments without disruption, though adjustments that cannot be accommodated and result in missed sessions may be subject to cancellation guidelines."
    p5 = "Where a deposit refund is due following an approved cancellation, our administrative office processes the transaction to the original card within three business days of confirmation. Your card-issuing bank may take an additional five to ten business days to reflect the credit on your statement. Any pre-authorized security hold is released automatically following the conclusion of your visit, and any applicable deductions are documented in writing with comprehensive receipts."
    p6 = "We will waive late cancellation and no-show fees whenever appointment changes stem from verified events beyond your reasonable control, provided you inform our concierge as soon as practically possible. Qualifying situations include severe meteorological emergencies that disrupt travel across Illinois, sudden documented medical emergencies, or significant airline delays when flight numbers were provided to our concierge during booking. We believe in treating our patrons with genuine equity and understanding."
    p7 = "In the rare and improbable circumstance where Overcoat Prism cannot fulfill a confirmed salon appointment—for instance, if a scheduled master cutter is unexpectedly indisposed or a requested heritage cloth bunch is delayed in customs transit—our concierge will contact you immediately, offer the finest available alternative appointments at no additional fee, and if preferred, reschedule your session with full priority or cancel your reservation without any fee or financial penalty whatsoever."
    p8 = f"If any provision within this cancellation policy requires further clarification prior to reserving your fitting session, please contact our concierge team. This policy constitutes an integral component of our broader Terms and Conditions, and formal legal inquiries may be directed to Overcoat Prism Bespoke Outerwear LLC, located at {ADDR}, by telephone at {PHONE}, or via electronic mail at {EMAIL}."

    paras = [p1, p2, p3, p4, p5, p6, p7, p8]
    check_paragraphs(paras, "cancellation-refund-policy.html")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cancellation &amp; Fitting Policy | Overcoat Prism Chicago</title>
<meta name="description" content="Free changes and cancellations up to 48 hours before your bespoke fitting. Review rescheduling terms, waivers, and refund timelines at Overcoat Prism.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://{DOMAIN}/cancellation-refund-policy.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Overcoat Prism">
<meta property="og:title" content="Cancellation &amp; Fitting Policy | Overcoat Prism">
<meta property="og:description" content="Cancellation &amp; Fitting Policy for bespoke outerwear appointments at Overcoat Prism in Chicago.">
<meta property="og:url" content="https://{DOMAIN}/cancellation-refund-policy.html">
<meta property="og:image" content="https://{DOMAIN}/assets/images/overcoatprism_asset_1.jpg">
<meta name="theme-color" content="#0D1117">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{GTAG}
</head>
<body>
{get_header("cancellation-refund-policy.html")}
<main id="main">

<section class="page-hero plain">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Cancellation &amp; Fitting Policy</nav>
    <h1>Cancellation &amp; Fitting Policy</h1>
    <p>Last updated: September 29, 2026 &bull; Overcoat Prism Bespoke Outerwear LLC</p>
  </div>
</section>

<section class="section-tight">
  <div class="wrap prose-wrap">
    <nav class="toc" aria-label="On this page">
      <b>On this page</b>
      <ol>
        <li><a href="#summary">1. Summary &amp; Overview</a></li>
        <li><a href="#table">2. Fee Schedule Table</a></li>
        <li><a href="#how">3. How to Cancel or Change</a></li>
        <li><a href="#guarantee">4. How Fees Are Handled</a></li>
        <li><a href="#amend">5. Amendments &amp; Rescheduling</a></li>
        <li><a href="#refunds">6. Refunds &amp; Security Hold</a></li>
        <li><a href="#exceptions">7. Situations Where Fees Are Waived</a></li>
        <li><a href="#atelier-cancel">8. If We Must Reschedule</a></li>
        <li><a href="#inquiries-canc">9. Questions &amp; Contacts</a></li>
      </ol>
    </nav>
    <article class="prose">
      <h2 id="summary">1. Summary &amp; Overview</h2>
      <p class="op-policy-p">{p1}</p>

      <h2 id="table">2. Fee Schedule Table</h2>
      <table>
        <thead><tr><th>Cancellation Notice Window</th><th>Applicable Fee</th></tr></thead>
        <tbody>
          <tr><td>More than 48 hours before scheduled fitting</td><td>$0 (Complimentary)</td></tr>
          <tr><td>Between 48 and 12 hours before appointment</td><td>50% of consultation deposit</td></tr>
          <tr><td>Less than 12 hours before appointment</td><td>100% of consultation deposit</td></tr>
          <tr><td>No-show without notification</td><td>100% of consultation deposit</td></tr>
        </tbody>
      </table>

      <h2 id="how">3. How to Cancel or Change a Booking</h2>
      <p class="op-policy-p">{p2}</p>

      <h2 id="guarantee">4. How Fees Are Handled</h2>
      <p class="op-policy-p">{p3}</p>

      <h2 id="amend">5. Amendments and Rescheduling</h2>
      <p class="op-policy-p">{p4}</p>

      <h2 id="refunds">6. Refunds and Security Pre-Authorizations</h2>
      <p class="op-policy-p">{p5}</p>

      <h2 id="exceptions">7. Situations Where Fees Are Waived</h2>
      <p class="op-policy-p">{p6}</p>

      <h2 id="atelier-cancel">8. If We Must Reschedule or Cancel</h2>
      <p class="op-policy-p">{p7}</p>

      <h2 id="inquiries-canc">9. Questions and Concierge Contact</h2>
      <p class="op-policy-p">{p8}</p>
    </article>
  </div>
</section>

</main>
{get_footer()}
</body>
</html>"""

def build_sitemap():
    pages = [
        "index.html", "about.html", "products.html", "booking.html", "contact.html", "faq.html",
        "cancellation-refund-policy.html", "privacy-policy.html", "terms-and-conditions.html",
        "disclaimer.html", "cookie-policy.html"
    ]
    xml_items = []
    for p in pages:
        xml_items.append(f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if p == "index.html" else "0.8"}</priority>
  </url>""")
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"".join(xml_items)}
</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /assets/private/

Sitemap: https://{DOMAIN}/sitemap.xml"""

def build_registries():
    meta_file = r"d:\antigravity website\scratch\overcoatprism_image_meta.json"
    with open(meta_file, "r", encoding="utf-8") as f:
        meta = json.load(f)

    # 1. IMAGE_REGISTRY.md
    reg_lines = [
        "# Overcoat Prism Image Registry",
        "",
        "| Asset Filename | Subject & Description | Size | MD5 Hash | Source |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for item in meta:
        reg_lines.append(f"| `{item['filename']}` | {item.get('description', item.get('name', 'Bespoke outerwear'))} | {item['size_bytes']//1024} KB | `{item['md5']}` | {item.get('source_url', 'Pexels.com')} |")
    image_registry_content = "\n".join(reg_lines)

    # 2. DESIGN_REGISTRY.md
    design_registry_content = f"""# Overcoat Prism Design Registry

## Archetype & Visual Identity
- **Archetype**: Modern Sartorial Atelier / Bespoke Outerwear Precision Framework
- **Layout Architecture**: Inspired by Ridevora Clean Geometry, Full Breadcrumb Hierarchy, Dual Hero (Panoramic Photo + Plain Minimalist), Split Editorial Storytelling Rows, High-Contrast Metrics Strip, Multi-Step Interactive Fitting Stepper, and Sticky Table of Contents.
- **Strict Compliance**: Strictly Zero Blog architecture. No blog files, blog links, or blog folders.

## Palette
- **Sartorial Obsidian (Main Background)**: `#0D1117`
- **Darker Obsidian (Sections)**: `#080C11`
- **Surface Elevation**: `#161B22`
- **Surface Card**: `#21262D`
- **Camel Wool Amber (Accent)**: `#D97706`
- **Accent Hover / Glow**: `#F59E0B` / `rgba(217, 119, 6, 0.22)`
- **Clean Light (Values Section)**: `#F8FAFC` & `#FFFFFF`
- **Text Main**: `#F1F5F9`
- **Text Muted**: `#94A3B8`

## Typography
- **Headings & Tailoring Accents**: `'Sora'`, 'Manrope', sans-serif (Weights: 500, 600, 700)
- **Body & Telemetry**: `'Manrope'`, -apple-system, sans-serif (Weights: 400, 500, 600, 700)

## Institutional Coordinates
- **Entity**: Overcoat Prism Bespoke Outerwear LLC
- **Commercial Address**: {ADDR}
- **Telephone**: {PHONE}
- **Inquiries**: {EMAIL}
- **Operating Hours**: {DESK_HOURS}
"""

    # 3. SITE_MANIFEST.json
    manifest = {
        "domain": DOMAIN,
        "category": "jacket",
        "niche": "Bespoke Outerwear & Winter Overcoat Atelier",
        "brand_name": "Overcoat Prism Bespoke Outerwear",
        "entity_name": "Overcoat Prism Bespoke Outerwear LLC",
        "address": ADDR,
        "phone": PHONE,
        "email": EMAIL,
        "operating_hours": DESK_HOURS,
        "gtag_id": "G-0LY0HY7L01",
        "pages": [
            "index.html", "about.html", "products.html", "booking.html", "contact.html", "faq.html",
            "cancellation-refund-policy.html", "privacy-policy.html", "terms-and-conditions.html",
            "disclaimer.html", "cookie-policy.html"
        ],
        "image_count": 20,
        "strict_no_blog": True,
        "architecture": "Ridevora Modern Precision Framework",
        "last_generated": "2026-09-29"
    }
    site_manifest_content = json.dumps(manifest, indent=2)

    return image_registry_content, design_registry_content, site_manifest_content

def generate_all():
    print(f"Generating pages for Overcoat Prism ({DOMAIN})...")
    
    pages = {
        "index.html": build_index(),
        "about.html": build_about(),
        "products.html": build_products(),
        "booking.html": build_booking(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "cancellation-refund-policy.html": build_cancellation(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots()
    }
    
    for filename, content in pages.items():
        fp = os.path.join(SITE_DIR, filename)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename} ({len(content)} bytes)")
    
    img_reg, des_reg, manifest = build_registries()
    with open(os.path.join(SITE_DIR, "IMAGE_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.write(img_reg)
    with open(os.path.join(SITE_DIR, "DESIGN_REGISTRY.md"), "w", encoding="utf-8") as f:
        f.write(des_reg)
    with open(os.path.join(SITE_DIR, "SITE_MANIFEST.json"), "w", encoding="utf-8") as f:
        f.write(manifest)
    print("Generated registries & manifest.")
    print("All files generated successfully.")

if __name__ == "__main__":
    generate_all()
