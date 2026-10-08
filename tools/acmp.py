#!/usr/bin/env python3
"""Minimal acmp.ru client (stdlib only) for solving tasks from a cloud session.

Usage:
  python3 tools/acmp.py next                 # smallest task number > 100 without a NNN.* file
  python3 tools/acmp.py task N               # print statement text (+ image URLs)
  python3 tools/acmp.py submit N FILE        # log in, submit (.py as Python, .cpp as GNU C++), wait for the verdict

Credentials come from the environment: ACMP_LOGIN and ACMP_PASSWORD.
Alternatively ACMP_COOKIE (a raw Cookie header of a logged-in browser) skips the login step.
ACMP_UID is the numeric user id used to filter the status page (default 295782).
"""
import html
import http.cookiejar
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://acmp.ru"
ENC = "windows-1251"
UID = os.environ.get("ACMP_UID", "295782")
PENDING = ("waiting", "compil", "running", "testing", "queue", "очеред", "провер")

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
opener.addheaders = [("User-Agent", "Mozilla/5.0 (acmp-cli)")]


def request(path, data=None, headers=None):
    req = urllib.request.Request(BASE + path, data=data, headers=headers or {})
    if os.environ.get("ACMP_COOKIE"):
        req.add_header("Cookie", os.environ["ACMP_COOKIE"])
    with opener.open(req, timeout=30) as r:
        return r.read().decode(ENC, "replace"), r.geturl()


class Text(HTMLParser):
    BLOCK = {"br", "p", "tr", "div", "li", "h1", "h2", "h3"}

    def __init__(self):
        super().__init__()
        self.out, self.skip, self.images = [], 0, []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "select"):
            self.skip += 1
        elif tag == "br":
            self.out.append("\n")
        elif tag == "img":
            src = dict(attrs).get("src", "")
            if "image.asp" in src:
                self.images.append(urllib.parse.urljoin(BASE + "/", src))

    def handle_endtag(self, tag):
        if tag in ("script", "style", "select"):
            self.skip -= 1
        elif tag in self.BLOCK:
            self.out.append("\n")
        elif tag == "td":
            self.out.append(" | ")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def task(n):
    page, _ = request(f"/index.asp?main=task&id_task={n}")
    p = Text()
    p.feed(page)
    t = "".join(p.out)
    start = t.find("ЗАДАЧА №")
    end = min(i for i in (t.find("Отправить решение"), t.find("Для отправки"), len(t)) if i > 0)
    t = re.sub(r"[ \t]+", " ", t[start:end])
    print("\n".join(s.strip() for s in t.splitlines() if s.strip(" |\xa0")))
    for u in p.images:
        print("IMAGE:", u)


def login():
    if os.environ.get("ACMP_COOKIE"):
        return
    user, pwd = os.environ.get("ACMP_LOGIN"), os.environ.get("ACMP_PASSWORD")
    if not user or not pwd:
        sys.exit("ACMP_LOGIN / ACMP_PASSWORD are not set")
    body = urllib.parse.urlencode({"lgn": user, "password": pwd}, encoding=ENC).encode()
    request("/index.asp?main=enter", body, {"Content-Type": "application/x-www-form-urlencoded"})
    page, _ = request("/index.asp?main=task&id_task=1")
    if "mode=upload" not in page:
        sys.exit("login failed: no submit form after logging in")


def rows(n):
    page, _ = request(f"/index.asp?main=status&id_mem={UID}&id_res=0&id_t={n}")
    out = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if cells and re.fullmatch(r"\d{6,}", cells[0]):
            out.append(cells)
    return out


def lang(n, path):
    if path.endswith(".py"):
        return "PY"
    page, _ = request(f"/index.asp?main=task&id_task={n}")
    opts = re.findall(r'<option[^>]*value=["\']?([^"\'\s>]+)["\']?[^>]*>([^<]*)', page)
    cpp = [o for o in opts if "C++" in o[1]]
    gnu = [o for o in cpp if "GNU" in o[1] or "G++" in o[1].upper()]
    if path.endswith(".cpp") and (gnu or cpp):
        return (gnu or cpp)[-1][0]
    sys.exit("no language for " + path + "; form options: " + "; ".join(f"{v}={t.strip()}" for v, t in opts))


def submit(n, path):
    login()
    code = lang(n, path)
    before = max((int(r[0]) for r in rows(n)), default=0)
    src = Path(path).read_text()
    b = "----acmpcli" + str(int(time.time()))
    parts = []
    for name, value in (("lang", code), ("source", src)):
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n')
    parts.append(f'--{b}\r\nContent-Disposition: form-data; name="fname"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n')
    parts.append(f"--{b}--\r\n")
    data = "".join(parts).encode(ENC, "replace")
    request(f"/index.asp?main=update&mode=upload&id_task={n}", data,
            {"Content-Type": f"multipart/form-data; boundary={b}",
             "Referer": f"{BASE}/index.asp?main=task&id_task={n}"})
    for _ in range(60):
        time.sleep(3)
        new = [r for r in rows(n) if int(r[0]) > before]
        if new:
            verdict = new[0][5].lower()
            if not any(w in verdict for w in PENDING):
                print(" | ".join(new[0]))
                return
    new = [r for r in rows(n) if int(r[0]) > before]
    sys.exit("no final verdict yet: " + (" | ".join(new[0]) if new else "submission not registered (rate limit or not logged in)"))


def nxt():
    root = Path(__file__).resolve().parent.parent
    have = {int(p.name.split(".")[0]) for p in root.rglob("*") if p.is_file() and re.match(r"\d{3,}\.", p.name)}
    print(next(i for i in range(101, 10**4) if i not in have))


if __name__ == "__main__":
    cmd = sys.argv[1:2]
    if cmd == ["next"]:
        nxt()
    elif cmd == ["task"]:
        task(int(sys.argv[2]))
    elif cmd == ["submit"]:
        submit(int(sys.argv[2]), sys.argv[3])
    else:
        sys.exit(__doc__)
