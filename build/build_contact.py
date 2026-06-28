# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, org_schema, PHONE_DISPLAY, PHONE_TEL, EMAIL, INSTAGRAM_HANDLE, INSTAGRAM_URL, LOCATION
from components import faq_list, CONTACT_FAQS

OUT = os.path.join(os.path.dirname(__file__), "..")

TEMPLATE = """
<section class="hero" style="padding-bottom:80px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:700px;">
      <div class="eyebrow on-dark">Get In Touch</div>
      <h1 class="h1">Let's Talk About Your Goals</h1>
      <p class="lede" style="margin:0 auto;">Questions, consultation bookings, or just want to know if coaching is right for you &mdash; reach out below.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col" style="align-items:flex-start;">
      <div class="reveal">
        <div class="eyebrow">Send A Message</div>
        <h2 class="h3" style="margin-bottom:24px;">Book Your Free Consultation</h2>
        <div class="form-card" style="padding:34px;box-shadow:none;border:1px solid var(--line);">
          <form data-lead-form>
            <div class="field"><label for="c-name">Full Name</label><input type="text" id="c-name" name="name" required></div>
            <div class="form-row">
              <div class="field"><label for="c-email">Email</label><input type="email" id="c-email" name="email" required></div>
              <div class="field"><label for="c-phone">Phone (WhatsApp)</label><input type="tel" id="c-phone" name="phone" required></div>
            </div>
            <div class="field"><label for="c-goal">What's your main goal?</label>
              <select id="c-goal" name="goal">
                <option value="">Select one</option>
                <option>Lose belly fat</option>
                <option>Lose 6-8kg overall</option>
                <option>Build strength</option>
                <option>Improve energy &amp; health</option>
                <option>Postpartum recovery</option>
                <option>Not sure yet</option>
              </select>
            </div>
            <div class="field"><label for="c-message">Message</label><textarea id="c-message" name="message" placeholder="Tell us a little about where you are right now..."></textarea></div>
            <button type="submit" class="btn btn-primary btn-block">Send Message {arrow_icon}</button>
          </form>
          <div class="form-success">
            {check_icon}
            <h3 class="h3" style="margin-bottom:10px;">Message Sent!</h3>
            <p class="muted" style="margin-bottom:24px;">We've received your details. For the fastest reply, continue on WhatsApp.</p>
            <a href="#" class="btn btn-whatsapp btn-block" data-whatsapp-submit>{wa_icon} Continue On WhatsApp</a>
          </div>
        </div>
      </div>

      <div class="reveal">
        <div class="eyebrow">Other Ways To Reach Us</div>
        <h2 class="h3" style="margin-bottom:24px;">Contact Details</h2>
        <div style="display:flex;flex-direction:column;gap:18px;">
          <a href="#" data-whatsapp="Hi Pramas, I'd like to book a free consultation." class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:#25D366;width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{wa_icon2}</div>
            <div><h4>WhatsApp</h4><p class="muted" style="font-size:.9rem;">Fastest response, usually within hours</p></div>
          </a>
          <a href="tel:{phone_tel}" class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:var(--navy);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{phone_icon}</div>
            <div><h4>Phone</h4><p class="muted" style="font-size:.9rem;">{phone_display}</p></div>
          </a>
          <a href="mailto:{email}" class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:var(--navy);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{mail_icon}</div>
            <div><h4>Email</h4><p class="muted" style="font-size:.9rem;">{email}</p></div>
          </a>
          <a href="{insta_url}" target="_blank" rel="noopener" class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:var(--red);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{insta_icon}</div>
            <div><h4>Instagram</h4><p class="muted" style="font-size:.9rem;">{insta_handle}</p></div>
          </a>
          <div class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:var(--navy);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{pin_icon}</div>
            <div><h4>Location</h4><p class="muted" style="font-size:.9rem;">{location}</p></div>
          </div>
          <div class="program-card" style="flex-direction:row;align-items:center;gap:18px;padding:24px;">
            <div class="ico" style="background:var(--navy);width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;">{clock_icon}</div>
            <div><h4>Business Hours</h4><p class="muted" style="font-size:.9rem;">Mon&ndash;Sat, 7:00 AM &ndash; 8:00 PM IST &middot; Sun: WhatsApp only</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Quick Questions</div>
      <h2 class="h2">Before You Reach Out</h2>
    </div>
    <div class="container-narrow" style="padding:0;">{faqs}</div>
  </div>
</section>
"""

content = TEMPLATE.format(
    arrow_icon=icon("arrow"),
    check_icon=icon("check"),
    wa_icon=icon("whatsapp"),
    wa_icon2=icon("whatsapp"),
    phone_tel=PHONE_TEL,
    phone_icon=icon("phone"),
    phone_display=PHONE_DISPLAY,
    mail_icon=icon("mail"),
    email=EMAIL,
    insta_url=INSTAGRAM_URL,
    insta_icon=icon("insta"),
    insta_handle=INSTAGRAM_HANDLE,
    pin_icon=icon("pin"),
    location=LOCATION,
    clock_icon=icon("clock"),
    faqs=faq_list(CONTACT_FAQS),
)

description = ("Get in touch with Pramas Diwan for online transformation coaching. WhatsApp, phone, email, "
               "Instagram and a free consultation booking form.")

html = page_shell(
    title="Contact Pramas Diwan | Book A Free Consultation",
    description=description,
    slug="contact.html",
    content_html=content,
    active_key="contact",
    schema_json=org_schema(),
)

with open(os.path.join(OUT, "contact.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Built contact.html")
