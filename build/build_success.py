# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema
from components import TESTIMONIALS, testimonial_cards

OUT = os.path.join(os.path.dirname(__file__), "..")

VIDEOS = [
    ("Sneha R.", "7kg in 12 Weeks &mdash; \u201cI finally stopped starting over.\u201d"),
    ("Pooja N.", "9kg in 14 Weeks &mdash; \u201cFor the first time it felt like I understood why.\u201d"),
    ("Anjali M.", "Postpartum Transformation &mdash; \u201cStronger than before my pregnancy.\u201d"),
    ("Deepika S.", "8kg in 14 Weeks &mdash; \u201cThe check-ins kept me honest.\u201d"),
    ("Kavya T.", "First Push-Up At 34 &mdash; \u201cThat moment changed my confidence.\u201d"),
    ("Ritika K.", "Desk-Job Back Pain, Gone &mdash; \u201cI have energy left for my kids now.\u201d"),
]

INTERVIEWS = [
    ("Meenal J.", "Jaipur",
     "What was the hardest part of starting?",
     "Honestly, believing it would be different this time. I'd started and quit so many programs that I almost didn't book the consultation call. I'm glad I did &mdash; eighteen weeks later I'd lost 11 kilos without a single crash diet phase."),
    ("Shreya B.", "Ahmedabad",
     "What changed in how you approached food?",
     "I stopped thinking of meals as 'good' or 'bad.' Pramas built a plan around what I already cook for my family, which meant I wasn't preparing separate meals or feeling deprived at the dinner table."),
    ("Ritika K.", "Hyderabad",
     "How did you fit training into a 10-hour workday?",
     "The sessions are short by design &mdash; 30 minutes, no commute, no gym timing to work around. I do them before my kids wake up. It's the first routine I've actually kept for more than a month."),
]

video_html = "".join([
    '<div class="video-testi reveal"><div class="play-btn">%s</div><div class="video-cap">%s</div></div>' % (icon("play"), cap)
    for name, cap in VIDEOS
])

interview_html = ""
for i, (name, city, q, a) in enumerate(INTERVIEWS):
    bg = "bg-off" if i % 2 else ""
    interview_html += """
<section class="section-sm %s">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <div class="photo-block" style="aspect-ratio:1/1;"><div class="ph-label">Client Interview Photo<br>%s, %s</div></div>
      </div>
      <div class="reveal">
        <div class="eyebrow">Client Interview</div>
        <h3 class="h3" style="margin-bottom:18px;">%s</h3>
        <p style="font-size:1.1rem;color:var(--ink-60);font-family:var(--font-display);font-style:italic;">&ldquo;%s&rdquo;</p>
        <p class="muted" style="margin-top:18px;font-weight:600;">&mdash; %s, %s</p>
      </div>
    </div>
  </div>
</section>""" % (bg, name, city, q, a, name, city)

content = """
<section class="hero" style="padding-bottom:80px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:760px;">
      <div class="eyebrow on-dark">Hear It From Them</div>
      <h1 class="h1">Success Stories, In Their Own Words</h1>
      <p class="lede" style="margin:0 auto;">Video reviews, client interviews, and full transformation stories &mdash; from women who started exactly where you might be right now.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Video Reviews</div>
      <h2 class="h2">Watch Real Transformation Stories</h2>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">In Their Words</div>
      <h2 class="h2">Written Testimonials</h2>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Client Interviews</div>
      <h2 class="h2">Three Women, Three Different Starting Points</h2>
    </div>
  </div>
</section>
%s

<section class="section bg-navy">
  <div class="container">
    <div class="cta-band reveal">
      <h2 class="h2">Ready To Write Your Own Success Story?</h2>
      <p>Every woman above booked a free consultation before anything else changed.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="apply.html" class="btn btn-outline">Apply For Coaching</a>
      </div>
    </div>
  </div>
</section>
""" % (video_html, testimonial_cards(TESTIMONIALS), interview_html, icon("calendar"))

description = ("Watch and read real success stories from Pramas Diwan's clients — video reviews, client interviews "
               "and transformation testimonials from busy Indian women and mothers.")

html = page_shell(
    title="Success Stories | Video Reviews & Client Interviews | Pramas Diwan",
    description=description,
    slug="success-stories.html",
    content_html=content,
    active_key="success",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "success-stories.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built success-stories.html")
