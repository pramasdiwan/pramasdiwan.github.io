# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, photo_block, org_schema, PHONE_DISPLAY
from components import (pain_grid, stats_band, programs_grid, transformation_cards,
                         why_succeed_grid, testimonial_cards, faq_list, HOME_FAQS, ba_slider)

OUT = os.path.join(os.path.dirname(__file__), "..")

content = """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy reveal in">
        <div class="eyebrow on-dark">Online Transformation Coaching For Women</div>
        <h1 class="h1">Helping Busy Moms Lose Stubborn Fat &amp; Build Strength <em class="serif">From Home</em></h1>
        <p class="lede">Personalized coaching, calisthenics training, mobility work, and sustainable nutrition guidance &mdash; built for women who have work, family, and zero time to waste on plans that don't fit real life.</p>
        <div class="hero-ctas">
          <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
          <a href="#" class="btn btn-outline" data-whatsapp="Hi Pramas, I'd like to know more about your coaching programs.">%s Chat On WhatsApp</a>
        </div>
        <div class="hero-trust">
          <div class="stat"><b>100+</b><span>Women Coached</span></div>
          <div class="stat"><b>6+ yrs</b><span>Coaching Experience</span></div>
          <div class="stat"><b>30 kg</b><span>Pramas' Own Transformation</span></div>
        </div>
      </div>
      <div class="hero-media reveal in">
        <div class="hero-photo">
          <div class="photo-fallback">
            %s
            <span>Photo of Pramas Diwan<br>(replace with professional brand photography)</span>
          </div>
        </div>
        <div class="hero-badge">
          <span class="num">100+</span>
          <span>Women transformed using sustainable, home-based coaching</span>
        </div>
        <div class="hero-badge top">
          <span class="num">-30kg</span>
          <span>Pramas' personal transformation</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Sound Familiar?</div>
      <h2 class="h2">Do Any Of These Sound Familiar?</h2>
      <p class="lede">You're not lazy, and you're not out of options. You've just never had a plan built for your actual life.</p>
    </div>
    %s
  </div>
</section>

<section class="section bg-navy">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <div class="hero-photo" style="aspect-ratio:4/5;">
          <div class="photo-fallback">
            %s
            <span>Before / After Transformation Photo<br>(replace with Pramas' real transformation photos)</span>
          </div>
        </div>
      </div>
      <div class="reveal">
        <div class="eyebrow on-dark">The Coach's Own Story</div>
        <h2 class="h2">I Lost 30 Kg. Now I Help Others Do The Same.</h2>
        <p class="lede" style="margin-bottom:24px;">I wasn't always the person handing out fitness advice. A few years ago, I was the overweight one &mdash; low energy, uncomfortable in my own skin, and tired of starting over every Monday.</p>
        <p style="color:rgba(248,250,252,.78);margin-bottom:18px;">What changed wasn't a miracle diet or a 5am bootcamp. It was learning to build habits I could actually keep &mdash; training I looked forward to, food I didn't dread, and consistency over intensity. Over time, that added up to a 30 kg transformation that has lasted, not bounced back.</p>
        <p style="color:rgba(248,250,252,.78);margin-bottom:32px;">Today, as a Certified Transformation Coach and K11 Certified Nutritionist, I help busy women and mothers go through that same shift &mdash; without crash diets, without giving up rice and roti, and without unrealistic expectations.</p>
        <a href="about.html" class="btn btn-outline">Read My Full Story %s</a>
      </div>
    </div>
  </div>
</section>

<section class="section-sm bg-off">
  <div class="container">
    <div class="reveal">%s</div>
  </div>
</section>
<style>.bg-off .stats-band{background:var(--navy);}</style>

<section class="section" id="programs">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Signature Programs</div>
      <h2 class="h2">Coaching Built Around Your Goal</h2>
      <p class="lede">Four programs, one philosophy: sustainable, personalized, and built for real life.</p>
    </div>
    %s
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Real Results</div>
      <h2 class="h2">Client Transformations</h2>
      <p class="lede">Drag the slider to see a real transformation. Every result below was built with consistent training and flexible nutrition &mdash; not shortcuts.</p>
    </div>
    <div class="grid grid-3" style="margin-bottom:36px;">
      <div class="reveal">%s<div style="text-align:center;margin-top:14px;"><strong>Sneha R.</strong><div class="muted" style="font-size:.88rem;">-7 kg in 12 weeks</div></div></div>
      <div class="reveal">%s<div style="text-align:center;margin-top:14px;"><strong>Deepika S.</strong><div class="muted" style="font-size:.88rem;">-8 kg in 14 weeks</div></div></div>
      <div class="reveal">%s<div style="text-align:center;margin-top:14px;"><strong>Meenal J.</strong><div class="muted" style="font-size:.88rem;">-11 kg in 18 weeks</div></div></div>
    </div>
    <div class="text-center reveal"><a href="transformations.html" class="btn btn-dark">See All Transformations %s</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Why Clients Succeed</div>
      <h2 class="h2">A System Designed To Actually Work</h2>
      <p class="lede">Most plans fail from a lack of structure and support, not a lack of willpower. Here's what's different.</p>
    </div>
    %s
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Testimonials</div>
      <h2 class="h2">What Clients Say After Working Together</h2>
    </div>
    <div class="grid grid-3">%s</div>
    <div class="grid grid-3" style="margin-top:40px;">
      <div class="video-testi reveal"><div class="play-btn">%s</div><div class="video-cap">Sneha's Story &mdash; 7kg in 12 Weeks (Video)</div></div>
      <div class="video-testi reveal"><div class="play-btn">%s</div><div class="video-cap">Pooja's Story &mdash; 9kg in 14 Weeks (Video)</div></div>
      <div class="video-testi reveal"><div class="play-btn">%s</div><div class="video-cap">Anjali's Story &mdash; Postpartum Transformation (Video)</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Common Questions</div>
      <h2 class="h2">Frequently Asked Questions</h2>
    </div>
    <div class="container-narrow" style="padding:0;">
      %s
    </div>
  </div>
</section>

<section class="section bg-navy" id="roadmap">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <div class="eyebrow on-dark">Free Resource</div>
        <h2 class="h2">Get Your Free Body Transformation Roadmap</h2>
        <p class="lede" style="margin-bottom:0;">Answer a few quick questions and get a personalized starting point &mdash; what to focus on first, what's realistic for your timeline, and how Pramas' coaching could help you get there.</p>
      </div>
      <div class="form-card reveal">
        <form data-lead-form>
          <div class="form-row">
            <div class="field"><label for="lg-name">Full Name</label><input type="text" id="lg-name" name="name" required></div>
            <div class="field"><label for="lg-age">Age</label><input type="number" id="lg-age" name="age" min="16" max="75" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="lg-weight">Current Weight (kg)</label><input type="number" id="lg-weight" name="weight" required></div>
            <div class="field"><label for="lg-goal">Primary Goal</label>
              <select id="lg-goal" name="goal" required>
                <option value="">Select one</option>
                <option>Lose belly fat</option>
                <option>Lose 6-8kg overall</option>
                <option>Build strength</option>
                <option>Improve energy &amp; health</option>
                <option>Postpartum recovery</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="field"><label for="lg-email">Email</label><input type="email" id="lg-email" name="email" required></div>
            <div class="field"><label for="lg-phone">Phone (WhatsApp)</label><input type="tel" id="lg-phone" name="phone" required></div>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Send Me My Free Roadmap %s</button>
          <p class="field-note text-center" style="margin-top:14px;">No spam. Just a personalized plan and an optional follow-up from our team.</p>
        </form>
        <div class="form-success">
          %s
          <h3 class="h3" style="margin-bottom:10px;">Got it!</h3>
          <p class="muted" style="margin-bottom:24px;">We've noted your details. For the fastest response, continue the conversation on WhatsApp.</p>
          <a href="#" class="btn btn-whatsapp btn-block" data-whatsapp-submit>%s Continue On WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <h2 class="h2">Your Transformation Starts With One Conversation</h2>
      <p>No pressure, no obligation. Just a real conversation about where you are and where you want to be.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="apply.html" class="btn btn-outline">Apply For Coaching</a>
      </div>
    </div>
  </div>
</section>
""" % (
    icon("arrow"), icon("whatsapp"), icon("award"),
    pain_grid(),
    icon("camera"), icon("arrow"),
    stats_band([
        ("100", "+", "Women Coached", "100"),
        ("6", "+", "Years Of Coaching Experience", "6"),
        ("30", " kg", "Pramas' Personal Transformation", "30"),
        ("91", "-day", "Flagship Program Length", "91"),
    ]),
    programs_grid(),
    ba_slider("Sneha"), ba_slider("Deepika"), ba_slider("Meenal"), icon("arrow"),
    why_succeed_grid(),
    testimonial_cards(),
    icon("play"), icon("play"), icon("play"),
    faq_list(HOME_FAQS),
    icon("arrow"),
    icon("check"),
    icon("whatsapp"),
    icon("calendar"),
)

description = ("Pramas Diwan is a Certified Transformation Coach helping busy Indian women and mothers lose stubborn "
               "fat, build strength and regain confidence through home-based calisthenics, mobility and sustainable "
               "nutrition coaching. Book a free consultation today.")

schema = """{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Pramas Diwan | Online Transformation Coach For Women",
  "description": "%s"
}""" % description

html = page_shell(
    title="Pramas Diwan | Online Transformation Coach For Busy Women &amp; Moms",
    description=description,
    slug="index.html",
    content_html=content,
    active_key="home",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built index.html")
