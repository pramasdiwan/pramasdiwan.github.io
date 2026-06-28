# -*- coding: utf-8 -*-
"""
build_sitemap.py
Generates sitemap.xml merging static pages + all blog articles (hardcoded + CMS).
Run after build_from_posts.py so _posts_manifest.json exists.
"""
import sys, os, json, glob
from datetime import date

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT  = os.path.dirname(BUILD_DIR)
sys.path.insert(0, BUILD_DIR)
from common import SITE_URL

STATIC_PAGES = [
    ("index.html",             "1.0", "weekly"),
    ("about.html",             "0.8", "monthly"),
    ("programs.html",          "0.8", "monthly"),
    ("transformations.html",   "0.7", "monthly"),
    ("success-stories.html",   "0.7", "monthly"),
    ("blog.html",              "0.8", "daily"),
    ("contact.html",           "0.7", "monthly"),
    ("apply.html",             "0.9", "monthly"),
]

today = date.today().isoformat()

xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]

for loc, prio, freq in STATIC_PAGES:
    xml.append("  <url>")
    xml.append("    <loc>%s/%s</loc>" % (SITE_URL, loc))
    xml.append("    <lastmod>%s</lastmod>" % today)
    xml.append("    <changefreq>%s</changefreq>" % freq)
    xml.append("    <priority>%s</priority>" % prio)
    xml.append("  </url>")

# Blog articles — from both hardcoded build and CMS posts
blog_slugs = set()

# Hardcoded sample articles
try:
    sys.path.insert(0, BUILD_DIR)
    from blog_data import ARTICLES
    for a in ARTICLES:
        blog_slugs.add(a["slug"])
except ImportError:
    pass

# CMS-generated posts (from manifest written by build_from_posts.py)
manifest_path = os.path.join(SITE_ROOT, "_posts_manifest.json")
if os.path.exists(manifest_path):
    with open(manifest_path, encoding="utf-8") as f:
        cms_posts = json.load(f)
    for p in cms_posts:
        blog_slugs.add(p["slug"])

# Also scan blog/ folder directly as a fallback
for fp in glob.glob(os.path.join(SITE_ROOT, "blog", "*.html")):
    slug = os.path.basename(fp).replace(".html", "")
    blog_slugs.add(slug)

for slug in sorted(blog_slugs):
    xml.append("  <url>")
    xml.append("    <loc>%s/blog/%s.html</loc>" % (SITE_URL, slug))
    xml.append("    <lastmod>%s</lastmod>" % today)
    xml.append("    <changefreq>monthly</changefreq>")
    xml.append("    <priority>0.6</priority>")
    xml.append("  </url>")

xml.append("</urlset>")

out = os.path.join(SITE_ROOT, "sitemap.xml")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(xml) + "\n")

print("sitemap.xml → %d URLs" % (len(STATIC_PAGES) + len(blog_slugs)))
