"""Build the K-φ Academy site.

Outputs:
  dist/index.html        full document, for GitHub Pages
  dist/academy.html      same page without the document skeleton, for the claude.ai preview
"""
import json, os, re, shutil, markdown
from content_foundation import COURSE
from content_fpa import COURSE as FPA
from content_ai import COURSE as AI
from content_cash import COURSE as CASH
from content_mcp import COURSE as MCP
from content_treasury_ai import COURSE as TAI
from content_outlines import OUTLINES, PATHS

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")


def md(text):
    text = text.strip().replace("- [ ] ", "- ☐ ")
    return markdown.markdown(text, extensions=["tables"])


OPEN = [COURSE, AI, MCP, FPA, CASH, TAI]


def data():
    out = []
    for c in OPEN:
        if c.get("neutral"):   # the vendor-neutral course names no product: the build stops if it ever does
            hit = re.findall(r"K-\u03c6|K-phi|Halden|practice company|Copilot in K", json.dumps(c, ensure_ascii=False))
            assert not hit, "neutral course mentions: " + ", ".join(sorted(set(hit)))
        f = json.loads(json.dumps(c))
        for ch in f["chapters"]:
            for l in ch["lessons"]:
                l["read"] = md(l["read"])
                v = "videos/" + l["code"].lower().replace(".", "-")
                if os.path.exists(os.path.join(HERE, "static", v + ".mp4")):
                    l["video"] = v + ".mp4"
                    if os.path.exists(os.path.join(HERE, "static", v + ".vtt")): l["captions"] = v + ".vtt"
        out.append(f)
    order = ["ai", "mcp", "foundation", "fpa", "cash", "build", "implementation", "treasury-ai"]  # owner, 2026-11-19: A > M > F
    allc = {c["id"]: c for c in out + OUTLINES}
    return {"courses": [allc[i] for i in order], "paths": PATHS}


# owner, 2026-11-20: "make sure that folks looking for free certifications in treasury or finance in Claude stumble upon
# our academy": a title and description that say free, finance, treasury, AI and certificate; structured data (schema.org
# Course, credential); one static page per course and per path that a crawler reads without running the app; a sitemap,
# robots.txt that welcomes search and AI crawlers, and llms.txt.
SITE = "https://academy.k-phi.com/"
TITLE = "K-φ Academy: free AI certification for finance and treasury"
DESC = ("Free online courses and a free credential for finance and treasury professionals: AI agents in finance, MCP, "
        "data foundations, FP&A and cash. Practise on a live company, pass a practical exam, and share a verifiable "
        "certificate on LinkedIn.")
ORG = {"@type": "Organization", "name": "K-φ", "alternateName": "K-phi", "url": "https://k-phi.com/",
       "sameAs": ["https://www.linkedin.com/company/115993299/"]}
HEAD = (f'<title>{TITLE}</title>\n<meta name="description" content="{DESC}">\n<link rel="canonical" href="{SITE}">\n'
        '<link rel="icon" type="image/svg+xml" href="favicon.svg">\n'
        '<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">\n'
        '<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">\n'
        '<link rel="icon" type="image/png" sizes="192x192" href="favicon-192x192.png">\n'
        '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n'
        f'<meta property="og:title" content="{TITLE}">\n'
        f'<meta property="og:description" content="{DESC}">\n'
        '<meta property="og:url" content="https://academy.k-phi.com/">\n'
        '<meta property="og:image" content="https://academy.k-phi.com/og-image.png">\n'
        '<meta name="twitter:card" content="summary_large_image">\n')


def esc(t):
    return (str(t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def hours(c):
    m = re.search(r"(\d+)\s*hours?(?:\s*(\d+)\s*minutes)?", c.get("duration", "")) or None
    mm = re.search(r"(\d+)\s*minutes", c.get("duration", ""))
    h = int(m.group(1)) if m else 0
    mi = int(m.group(2)) if m and m.group(2) else (int(mm.group(1)) if mm and not m else 0)
    return "PT%dH%dM" % (h, mi) if (h or mi) else None


def cname(c):
    """the vendor-neutral course carries no K-φ in its name (owner, 2026-11-20)"""
    return c["title"] if c.get("neutral") else "K-φ " + c["title"]


def course_ld(c, paths):
    ld = {"@type": "Course", "name": cname(c), "description": c.get("summary", ""), "url": SITE + "courses/" + c["id"] + ".html",
          "provider": ORG, "isAccessibleForFree": True, "inLanguage": "en",
          "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "category": "Free"},
          "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": hours(c) or "PT1H"},
          "about": ["Finance", "Treasury", "Artificial intelligence", "FP&A"],
          "educationalLevel": "Professional"}
    if c.get("outcomes"): ld["teaches"] = c["outcomes"]
    cred = [p for p in paths if c["id"] in p["courses"]]
    if cred: ld["educationalCredentialAwarded"] = cred[0]["credential"] + " (credential when the whole path is done)"
    return ld


def page(title, desc, url, ld, body):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{esc(title)}</title>\n<meta name="description" content="{esc(desc)}">\n<link rel="canonical" href="{url}">\n'
            f'<meta property="og:title" content="{esc(title)}">\n<meta property="og:description" content="{esc(desc)}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{SITE}og-image.png">\n'
            '<link rel="icon" type="image/svg+xml" href="../favicon.svg">\n'
            '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + '</script>\n'
            '<style>body{font:16px/1.6 system-ui,sans-serif;max-width:760px;margin:0 auto;padding:24px 16px;background:#0B0F1A;color:#EDEFF5}'
            'a{color:#E6FF00}h1{line-height:1.2}.free{display:inline-block;background:#E6FF00;color:#0B0F1A;font-weight:700;padding:2px 10px;border-radius:999px}'
            'li{margin:2px 0}.muted{color:#98A1B7}</style>\n</head>\n<body>\n'
            f'<p><a href="{SITE}">K-φ Academy</a></p>\n' + body + '\n</body>\n</html>\n')


def static_pages(d):
    """one plain page per course and per path, readable without running the app, plus sitemap, robots and llms.txt"""
    courses = {c["id"]: c for c in d["courses"]}
    paths = d["paths"]
    os.makedirs(os.path.join(DIST, "courses"), exist_ok=True)
    os.makedirs(os.path.join(DIST, "paths"), exist_ok=True)
    urls = [SITE]
    for c in d["courses"]:
        url = SITE + "courses/" + c["id"] + ".html"
        soon = c.get("status") != "available"
        chap = "".join(f'<h3>{esc(ch["code"])} · {esc(ch["title"])}</h3><ul>' + "".join(f'<li>{esc(l["code"])} {esc(l["title"])}</li>' for l in ch["lessons"]) + "</ul>" for ch in c["chapters"])
        inpaths = [p for p in paths if c["id"] in p["courses"]]
        body = (f'<h1>{esc(cname(c))}</h1>\n<p><span class="free">Free</span> <span class="muted">{esc(c.get("duration", ""))} · online · {"in preparation" if soon else "open now"}</span></p>\n'
                f'<p>{esc(c.get("summary", ""))}</p>\n<p><b>For:</b> {esc(c.get("audience", ""))}</p>\n'
                + (f'<h2>You will be able to</h2><ul>' + "".join(f"<li>{esc(o)}</li>" for o in c.get("outcomes", [])) + "</ul>\n" if c.get("outcomes") else "")
                + (f'<p><b>Exam:</b> {esc(c["exam"]["title"])}, a practical task on a live K-φ company, graded automatically.</p>\n' if c.get("exam") and not c.get("neutral") else "")
                + (f'<p><b>Continuing education:</b> {esc(c["cpe"])}</p>\n' if c.get("cpe") else "")
                + (f'<p><b>Part of:</b> ' + ", ".join(f'<a href="../paths/{p["id"]}.html">{esc(p["title"])}</a>' for p in inpaths) + '. A path done gives its credential, verifiable online and shareable on LinkedIn.</p>\n' if inpaths else "")
                + f'<h2>Lessons</h2>{chap}\n<p><a href="{SITE}#course-{c["id"]}">Start the course, free</a></p>')
        with open(os.path.join(DIST, "courses", c["id"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(page(cname(c) + ": free course for finance and treasury", c.get("summary", "") + (" Free, online, with a certificate of completion." if c.get("neutral") else " Free, online, with practice on a live company."), url, course_ld(c, paths), body))
        urls.append(url)
    for p in paths:
        url = SITE + "paths/" + p["id"] + ".html"
        cs = [courses[x] for x in p["courses"] if x in courses]
        ld = {"@type": "EducationalOccupationalCredential", "name": p["credential"], "description": p.get("who", "") + ": " + ", ".join(cname(c) for c in cs),
              "credentialCategory": "certificate", "recognizedBy": ORG, "url": url, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
              "competencyRequired": [cname(c) for c in cs]}
        body = (f'<h1>{esc(p["credential"])}</h1>\n<p><span class="free">Free credential</span> <span class="muted">{esc(p.get("hours", ""))} · {esc(p.get("who", ""))}</span></p>\n'
                + ('<p>Works with any AI assistant. Finish every lesson and pass the final assessment with more than 80%: the certificate of completion is issued at once, with a public page to verify it and a button to add it to LinkedIn.</p>\n' if p.get("neutral") else
                '<p>Finish every lesson of the path and pass its practical exam on a live K-φ company: the credential is issued at once, with a public page to verify it and a button to add it to LinkedIn.</p>\n')
                + '<h2>Courses</h2><ol>' + "".join(f'<li><a href="../courses/{c["id"]}.html">{esc(cname(c))}</a>: {esc(c.get("summary", ""))}</li>' for c in cs) + '</ol>\n'
                + f'<p><a href="{SITE}">Start, free</a></p>')
        with open(os.path.join(DIST, "paths", p["id"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(page(p["credential"] + ": free AI certification for " + p.get("who", "finance").lower(), "Free credential: " + ", ".join(cname(c) for c in cs) + (". Any AI assistant, final assessment above 80%, verifiable certificate of completion." if p.get("neutral") else ". Practical exam on a live company, verifiable certificate for LinkedIn."), url, ld, body))
        urls.append(url)
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("# search engines and AI assistants are welcome: the academy is free and public\nUser-agent: *\nAllow: /\n\nSitemap: " + SITE + "sitemap.xml\n")
    lines = ["# K-φ Academy", "", "> " + DESC, "",
             "K-φ Academy (" + SITE + ") is free. Courses are online and self-paced; learners practise in a K-φ company of their own, "
             "and a path is certified by a practical exam graded automatically. Credentials have a public verification page and can be added to LinkedIn.",
             "Agentic AI in Treasury teaches no product: every exercise works with any AI assistant and a spreadsheet, "
             "and it ends with an assessment passed with more than 80% and a certificate of completion, built for continuing education (CTP and FPAC holders can submit it under AFP's independent study rules).", "",
             "## Paths and credentials", ""]
    lines += [f'- [{p["credential"]}]({SITE}paths/{p["id"]}.html): {p.get("who", "")}, about {p.get("hours", "")}; courses: ' + ", ".join(cname(courses[x]) for x in p["courses"] if x in courses) for p in paths]
    lines += ["", "## Courses", ""]
    lines += [f'- [{cname(c)}]({SITE}courses/{c["id"]}.html): {c.get("summary", "")} ({c.get("duration", "")}, free{"" if c.get("status") == "available" else ", in preparation"})' for c in d["courses"]]
    with open(os.path.join(DIST, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return urls


TEMPLATE = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def main():
    os.makedirs(DIST, exist_ok=True)
    d = data()
    payload = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
    body = TEMPLATE.replace("/*__DATA__*/null", payload)
    with open(os.path.join(DIST, "academy.html"), "w", encoding="utf-8") as fh:
        fh.write(body)
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + HEAD +
            '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [dict(ORG, **{"@id": "https://k-phi.com/#org"}),
                {"@type": "WebSite", "name": "K-φ Academy", "url": SITE, "description": DESC, "publisher": {"@id": "https://k-phi.com/#org"}},
                {"@type": "ItemList", "name": "K-φ Academy courses", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": course_ld(c, d["paths"])} for i, c in enumerate(d["courses"])]}]}, ensure_ascii=False).replace("</", "<\\/") + '</script>\n'
            '</head>\n<body>\n' + re.sub(r'^<title>[^<]*</title>\n?', '', body) + '\n'
            '<nav class="seo-index" aria-label="All courses and paths" style="max-width:1180px;margin:40px auto 24px;padding:0 16px;font:13px/1.8 system-ui,sans-serif;color:#98A1B7">Free courses: ' + " · ".join(f'<a href="courses/{c["id"]}.html">{esc(cname(c))}</a>' for c in d["courses"]) + '</nav>\n'
            '</body>\n</html>\n')
    shutil.copytree(os.path.join(HERE, "static"), DIST, dirs_exist_ok=True)
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(full)
    static_pages(d)
    n = sum(len(ch["lessons"]) for c in OPEN for ch in c["chapters"])
    print(f"built: {n} lessons in {len(OPEN)} open courses, {len(OUTLINES)} outlines, {len(body)//1024} KB")


if __name__ == "__main__":
    main()
