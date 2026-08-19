# -*- coding: utf-8 -*-
"""Generates the ten static pages for the Cascade Doula proposal.
Output is plain HTML with no runtime build step. Re-run only if the shared
header/footer changes; individual pages are fine to hand-edit after."""
import os, pathlib

ASSET_V = "202608181741"   # bump when css/js change, GitHub Pages caches assets 10 min
ROOT = pathlib.Path.home() / "Documents/code/cascade-doula"

CALENDLY_SC = "https://calendly.com/cascadedoulanl/30min"
CALENDLY_LG = "https://calendly.com/cascadedoulanl/60-minute-consultation-clone"
IG = "https://www.instagram.com/doulanicolelakey/"

NAV = [
    ("Meet Nicole", "about/", False),
    ("Services", "services/", False),
    ("Birth Doula", "services-packages/", False),
    ("Body Ready Method", "body-ready-method/", False),
    ("Testimonials", "testimonials/", False),
    ("Creative Funding", "creative-funding/", True),
    ("Resources", "resources-for-mamas/", True),
    ("Consultation", "consultation/", True),
    ("Contact", "contact/", True),
]

def head(title, desc, p):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Cascade Doula Care</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Karla:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css?v={ASSET_V}">
</head>
<body>
"""

def header(current, p):
    links = []
    for label, href, secondary in NAV:
        cls = ' class="secondary"' if secondary else ""
        cur = ' aria-current="page"' if href == current else ""
        links.append(f'<a{cls} href="{p}{href}"{cur}>{label}</a>')
    links_html = "\n      ".join(links)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}"><img class="brand__mark" src="{p}assets/img/mark-clay.png" alt="" aria-hidden="true"><span>Cascade Doula Care</span></a>
    <button class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <nav class="nav" id="primary-nav">
      {links_html}
      <a class="btn" href="{p}consultation/">Book a free consult</a>
    </nav>
  </div>
</header>
"""

def footer(p):
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>Cascade Doula Care</h4>
        <p>Birth and postpartum support for families in Scotts&nbsp;Valley, Santa&nbsp;Cruz, San&nbsp;Jose and surrounding areas.</p>
        <p><a href="{IG}" rel="noopener">Instagram</a></p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="{p}about/">Meet Nicole</a></li>
          <li><a href="{p}services/">Services</a></li>
          <li><a href="{p}services-packages/">Birth Doula</a></li>
          <li><a href="{p}body-ready-method/">Body Ready Method</a></li>
          <li><a href="{p}testimonials/">Testimonials</a></li>
        </ul>
      </div>
      <div>
        <h4>Get started</h4>
        <ul>
          <li><a href="{p}consultation/">Book a consultation</a></li>
          <li><a href="{p}contact/">Contact</a></li>
          <li><a href="{p}creative-funding/">Creative funding</a></li>
          <li><a href="{p}resources-for-mamas/">Resources for mamas</a></li>
        </ul>
      </div>
      <div>
        <h4>Hours</h4>
        <p>Labor service: available 24/7<br>
        Doula hours: Mon-Fri, 9am-4pm</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; Cascade Doula Care</span>
      <span>Design proposal by Innovative Blockchain Solutions</span>
    </div>
  </div>
</footer>
<div class="sticky-cta">
  <a class="btn btn--ghost" href="{p}contact/">Send a note</a>
  <a class="btn" href="{p}consultation/">Book a consult</a>
</div>
<script src="{p}assets/js/site.js?v={ASSET_V}"></script>
</body>
</html>
"""

def hero(title, lede, img, p, short=False, ctas=True):
    cls = "hero hero--light hero--art hero--short" if short else "hero hero--light"
    btns = ""
    if ctas:
        btns = f"""
      <div class="btn-row">
        <a class="btn" href="{p}consultation/">Book a free consult</a>
        <a class="btn btn--ghost" href="{p}services-packages/">See what is included</a>
      </div>"""
    return f"""<section class="{cls}">
  <div class="hero__media"><img src="{p}assets/img/{img}" alt=""></div>
  <div class="wrap">
    <div class="hero__inner">
      <h1>{title}</h1>
      <p class="lede">{lede}</p>{btns}
    </div>
  </div>
</section>
"""

TRUST = """<div class="trust">
  <div class="wrap">
    <ul>
      <li>Medi-Cal covered</li>
      <li>Central California Alliance for Health</li>
      <li>FSA / HSA eligible</li>
      <li>Private pay &amp; sliding scale</li>
    </ul>
  </div>
</div>
"""

FORM_FIELDS = """      <div class="field-row">
        <div class="field"><label for="fn">First name</label><input id="fn" name="first_name" type="text" autocomplete="given-name"></div>
        <div class="field"><label for="ln">Last name</label><input id="ln" name="last_name" type="text" autocomplete="family-name"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email"></div>
        <div class="field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="due">Estimated due date</label><input id="due" name="due_date" type="date"></div>
        <div class="field"><label for="prov">Who is your provider?</label><input id="prov" name="provider" type="text"></div>
      </div>
      <div class="field"><label for="place">Planned place of delivery</label><input id="place" name="place" type="text" placeholder="Home, birth center, or hospital"></div>
      <div class="field">
        <label for="want">What are you looking for?</label>
        <select id="want" name="looking_for">
          <option>Birth Doula</option>
          <option>One on One Virtual Support</option>
          <option>Childbirth Education Classes</option>
          <option>Doula to Doula (Mentorship)</option>
          <option>Body Ready Method</option>
          <option>Not sure yet</option>
        </select>
      </div>
      <div class="field"><label for="tell">Tell me about yourself</label><textarea id="tell" name="about" placeholder="Whatever you would like me to know. There is no wrong note to send."></textarea></div>
      <button class="btn" type="submit">Send a note</button>
      <p class="form-note">Nicole reads every note herself and will reach out soon.</p>
      <div class="form-status" tabindex="-1">This is a design proposal, so the form is not connected yet. On the real site this would reach Nicole directly.</div>
"""

def form_block(p, heading="Tell me a little about you and your baby"):
    return f"""<section class="section section--sand" id="contact-form">
  <div class="wrap">
    <div class="split split--top">
      <div>
        <p class="eyebrow">Get in touch</p>
        <h2>{heading}</h2>
        <p class="lede">I would love to hear from you. Tell me a little about you and your baby, and I will reach out soon. There is no wrong note to send.</p>
        <p><strong>Labor service:</strong> available 24/7<br><strong>Doula hours:</strong> Monday to Friday, 9am to 4pm</p>
        <div class="btn-row">
          <a class="btn btn--ghost" href="{CALENDLY_SC}" rel="noopener">Santa&nbsp;Cruz consultation</a>
          <a class="btn btn--ghost" href="{CALENDLY_LG}" rel="noopener">Los&nbsp;Gatos consultation</a>
        </div>
        <div class="form-aside">
          <img class="form-aside__photo" src="{p}assets/img/nicole.jpg" alt="Nicole Lakey">
          <div><blockquote>&ldquo;Working with Nicole was the single best decision I made to support my birthing journey.&rdquo;</blockquote>
          <cite>Janae</cite></div>
        </div>
      </div>
      <div class="form-panel">
        <form data-demo-form novalidate>
{FORM_FIELDS}        </form>
      </div>
    </div>
  </div>
</section>
"""

def cta_band(p):
    return f"""<section class="section section--ink">
  <div class="wrap narrow" style="text-align:center">
      <div class="motifs">
        <img src="{p}assets/img/line-1.png" alt="" aria-hidden="true">
        <img src="{p}assets/img/line-2.png" alt="" aria-hidden="true">
        <img src="{p}assets/img/line-3.png" alt="" aria-hidden="true">
      </div>
    <h2>Let's talk before your due date gets close</h2>
    <p class="lede">A free consultation is the easiest first step.<br class="br-wide"> No pressure, just a conversation about the birth you want.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="{p}consultation/">Book a free consult</a>
      <a class="btn btn--ghost" href="{p}contact/">Send a note instead</a>
    </div>
  </div>
</section>
"""

def write(path, body):
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(body, encoding="utf-8")
    print("wrote", path)


QUOTES = [
    ("I knew I wanted to use Nicole as my doula within the first few moments I spoke with her.", "Rose B."),
    ("Nicole was an incredible support during the end of my pregnancy and throughout my 30+ hour labor.", "Cassidy"),
    ("Nicole was absolutely FANTASTIC. Having a doula in general was a great decision, but having Nicole as my doula was even better.", "Monica"),
    ("Nicole was such an invaluable part of our birth; I actually do not know how women give birth without her.", "Caty"),
    ("Nicole's support was invaluable during labor and delivery, and especially postpartum.", "Selah"),
    ("Nicole was extremely influential on the outcome of my birth experience!", "Elizabeth"),
    ("Nicole was everything I hoped for in a doula - compassionate, empathetic, and deeply supportive.", "Cascade Doula client"),
    ("We were first recommended Nicole by our midwife, and choosing her was easily the best decision we made.", "Anna Paula Rocha da Rosa"),
    ("Nicole was my doula for the birth of my first child. She made me so comfortable and confident.", "Linda"),
    ("I feel that we have Nicole to thank for holding our hands and hearts through some of the most trying hours.", "Jessie B."),
    ("Working with Nicole was the single best decision I made to support my birthing journey.", "Janae"),
    ("Having Nicole as my birth doula was one of the best decisions I made for my labor and delivery.", "Siyi"),
    ("I am incredibly grateful for Nicole's support throughout my birth journey.", "Roopal"),
    ("As a first-time mom who was induced early due to third-trimester complications, I was bracing myself.", "Victoria"),
    ("She stepped in when I needed her in my most vulnerable state.", "Diana R."),
    ("Nicole was exactly what my spouse and I needed as we prepared for the arrival of our baby.", "LeAnna"),
    ("She will always put her mama's first by answering your calls, checking in by texts.", "Melanie K."),
    ("As with most births, we were dealing with an unexpected hiccup in our birth plan.", "Lauren"),
    ("We were incredibly fortunate to have had such an amazing doula by our side.", "Elwyn &amp; Nick Meehan"),
    ("I am so grateful for her support, calming presence and constant coaching.", "Sheila E."),
    ("She helped guide our birth wish list and it felt good knowing we had our own advocate.", "Melina L."),
    ("Nicole was with me by my side and she knew with confidence exactly where I was in the progression.", "Briana K."),
    ("She gently whispered calm directions in my ear when all seemed so chaotic.", "Genevieve"),
    ("I wholeheartedly believe my pre/post pregnancy and labor and delivery went so well because of Nicole!", "Stephanie"),
    ("Working with Nicole during my pregnancy and birth was a wonderful experience.", "Maddy"),
    ("Nicole is a phenomenal doula! I am beyond grateful for the services and support she provided.", "Jess"),
    ("There will never be enough words to explain how powerful and necessary Nicole's support was.", "Caitlin"),
    ("I am so glad I made the decision to include Nicole in my pregnancy and birth experience.", "Hallie"),
    ("We are so grateful to have had Nicole as our doula.", "Mary &amp; Parker"),
]

def quote_html(q, who):
    return f'<figure class="quote"><p>&ldquo;{q}&rdquo;</p><cite>{who}</cite></figure>'

PACKAGE_ITEMS = [
    "Two 2-hour prenatal visits to assess your needs and desires for birth, provide useful tools for labor and birth so you feel empowered and supported, and establish your postpartum plan",
    "Help with any concerns, plus information about holistic and natural remedies for minor pregnancy discomforts",
    "Continuous physical, emotional, and informational support for you and your partner for the duration of labor and birth",
    "Initial breastfeeding support immediately after birth to help your baby latch on properly",
    "Two postpartum follow-up visits, plus references to lactation consultants, meal delivery, placenta encapsulation, massage, chiropractic and acupuncture",
    "Unlimited phone and chat support throughout pregnancy and early labor",
    "Additional support such as extra visits or birth photography, available for doula clients",
]

# ---------------------------------------------------------------- home
p = ""
home = head("Birth &amp; Postpartum Doula in Santa&nbsp;Cruz", "Birth and postpartum doula support for families in Scotts&nbsp;Valley, Santa&nbsp;Cruz and San&nbsp;Jose.", p)
home += header("", p)
home += hero(
    "Unbiased, unwavering support for the birth you&nbsp;want",
    "Birth and postpartum care for mothers and families in Scotts&nbsp;Valley, Santa&nbsp;Cruz, San&nbsp;Jose and surrounding areas.",
    "photo-boardwalk.jpg", p)
home += TRUST
home += f"""<section class="section section--ink">
  <div class="wrap">
    <div class="ornament__line">
      <p class="band-lead">Every birth is different. The support should be too.</p>
    </div>
    <div class="grid grid--3">
      <div class="card card--feature card--num"><span class="card__num">01</span><h3>Connect</h3><p>Giving birth is one of the most important moments in your life. Surround yourself with people who make you feel safe, strong, and supported.</p></div>
      <div class="card card--feature card--num"><span class="card__num">02</span><h3>Empower</h3><p>We'll discuss your wishes and work together to build a personalized birth blueprint, so you can greet this transformative event with confidence.</p></div>
      <div class="card card--feature card--num"><span class="card__num">03</span><h3>Prepare</h3><p>As your doula, I am here to provide education and resources so you are prepared to advocate for the birth you want, and to support you through whatever your birth brings.</p></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="split split--fill">
      <div class="split__media"><img src="{p}assets/img/nicole.jpg" alt="Nicole Lakey, birth doula"></div>
      <div>
        <p class="eyebrow">Meet Nicole</p>
        <h2>Fifteen years in medicine, then a calling</h2>
        <p>After a 15-year career in the medical field, Nicole followed her true passion for supporting families through the transformative process of childbirth. As a birth doula and a certified Body Ready Method&reg; Pro, she helps you feel strong, confident, and prepared in your own body.</p>
        <p>Her easygoing, confident personality, paired with a good sense of humor, puts everyone at ease. She works seamlessly alongside hospital staff, birth center teams, and home birth providers, and sees her role as a collaborative one.</p>
        <div class="btn-row"><a class="btn btn--onlight-dark" href="{p}about/">Read Nicole's story</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--fill">
      <div>
        <p class="eyebrow">The birth doula package</p>
        <h2>What is included</h2>
        <p class="lede">Services are tailored to your specific needs. A basic package includes:</p>
        <ul class="checklist">
          {"".join(f"<li>{i}</li>" for i in PACKAGE_ITEMS[:5])}
        </ul>
        <div class="btn-row"><a class="btn" href="{p}services-packages/">See the full package</a></div>
      </div>
      <div class="split__media"><img src="{p}assets/img/photo-boardwalk.jpg" alt=""></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <p class="eyebrow">In their words</p>
    <h2 style="margin-bottom:1em">Families Nicole has supported</h2>
    <div class="grid grid--3">
      {quote_html(*QUOTES[0])}
      {quote_html(*QUOTES[3])}
      {quote_html(*QUOTES[10])}
    </div>
    <div class="btn-row"><a class="btn btn--onlight-dark" href="{p}testimonials/">Read all testimonials</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--fill">
      <div class="split__media"><img src="{p}assets/img/photo-coast.jpg" alt=""></div>
      <div>
        <p class="eyebrow">Body Ready Method&reg;</p>
        <h2>Prepare your body, not just your birth plan</h2>
        <p>An evidence-based approach that optimizes movement, alignment, and body balance to support a more functional pregnancy, efficient birth, and smoother recovery.</p>
        <div class="btn-row"><a class="btn btn--onlight-dark" href="{p}body-ready-method/">Explore Body Ready Method</a></div>
      </div>
    </div>
  </div>
</section>
"""
home += form_block(p)
home += cta_band(p)
home += footer(p)
write("index.html", home)

p = "../"

# ---------------------------------------------------------------- about
b = head("Meet Nicole", "Nicole Lakey, birth doula and certified Body Ready Method Pro serving Santa&nbsp;Cruz county.", p)
b += header("about/", p)
b += hero("Meet Nicole", "Birth doula, certified Body Ready Method&reg; Pro, and a steady hand through the most important hours of your life.", "photo-couple.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap">
    <div class="split split--top">
      <div class="split__media"><img src="{p}assets/img/nicole.jpg" alt="Nicole Lakey"></div>
      <div>
        <p>After a 15-year career in the medical field, Nicole has followed her true passion for supporting families during the transformative process of childbirth. As a birth doula and a certified Body Ready Method&reg; Pro, she has discovered her true calling: helping you feel strong, confident, and prepared in your own body.</p>
        <p>Nicole's work is driven by a deep belief that every person deserves to feel supported, informed, and empowered as they navigate pregnancy, birth, and the postpartum period. She brings a unique, hands-on approach to her care, bridging the gap between emotional encouragement and physical preparation. Through her certification in the Body Ready Method&reg;, she helps families work with their bodies to create space for baby to engage and descend, leading to more comfortable pregnancies and efficient labors. She is also an expert in the use of the birth sling, providing loving, hands-on physical support throughout the intensity of labor.</p>
        <p>Whether preparing your body for birth or focusing on healing and recovery postpartum, Nicole's goal is simple: to remind you how powerful you are. She provides education and unbiased information to help families speak up and make the best decisions for themselves. Her easygoing, confident, and approachable personality, paired with a good sense of humor, helps put everyone at ease. Nicole works seamlessly alongside hospital staff, birth center teams, and home birth providers, viewing her role as a collaborative team member dedicated to creating a calm and supportive environment.</p>
        <p>When she is not supporting families, Nicole is at home with her husband and their three children, living out her belief that with the right support, you truly can thrive.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap narrow">
    <p class="eyebrow">The short version</p>
    <h2>Why work with a doula?</h2>
    <p>A doula is a trained professional who provides support for the birthing mother and her birth partner during pregnancy, labor and delivery. A doula is a wonderful option both for first time parents and for those who want to refresh their knowledge or enhance their skills for achieving their desired birth experience.</p>
    <p>They can also assist with clarifying your birth preferences and explaining the options available to you. Your doula can help guide you and your partner through all stages of labor, regardless of whether you choose to give birth at home, at a birth center, or in a hospital, and provide support to help you feel safe, cope with early labor, manage pain during active labor, and stay with you until you meet your baby.</p>
    <p>Doulas often hear, &ldquo;I looked over at you and you gave me a look that let me know that everything was okay.&rdquo; We keep an eye on the big picture and anticipate your next need. Always ready, always prepared.</p>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("about/index.html", b)

# ---------------------------------------------------------------- services
b = head("Services", "One-on-one support for expecting families, plus insurance billing guidance for birth workers.", p)
b += header("services/", p)
b += hero("One-on-one support for expecting families", "Empowered, informed, and supported every step of the way.", "photo-garden.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap narrow">
    <p class="lede">Pregnancy is more than just preparing for birth. It is a journey filled with choices, emotions, and deep transformation. I offer personalized one-on-one sessions for birthing families who want to feel confident, grounded, and informed as they prepare to welcome their baby.</p>
  </div>
  <div class="wrap" style="margin-top:48px">
    <div class="grid grid--2">
      <div class="card"><h3>Childbirth education</h3><p>Learn what to expect during labor and birth, understand your options, and gain tools for comfort, advocacy, and informed decision-making.</p></div>
      <div class="card"><h3>Setting birth intentions</h3><p>Clarify your hopes, preferences, and values around birth. Together we'll explore what matters most to you so you can feel empowered in any birthing environment.</p></div>
      <div class="card"><h3>Emotional &amp; mental preparation</h3><p>Create space to release fears, build confidence, and prepare mentally and emotionally for the transition into parenthood.</p></div>
      <div class="card"><h3>Partner involvement</h3><p>Support your partner or support person in feeling prepared, connected, and ready to be an active part of the experience.</p></div>
    </div>
    <div class="wrap narrow" style="padding:0;margin-top:40px">
      <p>Each session is tailored to meet your unique needs, questions, and vision for birth. Whether you're birthing at home, in a hospital, or a birth center, this is your space to learn, plan, and connect. Let's create a calm, empowered start to your birth journey.</p>
      <div class="btn-row" style="justify-content:center"><a class="btn" href="{p}consultation/">Book a free consult</a></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="split split--fill">
      <div>
        <p class="eyebrow">Support for birth workers</p>
        <h2>One-on-one insurance billing guidance</h2>
        <p>Are you a birth worker looking to expand your practice by offering services that are reimbursable through insurance, but don't know where to start? I offer personalized one-on-one support to help doulas and other perinatal professionals navigate the process of setting up and submitting insurance claims with confidence.</p>
        <p>Whether you're brand new to billing or looking to refine your current system, I'll guide you through:</p>
        <ul class="checklist">
          <li>Understanding what services can be billed</li>
          <li>Gathering and organizing the required documentation</li>
          <li>Setting up systems to streamline your billing process</li>
          <li>Navigating superbills, CPT codes, and ICD-10 codes</li>
          <li>Communicating effectively with clients and insurers</li>
        </ul>
        <p>This is not just about billing. It is about building a sustainable, professional practice that honors your time and expertise.</p>
      </div>
      <div class="split__media"><img src="{p}assets/img/photo-boardwalk.jpg" alt=""></div>
    </div>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("services/index.html", b)

# ---------------------------------------------------------------- birth doula package
b = head("Birth Doula", "The birth doula package: prenatal visits, continuous labor support, and postpartum follow-up.", p)
b += header("services-packages/", p)
b += hero("The birth doula package", "Tailored to your specific needs. Here is what a basic package includes.", "photo-coast.jpg", p, short=True, ctas=False)
b += TRUST
b += f"""<section class="section">
  <div class="wrap">
    <div class="split split--fill">
      <div>
        <ul class="checklist">
          {"".join(f"<li>{i}</li>" for i in PACKAGE_ITEMS)}
        </ul>
        <p style="margin-top:26px"><strong>Nicole is contracted with Central California Alliance for Health and Medi-Cal, and offers private pay and sliding scale.</strong></p>
        <div class="btn-row"><a class="btn" href="{p}consultation/">Book a free consult</a><a class="btn btn--ghost" href="{p}creative-funding/">Ways to pay</a></div>
      </div>
      <div class="split__media"><img src="{p}assets/img/photo-garden.jpg" alt=""></div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h2 style="margin-bottom:1em">Three stages, one steady presence</h2>
    <div class="grid grid--3">
      <div class="card card--feature card--num"><span class="card__num">01</span><h3>Before</h3><p>An initial prenatal appointment covering labor ideas, pain management, and building your birth plan. A second prenatal covers early labor planning, what to pack, and comfort techniques. In person or virtually.</p></div>
      <div class="card card--feature card--num"><span class="card__num">02</span><h3>During</h3><p>Position ideas, reminders of your plans and goals, and making sure you feel safe and respected. Your partner is supported too, including when to eat, drink, and rest.</p></div>
      <div class="card card--feature card--num"><span class="card__num">03</span><h3>After</h3><p>Postpartum support focused on the Golden Hour, skin-to-skin contact, and breastfeeding guidance, plus two follow-up visits.</p></div>
    </div>
  </div>
</section>
"""
b += form_block(p, "Ready to talk it through?")
b += footer(p)
write("services-packages/index.html", b)

# ---------------------------------------------------------------- testimonials
b = head("Testimonials", "What families say about working with Nicole.", p)
b += header("testimonials/", p)
b += hero("Families Nicole has supported", "Twenty-nine notes from mothers, partners, and families across Santa&nbsp;Cruz county.", "photo-couple.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap">
    <div class="quote-cols">
      {"".join(quote_html(q, w) for q, w in QUOTES)}
    </div>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("testimonials/index.html", b)

# ---------------------------------------------------------------- consultation
b = head("Consultation", "Book a free consultation with Nicole in Santa&nbsp;Cruz or Los&nbsp;Gatos.", p)
b += header("consultation/", p)
b += hero("Book a free consultation", "The easiest first step. Pick the location that works for you and grab a time.", "photo-boardwalk.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap">
    <div class="grid grid--2">
      <div class="card">
        <p class="eyebrow">30 minutes</p>
        <h3>Santa&nbsp;Cruz consultation</h3>
        <p>A short conversation about where you are, what you are hoping for, and whether we are a good fit.</p>
        <div class="btn-row"><a class="btn" href="{CALENDLY_SC}" rel="noopener">Book now &middot; Santa&nbsp;Cruz</a></div>
      </div>
      <div class="card">
        <p class="eyebrow">60 minutes</p>
        <h3>Los&nbsp;Gatos consultation</h3>
        <p>A longer sit-down for families who want to go deeper on birth preferences and planning.</p>
        <div class="btn-row"><a class="btn" href="{CALENDLY_LG}" rel="noopener">Book now &middot; Los&nbsp;Gatos</a></div>
      </div>
    </div>
    <div class="wrap narrow" style="padding:0;margin-top:44px;text-align:center">
      <p>Prefer to write first? <a href="{p}contact/">Send a note</a> and Nicole will reach out.</p>
      <p><strong>Labor service:</strong> available 24/7 &nbsp;&middot;&nbsp; <strong>Doula hours:</strong> Monday to Friday, 9am to 4pm</p>
    </div>
  </div>
</section>
"""
b += footer(p)
write("consultation/index.html", b)

# ---------------------------------------------------------------- contact
b = head("Contact", "Send Nicole a note about you and your baby.", p)
b += header("contact/", p)
b += hero("Hi, I am Nicole", "I would love to hear from you. There is no wrong note to send.", "photo-garden.jpg", p, short=True, ctas=False)
b += form_block(p, "Tell me a little about you and your baby")
b += footer(p)
write("contact/index.html", b)

# ---------------------------------------------------------------- creative funding
b = head("Creative Funding", "FSA/HSA, insurance, employer benefits, registries, and Medi-Cal coverage for doula care.", p)
b += header("creative-funding/", p)
b += hero("Every family deserves a doula", "I believe every family deserves the support of a doula, and want to make that as accessible as possible.", "photo-couple.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap">
    <p class="eyebrow">Payment options &amp; insurance coverage</p>
    <h2 style="margin-bottom:1em">Creative ways to fund doula care</h2>
    <div class="grid grid--3">
      <div class="card"><h3>FSA / HSA accounts</h3><p>Doula care often qualifies. I will provide a superbill or invoice for insurance reimbursement.</p></div>
      <div class="card"><h3>Insurance coverage</h3><p>I currently accept Kaiser and Medi-Cal, and more companies are joining every month.</p></div>
      <div class="card"><h3>Employer benefits</h3><p>Some employers offer programs like Carrot that cover doula services.</p></div>
      <div class="card"><h3>Baby registry</h3><p>Add doula support to your registry with platforms like Be Her Village or Little Honey Money.</p></div>
      <div class="card"><h3>Give back</h3><p>You can create a donation fund to help local mamas in need access the care they deserve.</p></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap narrow">
    <p class="eyebrow">Covered options</p>
    <h2>Medi-Cal</h2>
    <p>My doula services are covered through Medi-Cal. This package includes:</p>
    <ul class="checklist">
      <li>Up to 8 prenatal and/or postpartum visits, in person or virtual, mixed as needed</li>
      <li>Birth support, in person or virtual, if desired</li>
      <li>Medi-Cal clients may also qualify for up to 9 additional postpartum visits with a provider's referral</li>
    </ul>
    <div class="btn-row"><a class="btn" href="{p}contact/">Ask about your coverage</a></div>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("creative-funding/index.html", b)

# ---------------------------------------------------------------- body ready method
b = head("Body Ready Method", "Evidence-based movement and alignment work for pregnancy, birth, and recovery.", p)
b += header("body-ready-method/", p)
b += hero("Body Ready Method&reg;", "Helping you move through pregnancy, birth, and postpartum with strength and ease.", "photo-boardwalk.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap narrow">
    <p class="eyebrow">What it is</p>
    <h2>What is Body Ready Method&reg;?</h2>
    <p class="lede">BRM&reg; is an evidence-based approach that optimizes movement, alignment, and body balance to support a more functional pregnancy, efficient birth, and smoother recovery.</p>
    <p>The method uses five pillars to train the body for pregnancy, birth, and recovery.</p>
  </div>
  <div class="wrap" style="margin-top:40px">
    <div class="grid grid--3">
      <div class="card card--feature card--num"><span class="card__num">01</span><h3>Upper Body Mobility</h3></div>
      <div class="card card--feature card--num card--pillar"><span class="card__num">02</span><h3>Core</h3></div>
      <div class="card card--feature card--num card--pillar"><span class="card__num">03</span><h3>Pelvis</h3></div>
      <div class="card card--feature card--num card--pillar"><span class="card__num">04</span><h3>Pelvic Floor</h3></div>
      <div class="card card--feature card--num card--pillar"><span class="card__num">05</span><h3>Movement Patterns</h3></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="split split--fill">
      <div>
        <p class="eyebrow">Is this for you?</p>
        <h2>Who should work with me</h2>
        <ul class="checklist">
          <li>You are pregnant and preparing for birth</li>
          <li>You have experienced difficult births previously</li>
          <li>You worry about core strength, diastasis recti, or pelvic floor concerns</li>
          <li>You prioritize function over fitness</li>
        </ul>
        <h3 style="margin-top:34px">Why work with a BRM&reg; Pro?</h3>
        <p>Body Ready Method&reg; Professionals understand how to support the pregnant body to find resilience, strength, and mobility. We are experts in pelvic mechanics and understand what to do during every stage of the birthing process.</p>
        <div class="btn-row"><a class="btn" href="{CALENDLY_SC}" rel="noopener">Schedule a discovery call</a></div>
      </div>
      <div class="split__media"><img src="{p}assets/img/photo-garden.jpg" alt=""></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <p class="eyebrow">1:1 assessment &amp; follow-up</p>
    <h2>Sessions and pricing</h2>
    <p>Sessions are tailored to individual needs, offered in office or virtually.</p>
    <ul class="prices">
      <li><span><span class="price-name">Initial assessment</span><br><span class="price-meta">90 minutes</span></span><span class="price-amt">$175</span></li>
      <li><span><span class="price-name">Follow-up session</span><br><span class="price-meta">60 minutes</span></span><span class="price-amt">$125</span></li>
      <li><span><span class="price-name">Comprehensive package</span><br><span class="price-meta">1 initial + 2 follow-ups</span></span><span class="price-amt">$395</span></li>
      <li><span><span class="price-name">End of pregnancy intensive</span><br><span class="price-meta">90 minutes</span></span><span class="price-amt">$225</span></li>
      <li><span><span class="price-name">Postpartum session</span><br><span class="price-meta">60 to 90 minutes</span></span><span class="price-amt">$125</span></li>
    </ul>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("body-ready-method/index.html", b)

# ---------------------------------------------------------------- resources
b = head("Resources for Mamas", "Resources Nicole has collected for the families she works with.", p)
b += header("resources-for-mamas/", p)
b += hero("For my mamas", "Some resources I have collected for you.", "photo-garden.jpg", p, short=True, ctas=False)
b += f"""<section class="section">
  <div class="wrap">
    <div class="grid grid--3">
      <div class="card">
        <p class="eyebrow">Postpartum meal service</p>
        <h3>Milky Oat</h3>
        <p>Nourishing meals delivered for the postpartum weeks, so feeding yourself is one less thing to think about.</p>
        <div class="btn-row"><a class="btn btn--onlight-dark" href="https://milkyoat.com/?sca_ref=11078496.4bVqEYbNnwoih8Wh" rel="noopener">Visit Milky Oat</a></div>
      </div>
    </div>
    <div class="wrap narrow" style="padding:0;margin-top:44px">
      <p class="form-note">More resources coming. If there is something you are looking for and cannot find, <a href="{p}contact/">ask me</a> and I will point you in the right direction.</p>
    </div>
  </div>
</section>
"""
b += cta_band(p) + footer(p)
write("resources-for-mamas/index.html", b)
print("DONE")
