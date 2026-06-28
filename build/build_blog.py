# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import icon, page_shell, SITE_URL
from blog_data import ARTICLES

OUT = os.path.join(os.path.dirname(__file__), "..")
BLOG_OUT = os.path.join(OUT, "blog")
os.makedirs(BLOG_OUT, exist_ok=True)

CATEGORIES = ["Fat Loss", "Women's Fitness", "Calisthenics", "Mobility", "Nutrition", "Healthy Habits"]

# ---------------------------------------------------------------- INDEX ----
def blog_card(a):
    return """
    <a href="blog/{slug}.html" class="blog-card reveal" data-category="{cat}" style="display:block;">
      <div class="blog-thumb"><span class="cat">{cat}</span></div>
      <div class="blog-body">
        <div class="meta">{cat} &middot; {read}</div>
        <h3>{title}</h3>
        <p>{excerpt}</p>
        <span class="blog-read">Read Article {arrow}</span>
      </div>
    </a>""".format(slug=a["slug"], cat=a["category"], read=a["read_time"],
                    title=a["title"], excerpt=a["excerpt"], arrow=icon("arrow"))

filter_btns = '<button class="active" data-filter="all">All Articles</button>' + "".join(
    ['<button data-filter="%s">%s</button>' % (c, c) for c in CATEGORIES]
)

index_content = """
<section class="hero" style="padding-bottom:70px;">
  <div class="container">
    <div class="section-head reveal in" style="margin:0 auto;max-width:760px;">
      <div class="eyebrow on-dark">The Blog</div>
      <h1 class="h1">Fat Loss, Fitness &amp; Nutrition &mdash; Built For Real Indian Life</h1>
      <p class="lede" style="margin:0 auto;">Practical, no-nonsense articles on fat loss, women's fitness, calisthenics, mobility, nutrition and the habits that make it all stick.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="blog-filters reveal">%s</div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section bg-navy">
  <div class="container">
    <div class="cta-band reveal">
      <h2 class="h2">Want A Plan Built Specifically For You?</h2>
      <p>Articles are a great start. A personalized coaching plan is how you actually get there.</p>
      <div class="cta-row">
        <a href="contact.html" class="btn btn-primary">Book Free Consultation %s</a>
        <a href="apply.html" class="btn btn-outline">Apply For Coaching</a>
      </div>
    </div>
  </div>
</section>
""" % (filter_btns, "".join([blog_card(a) for a in ARTICLES]), icon("calendar"))

index_html = page_shell(
    title="Blog | Fat Loss, Fitness & Nutrition Tips For Women | Pramas Diwan",
    description="Practical articles on fat loss, women's fitness, calisthenics, mobility, nutrition and healthy habits — written for busy Indian women and mothers.",
    slug="blog.html",
    content_html=index_content,
    active_key="blog",
)
with open(os.path.join(OUT, "blog.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("Built blog.html")

# ------------------------------------------------------------- ARTICLES ----
ARTICLE_TEMPLATE = """
<section class="article-hero">
  <div class="container">
    <div class="breadcrumb">
      <a href="../index.html">Home</a> <span>/</span> <a href="../blog.html">Blog</a> <span>/</span> <span>{category}</span>
    </div>
    <div class="eyebrow on-dark">{category}</div>
    <h1 class="h1" style="max-width:780px;">{title}</h1>
    <div class="article-meta-row">
      <span>{clock_icon} {read_time}</span>
      <span>{user_icon} Pramas Diwan</span>
    </div>
  </div>
</section>

<article class="article-body">
  {body}

  <div class="article-cta reveal">
    <h3 class="h3" style="margin-bottom:10px;">Want This Built Into A Personalized Plan?</h3>
    <p class="muted" style="margin-bottom:22px;">Reading is a great start. A coaching plan tailored to your body and schedule is how you actually get results.</p>
    <div class="cta-row">
      <a href="../contact.html" class="btn btn-primary">Book Free Consultation {arrow_icon}</a>
      <a href="../apply.html" class="btn btn-outline-dark">Apply For Coaching</a>
    </div>
  </div>
</article>

<section class="section bg-off">
  <div class="container">
    <div class="section-head reveal">
      <div class="eyebrow">Keep Reading</div>
      <h2 class="h3">More From The Blog</h2>
    </div>
    <div class="grid grid-3">{related}</div>
  </div>
</section>
"""

def related_cards(current):
    same_cat = [a for a in ARTICLES if a["category"] == current["category"] and a["slug"] != current["slug"]]
    others = [a for a in ARTICLES if a not in same_cat and a["slug"] != current["slug"]]
    picks = (same_cat + others)[:3]
    cards = []
    for a in picks:
        cards.append("""
        <a href="{slug}.html" class="blog-card reveal" style="display:block;">
          <div class="blog-thumb"><span class="cat">{cat}</span></div>
          <div class="blog-body">
            <div class="meta">{cat} &middot; {read}</div>
            <h3 style="font-size:1.05rem;">{title}</h3>
            <span class="blog-read">Read Article {arrow}</span>
          </div>
        </a>""".format(slug=a["slug"], cat=a["category"], read=a["read_time"], title=a["title"], arrow=icon("arrow")))
    return "".join(cards)

for a in ARTICLES:
    body = a["body"]
    related = related_cards(a)
    content = ARTICLE_TEMPLATE.format(
        category=a["category"], title=a["title"], read_time=a["read_time"],
        clock_icon=icon("clock"), user_icon=icon("users"),
        body=body, arrow_icon=icon("arrow"), related=related,
    )
    schema = """{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "%s",
  "description": "%s",
  "author": {"@type": "Person", "name": "Pramas Diwan"},
  "publisher": {"@type": "Organization", "name": "Pramas Diwan Coaching"},
  "mainEntityOfPage": "%s/blog/%s.html",
  "articleSection": "%s"
}""" % (a["title"].replace('"', "'"), a["excerpt"].replace('"', "'"), SITE_URL, a["slug"], a["category"])

    html = page_shell(
        title="%s | Pramas Diwan Blog" % a["title"],
        description=a["excerpt"],
        slug="blog/%s.html" % a["slug"],
        content_html=content,
        active_key="blog",
        depth=1,
        schema_json=schema,
    )
    with open(os.path.join(BLOG_OUT, a["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Built %d blog articles" % len(ARTICLES))
