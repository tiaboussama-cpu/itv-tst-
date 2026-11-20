"""Audit du maillage interne : liens entrants par page, dans le contenu (<main>) seulement,
sans compter l'en-tête ni le pied de page. Usage : python _build/link_audit.py"""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
pages = {}
for p in ROOT.rglob("index.html"):
    if "_build" in p.parts:
        continue
    rel = p.parent.relative_to(ROOT).as_posix()
    pages["/" if rel == "." else f"/{rel}/"] = p

def norm(page_url, href):
    href = href.split("#")[0].split("?")[0]
    if not href or href.startswith(("http", "mailto", "data", "/")):
        return None if not href.startswith("/") else href
    parts = [x for x in page_url.strip("/").split("/") if x]
    for seg in href.split("/"):
        if seg == "..":
            parts.pop()
        elif seg and seg != ".":
            parts.append(seg)
    url = "/" + "/".join(parts)
    if url.endswith("index.html"):
        url = url[: -len("index.html")]
    return url if url.endswith("/") else url + "/"

inbound = defaultdict(set)
outbound = {}
broken = []
for url, path in pages.items():
    html = path.read_text(encoding="utf-8")
    main = re.search(r"<main>(.*)</main>", html, re.S).group(1)
    targets = set()
    for href in re.findall(r'href="([^"]+)"', main):
        t = norm(url, href)
        if t is None:
            continue
        if t not in pages:
            broken.append((url, href))
            continue
        if t != url:
            targets.add(t)
    outbound[url] = targets
    for t in targets:
        inbound[t].add(url)

print(f"{'page':42} {'entrants':>8} {'sortants':>8}")
for url in sorted(pages, key=lambda u: len(inbound[u])):
    print(f"{url:42} {len(inbound[url]):>8} {len(outbound[url]):>8}")
orph = [u for u in pages if u != "/" and not inbound[u]]
print("\npages orphelines (0 lien dans le contenu) :", orph or "aucune")
print("liens cassés :", broken or "aucun")
