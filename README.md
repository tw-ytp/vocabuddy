# YTP VocaBuddy 開發者之路

> **GitHub 與 AI 應用程式開發**——線上自學教材
> 教材網址：<https://tw-ytp.github.io/vocabuddy/>

寫給**已經受過紮實程式訓練的高中生**：你熟 Python 或 C++、打過程式競賽，但沒碰過版本控制、網頁與 API。這份教材帶你補上那塊拼圖——把程式碼變成一個**真的有人在用的服務**。

五篇課程、十三個主線 Lab（外加一個選修特別篇），全程動手做同一個作品：**VocaBuddy 背單字夥伴**。

---

## 課程結構

| 篇 | 主題 | 你會做出什麼 |
|---|---|---|
| 第一篇 | GitHub 協作 | 倉庫上線、會用分支與 PR｜App：靜態單字卡骨架 |
| 第二篇 | AI 與 LLM | 懂原理、把 AI 接進程式｜App：AI 例句生成器 |
| 第三篇 | 開發實戰（四個 Sprint） | 完整協作流程｜App：SRS 排程＋智慧出題 |
| 第四篇 | 上線與發表 | 部署、PWA、CI、Demo｜App：正式發布 |
| **第五篇** | **AI-Native 開發** | 代理迴圈、專案指示檔、技能、子代理｜工作流：AI 成為隊友 |
| 附錄 E | 特別篇（選修）：本地端 LLM | Ollama 跑開源模型＋降階容錯 |

**附錄**：A 一頁速查卡｜B 時效資訊表｜C 詞彙表（另見 [`glossary.md`](glossary.md)）｜D 給老師與主辦單位

---

## 教材特色

- **單一自包含 HTML**：零依賴、可離線、可放任何靜態主機。外部連線只有 Google Fonts。
- **33 幅可步進的 SVG 動圖**，其中 4 幅可互動（token 機率分布、temperature 滑桿、SRS 遺忘曲線模擬、指示檔作用範圍）。
- **13 個主線 Lab**，每個都附完整程式碼、驗收清單與自助排錯——**假設你沒有助教**，一個人也走得完。
- **會過期的東西全部集中在附錄 B**（時效資訊表），正文只寫長期不變的原理。改版時改那一頁就好。
- **工具中立**：第五篇的觀念適用於任何代理式編碼工具（Claude Code、OpenAI Codex、Google Antigravity、Cursor、GitHub Copilot、Gemini CLI……）。示範統一用一種工具，每處標明換工具要改哪裡。
- 亮／暗主題、手機版全數實測。

---

## 給開課者

教材**附錄 D** 是給老師與主辦單位的專章，內含：

- 範例 Repo 與檢查點（tag）建置指引
- 課程節奏參考
- 線上課的助教在做什麼——以及為什麼自學者不需要他們
- AI-Native 工作坊（4 小時場）帶法
- 驗收與 Demo 帶法

部署、維運與改版流程見 [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md)。

---

## 本地預覽

單一 HTML 檔，直接用瀏覽器打開 `index.html` 即可。若要模擬正式站的路徑行為：

```bash
python3 -m http.server 8000
# 瀏覽器開 http://localhost:8000
```

---

## 發現錯誤或有改善建議？

直接在本倉庫[開一個 issue](https://github.com/tw-ytp/vocabuddy/issues)——這正是本教材教你的協作方式。

回報時請附上：**哪一節／哪個 Lab、你看到什麼、你預期看到什麼**。若是附錄 B 的時效資訊過期，請一併附上你查到的新狀態與來源。

---

## 授權

| 對象 | 授權 |
|---|---|
| 教材內容（文字、圖表、結構） | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hant) |
| 教材中的程式碼片段 | MIT |

詳見 [`LICENSE`](LICENSE)。教材中提及的第三方產品名稱與商標屬各自所有人。

---

*教材版本 v2.0（2026-09-08）・貫穿案例：VocaBuddy 背單字夥伴・版本沿革見 [`CHANGELOG.md`](CHANGELOG.md)*
