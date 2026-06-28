# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema

OUT = os.path.join(os.path.dirname(__file__), "..")

CERTS = [
    ("award", "Certified Transformation Coach", "Specialized training in body recomposition coaching for sustainable, long-term results."),
    ("clipboard", "K11 Certified Nutritionist", "Accredited nutrition certification focused on practical, real-world meal planning."),
    ("flame", "Strength & Transformation Coach", "Calisthenics and bodyweight strength progressions for every starting level."),
    ("heart", "Mobility & Nutrition Specialist", "Joint-friendly mobility programming paired with flexible nutrition coaching."),
]

TIMELINE = [
    ("01", "The Starting Point", "Overweight, low on energy, and stuck in a cycle of starting and quitting &mdash; the same place most of my clients start from today."),
    ("02", "Learning What Actually Works", "Years of trial, error and study into training and nutrition science &mdash; discovering that consistency beats intensity, every time."),
    ("03", "The 30 Kg Transformation", "A gradual, sustainable transformation built on habits, not extremes &mdash; one that has lasted, not bounced back."),
    ("04", "Getting Certified", "Formal certification as a Transformation Coach and K11 Nutritionist, turning personal experience into a structured coaching method."),
    ("05", "Coaching My First Clients", "Building custom programs for the first wave of clients &mdash; mostly busy women who'd been let down by generic fitness advice."),
    ("06", "100+ Women Coached", "Six years and 100+ transformations later, the focus remains the same: sustainable change for women who don't have time to waste."),
]

content = """
<section class="hero" style="padding-bottom:90px;">
  <div class="container">
    <div class="hero-grid">
      <div class="reveal in">
        <div class="eyebrow on-dark">About The Coach</div>
        <h1 class="h1">I Know What It Feels Like To Be Stuck In Your Own Body.</h1>
        <p class="lede">I'm Pramas Diwan &mdash; Certified Transformation Coach, K11 Certified Nutritionist, and someone who lost 30 kg the hard, sustainable way. Now I help busy women and mothers do the same.</p>
      </div>
      <div class="reveal in">
        <div class="hero-photo">
          <div class="photo-fallback">%s<span>Professional Photo of Pramas Diwan<br>(replace with real brand photography)</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <div class="eyebrow">My Story</div>
        <h2 class="h2">From 30 Kg Overweight To Coaching 100+ Transformations</h2>
        <p style="margin:22px 0 18px;color:var(--ink-60);">I wasn't a fitness person growing up. For years, I carried extra weight, had no energy by the afternoon, and avoided cameras whenever I could. I tried the diets everyone tries &mdash; cutting carbs completely, skipping meals, punishing workout routines I couldn't sustain past a week.</p>
        <p style="margin-bottom:18px;color:var(--ink-60);">None of it stuck, because none of it was built to last. The turning point wasn't a single dramatic decision &mdash; it was learning to build small, repeatable habits around training and food that I could actually maintain on a hard day, not just a motivated one.</p>
        <p style="margin-bottom:18px;color:var(--ink-60);">Over time, that approach took me from being the overweight one to losing approximately 30 kilograms &mdash; and keeping it off. Today, as a Certified Transformation Coach and K11 Certified Nutritionist, I've spent 6+ years helping over 100 women, most of them busy mothers and working professionals, go through that same shift.</p>
        <p style="color:var(--ink-60);">I built my coaching specifically for women who are overweight, exhausted, short on time, and tired of diets that ask them to give up the food they grew up on. No crash diets. No starvation. No giving up rice and roti. Just sustainable habits, applied consistently, for long enough to change your body and your relationship with it.</p>
      </div>
      <div class="reveal">
        <div class="hero-photo" style="aspect-ratio:4/5;">
          <div class="photo-fallback">%s<span>Before / After Transformation Photo<br>(replace with Pramas' real 30kg transformation photos)</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Certifications</div>
      <h2 class="h2">Credentials Behind The Coaching</h2>
    </div>
    <div class="feature-grid">
      %s
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <div class="eyebrow">The Journey</div>
        <h2 class="h2">How It All Started</h2>
        <p class="lede" style="margin-bottom:0;">Six years, one transformation, and over a hundred more since.</p>
      </div>
      <div class="reveal">
        <div class="timeline">
          %s
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-navy">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow on-dark">Mission &amp; Philosophy</div>
      <h2 class="h2">Coaching Built On What Actually Works</h2>
    </div>
    <div class="grid grid-3">
      <div class="reveal" style="background:rgba(255,255,255,.05);border-radius:var(--radius);padding:34px;">
        <div class="ico" style="background:var(--red);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">%s</div>
        <h4 style="color:#fff;margin-bottom:10px;">No Crash Diets</h4>
        <p style="color:rgba(255,255,255,.65);font-size:.94rem;">Extreme restriction always rebounds. Every plan is built to be sustained, not survived.</p>
      </div>
      <div class="reveal" style="background:rgba(255,255,255,.05);border-radius:var(--radius);padding:34px;">
        <div class="ico" style="background:var(--red);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">%s</div>
        <h4 style="color:#fff;margin-bottom:10px;">Rice &amp; Roti Stay On The Plate</h4>
        <p style="color:rgba(255,255,255,.65);font-size:.94rem;">Fat loss doesn't require giving up the food you grew up eating &mdash; just learning balance and portion.</p>
      </div>
      <div class="reveal" style="background:rgba(255,255,255,.05);border-radius:var(--radius);padding:34px;">
        <div class="ico" style="background:var(--red);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;margin-bottom:18px;">%s</div>
        <h4 style="color:#fff;margin-bottom:10px;">Consistency Over Intensity</h4>
        <p style="color:rgba(255,255,255,.65);font-size:.94rem;">A realistic plan you follow for 12 weeks beats a perfect plan you quit in 12 days.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band reveal" style="background:var(--red-50);">
      <h2 class="h2" style="color:var(--navy);">Ready To Start Your Own Transformation?</h2>
      <p style="color:var(--ink-60);">Let's talk about where you are, where you want to be, and whether coaching together is the right fit.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="apply.html" class="btn btn-outline-dark">Apply For Coaching</a>
      </div>
    </div>
  </div>
</section>
""" % (
    icon("camera"),
    icon("camera"),
    "".join(['<div class="feature-card reveal"><div class="ico">%s</div><h4>%s</h4><p>%s</p></div>' % (icon(i), t, d) for i, t, d in CERTS]),
    "".join(['<div class="tl-item reveal"><div class="tl-dot">%s</div><h4>%s</h4><p>%s</p></div>' % (n, t, d) for n, t, d in TIMELINE]),
    icon("heart"), icon("flame"), icon("trend"),
    icon("arrow"),
)

description = ("Meet Pramas Diwan — Certified Transformation Coach and K11 Certified Nutritionist who lost 30kg "
               "himself and has since coached 100+ women through sustainable fat loss and strength transformations.")

html = page_shell(
    title="About Pramas Diwan | Certified Transformation Coach & Nutritionist",
    description=description,
    slug="about.html",
    content_html=content,
    active_key="about",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "about.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built about.html")
