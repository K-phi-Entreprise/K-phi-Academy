"""Build the K-φ Academy site.

Outputs:
  dist/index.html        full document, for GitHub Pages
  dist/academy.html      same page without the document skeleton, for the claude.ai preview
"""
import json, os, re, shutil, markdown
from content_foundation import COURSE
from content_fpa import COURSE as FPA
from content_cash import COURSE as CASH
from content_outlines import OUTLINES, PATHS

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")


def md(text):
    text = text.strip().replace("- [ ] ", "- ☐ ")
    return markdown.markdown(text, extensions=["tables"])


OPEN = [COURSE, FPA, CASH]


def data():
    out = []
    for c in OPEN:
        f = json.loads(json.dumps(c))
        for ch in f["chapters"]:
            for l in ch["lessons"]:
                l["read"] = md(l["read"])
        out.append(f)
    order = ["foundation", "fpa", "cash", "build", "implementation"]
    allc = {c["id"]: c for c in out + OUTLINES}
    return {"courses": [allc[i] for i in order], "paths": PATHS}


DESC = "Courses and certification for K-φ: Foundation, FP&A, Cash and Build. Every exam is a real task on a live tenant, graded automatically."
HEAD = (f'<meta name="description" content="{DESC}">\n'
        '<link rel="icon" type="image/svg+xml" href="favicon.svg">\n'
        '<link rel="icon" type="image/x-icon" href="favicon.ico">\n'
        '<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">\n'
        '<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">\n'
        '<link rel="icon" type="image/png" sizes="192x192" href="favicon-192x192.png">\n'
        '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n'
        '<meta property="og:title" content="K-φ Academy">\n'
        f'<meta property="og:description" content="{DESC}">\n'
        '<meta property="og:url" content="https://academy.k-phi.com/">\n'
        '<meta property="og:image" content="https://academy.k-phi.com/og-image.png">\n'
        '<meta name="twitter:card" content="summary_large_image">\n')

TEMPLATE = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def main():
    os.makedirs(DIST, exist_ok=True)
    payload = json.dumps(data(), ensure_ascii=False).replace("</", "<\\/")
    body = TEMPLATE.replace("/*__DATA__*/null", payload)
    with open(os.path.join(DIST, "academy.html"), "w", encoding="utf-8") as fh:
        fh.write(body)
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + HEAD +
            '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    for f in os.listdir(os.path.join(HERE, "static")):
        shutil.copy(os.path.join(HERE, "static", f), os.path.join(DIST, f))
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(full)
    n = sum(len(ch["lessons"]) for c in OPEN for ch in c["chapters"])
    print(f"built: {n} lessons in {len(OPEN)} open courses, {len(OUTLINES)} outlines, {len(body)//1024} KB")


if __name__ == "__main__":
    main()
