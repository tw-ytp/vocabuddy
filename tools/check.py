#!/usr/bin/env python3
"""
教材結構自動檢查
用法：python3 tools/check.py [index.html]

檢查項目：
  1. 側欄／路由／頁面三者一致
  2. 站內連結沒有指向不存在的頁面
  3. 每幅動圖的 HTML 與 JS 說明對得上，且步數相同
  4. HTML 標籤平衡
  5. 驗收清單 id 不重複
  6. 測驗題號不重複、正解在選項內、選項順序正常
  7. 版本號三處一致

抓不到的（仍需人工看）：內容正確性、前後文一致、附錄 B 是否過期、語調一致。
詳見 docs/MAINTENANCE.md §4.5–4.6。
"""
import re
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "index.html"
h = open(PATH, encoding="utf-8").read()

problems = []


def bad(msg):
    problems.append(msg)


# 1. 路由與頁面
secs = set(re.findall(r'<section class="page" id="p-([^"]+)">', h))
m = re.search(r"var PAGES = \[(.*?)\];", h, re.S)
if not m:
    bad("找不到 PAGES 路由陣列")
    pages = set()
else:
    pages = {x.strip().strip('"') for x in m.group(1).split(",")}
    if pages != secs:
        bad(f"路由與頁面不一致：只在一邊出現 → {sorted(pages ^ secs)}")

nav = set(re.findall(r'<a href="#/([^"]+)"', h))
if nav - secs:
    bad(f"側欄有指向不存在頁面的項目：{sorted(nav - secs)}")

# 2. 站內壞連結
dead = {n for n in re.findall(r'href="#/([^"]+)"', h) if n not in secs}
if dead:
    bad(f"壞連結：{sorted(dead)}")

# 3. 動圖
figs = set(re.findall(r'data-fig="([^"]+)"', h))
keys = set(re.findall(r"^  ([a-zA-Z]+): \{ caps: \[", h, re.M))
if figs != keys:
    bad(f"動圖的 HTML 與 JS 不對應：{sorted(figs ^ keys)}")

for k in sorted(figs & keys):
    fm = re.search(r'<figure class="fig" data-fig="%s">(.*?)</figure>' % k, h, re.S)
    cm = re.search(r"  %s: \{ caps: \[(.*?)\], cmds:" % k, h, re.S)
    if not (fm and cm):
        bad(f"動圖 {k}：找不到對應區塊")
        continue
    steps = [int(x) for x in re.findall(r'data-s="(\d+)"', fm.group(1))]
    ncaps = len(re.findall(r'^\s+"', cm.group(1), re.M))
    if steps and max(steps) != ncaps:
        bad(f"動圖 {k}：SVG 有 {max(steps)} 步，說明卻有 {ncaps} 條")

# 4. 標籤平衡
for tag in ["section", "figure", "table", "ol", "ul", "div", "label"]:
    o = len(re.findall(r"<%s[ >]" % tag, h))
    c = len(re.findall(r"</%s>" % tag, h))
    if o != c:
        bad(f"<{tag}> 標籤不平衡：{o} 開 / {c} 閉")

# 5. 驗收清單 id
cks = re.findall(r'data-ck="([^"]+)"', h)
dup = sorted({x for x in cks if cks.count(x) > 1})
if dup:
    bad(f"驗收框 id 重複（會導致勾選狀態互相干擾）：{dup}")

# 6. 測驗
qs = re.findall(r'data-q="(\d+)"', h)
dupq = sorted({x for x in qs if qs.count(x) > 1})
if dupq:
    bad(f"測驗題號重複：{dupq}")

for qm in re.finditer(
    r'<div class="quiz" data-q="(\d+)" data-ans="([a-z])">(.*?)</div>\s*</div>', h, re.S
):
    qid, ans, block = qm.group(1), qm.group(2), qm.group(3)
    vals = re.findall(r'value="([a-z])"', block)
    if ans not in vals:
        bad(f"第 {qid} 題：正解 {ans} 不在選項 {vals} 內")
    if sorted(vals) != vals:
        bad(f"第 {qid} 題：選項順序錯亂 {vals}")
    names = set(re.findall(r'name="(q\d+)"', block))
    if len(names) != 1:
        bad(f"第 {qid} 題：選項的 name 不一致 {sorted(names)}")

# 7. 版本號一致
side = re.search(r"線上自學教材・v([\d.]+)", h)
foot = re.search(r"教材版本 v([\d.]+)", h)
if not side or not foot:
    bad("找不到版本號（側欄或附錄 B 頁尾）")
elif side.group(1) != foot.group(1):
    bad(f"版本號不一致：側欄 v{side.group(1)}、附錄 B 頁尾 v{foot.group(1)}")

# 結果
print(f"檢查對象：{PATH}（{len(h.encode()) / 1024:.0f} KB）")
print(f"  頁面 {len(secs)}　動圖 {len(figs)}　測驗 {len(qs)} 題　驗收框 {len(cks)}")
if side:
    print(f"  版本 v{side.group(1)}")
print()
if problems:
    for p in problems:
        print("✗", p)
    print(f"\n共 {len(problems)} 項問題。")
    sys.exit(1)
print("✓ 全部通過。")
print("  提醒：自動檢查抓不到內容正確性與附錄 B 是否過期，請一併人工複查（見 docs/MAINTENANCE.md §4.6）。")
