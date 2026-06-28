# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema
from components import WHY_SUCCEED

OUT = os.path.join(os.path.dirname(__file__), "..")

STEPS = [
    ("01", "Submit Your Application", "Tell us about your goals, current fitness level and biggest challenge using the form below."),
    ("02", "Free Consultation Call", "Pramas personally reviews every application and discusses your goals, schedule and the right program fit."),
    ("03", "Start Your Program", "Once you're ready, your personalized training and nutrition plan is built and you begin coaching."),
]

content = """
<section class="hero" style="padding-bottom:80px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:760px;">
      <div class="eyebrow on-dark">Apply For Coaching</div>
      <h1 class="h1">Ready To Start? Tell Us About Yourself.</h1>
      <p class="lede" style="margin:0 auto;">Applications are reviewed personally by Pramas. This isn't a sales form &mdash; it's how we make sure coaching together is genuinely the right fit before anything else happens.</p>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="grid grid-3">
      %s
    </div>
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="two-col" style="align-items:flex-start;">
      <div class="reveal" style="position:sticky;top:110px;">
        <div class="eyebrow">Why Apply</div>
        <h2 class="h3" style="margin-bottom:18px;">What You Get As A Coaching Client</h2>
        <div style="display:flex;flex-direction:column;gap:16px;">
          %s
        </div>
        <div class="pill" style="margin-top:24px;background:var(--green-50);border-color:transparent;color:#15803D;">%s No obligation &mdash; applying doesn't commit you to anything.</div>
      </div>

      <div class="reveal">
        <div class="form-card">
          <form data-lead-form>
            <h3 class="h3" style="margin-bottom:24px;">Coaching Application</h3>
            <div class="form-row">
              <div class="field"><label for="a-name">Full Name</label><input type="text" id="a-name" name="name" required></div>
              <div class="field"><label for="a-age">Age</label><input type="number" id="a-age" name="age" min="16" max="75" required></div>
            </div>
            <div class="form-row">
              <div class="field"><label for="a-weight">Current Weight (kg)</label><input type="number" id="a-weight" name="weight" required></div>
              <div class="field"><label for="a-level">Current Fitness Level</label>
                <select id="a-level" name="fitness_level" required>
                  <option value="">Select one</option>
                  <option>Complete beginner</option>
                  <option>Some experience, inconsistent</option>
                  <option>Regularly active, want structure</option>
                  <option>Returning after a long break</option>
                </select>
              </div>
            </div>
            <div class="field"><label for="a-goal">Primary Goal</label>
              <select id="a-goal" name="primary_goal" required>
                <option value="">Select one</option>
                <option>Lose belly fat</option>
                <option>Lose 6-8kg overall</option>
                <option>Build strength</option>
                <option>Improve energy &amp; mobility</option>
                <option>Postpartum recovery</option>
              </select>
            </div>
            <div class="field"><label for="a-challenge">Biggest Challenge Right Now</label>
              <textarea id="a-challenge" name="biggest_challenge" placeholder="E.g. lack of time, inconsistent eating, low energy, past failed diets..." required></textarea>
            </div>
            <div class="form-row">
              <div class="field"><label for="a-phone">Phone (WhatsApp)</label><input type="tel" id="a-phone" name="phone" required></div>
              <div class="field"><label for="a-email">Email</label><input type="email" id="a-email" name="email" required></div>
            </div>
            <div class="field"><label for="a-why">Why Do You Want Coaching Right Now?</label>
              <textarea id="a-why" name="why_coaching" placeholder="What's driving you to make a change at this point in your life?" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Submit Application %s</button>
            <p class="field-note text-center" style="margin-top:14px;">Applications are typically reviewed within 24&ndash;48 hours.</p>
          </form>
          <div class="form-success">
            %s
            <h3 class="h3" style="margin-bottom:10px;">Application Received!</h3>
            <p class="muted" style="margin-bottom:24px;">Pramas will personally review your application. For a faster response, continue the conversation on WhatsApp now.</p>
            <a href="#" class="btn btn-whatsapp btn-block" data-whatsapp-submit>%s Continue On WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (
    "".join(['<div class="reveal" style="text-align:center;padding:20px;"><div class="tl-dot" style="margin:0 auto 18px;">%s</div><h4 style="margin-bottom:8px;">%s</h4><p class="muted" style="font-size:.92rem;">%s</p></div>' % (n, t, d) for n, t, d in STEPS]),
    "".join(['<div style="display:flex;gap:14px;align-items:flex-start;"><div class="ico" style="background:var(--navy);width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">%s</div><div><h4 style="font-size:.98rem;margin-bottom:4px;">%s</h4><p class="muted" style="font-size:.86rem;">%s</p></div></div>' % (icon(i), t, d) for i, t, d in WHY_SUCCEED[:6]]),
    icon("check"),
    icon("arrow"),
    icon("check"),
    icon("whatsapp"),
)

description = ("Apply for 1:1 transformation coaching with Pramas Diwan. Tell us about your goals, fitness level "
               "and biggest challenge — applications are reviewed personally, no obligation.")

html = page_shell(
    title="Apply For Coaching | Pramas Diwan Transformation Coaching",
    description=description,
    slug="apply.html",
    content_html=content,
    active_key="apply",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "apply.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built apply.html")
