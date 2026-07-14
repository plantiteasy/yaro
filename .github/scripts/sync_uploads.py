#!/usr/bin/env python3
"""Забирает новые файлы гостей из Uploadcare и добавляет их в галерею сайта."""
import json, os, sys, urllib.request, pathlib

PUB = os.environ["UC_PUB"]
SECRET = os.environ["UC_SECRET"]
ROOT = pathlib.Path(__file__).resolve().parents[2]
SEEN_PATH = ROOT / "data" / "uploads-seen.json"
UPLOAD_DIR = ROOT / "photos" / "uploads"
GALLERY = ROOT / "gallery.json"
MAX_BYTES = 95 * 1024 * 1024

def api(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.uploadcare-v0.7+json",
        "Authorization": f"Uploadcare.Simple {PUB}:{SECRET}",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

seen = set()
if SEEN_PATH.exists():
    seen = set(json.load(open(SEEN_PATH)))

files, url = [], "https://api.uploadcare.com/files/?limit=100&stored=true&ordering=-datetime_uploaded"
data = api(url)
files = data.get("results", [])

new_items, new_names = [], []
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
for f in files:
    uuid = f["uuid"]
    if uuid in seen:
        continue
    seen.add(uuid)
    mime = f.get("mime_type", "")
    size = f.get("size", 0)
    if size > MAX_BYTES or not (mime.startswith("image/") or mime.startswith("video/")):
        continue
    is_video = mime.startswith("video/")
    # У каждого проекта Uploadcare свой CDN-домен (ucarecd.net) — берём его из original_file_url
    orig = f.get("original_file_url") or f"https://ucarecdn.com/{uuid}/x"
    cdn_base = orig.split(uuid)[0] + uuid + "/"
    if is_video:
        ext = {"video/mp4": "mp4", "video/quicktime": "mov", "video/webm": "webm"}.get(mime, "mp4")
        src_url = cdn_base
    else:
        ext = "jpg"
        src_url = cdn_base + "-/format/jpeg/-/quality/smart/-/resize/1600x/"
    dest = UPLOAD_DIR / f"{uuid[:8]}.{ext}"
    try:
        urllib.request.urlretrieve(src_url, dest)
    except Exception as e:
        print(f"skip {uuid}: {e}")
        continue
    by = (f.get("metadata") or {}).get("by", "").strip()
    item = {"src": f"photos/uploads/{dest.name}", "cat": "free"}
    if is_video:
        item["type"] = "video"
    if by:
        item["by"] = by
    new_items.append(item)
    new_names.append(f"{dest.name}" + (f" (от: {by})" if by else ""))

if new_items:
    g = json.load(open(GALLERY))
    g["items"] += new_items
    json.dump(g, open(GALLERY, "w"), ensure_ascii=False, indent=1)

SEEN_PATH.parent.mkdir(parents=True, exist_ok=True)
json.dump(sorted(seen), open(SEEN_PATH, "w"), indent=0)

out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as fh:
        fh.write(f"count={len(new_items)}\n")
        fh.write("names<<EOF\n" + "\n".join(new_names) + "\nEOF\n")
print(f"new items: {len(new_items)}")
