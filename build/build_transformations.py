# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema
from components import TRANSFORMATIONS, transformation_cards, ba_slider, stats_band

OUT = os.path.join(os.path.dirname(__file__), "..")

CASE_STUDIES = [
    {
        "name": "Sneha R.", "role": "Working Mother of Two, Pune", "dur": "12 Weeks", "kg": "7 kg", "waist": "4.5 in",
        "before": "Sneha came to coaching after trying four different diets in two years, each one ending in regained weight. She had 30&ndash;40 minutes a day, no gym access, and a deep distrust of fitness advice after repeated disappointment.",
        "program": "91 Days Health Mastery Program &mdash; home calisthenics 5x/week paired with a flexible, rice-and-roti-inclusive meal plan, with weekly check-ins to adjust around her work travel.",
        "result": "Lost 7 kg and 4.5 inches off her waist in 12 weeks, while reporting more energy at work than she'd had in years. She's continued independently for 6 months past the program with no regain.",
    },
    {
        "name": "Anjali M.", "role": "New Mother, Bengaluru", "dur": "16 Weeks", "kg": "6.5 kg", "waist": "5 in",
        "before": "Eight months postpartum, Anjali couldn't recognize her body in photos and had been told generic gym programs weren't realistic with a newborn at home.",
        "program": "Calisthenics For Moms, with pelvic-floor-safe core work and sessions built around her baby's nap schedule, plus a postpartum-appropriate nutrition plan.",
        "result": "Rebuilt full-body strength from scratch, lost 6.5 kg, and reported feeling stronger than before her pregnancy &mdash; with energy to spare for her baby in the evenings.",
    },
    {
        "name": "Meenal J.", "role": "Homemaker, Jaipur", "dur": "18 Weeks", "kg": "11 kg", "waist": "7 in",
        "before": "Meenal had struggled with weight for over a decade and felt fitness content online was never built for someone starting from her level.",
        "program": "An extended 91 Days Health Mastery cycle with a slow, joint-friendly progression and a heavily personalized nutrition plan around her family's home cooking.",
        "result": "Lost 11 kg and 7 inches off her waist over 18 weeks &mdash; the largest sustained transformation in this case study set, achieved without a single crash diet phase.",
    },
]

gallery_html = transformation_cards(TRANSFORMATIONS, with_slider=False)

case_html = ""
for i, c in enumerate(CASE_STUDIES):
    bg = "bg-off" if i % 2 else ""
    case_html += """
<section class="section %s">
  <div class="container">
    <div class="two-col">
      <div class="reveal">%s</div>
      <div class="reveal">
        <div class="eyebrow">Case Study</div>
        <h2 class="h3" style="margin-bottom:6px;">%s</h2>
        <p class="muted" style="margin-bottom:24px;">%s &middot; %s Program</p>
        <div class="grid grid-3" style="margin-bottom:28px;">
          <div class="pill" style="justify-content:center;">-%s Lost</div>
          <div class="pill" style="justify-content:center;">-%s Waist</div>
          <div class="pill" style="justify-content:center;">%s</div>
        </div>
        <h4 style="margin-bottom:8px;">Where She Started</h4>
        <p class="muted" style="margin-bottom:18px;">%s</p>
        <h4 style="margin-bottom:8px;">The Program</h4>
        <p class="muted" style="margin-bottom:18px;">%s</p>
        <h4 style="margin-bottom:8px;">The Result</h4>
        <p class="muted">%s</p>
      </div>
    </div>
  </div>
</section>""" % (bg, ba_slider(c["name"]), c["name"], c["role"], c["dur"], c["kg"], c["waist"], c["dur"],
                  c["before"], c["program"], c["result"])

content = """
<section class="hero" style="padding-bottom:80px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:760px;">
      <div class="eyebrow on-dark">Real Clients, Real Results</div>
      <h1 class="h1">Client Transformations</h1>
      <p class="lede" style="margin:0 auto;">Drag any slider below to compare before and after. Every transformation here was built with consistent home training and flexible, sustainable nutrition.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="reveal">%s</div>
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">The Gallery</div>
      <h2 class="h2">More Transformations</h2>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>

<div class="divider container" style="margin:0 auto;"></div>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">In Depth</div>
      <h2 class="h2">Detailed Case Studies</h2>
      <p class="lede">A closer look at three transformations &mdash; where they started, what the program looked like, and what changed.</p>
    </div>
  </div>
</section>
%s

<section class="section bg-navy">
  <div class="container">
    <div class="cta-band reveal">
      <h2 class="h2">Your Transformation Could Be Next</h2>
      <p>Every story above started with a single consultation call. Yours can too.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="success-stories.html" class="btn btn-outline">Watch Success Stories</a>
      </div>
    </div>
  </div>
</section>
""" % (
    ba_slider("Sneha R."),
    gallery_html,
    case_html,
    icon("calendar"),
)

description = ("Browse real client transformations from Pramas Diwan's coaching &mdash; before/after sliders, weight "
               "loss results, and detailed case studies from busy Indian women and mothers.")

html = page_shell(
    title="Client Transformations & Before/After Results | Pramas Diwan",
    description=description,
    slug="transformations.html",
    content_html=content,
    active_key="transformations",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "transformations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built transformations.html")
