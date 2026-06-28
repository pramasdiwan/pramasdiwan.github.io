# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema
from components import PROGRAMS

OUT = os.path.join(os.path.dirname(__file__), "..")

PHASES = [
    ("Wk 1-3", "Foundation Phase", "Build the training habit, learn correct movement form, and reset your nutrition baseline without drastic changes."),
    ("Wk 4-7", "Strength Building", "Progressive calisthenics overload, increased training capacity, and fat-loss nutrition fully personalized to your results so far."),
    ("Wk 8-11", "Acceleration", "Plateau-breaking adjustments, refined portion and macro targets, and visible changes in strength, energy and body composition."),
    ("Wk 12-13", "Lock-In & Beyond", "Consolidate new habits, plan for life after the program, and set the foundation to maintain results independently."),
]

DETAIL_BLOCKS = {
    "health-mastery": {
        "structure": [
            "Personalized calisthenics &amp; mobility training plan, updated as you progress",
            "Custom nutrition plan built around your food preferences and schedule",
            "Weekly 1:1 video or call check-ins to review progress and adjust the plan",
            "App-based workout and habit tracking, available anytime",
            "Direct WhatsApp access to Pramas for questions and support",
        ],
        "outcomes": [
            "6&ndash;8 kg average fat loss over 12 weeks",
            "Visible reduction in belly fat &amp; waist measurement",
            "Significant gains in strength and mobility",
            "Sustainable habits you keep long after day 91",
        ],
    },
    "calisthenics-moms": {
        "structure": [
            "Bodyweight strength progressions, scaled to your current level",
            "Core and pelvic-floor-safe programming, ideal post-pregnancy",
            "Short, focused sessions designed around nap times &amp; school runs",
            "Video form checks to keep every movement safe and effective",
        ],
        "outcomes": [
            "Build from zero to 8&ndash;10 clean push-ups",
            "Visibly improved posture and core strength",
            "Noticeably reduced joint stiffness and back discomfort",
        ],
    },
    "fat-loss": {
        "structure": [
            "Calorie and macro plan built around your real food preferences",
            "Home workout routine paired directly with your nutrition targets",
            "Weekly measurement &amp; progress photo tracking",
            "Ongoing adjustments as your body and results change",
        ],
        "outcomes": [
            "1&ndash;1.5% body weight lost per week, sustained",
            "Reduced belly fat without muscle loss",
            "A nutrition approach you can maintain past the program",
        ],
    },
    "nutrition": {
        "structure": [
            "Personalized meal plan built around your kitchen and routine",
            "Portion and macro guidance designed to last a lifetime",
            "Strategy for eating out, festivals and family functions",
            "Monthly plan revisions as your goals evolve",
        ],
        "outcomes": [
            "Stable energy levels throughout the day",
            "Fewer cravings and less emotional eating",
            "A realistic, repeatable relationship with food",
        ],
    },
}

def detail_section(p, idx):
    d = DETAIL_BLOCKS[p["id"]]
    structure_html = "".join(['<li>%s%s</li>' % (icon("check"), s) for s in d["structure"]])
    outcomes_html = "".join(['<li>%s%s</li>' % (icon("check"), s) for s in d["outcomes"]])
    reverse = "direction:rtl;" if idx % 2 else ""
    inner_reverse = "direction:ltr;"
    bg = "bg-off" if idx % 2 else ""
    phase_block = ""
    if p["id"] == "health-mastery":
        phase_block = '<div class="timeline" style="margin-top:30px;">%s</div>' % "".join(
            ['<div class="tl-item"><div class="tl-dot" style="font-size:.78rem;">%s</div><h4>%s</h4><p>%s</p></div>' % (w, t, desc) for w, t, desc in PHASES]
        )
    return """
<section class="section %s" id="%s">
  <div class="container">
    <div class="two-col" style="%s">
      <div class="reveal" style="%s">
        <span class="program-tag">%s</span>
        <h2 class="h2" style="margin-bottom:14px;">%s</h2>
        <p class="lede" style="margin-bottom:28px;">%s</p>
        <h4 style="margin-bottom:14px;">Program Structure</h4>
        <ul class="program-list" style="margin-bottom:28px;">%s</ul>
        %s
      </div>
      <div class="reveal" style="%s">
        <div class="program-card featured" style="height:auto;">
          <h4 style="color:#fff;margin-bottom:18px;">Expected Outcomes</h4>
          <ul class="program-list" style="margin-bottom:24px;">%s</ul>
          <p class="program-price">Pricing: <span class="price-cta">shared on your free consultation call</span>, based on your program length &amp; goals.</p>
          <a href="apply.html" class="btn btn-primary btn-block">Apply For This Program %s</a>
          <a href="contact.html" class="btn btn-outline btn-block" style="margin-top:12px;">Ask A Question First</a>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (bg, p["id"], reverse, inner_reverse, p["tag"], p["name"], p["for"], structure_html, phase_block,
       inner_reverse, outcomes_html, icon("arrow"))

sections_html = "".join([detail_section(p, i) for i, p in enumerate(PROGRAMS)])

intro = """
<section class="hero" style="padding-bottom:90px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:760px;">
      <div class="eyebrow on-dark">Coaching Programs</div>
      <h1 class="h1">Find The Program Built For Where You Are Right Now</h1>
      <p class="lede" style="margin:0 auto;">Every program shares the same philosophy &mdash; sustainable, personalized, and built for busy, real lives. Pick the focus that matches your current goal.</p>
    </div>
    <div class="badge-row" style="justify-content:center;margin-top:34px;">
      <a href="#health-mastery" class="pill" style="background:rgba(255,255,255,.08);color:#fff;border-color:rgba(255,255,255,.18);">%s 91 Days Health Mastery</a>
      <a href="#calisthenics-moms" class="pill" style="background:rgba(255,255,255,.08);color:#fff;border-color:rgba(255,255,255,.18);">%s Calisthenics For Moms</a>
      <a href="#fat-loss" class="pill" style="background:rgba(255,255,255,.08);color:#fff;border-color:rgba(255,255,255,.18);">%s Fat Loss Coaching</a>
      <a href="#nutrition" class="pill" style="background:rgba(255,255,255,.08);color:#fff;border-color:rgba(255,255,255,.18);">%s Nutrition Coaching</a>
    </div>
  </div>
</section>
""" % (icon("check"), icon("check"), icon("check"), icon("check"))

outro = """
<section class="section bg-navy">
  <div class="container">
    <div class="cta-band reveal">
      <h2 class="h2">Not Sure Which Program Fits You?</h2>
      <p>Book a free consultation and Pramas will recommend the right starting point based on your goals, schedule and current fitness level.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="apply.html" class="btn btn-outline">Apply For Coaching</a>
      </div>
    </div>
  </div>
</section>
""" % icon("calendar")

content = intro + sections_html + outro

description = ("Explore Pramas Diwan's coaching programs: the 91 Days Health Mastery Program, Calisthenics For Moms, "
               "Fat Loss Coaching and Nutrition Coaching. Personalized, sustainable, built for busy Indian women.")

html = page_shell(
    title="Coaching Programs | 91 Days Health Mastery, Calisthenics & More | Pramas Diwan",
    description=description,
    slug="programs.html",
    content_html=content,
    active_key="programs",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "programs.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built programs.html")
