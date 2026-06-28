# -*- coding: utf-8 -*-
"""Reusable HTML component generators + shared content data."""
from common import icon

# ---------------------------------------------------------------- FAQ ------
def faq_list(items, list_id="faqList"):
    rows = []
    for q, a in items:
        rows.append("""
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>%s</span>
          <span class="plus">%s</span>
        </button>
        <div class="faq-a"><div class="faq-a-inner"><p>%s</p></div></div>
      </div>""" % (q, icon("plus"), a))
    return '<div class="faq-list" id="%s">%s</div>' % (list_id, "".join(rows))


# --------------------------------------------------------- TESTIMONIALS ----
TESTIMONIALS = [
    ("Sneha R.", "Lost 7 kg in 12 weeks · Working Mother, Pune",
     "I'd tried four different diets before this and always gained the weight back within a month. What was different with Pramas was that he never once asked me to give up rice. Twelve weeks in, my jeans from my college days fit again, and I'm not white-knuckling my way through it &mdash; I actually enjoy my meals."),
    ("Anjali M.", "Lost 6.5 kg · New mom, Bengaluru",
     "Eight months after my delivery I still couldn't recognize my own body in photos. I had maybe 20 minutes a day and no gym access. Pramas built a home programme around my baby's nap schedule. I'm stronger now than I was before I got pregnant."),
    ("Deepika S.", "Lost 8 kg · Homemaker, Delhi",
     "The weekly check-ins kept me honest in a way no app ever could. Even on weeks I slipped, Pramas adjusted the plan instead of making me feel guilty. That's the only reason I made it past week 4 this time, when I'd quit everything else by week 2."),
    ("Ritika K.", "Reduced belly fat, up 4kg lean strength · IT Professional, Hyderabad",
     "I work 10-hour days at a desk and was convinced I simply didn't have the energy for fitness. The mobility and calisthenics sessions take 30 minutes and I do them in my living room. My back pain is gone and I have energy left for my kids in the evening."),
    ("Pooja N.", "Lost 9 kg in 14 weeks · Teacher, Mumbai",
     "What stood out was how Pramas explained the 'why' behind everything &mdash; why crash diets don't work, why I kept regaining weight, why my old approach was setting me up to fail. For the first time fat loss felt like something I understood, not something I was suffering through."),
    ("Kavya T.", "Lost 5 kg, gained visible muscle tone · Marketing Manager, Chennai",
     "I came in wanting to lose weight and left caring more about getting strong. Being able to do a full push-up at 34, after never managing one in my life, did more for my confidence than the number on the scale."),
]

def testimonial_cards(items=None):
    items = items or TESTIMONIALS
    cards = []
    for name, role, quote in items:
        initials = "".join([p[0] for p in name.split() if p])[:2].upper()
        stars = icon("star") * 5
        cards.append("""
        <div class="testi-card reveal">
          <div class="testi-stars">%s</div>
          <p class="testi-quote">&ldquo;%s&rdquo;</p>
          <div class="testi-person">
            <div class="testi-avatar">%s</div>
            <div><div class="name">%s</div><div class="role">%s</div></div>
          </div>
        </div>""" % (stars, quote, initials, name, role))
    return "".join(cards)


# --------------------------------------------------------- TRANSFORMATIONS -
TRANSFORMATIONS = [
    ("Sneha R.", "12 weeks", "7 kg", "-4.5 in waist", "Working mother of two, Pune"),
    ("Anjali M.", "16 weeks", "6.5 kg", "-5 in waist", "New mom, Bengaluru"),
    ("Deepika S.", "14 weeks", "8 kg", "-6 in waist", "Homemaker, Delhi"),
    ("Pooja N.", "14 weeks", "9 kg", "-5.5 in waist", "Teacher, Mumbai"),
    ("Ritika K.", "12 weeks", "4 kg", "-3.5 in waist", "IT professional, Hyderabad"),
    ("Kavya T.", "10 weeks", "5 kg", "-4 in waist", "Marketing manager, Chennai"),
    ("Meenal J.", "18 weeks", "11 kg", "-7 in waist", "Homemaker, Jaipur"),
    ("Shreya B.", "12 weeks", "6 kg", "-4 in waist", "Working mother, Ahmedabad"),
]

def transformation_cards(items=None, with_slider=False):
    items = items or TRANSFORMATIONS
    cards = []
    for name, dur, kg, inch, role in items:
        media = ba_slider(name) if with_slider else photo_block_inline()
        cards.append("""
        <div class="tf-card reveal">
          %s
          <div class="tf-card-body">
            <h4>%s</h4>
            <div class="tf-meta">%s &middot; %s</div>
            <div class="tf-result-row">
              <div><div class="val">-%s</div><div class="lbl">Weight Lost</div></div>
              <div><div class="val">%s</div><div class="lbl">Waist Change</div></div>
              <div><div class="val">%s</div><div class="lbl">Duration</div></div>
            </div>
          </div>
        </div>""" % (media, name, role, dur, kg, inch, dur))
    return "".join(cards)

def photo_block_inline():
    return '<div class="photo-block" style="aspect-ratio:4/5;"><div class="ph-label">Transformation Photo<br>Before &amp; After</div></div>'

def ba_slider(name="Client"):
    return ('<div class="ba-slider">'
            '<div class="ba-after"><div class="ba-fallback">After Photo<br>%s</div></div>'
            '<div class="ba-tag after">After</div>'
            '<div class="ba-before"><div class="ba-inner"><div class="ba-fallback">Before Photo<br>%s</div></div></div>'
            '<div class="ba-tag before">Before</div>'
            '<div class="ba-handle"><div class="grip">%s</div></div>'
            '</div>') % (name, name, icon("drag"))


# --------------------------------------------------------------- STATS -----
def stats_band(items):
    cells = []
    for num, suffix, label, counter_val in items:
        cells.append("""
        <div class="stat-cell">
          <div class="num"><span data-counter="%s" data-suffix="%s">0%s</span></div>
          <div class="lbl">%s</div>
        </div>""" % (counter_val, suffix, suffix, label))
    return '<div class="stats-band">%s</div>' % "".join(cells)


# --------------------------------------------------------------- PAIN ------
PAIN_POINTS = [
    ("frown", "My clothes don't fit the way they used to, and it's affecting my confidence."),
    ("battery", "I'm exhausted by 4pm, every single day, with nothing left for myself."),
    ("clock", "Between work and family, I genuinely don't have time to get to a gym."),
    ("scale", "I've tried five different diets. Something always brings the weight back."),
    ("heart", "I avoid being in photos with my own kids because of how I look in them."),
    ("frown", "I don't know what to eat anymore &mdash; every plan contradicts the last one."),
    ("flame", "My joints ache and my body feels stiff in a way it never used to."),
    ("target", "I start strong every time, then lose all consistency within two weeks."),
]

def pain_grid(items=None):
    items = items or PAIN_POINTS
    cards = []
    for ico, text in items:
        cards.append("""
        <div class="pain-card reveal"><div class="ico">%s</div><p>%s</p></div>""" % (icon(ico), text))
    return '<div class="pain-grid">%s</div>' % "".join(cards)


# ------------------------------------------------------------ PROGRAMS -----
PROGRAMS = [
    {
        "id": "health-mastery",
        "tag": "Flagship Program",
        "name": "91 Days Health Mastery Program",
        "for": "Women who want a complete, done-for-you system covering training, nutrition and mindset.",
        "points": [
            "Personalized calisthenics &amp; strength training plan",
            "Flexible, sustainable nutrition coaching &mdash; rice and roti included",
            "Weekly 1:1 check-ins and plan adjustments",
            "Mobility &amp; recovery work built in",
            "App-based workout and habit tracking",
            "Direct WhatsApp access to Pramas for support",
        ],
        "outcome": "Most clients lose 6&ndash;8 kg, rebuild strength from zero, and walk away with habits that hold past day 91.",
        "featured": True,
    },
    {
        "id": "calisthenics-moms",
        "tag": "Strength Training",
        "name": "Calisthenics For Moms",
        "for": "Mothers who want to build real strength at home, with zero gym equipment or gym timings.",
        "points": [
            "Bodyweight strength progressions for every level",
            "Designed around nap times &amp; school-run schedules",
            "Posture, core and pelvic-floor-safe programming",
            "Video-guided form correction",
            "Progress tracked week over week",
        ],
        "outcome": "Clients typically go from 0 push-ups to 8&ndash;10 clean reps, with visibly improved posture and core strength, in 8&ndash;10 weeks.",
        "featured": False,
    },
    {
        "id": "fat-loss",
        "tag": "Fat Loss",
        "name": "Fat Loss Coaching",
        "for": "Women whose main goal is to lose stubborn belly fat without crash dieting or starving themselves.",
        "points": [
            "Custom calorie &amp; macro plan built around your food preferences",
            "No food groups eliminated, no extreme restriction",
            "Home workout routine paired with your nutrition plan",
            "Weekly progress photos &amp; measurement tracking",
            "Plateau-busting adjustments as your body changes",
        ],
        "outcome": "Average results of 1&ndash;1.5% body weight lost per week, sustained, not the rapid water-weight loss that comes right back.",
        "featured": False,
    },
    {
        "id": "nutrition",
        "tag": "Nutrition",
        "name": "Nutrition Coaching",
        "for": "Women who are confused about what to eat and want a plan that actually fits Indian home food.",
        "points": [
            "Meal plans built around your kitchen, not a generic template",
            "Macro &amp; portion guidance you can use for life",
            "Eating out, festivals &amp; family functions accounted for",
            "Emotional eating &amp; cravings support",
            "Monthly plan revisions as your goals evolve",
        ],
        "outcome": "Clients report stable energy, fewer cravings, and a sustainable relationship with food within 4&ndash;6 weeks.",
        "featured": False,
    },
]

def program_card(p, link_prefix=""):
    cls = "program-card featured" if p.get("featured") else "program-card"
    points_html = "".join(['<li>%s%s</li>' % (icon("check"), pt) for pt in p["points"]])
    return """
        <div class="%s reveal" id="%s">
          <span class="program-tag">%s</span>
          <h3 class="h3">%s</h3>
          <p class="program-for">%s</p>
          <ul class="program-list">%s</ul>
          <p class="program-price"><span class="price-cta">Pricing shared on your free consultation call</span> &mdash; tailored to your program length &amp; goals.</p>
          <a href="%sapply.html" class="btn %s btn-block">Apply For This Program %s</a>
        </div>""" % (cls, p["id"], p["tag"], p["name"], p["for"], points_html,
                      link_prefix, "btn-outline" if p.get("featured") else "btn-dark", icon("arrow"))

def programs_grid(items=None, link_prefix=""):
    items = items or PROGRAMS
    return '<div class="grid grid-2" style="align-items:stretch;">%s</div>' % "".join([program_card(p, link_prefix) for p in items])


# ----------------------------------------------------------- WHY-SUCCEED ---
WHY_SUCCEED = [
    ("clipboard", "Custom Plans", "Every plan is built around your body, your schedule and your food &mdash; never a copy-paste template."),
    ("calendar", "Weekly Check-Ins", "You're never left guessing. Weekly reviews mean your plan adjusts as your body changes."),
    ("users", "Personal Accountability", "Direct access to Pramas keeps you consistent on the weeks motivation alone won't cut it."),
    ("heart", "Flexible Nutrition", "Rice, roti and your favourite foods stay on the plate. No food is off-limits forever."),
    ("home", "Home Workouts", "No gym membership, no commute, no equipment required to get started."),
    ("smartphone", "App-Based Tracking", "Your workouts, meals and progress, organized in one place you can check anytime."),
    ("shield", "24x7 Support", "Questions don't wait for office hours. Neither does your coach."),
    ("trend", "Built To Last", "The goal isn't 12 weeks of willpower. It's a body and habits you keep for good."),
]

def why_succeed_grid(items=None):
    items = items or WHY_SUCCEED
    cards = []
    for ico, title, desc in items:
        cards.append("""
        <div class="feature-card reveal"><div class="ico">%s</div><h4>%s</h4><p>%s</p></div>""" % (icon(ico), title, desc))
    return '<div class="feature-grid">%s</div>' % "".join(cards)


# -------------------------------------------------------------- FAQS -------
HOME_FAQS = [
    ("Do I need a gym membership or equipment for this?", "No. Every program is built around bodyweight calisthenics and home-friendly movements. Some clients add light dumbbells later by choice, but it's never required to get results."),
    ("Will I have to stop eating rice and roti?", "No. Pramas' entire nutrition philosophy is built around Indian staples, not against them. You'll learn portion sizes and balance, not elimination."),
    ("I've failed at diets before. Why would this be different?", "Most diets fail because they're too restrictive to sustain. This program is built around what you'll actually keep doing &mdash; with weekly adjustments based on your real life, not a rigid template."),
    ("How much time do I need each day?", "Most clients train 30&ndash;45 minutes, 4&ndash;5 times a week. Sessions are designed to fit around nap times, work hours and family schedules."),
    ("I'm a complete beginner. Is this still for me?", "Yes &mdash; most clients start at beginner level. Every movement has a regression, so you progress at a pace that's safe and sustainable for your starting point."),
    ("How is coaching delivered? Is it really online?", "Everything is delivered online &mdash; your training plan, nutrition guidance, check-ins and support &mdash; through an app and WhatsApp, so you can train from home anywhere in India."),
    ("How much weight can I realistically expect to lose?", "Most clients lose 6&ndash;8 kg over 12 weeks with consistent effort. Results depend on your starting point, adherence and goals, which we'll map out on your consultation call."),
    ("I had a baby recently. Is this safe for postpartum bodies?", "Yes. Programs are adjusted for postpartum recovery, including core and pelvic-floor-safe progressions. Always get your doctor's clearance to exercise first."),
    ("What if I have joint pain or an old injury?", "Let Pramas know on your consultation call. Movements are regressed or substituted around injuries so you can train safely."),
    ("Do you provide a meal plan or just general advice?", "You get a structured, personalized nutrition plan built around your food preferences &mdash; not generic advice."),
    ("How often do I get to speak with Pramas directly?", "You get weekly structured check-ins plus direct WhatsApp access in between for questions, form checks and support."),
    ("What happens after the 91 days are over?", "You'll have the strength, habits and nutrition knowledge to maintain results independently. Many clients also choose to continue into a maintenance or strength-focused phase."),
    ("Is there a minimum commitment or contract?", "Programs are sold in blocks (typically 12&ndash;16 weeks) because that's what real change requires. Exact terms are discussed on your consultation call."),
    ("I travel often for work. Can I still follow the program?", "Yes. Workouts require no equipment and can be done in a hotel room, and nutrition guidance adapts to eating out and travel."),
    ("How do I get started?", "Book a free consultation call using the button on this page. We'll discuss your goals, current routine and answer your questions before you commit to anything."),
    ("What makes you different from a regular online fitness coach?", "The combination of K11 nutrition certification, calisthenics specialization, and Pramas' own 30 kg transformation &mdash; built specifically for the realities of Indian working women and mothers, not adapted from a generic Western program."),
]

CONTACT_FAQS = [
    ("What's the fastest way to reach you?", "WhatsApp is the quickest way to get a response, usually within a few hours during business hours."),
    ("Do you offer in-person training?", "Coaching is fully online to serve clients across India, regardless of city. All training is designed to be done from home."),
    ("Can I ask questions before committing to a program?", "Absolutely &mdash; that's exactly what the free consultation call is for. No obligation, no pressure."),
]

