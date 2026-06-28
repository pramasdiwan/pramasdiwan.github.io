# -*- coding: utf-8 -*-
"""
build_from_posts.py
Reads every .md file in _posts/, parses YAML frontmatter,
converts Markdown body to HTML, and writes blog/*.html pages.
Run automatically by the GitHub Actions workflow when CMS saves a post.
"""
import sys, os, re

# ── add build/ to path so we can import common.py ────────────────────────────
BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT  = os.path.dirname(BUILD_DIR)
sys.path.insert(0, BUILD_DIR)

from common import icon, page_shell, SITE_URL
from blog_data import ARTICLES as SAMPLE_ARTICLES  # fallback for related posts

POSTS_DIR = os.path.join(SITE_ROOT, "_posts")
BLOG_OUT   = os.path.join(SITE_ROOT, "blog")
os.makedirs(BLOG_OUT, exist_ok=True)

# ── tiny YAML frontmatter parser (no PyYAML dependency) ─────────────────────
def parse_frontmatter(text):
    """Split --- frontmatter --- from body. Returns (meta_dict, body_str)."""
    meta = {}
    if not text.startswith("---"):
        return meta, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return meta, text
    fm_block, body = parts[1], parts[2].strip()
    for line in fm_block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip('"').strip("'")
    return meta, body

# ── minimal Markdown → HTML converter ───────────────────────────────────────
def md_to_html(md):
    lines = md.split("\n")
    html_lines = []
    in_ul = False
    in_p  = False

    def close_open():
        nonlocal in_ul, in_p
        if in_ul:  html_lines.append("</ul>"); in_ul = False
        if in_p:   html_lines.append("</p>");  in_p  = False

    for line in lines:
        stripped = line.strip()

        # Headings
        if stripped.startswith("#### "):
            close_open()
            html_lines.append("<h4>%s</h4>" % inline_md(stripped[5:]))
        elif stripped.startswith("### "):
            close_open()
            html_lines.append("<h3>%s</h3>" % inline_md(stripped[4:]))
        elif stripped.startswith("## "):
            close_open()
            html_lines.append("<h2>%s</h2>" % inline_md(stripped[3:]))
        elif stripped.startswith("# "):
            close_open()
            html_lines.append("<h1>%s</h1>" % inline_md(stripped[2:]))

        # Unordered list items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if in_p: html_lines.append("</p>"); in_p = False
            if not in_ul: html_lines.append("<ul>"); in_ul = True
            html_lines.append(
                "<li>%s%s</li>" % (icon("check"), inline_md(stripped[2:]))
            )

        # Blank line
        elif stripped == "":
            close_open()

        # Normal paragraph text
        else:
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if not in_p:
                html_lines.append("<p>"); in_p = True
            html_lines.append(inline_md(stripped))

    close_open()
    return "\n".join(html_lines)

def inline_md(text):
    """Convert inline **bold**, *italic*, `code`, and [link](url)."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",         text)
    text = re.sub(r"`(.+?)`",       r"<code>\1</code>",     text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text

# ── article page template ─────────────────────────────────────────────────────
ARTICLE_TEMPLATE = """
<section class="article-hero">
  <div class="container">
    <div class="breadcrumb">
      <a href="../index.html">Home</a> <span>/</span>
      <a href="../blog.html">Blog</a> <span>/</span>
      <span>{category}</span>
    </div>
    <div class="eyebrow on-dark">{category}</div>
    <h1 class="h1" style="max-width:780px;">{title}</h1>
    <div class="article-meta-row">
      <span>{clock_icon} {read_time}</span>
      <span>{user_icon} Pramas Diwan</span>
      <span>{calendar_icon} {date}</span>
    </div>
  </div>
</section>

{featured_img_html}

<article class="article-body">
  {body_html}

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
    <div class="grid grid-3">{related_html}</div>
  </div>
</section>
"""

def related_cards(current_slug, current_cat, all_posts):
    same = [p for p in all_posts if p.get("category") == current_cat and p["slug"] != current_slug]
    other = [p for p in all_posts if p not in same and p["slug"] != current_slug]
    picks = (same + other)[:3]
    cards = []
    for p in picks:
        cards.append("""
        <a href="{slug}.html" class="blog-card reveal" style="display:block;">
          <div class="blog-thumb"><span class="cat">{cat}</span></div>
          <div class="blog-body">
            <div class="meta">{cat} &middot; {read}</div>
            <h3 style="font-size:1.05rem;">{title}</h3>
            <span class="blog-read">Read Article {arrow}</span>
          </div>
        </a>""".format(
            slug=p["slug"], cat=p.get("category", "Blog"),
            read=p.get("read_time", "5 min read"),
            title=p["title"], arrow=icon("arrow")
        ))
    return "".join(cards)

# ── load all posts ────────────────────────────────────────────────────────────
def load_all_posts():
    posts = []
    if not os.path.isdir(POSTS_DIR):
        return posts
    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        slug = fname.replace(".md", "")
        text = open(os.path.join(POSTS_DIR, fname), encoding="utf-8").read()
        meta, body = parse_frontmatter(text)
        posts.append({
            "slug":      slug,
            "title":     meta.get("title", slug.replace("-", " ").title()),
            "category":  meta.get("category", "Blog"),
            "excerpt":   meta.get("excerpt", ""),
            "read_time": meta.get("read_time", "5 min read"),
            "date":      meta.get("date", ""),
            "featured_image":     meta.get("featured_image", ""),
            "featured_image_alt": meta.get("featured_image_alt", ""),
            "seo_title": meta.get("meta_title", ""),
            "seo_desc":  meta.get("meta_description", ""),
            "noindex":   meta.get("noindex", "false").lower() == "true",
            "body_md":   body,
        })
    return posts

def build_posts():
    posts = load_all_posts()

    if not posts:
        print("No .md files found in _posts/ — nothing to build.")
        return

    for p in posts:
        body_html = md_to_html(p["body_md"])

        # Featured image block
        if p["featured_image"]:
            fi_html = """<div style="max-width:860px;margin:0 auto;padding:0 28px 40px;">
  <img src="{src}" alt="{alt}" style="width:100%;border-radius:16px;display:block;">
</div>""".format(src=p["featured_image"], alt=p["featured_image_alt"])
        else:
            fi_html = ""

        related = related_cards(p["slug"], p["category"], posts)

        content = ARTICLE_TEMPLATE.format(
            category=p["category"],
            title=p["title"],
            read_time=p["read_time"],
            date=p["date"],
            clock_icon=icon("clock"),
            user_icon=icon("users"),
            calendar_icon=icon("calendar"),
            featured_img_html=fi_html,
            body_html=body_html,
            arrow_icon=icon("arrow"),
            related_html=related,
        )

        # SEO meta
        page_title = p["seo_title"] or ("%s | Pramas Diwan Blog" % p["title"])
        page_desc  = p["seo_desc"]  or p["excerpt"]
        robots_tag = ""
        if p["noindex"]:
            robots_tag = '<meta name="robots" content="noindex, follow">\n'

        schema = """{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "%s",
  "description": "%s",
  "author": {"@type": "Person", "name": "Pramas Diwan"},
  "publisher": {"@type": "Organization", "name": "Pramas Diwan Coaching"},
  "datePublished": "%s",
  "mainEntityOfPage": "%s/blog/%s.html",
  "articleSection": "%s"
}""" % (
            p["title"].replace('"', "'"),
            page_desc.replace('"', "'"),
            p["date"],
            SITE_URL, p["slug"],
            p["category"],
        )

        html = page_shell(
            title=page_title,
            description=page_desc,
            slug="blog/%s.html" % p["slug"],
            content_html=content,
            active_key="blog",
            depth=1,
            schema_json=schema,
            extra_head=robots_tag,
        )

        out_path = os.path.join(BLOG_OUT, p["slug"] + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("  Built blog/%s.html" % p["slug"])

    print("\nDone — %d post(s) built from _posts/" % len(posts))

    # Also write a _posts_manifest.json so build_blog.py can merge CMS posts
    # with the hardcoded sample articles for the blog index
    import json
    manifest = [{"slug": p["slug"], "title": p["title"],
                  "category": p["category"], "excerpt": p["excerpt"],
                  "read_time": p["read_time"]} for p in posts]
    with open(os.path.join(SITE_ROOT, "_posts_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest written → _posts_manifest.json")

if __name__ == "__main__":
    build_posts()
