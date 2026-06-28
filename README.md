[README.md](https://github.com/user-attachments/files/29429373/README.md)
# Pramas Diwan — Transformation Coaching Website

A complete, production-ready static website for Pramas Diwan's online fitness coaching brand.

---

## What's Included

| Path | Description |
|---|---|
| `index.html` | Home page (all 10 sections) |
| `about.html` | Full coach story, certifications, timeline, philosophy |
| `programs.html` | 4 programs with detailed breakdowns |
| `transformations.html` | Gallery, before/after sliders, 3 detailed case studies |
| `success-stories.html` | Video reviews, written testimonials, 3 client interviews |
| `blog.html` | SEO blog index with category filtering |
| `blog/*.html` | 12 individual SEO articles (2 per category) |
| `contact.html` | Contact form, all channel links, FAQ, business hours |
| `apply.html` | Full coaching application form with 3-step process |
| `sitemap.xml` | All 20 URLs for search engine submission |
| `robots.txt` | Allows all crawlers, references sitemap |
| `assets/css/style.css` | Complete design system + component library |
| `assets/js/main.js` | Nav, FAQ accordion, B/A sliders, forms, counters, reveal |
| `assets/img/og-cover.jpg` | Open Graph cover image (1200×630) |
| `assets/img/icon-*.png` | App/PWA icons |
| `assets/img/apple-touch-icon.png` | Apple home-screen icon |

---

## Before Going Live — Action List

### 1. Replace placeholder content
- [ ] **Photos**: Replace all `<div class="photo-block">` and `<div class="hero-photo">` placeholder divs with real photography from Pramas (before/after transformation shots, professional brand portraits)
- [ ] **Video testimonials**: Replace the `<div class="video-testi">` placeholders with real `<video>` or `<iframe>` embeds (YouTube/Vimeo)
- [ ] **Before/After sliders**: The sliders are fully functional — add real client transformation images as `<img>` tags inside `.ba-before .ba-inner` and `.ba-after`

### 2. Update contact details in `build/common.py`
```python
PHONE_DISPLAY = "+91 XXXXX XXXXX"       # real WhatsApp-linked number
PHONE_TEL     = "+91XXXXXXXXXX"          # same, no spaces, with country code
EMAIL         = "coach@pramasdiwan.com"  # real inbox
INSTAGRAM_URL = "https://instagram.com/YOUR_HANDLE"
SITE_URL      = "https://www.pramasdiwan.com"  # live domain
```
Then re-run all build scripts (see Build section below), or find-replace directly in the HTML.

### 3. Connect a real form backend
The forms currently:
- Show a confirmation message
- Open a pre-filled WhatsApp link
- Log the data to `console.log`

For real lead capture, replace the `// In production: replace this block...` comment in `assets/js/main.js` with a `fetch()` POST to your preferred backend — Formspree, Netlify Forms, Google Apps Script, or a custom CRM webhook.

### 4. WhatsApp business number
In `assets/js/main.js`, change:
```js
var WHATSAPP_NUMBER = "919999999999";
```
To the real 12-digit international format (91 + 10-digit Indian mobile, no + or spaces).

### 5. Update the Open Graph image
The `assets/img/og-cover.jpg` was generated as a placeholder with brand colours and stats. Replace it with a real branded photo (1200×630 px, JPEG) for best social sharing appearance.

---

## Deployment

The entire site is **static HTML/CSS/JS** — no server, no build step, no dependencies.

### Netlify (recommended — free)
1. Drag the `pramasdiwan/` folder to **netlify.com/drop**
2. Add your custom domain in Site Settings → Domain Management
3. Enable HTTPS (one click)

### Vercel
```bash
npm i -g vercel
cd /path/to/pramasdiwan
vercel --prod
```

### Any cPanel / shared hosting
Upload all files via File Manager or FTP, keeping the folder structure intact. Point your domain's document root to the uploaded folder.

### GitHub Pages
Push to a GitHub repo, enable Pages from the `main` branch root, add a custom domain.

---

## Re-Building Pages (Optional)

The site is pre-built — you can deploy the HTML directly. If you want to regenerate pages after changing shared content (e.g. contact details, program descriptions, FAQs):

```bash
cd build/
python3 build_home.py
python3 build_about.py
python3 build_programs.py
python3 build_transformations.py
python3 build_success.py
python3 build_contact.py
python3 build_apply.py
python3 build_blog.py
```

Requires Python 3.8+, no external dependencies.

---

## SEO Notes

- Every page has unique `<title>`, `<meta name="description">`, Open Graph tags, and canonical URL
- Schema.org `ProfessionalService` markup on all main pages
- `Article` schema on all blog posts
- `sitemap.xml` at root — submit to Google Search Console after going live
- SEO-friendly URL slugs throughout
- Blog articles are 800–1,000 words, keyword-targeted for Indian women's fitness queries

---

## Browser & Device Support

- Chrome, Firefox, Safari, Edge (latest)
- iOS Safari 14+, Android Chrome 90+
- Responsive at 320px minimum width
- Respects `prefers-reduced-motion` for all animations
- Keyboard-accessible focus states throughout

---

## Colour Reference

| Token | Hex | Usage |
|---|---|---|
| Navy | `#0F172A` | Primary backgrounds, text |
| Red | `#DC2626` | CTAs, accents, tags |
| Off-white | `#F8FAFC` | Section backgrounds |
| Green | `#22C55E` | Success states, check icons |
| Ink | `#111827` | Body text |

---

## Typography

| Role | Font | Source |
|---|---|---|
| Display / headings | Fraunces | Google Fonts |
| Body / UI | Inter | Google Fonts |

Both loaded via Google Fonts CDN with `display=swap`.

---

Built with: Pure HTML5 · CSS3 (custom properties) · Vanilla JS · Python build scripts
No frameworks. No runtime dependencies. Deploys anywhere.
