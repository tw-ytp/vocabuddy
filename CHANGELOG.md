# 版本沿革

本教材的版本號規則見 [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) §3.3。

---

## v2.2.1 — 2026-10-14

**附錄 B 新增「免費雲端 GPU」一列**

為沒有顯卡的學生補上第三條路（雲端 API／本地端／借來的 GPU）。內容取自 Kaggle 官方文件 <https://www.kaggle.com/docs/efficient-gpu-usage>（查證 2026-10-14）：免費 Tesla P100、每週 30 小時額度、互動工作階段閒置 60 分鐘結束；雙 T4（`T4 x2`）為筆記本加速器選單的選項，2026-10-10 實測可用但官方該頁未列型號清單。

依教材「查不到就留白」的紀律，三件事明確標為未查證：開啟 GPU／網路是否需手機驗證、未成年帳號規定、**把 Notebook 當對外 API 服務是否符合 Kaggle 使用條款**。

修訂版，不打 tag（見 `docs/MAINTENANCE.md` §3.3）。正文未動。

---

## v2.2 — 2026-10-14

**Lab 1–14 全線實作勘誤修訂（E-012～E-032）**

接續 v2.1。勘誤同樣來自在 `ytp26h2/ytp26h2-labs` 照教材逐步實作的實際卡關，本輪覆蓋第三篇四個 Sprint、第四篇上線三連發，以及第五篇 Lab 11–14。原始勘誤表見 [`docs/ERRATA.md`](https://github.com/ytp26h2/ytp26h2-labs/blob/main/docs/ERRATA.md)。**21 條全部採納。**

### 高嚴重度

| # | 章節 | 修訂 |
|---|---|---|
| E-014 | Sprint 2・本輪新知②・急救表、附錄 B | **新一代模型不再接受 `temperature`**，送出回 400，而錯誤被 `catch` 吞掉，畫面只顯示「AI 暫時不可用」。拿掉 `temperature`；Structured Output 由「三板斧」改為「兩件事」（JSON 骨架＋程式端驗證）；急救表新增「網路正常卻一直不可用 → F12 Network 看回應」；附錄 B 新增採樣參數一列 |

### 第五篇（E2 工作坊直接使用，優先處理）

| # | 章節 | 修訂 |
|---|---|---|
| E-027 | Lab 11 步驟 3／5・驗收 | 第 3 題的正確答案**取決於倉庫做到哪裡**（Lab 1 是 `index.html` 的 `WORDS`、8 字；Sprint 4 後是 `words.js`、18 字以上），新增對照表；瀏覽器驗證不再寫死「按下一張」 |
| E-028 | 5.4 指示檔範例 | 「怎麼跑起來」改為 `python3 -m http.server`——Lab 9 之後 App 是 PWA，範例若教 `file://`，AI 會照著一直叫人用 `file://` |
| E-029 | Lab 12 步驟 4 | 辨識規矩要挑「模型照抄現狀也不會自然做到」的事（本倉庫實測：要求中文註解會得到**假陽性**），改用 `// 用途：` 這類固定記號，並建議先跑對照組 |
| E-030 | Lab 14 前置 | 照順序做的話 Lab 13 的 PR 已合併，改為用 `git diff lab12-done lab13-done` |
| E-032 | Lab 14 步驟 3・卡住了？④ | 步驟 2 剛把子代理限制成唯讀，它就**跑不了 `git diff`**。改為在主對話取出 diff 全文再交給它，並說明另一種作法是放寬唯讀指令 |

### 第三篇

| # | 章節 | 修訂 |
|---|---|---|
| E-012 | Sprint 1 `next()` | `stats()` 移到第一行——答完最後一張時卡片說「今日完成！」而上方停在「剩 1 張」 |
| E-013 | Sprint 1 驗收第 3 項 | 註明佇列進度**不保留**（Sprint 1 的刻意簡化），避免誤以為 localStorage 沒生效 |
| E-015 | Sprint 2 `show()` | 模型輸出不再用 `innerHTML` 插入，改 `createElement`＋`textContent` |
| E-016 | Sprint 2 `getKey()`・急救表 | `prompt()` 按取消回 `null`，舊版會存成字串 `"null"` 而不再詢問；加 `if (!k) return null;`，並在收到 401 時自動清掉 `vb-key` |
| E-017 | Sprint 3 時間旅行・驗收第 3 項 | 新卡答對進盒 2，第一個間隔是 **2 天**：`vbTravel(1)` 是空的，`vbTravel(2)` 才回來；間隔序列改為 2→4→8→16；答錯的卡當天排隊尾重考 |
| E-018 | Sprint 3 `test_srs.js`・驗收第 1 項 | 新增第五條 `schedule(2, true, 100) → { box: 3, due: 104 }`——原本四條沒有一條蓋到盒 3，`INTERVALS[3]` 改壞測試照樣通過。驗收改為「每一格改壞都會被抓到」 |
| E-019 | Sprint 3 `today()` | 原式算的是 UTC 日，台灣要早上 8 點才換日；改用本地日 |
| E-020 | Sprint 4 `smartQuiz()` | 題目與解析改用 `createElement`＋`textContent`（與 E-015 同類） |
| E-021 | Sprint 4 答題寫回 | 不再用模型回的字串當 `log` 的鍵：先把 `q.answer` 對回單字包裡的本尊，對不上就不出題 |
| E-022 | Sprint 4 AI 出題 | 補上 `callClaude(system, user)` 的**完整程式**（原本只在註解裡提一句「把 Sprint 2 的 fetch 抽成共用函式」），並明說要回頭改 `aiExample()` |

### 第四篇

| # | 章節 | 修訂 |
|---|---|---|
| E-023 | Lab 9 PWA 化・急救表 | `file://` 下註冊 service worker 會噴紅字；改為只在 http(s) 下註冊並加 `.catch()`，急救表補一列 |
| E-024 | 4.3／Lab 9 `ci.yml` | `on: [push, pull_request]` 會讓 PR 的每個 commit 跑兩次；改為 `push` 只跟 `main`、`pull_request` 跑一次 |
| E-025 | 4.2 `sw.js` | `SHELL` 補上 `icon.png`，否則離線時圖示抓不到 |
| E-026 | 附錄 D・Lab 9／Lab 10 驗收 | `v1.0` 的內容與 Lab 9 驗收對不上（作品級 README 是 Lab 10 的事）。附錄 D 的 `v1.0` 改為只含 Pages＋PWA＋CI，新增 `v1.1`（作品級 README＋畢業挑戰），Lab 10 驗收加上打 tag |

### 跨章節

- **E-031**：`git grep sk-` 會命中教材自己的說明文字與示範假 key，學生會以為外洩。全書七處改為 `git grep sk-ant-api`，並補上查歷史的 `git log -p -S'sk-ant-api' --all` 與「真金鑰長成 `sk-ant-api03-` 開頭」的說明。
- **E-006 延伸**：v2.1 只改了 Lab 2、Lab 3，本版把 Sprint 1～4、Lab 9 與附錄 E Lab 4 的 `closes #3`～`closes #8` 一併改為 `closes #N`。

### 驗證

- `tools/check.py` 全數通過（58 頁・28 幅步進圖・27 題・91 個驗收框・版本號三處一致）。
- **程式全部由教材原始碼直接擷取後實測**（Node 22／無頭 Chromium）：
  - `test_srs.js` 五條通過；**把 `INTERVALS` 五格各改壞一次，五次全被抓到**（修訂前第 3 格改壞不會紅）。
  - SRS 排程：新卡答對後 `due = 今天 + 2`，連續全對的間隔序列為 2→4→8→16，答錯打回盒 1 間隔 1——與修訂後的教材說法一致。
  - `today()` 本地日：23:30 與隔日 00:30 分屬不同日（UTC 日要到隔日 08:30 才換）。
  - Sprint 1 全頁操作到底：卡片顯示「今日完成！」時計數同步為「剩 0 張」。
  - Service worker：修訂後的註冊程式在 `file://` 下無 console 錯誤；修訂前的版本可穩定重現 `origin ('null') is not supported`。
  - `smartQuiz()`：注入 `<img onerror>` 的題目與解析不會執行、以純文字呈現；模型回 `"Algorithm"` 時 `log` 的鍵是 `algorithm`；答案不在單字包時不出題。Sprint 2 的 `show()` 同樣擋住注入。
  - `check_words.js`：單字只剩一個時確實擋下。
  - `ci.yml`：YAML 可正常解析，`on` 為 `push(main)` ＋ `pull_request`。
- 十四個改動頁面於亮色、暗色、手機寬度（390px）全頁截圖檢視，無破版、無 console 錯誤。

### 未納入

- 附錄 F「雲端 GPU 特別篇」仍未合併（裁示：待其餘 Lab 實作、修訂完成後一起進倉庫）。
- v2 回傳的 `zh` 欄位語意不穩，仍留給 Sprint 2 的 Structured Output 處理。

---

## v2.1 — 2026-10-14

**Lab 1–3 實作勘誤修訂（E-001～E-011）**

勘誤來源不是紙上審閱，而是 2026-10-13 在 `ytp26h2/ytp26h2-labs` 照教材 v2.0 逐步實作 Lab 1–3 時的實際卡關；其中 E-009、E-011 有真實 API 呼叫實證。原始勘誤表見 [`ytp26h2/ytp26h2-labs` 的 `docs/ERRATA.md`](https://github.com/ytp26h2/ytp26h2-labs/blob/main/docs/ERRATA.md)。

### 高嚴重度（學生照抄教材就會卡住）

| # | 章節 | 修訂 |
|---|---|---|
| E-009 | 2.5、Lab 3 v1／v2 | 回應的 `content` 是**區塊列表**，新模型常先回 `thinking` 區塊；`content[0].text` 會噴 `AttributeError`。改為依 `type` 挑出所有 `text` 區塊（新增 `text_of()`），並在 2.5 新增說明框 |
| E-011 | 2.5、Lab 3 v1／v2 | `max_tokens` **包含 thinking 的 token**，`300` 幾乎全被想掉、印出空白且不報錯。v1／2.5 改 `2000`、v2 改 `1024`，並在 2.5 說明如何用 `stop_reason` 判斷 |

### 中嚴重度

| # | 章節 | 修訂 |
|---|---|---|
| E-001 | Lab 1 步驟 4、Lab 9 步驟 1 | 建倉庫時即預告「Lab 9 的 Pages 需要 Public，所以金鑰一次都不要進歷史」；Lab 9 回指 Lab 1 |
| E-004 | Lab 1 急救表 | 頭像灰色問號補上 **noreply 信箱**的情況（勾了 Keep my email private 時，`user.email` 必須設成 noreply 信箱才會歸戶） |
| E-006 | Lab 2 步驟 1／2／5・驗收，Lab 3 步驟 2／6・驗收 | issue 與 PR **共用編號**，不一定是 `#1`／`#2`。改為「記下實際編號 N」寫法 |
| E-007 | Lab 3 v1／v2、2.5、Sprint 2、附錄 B | 模型名稱 `claude-sonnet-4-5` → `claude-sonnet-5-5`；附錄 B 改列三個現行型號並註明「不要自己加日期後綴」 |

### 低嚴重度

| # | 章節 | 修訂 |
|---|---|---|
| E-002 | Lab 1 步驟 2 起始碼 | `#card` 初值不寫死，載入時呼叫 `render()`——資料只有一份，畫面永遠照資料畫 |
| E-003 | Lab 1 步驟 1／6 | Windows 補 `core.autocrlf input`（保護個人）與 `.gitattributes`（保護倉庫），避免假 diff |
| E-005 | Lab 2 步驟 2、Sprint 4 `check_words.js` | `quiz()` 加 `WORDS.length < 2` 守衛（否則 `do…while` 無窮迴圈）；資料檢查腳本同步加「至少 2 個字」 |
| E-008 | Lab 3 前置與步驟 1、附錄 B | Python 3.9+ → **3.10+**；3.9 會靜默裝到 SDK 0.x |
| E-010 | Lab 3 v2、驗收第 4 項 | 沒設 key 時 client 建立在 `try` 外、降階接不到；改為函式開頭先檢查環境變數。驗收拆成「有 key 但斷網」與「完全沒設 key」兩項 |

### 一併處理（非勘誤表項目，為前後文一致）

- **Sprint 2 的 JavaScript 版**有與 E-007／E-009／E-011 完全相同的三處問題（`claude-sonnet-4-5`、`data.content[0].text`、`max_tokens: 300`），一併修正——Sprint 4 的 `callClaude()` 沿用這段骨架，因此也一併受益。
- Lab 3 急救表新增四列（SDK 裝到 0.x／`ThinkingBlock` AttributeError／`Could not resolve authentication method`／輸出空白）。
- 附錄 C 與 `glossary.md` 新增三條：`content block`、`thinking`、`max_tokens`（共 115 條）。
- `docs/MAINTENANCE.md` 版本字樣與「回報管道」一節同步（頁尾措辭已於 v2.0 上線後改過）。

### 驗證紀錄

- `tools/check.py` 全部通過（58 頁・28 幅步進圖・27 題・90 個驗收框・版本號三處一致）。
- Lab 3 修訂後 v1／v2 由教材原始碼直接擷取後實測（`anthropic` 1.13.0／Python 3.13）：v1 無 key 印提示並以 exit 1 結束、v2 無 key 印罐頭 exit 0、v2 有 key 但連不上（base URL 指向 `127.0.0.1:9`）走罐頭 exit 0；`text_of()` 以含 `thinking` 區塊的回應單元測試通過。
- Lab 1 起始碼與 Lab 2 `quiz()` 以無頭瀏覽器實測：首張卡顯示 `algorithm`、翻面與換字正常、「考我」連按十次無連續重複、`WORDS` 只剩一字時不卡死。

### 未納入

- Lab 4 及之後的章節未改（本次沒有實作證據）。
- v2 回傳的 `zh` 欄位語意不穩（偶爾給單字解釋而非例句翻譯）留給第三篇 Sprint 2 的 Structured Output 處理，不列為勘誤。

---

## v2.0 — 2026-09-08

**新增第五篇「AI-Native 開發：讓 AI 進到你的工作流」**

主線由四篇擴為五篇、Lab 由 9 個增為 13 個、動圖由 26 幅增為 33 幅、自我檢測由 22 題增為 27 題。

### 新增內容

| 節／Lab | 標題 |
|---|---|
| 5.0 | 篇首：讓 AI 進到你的工作流 |
| 5.1 | 什麼是代理式編碼工具（含六工具跨平台對照表・圖 27） |
| Lab 11 | 開工準備——自己裝好，自己跑起來 |
| 5.2 | 上下文視窗是預算，不是容器（圖 28） |
| 5.3 | 權限與紅線：哪些事永遠不放手（圖 29） |
| 5.4 | 專案指示檔：把隊規寫下來（圖 30） |
| Lab 12 | 讓 AI 認識你的專案 |
| 5.5 | 技能與子代理：教一次，用很多次（圖 31） |
| Lab 13 | 你的第一個技能 |
| Lab 14 | 讓子代理幫你 review |
| 5.6 | 讀懂一份陌生的程式碼（圖 32） |
| 5.7 | 驗證：AI 寫的，你負責（圖 33） |
| 5.8 | 綜合驗收：讓 Repo 說話（17 項證據地圖） |
| quiz5 | 第五組自我檢測（五題） |

### 設計原則

- **自學可獨立完成**：新增 Lab 11 專責工具安裝；每個 Lab 附「卡住了？」自助排錯（新增 `.stuckbox` 樣式）；導讀新增「這份教材假設你沒有助教」。安裝**刻意不寫死指令**，只教三個共通步驟與驗證方式，實際指令指向官方頁。
- **工具中立**：正文只用通稱（代理式編碼工具／專案指示檔／技能／子代理／工具協定），具體產品名與路徑全部收進附錄 B。示範統一用一種工具，每處標明換工具要改哪裡。
- **老師的話另闢專章**：所有開課者資訊集中於附錄 D，正文不寫給老師。

### 連動修改

- 導讀：篇數與 Lab 總數、旅程圖新增第五站、新增「假設你沒有助教」
- 第一篇 1.7：新增「子代理 review 不取代人審」
- 第二篇 2.5：新增「別跟第五篇搞混了」指路卡（區分「程式呼叫模型」與「模型幫你寫程式」）
- 第四篇 4.4：安全清單新增權限分級列；4.5：連結至 5.8 並補 AI 產出真實性
- 附錄 A：新增「代理式工具日常」與「卡住時的五個檢查」兩區
- 附錄 B：新增第五篇專區共 11 條（含「刻意留白：查不到的項目」）
- 附錄 C：新增第五篇 16 個詞條（全表共 112 條）
- 附錄 D：新增 `lab11-done`～`lab14-done` 四個檢查點；新增三節——「線上課的助教在做什麼」「AI-Native 工作坊（4 小時場）帶法」「驗收與 Demo 帶法」
- 第四篇自我檢測結語改為承接第五篇

### 首次以 GitHub Pages 發布

倉庫 `tw-ytp/vocabuddy`，網址 <https://tw-ytp.github.io/vocabuddy/>。
新增 `README.md`、`LICENSE`（CC BY-NC-SA 4.0 ＋ MIT）、`CHANGELOG.md`、
`docs/MAINTENANCE.md`（部署／維運／改版手冊）、`tools/check.py`（結構自動檢查）、`.gitignore`，
`glossary.md` 同步更新至 112 條。

上線後補入（原保留至 Pages 實際存在才寫）：

- **導讀新增「順帶一提」**：說明「你正在看的這個網頁，就是用第四篇會教你的方法上線的」，
  並指向教材倉庫——讀完第一篇看得懂那裡的 commit 與 PR，讀完第四篇會用同一套方法上線。
- **附錄 B 頁尾**：原本寫「公開版可直接在其 GitHub 倉庫開 issue」但倉庫並不存在，
  現改為教材網址、原始檔位址、issue 連結與授權標示的真實連結。
- **附錄 D**：自架說明改為指向正式部署位址，並指出維運手冊的位置。

---

## v1.3 — 2026-08

- 更名為「YTP VocaBuddy」
- 本地端 LLM（2.6、2.7、Lab 4）移出主線，改為**附錄 E 特別篇・選修**；主線 Lab 調整為九個
- 新增附錄 E 導讀頁

## v1.0 — 2026-08-24

教材完成，四篇 21 節、10 個 Lab、4 組自我檢測、附錄 A–D、26 幅 SVG 圖。

- **第四篇** 上線與發表：GitHub Pages 部署、PWA、GitHub Actions CI、金鑰與安全總複習、發表與畢業挑戰；Lab 9「上線三連發」、Lab 10「發表與畢業」
- 新增附錄 D「教師／主辦：範例 Repo 與檢查點建置指引」

## v0.3 — 2026-08-23

- **第三篇** 開發實戰：四個 Sprint（Lab 5–8）——MVP 複習佇列、AI 例句上卡片、SRS 排程演算法、智慧出題與共編
- 招牌動圖：圖 20「遺忘曲線 × Leitner 盒」互動模擬

## v0.2 — 2026-08-23

- **第二篇** AI 與 LLM：下一個 token 機率、token 與 embedding、attention、取樣與 temperature、Claude API、本地模型
- Lab 3（例句生成 CLI）、Lab 4（本地模型與切換）
- 互動動圖：token 機率分布、temperature 滑桿
- 附錄 C 詞彙表上線

## v0.1 — 2026-08-23

- 網站骨架（側欄導航、hash 路由、亮暗主題、手機版抽屜選單）
- **第一篇** GitHub 全七節、Lab 1–2、自我檢測
- 附錄 A 速查卡、附錄 B 時效資訊表
