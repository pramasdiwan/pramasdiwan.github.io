# -*- coding: utf-8 -*-
"""
Shared building blocks for generating the Pramas Diwan static site.
Import this module from each page-builder script.
"""

SITE_NAME = "Pramas Diwan"
SITE_URL = "https://www.pramasdiwan.com"  # TODO: replace with the live production domain
PHONE_DISPLAY = "+91 99999 99999"          # TODO: replace with real number
PHONE_TEL = "+919999999999"
EMAIL = "coach@pramasdiwan.com"            # TODO: replace with real inbox
INSTAGRAM_HANDLE = "@pramasdiwan.fit"      # TODO: replace with real handle
INSTAGRAM_URL = "https://instagram.com/pramasdiwan.fit"
LOCATION = "Online Coaching — Serving Clients Pan-India"

# ---------------------------------------------------------------- ICONS ----
ICONS = {
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
"arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
"plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>',
"star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 21 12 17.27 5.82 21 7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>',
"whatsapp": '<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16.04 3C9.4 3 4 8.37 4 14.98c0 2.36.65 4.55 1.78 6.44L4 29l7.78-1.7a13 13 0 0 0 4.26.72c6.64 0 12.04-5.37 12.04-11.98C28.08 8.37 22.68 3 16.04 3zm0 21.83c-1.43 0-2.82-.36-4.06-1.04l-.29-.16-4.62 1 1.02-4.45-.19-.3a9.7 9.7 0 0 1-1.5-5.22c0-5.4 4.43-9.78 9.86-9.78 5.43 0 9.85 4.39 9.85 9.78 0 5.4-4.42 9.78-9.85 9.78l-.22-.6zm5.4-7.34c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.66.15-.2.3-.76.96-.93 1.16-.17.2-.34.22-.64.07-.3-.15-1.25-.46-2.38-1.46-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.61.13-.13.3-.34.45-.5.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.66-1.6-.91-2.18-.24-.58-.48-.5-.66-.5h-.56c-.2 0-.52.07-.79.37s-1.04 1.02-1.04 2.48 1.07 2.87 1.22 3.07c.15.2 2.1 3.21 5.09 4.5.71.31 1.27.49 1.7.62.71.23 1.36.2 1.87.12.57-.08 1.75-.71 2-1.4.24-.68.24-1.27.17-1.4-.07-.12-.27-.2-.57-.35z"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z" opacity="0"/><path d="M22 6L12 13 2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg>',
"pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
"insta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1"/></svg>',
"yt": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2s-.23-1.62-.94-2.34c-.9-.94-1.9-.94-2.36-1C16.4 3.6 12 3.6 12 3.6h-.01s-4.4 0-7.7.26c-.46.06-1.46.06-2.36 1C1.23 5.58 1 7.2 1 7.2S.76 9.1.76 11v1.78c0 1.9.24 3.8.24 3.8s.23 1.62.94 2.34c.9.94 2.08.9 2.6 1C6.4 20.2 12 20.26 12 20.26s4.4-.01 7.7-.27c.46-.06 1.46-.06 2.36-1 .71-.72.94-2.34.94-2.34s.24-1.9.24-3.8V11c0-1.9-.24-3.8-.24-3.8zM9.7 14.94V8.6l6.2 3.17-6.2 3.17z"/></svg>',
"target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/></svg>',
"flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 17a2.5 2.5 0 0 0 2.5-2.5c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7.5 7.5 0 1 1-15 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
"calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
"users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
"award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M8.21 13.89L7 23l5-3 5 3-1.21-9.12"/></svg>',
"heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
"drag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 7 4 12 8 17"/><polyline points="16 7 20 12 16 17"/></svg>',
"shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
"clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>',
"trend": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
"play": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
"smartphone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
"home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
"battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="7" width="18" height="10" rx="2"/><line x1="23" y1="11" x2="23" y2="13"/></svg>',
"scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="12" x2="14.5" y2="14"/></svg>',
"camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
"frown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>',
}

def icon(name, cls=""):
    svg = ICONS.get(name, "")
    if cls:
        svg = svg.replace("<svg ", '<svg class="%s" ' % cls, 1)
    return svg


# ------------------------------------------------------------- NAV/FOOTER ---
NAV_ITEMS = [
    ("Home", "index.html", "home"),
    ("About", "about.html", "about"),
    ("Programs", "programs.html", "programs"),
    ("Transformations", "transformations.html", "transformations"),
    ("Success Stories", "success-stories.html", "success"),
    ("Blog", "blog.html", "blog"),
    ("Contact", "contact.html", "contact"),
]

def root_prefix(depth):
    """depth=0 for files in site root, depth=1 for files in /blog/"""
    return "../" if depth else ""

def header_html(active_key, depth=0):
    rp = root_prefix(depth)
    links = []
    for label, href, key in NAV_ITEMS:
        cls = ' class="active"' if key == active_key else ""
        links.append('<a href="%s%s"%s>%s</a>' % (rp, href, cls, label))
    links_html = "\n        ".join(links)
    return """
<header class="site-header">
  <div class="nav-wrap">
    <a href="%(rp)sindex.html" class="brand"><span class="mark">PD</span> Pramas Diwan</a>
    <nav class="nav-links" id="navLinks">
        %(links)s
        <a href="%(rp)sapply.html" class="btn btn-primary btn-sm" style="margin-top:10px;">Apply For Coaching</a>
    </nav>
    <div class="nav-cta">
      <a href="%(rp)sapply.html" class="btn btn-outline btn-sm">Apply Now</a>
      <a href="%(rp)scontact.html" class="btn btn-primary btn-sm">Book Free Consultation</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
""" % {"rp": rp, "links": links_html}

def footer_html(depth=0):
    rp = root_prefix(depth)
    return """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="%(rp)sindex.html" class="brand"><span class="mark">PD</span> Pramas Diwan</a>
        <p>Helping busy Indian women and mothers lose stubborn fat, build strength, and feel like themselves again &mdash; through sustainable training and nutrition, from home.</p>
        <div class="footer-social">
          <a href="%(insta)s" target="_blank" rel="noopener" aria-label="Instagram">%(insta_icon)s</a>
          <a href="%(wa)s" target="_blank" rel="noopener" aria-label="WhatsApp">%(wa_icon)s</a>
          <a href="mailto:%(email)s" aria-label="Email">%(mail_icon)s</a>
        </div>
      </div>
      <div>
        <h5>Explore</h5>
        <ul>
          <li><a href="%(rp)sabout.html">About Pramas</a></li>
          <li><a href="%(rp)sprograms.html">Programs</a></li>
          <li><a href="%(rp)stransformations.html">Transformations</a></li>
          <li><a href="%(rp)ssuccess-stories.html">Success Stories</a></li>
          <li><a href="%(rp)sblog.html">Blog</a></li>
        </ul>
      </div>
      <div>
        <h5>Programs</h5>
        <ul>
          <li><a href="%(rp)sprograms.html#health-mastery">91 Days Health Mastery</a></li>
          <li><a href="%(rp)sprograms.html#calisthenics-moms">Calisthenics For Moms</a></li>
          <li><a href="%(rp)sprograms.html#fat-loss">Fat Loss Coaching</a></li>
          <li><a href="%(rp)sprograms.html#nutrition">Nutrition Coaching</a></li>
          <li><a href="%(rp)sapply.html">Apply For Coaching</a></li>
        </ul>
      </div>
      <div>
        <h5>Get In Touch</h5>
        <ul>
          <li><a href="tel:%(phone_tel)s">%(phone_display)s</a></li>
          <li><a href="mailto:%(email)s">%(email)s</a></li>
          <li><a href="%(rp)scontact.html">%(location)s</a></li>
          <li><a href="%(rp)scontact.html">Contact Page &amp; Form</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year></span> Pramas Diwan Coaching. All rights reserved.</span>
      <span>Results vary by individual effort, adherence and starting point.</span>
    </div>
  </div>
</footer>

<a href="#" class="float-whatsapp" aria-label="Chat on WhatsApp">
  <span class="ping"></span>%(wa_icon_big)s
</a>

<div class="sticky-cta">
  <a href="%(rp)scontact.html" class="btn btn-primary">Book Free Consultation</a>
  <a href="#" class="btn btn-whatsapp" data-whatsapp="Hi Pramas, I'd like to know more about your coaching programs.">%(wa_icon_sm)s WhatsApp</a>
</div>
""" % {
        "rp": rp,
        "insta": INSTAGRAM_URL,
        "insta_icon": icon("insta"),
        "wa": "https://wa.me/" + PHONE_TEL.replace("+", ""),
        "wa_icon": icon("whatsapp"),
        "wa_icon_big": icon("whatsapp"),
        "wa_icon_sm": icon("whatsapp"),
        "mail_icon": icon("mail"),
        "email": EMAIL,
        "phone_tel": PHONE_TEL,
        "phone_display": PHONE_DISPLAY,
        "location": LOCATION,
    }


def page_shell(title, description, slug, content_html, active_key, depth=0,
               og_image="assets/img/og-cover.jpg", schema_json="", extra_head=""):
    rp = root_prefix(depth)
    canonical = "%s/%s" % (SITE_URL, slug)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="canonical" href="%(canonical)s">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0F172A">

<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(description)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:site_name" content="Pramas Diwan">
<meta property="og:image" content="%(site_url)s/%(og_image)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(description)s">

<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%%3E%%3Crect width='100' height='100' rx='22' fill='%%230F172A'/%%3E%%3Ctext x='50' y='66' font-size='44' font-family='Georgia,serif' fill='%%23fff' text-anchor='middle'%%3EPD%%3C/text%%3E%%3C/svg%%3E">
<link rel="stylesheet" href="%(rp)sassets/css/style.css">
%(extra_head)s
%(schema)s
</head>
<body>
%(header)s
%(content)s
%(footer)s
<script src="%(rp)sassets/js/main.js" defer></script>
</body>
</html>
""" % {
        "title": title,
        "description": description,
        "canonical": canonical,
        "site_url": SITE_URL,
        "og_image": og_image,
        "rp": rp,
        "extra_head": extra_head,
        "schema": ("<script type=\"application/ld+json\">\n%s\n</script>" % schema_json) if schema_json else "",
        "header": header_html(active_key, depth),
        "content": content_html,
        "footer": footer_html(depth),
    }


def photo_block(label, ratio="4/5", light=False, extra_class=""):
    cls = "photo-block light" if light else "photo-block"
    return """<div class="%s %s" style="aspect-ratio:%s;">
      <div class="ph-label">%s</div>
    </div>""" % (cls, extra_class, ratio, label)


def org_schema():
    return """{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Pramas Diwan Coaching",
  "image": "%s/assets/img/og-cover.jpg",
  "url": "%s",
  "telephone": "%s",
  "email": "%s",
  "priceRange": "$$",
  "areaServed": "IN",
  "founder": {
    "@type": "Person",
    "name": "Pramas Diwan",
    "jobTitle": "Transformation Coach & K11 Certified Nutritionist"
  },
  "sameAs": ["%s"]
}""" % (SITE_URL, SITE_URL, PHONE_TEL, EMAIL, INSTAGRAM_URL)
