"""Build the K-φ Academy site.

Outputs:
  dist/index.html        full document, for GitHub Pages
  dist/academy.html      same page without the document skeleton, for the claude.ai preview
"""
import json, os, re, markdown
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


TEMPLATE = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()


def main():
    os.makedirs(DIST, exist_ok=True)
    payload = json.dumps(data(), ensure_ascii=False).replace("</", "<\\/")
    body = TEMPLATE.replace("/*__DATA__*/null", payload)
    with open(os.path.join(DIST, "academy.html"), "w", encoding="utf-8") as fh:
        fh.write(body)
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(full)
    n = sum(len(ch["lessons"]) for c in OPEN for ch in c["chapters"])
    print(f"built: {n} lessons in {len(OPEN)} open courses, {len(OUTLINES)} outlines, {len(body)//1024} KB")


if __name__ == "__main__":
    main()
