# YTP VocaBuddy 開發者之路　詞彙表 Glossary

> 全站縮寫與術語總表，依篇章分組。教材正文中每個縮寫第一次出現時都寫了全名；忘記時回這裡查。
> 本檔與教材網頁的附錄 C 內容一致，方便列印或發給隊友。

教材網址：<https://tw-ytp.github.io/vocabuddy/>

## 第一篇・Git 與 GitHub

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| VCS | Version Control System | 版本控制系統 | 把每個時間點的程式快照存成可回復、可比對的歷史 |
| repo | repository | 倉庫 | 一個專案的全部檔案＋完整歷史 |
| commit | — | 提交 | 一份完整快照＋作者、時間、訊息、parent 指標 |
| SHA-1 | Secure Hash Algorithm 1 | 雜湊演算法 | 由內容算出的識別碼，是每個 commit 的身分證 |
| DAG | Directed Acyclic Graph | 有向無環圖 | Git 歷史的資料結構：節點＝快照、邊＝parent 指標 |
| LCA | Lowest Common Ancestor | 最近共同祖先 | 兩分支合併時 Git 尋找的比較基準點 |
| HEAD | — | — | 「你現在站在哪個分支」的指標 |
| branch | — | 分支 | 指向某個 commit 的具名指標，開一條近乎零成本 |
| merge | — | 合併 | 把另一條分支的改動收進目前分支 |
| fast-forward | — | 快轉 | 對方是你的直系後代時，合併＝指標前推 |
| conflict | merge conflict | （合併）衝突 | 兩邊改到同一行，Git 停下來請人裁決 |
| staging area | — | 暫存區 | 下一次提交的打包清單，git add 的目的地 |
| origin | — | — | 預設遠端倉庫的代稱 |
| clone / push / pull / fetch | — | — | 整包下載／推上遠端／拉下合併／只下載不合併 |
| PR | Pull Request | 合併請求 | 「請把我的分支合進 main」＋審核討論的頁面 |
| code review | — | 程式碼審查 | 合併前由他人逐行檢查 diff 並留言 |
| issue | — | — | 倉庫的任務單／待辦清單 |
| README | — | — | 倉庫首頁文件，作品的門面 |
| .gitignore | — | — | 列出不進版本控制的檔案（編譯產物、金鑰） |
| GitHub Flow | — | — | main 保持可用；改動走分支＋PR 審核後合併 |
| stash | — | 暫存口袋 | 把未提交的修改先收起來，稍後再拿回 |
| revert | — | 反向提交 | 用一個內容相反的新 commit 安全撤銷歷史 |
| reflog | reference log | — | HEAD 足跡全紀錄，救災用的保險絲 |
| fork | — | — | 把別人的倉庫複製到自己帳號下再貢獻 |
| diff | difference | 差異比對 | 兩個版本間逐行的增刪對照；review 看的就是它 |
| git reset | — | — | 把分支指標整個拉回某節點（--hard 連工作區一起重置；僅限未 push 的本地歷史） |
| Markdown | — | — | 輕量標記語言：用純文字符號（#、-、```）表達格式，README 的標準寫法 |
| Git Bash | — | — | Windows 版 Git 附帶的終端機，指令與 macOS／Linux 相同 |

## 第二篇・AI 與 LLM

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| AI | Artificial Intelligence | 人工智慧 | 讓機器展現智能行為的技術總稱 |
| LLM | Large Language Model | 大型語言模型 | 預測「下一個 token 機率分布」的超大神經網路 |
| token | — | — | 模型處理文字的最小單位；常見字整顆、少見字拆片 |
| embedding | — | 詞嵌入 | token → 高維向量的映射；意義相近則向量相近 |
| attention | — | 注意力 | 每個 token 對其他 token 打分數、做加權平均以吸收上下文 |
| Transformer | — | — | 以 attention 層堆疊而成的架構，現代 LLM 的基礎 |
| softmax | — | — | 把一組分數轉成總和為 1 的機率分布 |
| temperature | — | 溫度 | 取樣的銳化旋鈕：低→穩定保守，高→多樣狂野 |
| top-p | nucleus sampling | — | 只在累積機率前 p 的候選中取樣，砍掉怪尾巴 |
| context window | — | 上下文窗口 | 模型一次能看見的 token 上限，prompt＋歷史＋回答全算 |
| hallucination | — | 幻覺 | 模型輸出流暢但不真實的內容——機率模型的天性 |
| prompt | — | 提示 | 你給模型的輸入文字；品質決定輸出品質 |
| system prompt | — | 系統提示 | 對話的人設與規則，優先權高於一般訊息 |
| API | Application Programming Interface | 應用程式介面 | 服務開給「程式」呼叫的窗口 |
| API key | — | 金鑰 | 呼叫 API 的身分憑證＝你的錢包，永不進 Git |
| SDK | Software Development Kit | 軟體開發套件 | 官方包好的函式庫，把 HTTP 細節藏起來 |
| CLI | Command-Line Interface | 命令列介面 | 在終端機用指令操作的程式形式 |
| JSON | JavaScript Object Notation | — | 程式間交換資料的通用文字格式 |
| open-weight | — | 開源權重 | 公開釋出模型參數，人人可下載自跑（如 Qwen、Llama） |
| MoE | Mixture of Experts | 混合專家 | 參數拆成專家群，每個 token 只喚醒少數幾個 |
| quantization | — | 量化 | 降低參數精度（如 16→4 bit）換取體積與速度 |
| Ollama | — | — | 本地模型管理器：下載、執行、開本機 API 一手包 |
| fallback | — | 降階／備援 | 主要路徑失敗時自動改走的備用路徑 |
| rate limit | — | 速率限制 | API 對呼叫頻率的上限，超過回 429，等待後重試 |
| CEFR | Common European Framework of Reference | 歐洲語言共同參考架構 | A1–C2 的語言難度分級，教材例句用 B1 |
| HTTP / HTTPS | HyperText Transfer Protocol (Secure) | 超文本傳輸協定 | 網路上「送請求、收回應」的標準協定；S 表示加密傳輸 |
| vector | — | 向量 | 一列實數（ℝⁿ 中的點）；embedding 的數學形式 |
| dot product | — | 內積 | 兩向量對應元素相乘再相加；衡量方向相似的基本運算 |
| norm | — | 模長 | 向量的長度（各元素平方和開根號） |
| cosine similarity | — | 餘弦相似度 | 內積除以兩向量模長的乘積＝夾角餘弦；值域 [−1, 1]，越接近 1 語意越近 |
| lookup table | — | 查表 | 給定輸入直接查出預存輸出、不做計算的對應；embedding 層本質是一張 \|詞彙表\|×n 的表 |
| NNS | nearest neighbor search | 最近鄰搜尋 | 給定查詢點，在資料集中找距離最近的點——語意搜尋與 RAG 檢索的核心運算 |
| closest pair | closest pair of points | 最近點對問題 | 在一組點中找出彼此距離最近的一對；經典分治題，O(n log n)——與最近鄰搜尋是不同問題設定 |
| localhost | — | 本機位址 | 指向「這台電腦自己」的網路位址，外部連不進來 |
| port | — | 埠 | 同一台電腦上區分不同網路服務的編號（如 Ollama 的 11434） |

## 第三篇・開發實戰

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| user story | — | 使用者故事 | 需求格式：「身為…我想要…以便…」，逼你想清楚誰要什麼 |
| localStorage | — | — | 瀏覽器內建的小倉庫，資料留在這台裝置；讀寫要包 try/catch |
| fetch / async・await | — | — | JavaScript 發 HTTP 請求與等待回應的語法 |
| Structured Output | — | 結構化輸出 | 用 JSON 骨架＋低溫＋程式驗證，讓 AI 回固定形狀的資料 |
| cache | — | 快取 | 算過的結果存起來重用：省錢、變快、離線可用 |
| CORS | Cross-Origin Resource Sharing | 跨來源資源共享 | 瀏覽器對跨網域請求的安全規範 |
| forgetting curve | — | 遺忘曲線 | 記憶隨時間指數衰減；成功回想後重置且衰減變慢 |
| Leitner system | — | 萊特納盒 | SRS 實作：答對晉級間隔加倍，答錯打回盒 1 |
| SM-2 | SuperMemo 2 | — | Anki 採用的 SRS 演算法，以容易度係數 EF 微調每張卡的間隔 |
| pure function | — | 純函式 | 不碰外部狀態、同輸入必同輸出——因此可測試 |
| unit test | — | 單元測試 | 用程式驗證函式行為的測資；改壞立刻被抓到 |
| retrieval | — | 檢索 | 從一堆資料中挑出此刻最相關的幾筆——RAG 的 R |
| migration | data migration | 資料遷移 | 資料格式改版時，讓舊資料自動升級的邏輯 |

## 第四篇・上線與發表

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| deploy | — | 部署 | 把作品放上永遠開機的伺服器，讓網址取代壓縮檔 |
| static site | — | 靜態網站 | 只有 HTML/CSS/JS 檔案、邏輯全在瀏覽器執行的網站 |
| GitHub Pages | — | — | GitHub 內建的免費靜態網站主機：push main 即上線 |
| manifest | web app manifest | — | 網站的「App 身分證」：名稱、圖示、獨立視窗設定 |
| service worker | — | — | 常駐背景的腳本，攔截請求、先問快取——離線的關鍵 |
| GitHub Actions | — | — | GitHub 內建自動化：事件觸發、雲端機器照劇本執行 |
| workflow | — | 工作流程 | Actions 的劇本檔（.github/workflows/*.yml） |
| runner | — | — | 執行 workflow 的乾淨雲端機器 |
| YAML | YAML Ain't Markup Language | — | 以縮排表達結構的設定檔格式，對空格敏感 |
| badge | — | 徽章 | README 上的即時狀態小圖（如 CI 綠勾） |
| BYOK | Bring Your Own Key | 自帶金鑰 | 使用者輸入自己的 API key，只存在自己裝置 |
| proxy | backend proxy | 後端代理 | 自建伺服器代呼 API，把 key 藏在伺服器端 |
| tag | Git tag | 標籤 | 釘在特定 commit 上不會動的指標，用來標記里程碑 |
| template repository | — | 範本倉庫 | 可一鍵複製成乾淨新專案的倉庫（不帶歷史） |

## 第五篇・AI-Native 開發

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| agentic coding tool | — | 代理式編碼工具 | 有工具、有權限、會自己跑迴圈的編碼助手；不只回答，還動手 |
| agentic loop | — | 代理迴圈 | 蒐集上下文 → 採取行動 → 驗證結果，沒過就再一輪 |
| plan mode | — | 計劃模式 | 先給出計畫、你同意才開工的操作模式 |
| permission mode | — | 權限模式 | 決定哪些動作要問你、哪些可以直接做的設定 |
| compaction | — | 壓縮 | 把對話歷史濃縮成摘要以騰出上下文空間；會丟細節 |
| project instruction file | — | 專案指示檔 | 放在倉庫根目錄、進版控、每次啟動都被讀的隊規 |
| CLAUDE.md | — | — | Claude Code 讀取的專案指示檔檔名（官方明示不讀 AGENTS.md） |
| AGENTS.md | — | — | 跨工具的專案指示檔共同檔名，由 Agentic AI Foundation 託管 |
| SKILL.md | — | — | 一個技能的主檔；開頭是 YAML frontmatter，name 與 description 必填 |
| Agent Skills | — | 代理技能 | 把「某一類任務的固定步驟」寫成可重複使用的開放標準格式 |
| frontmatter | — | 前置資料 | 檔案開頭以 --- 圍起的 YAML 中繼資料區塊 |
| description | — | （技能的）描述 | 技能被不被觸發的關鍵：要寫「什麼時候該用」，不是「這是什麼」 |
| allowed-tools | — | — | 限制技能或代理可用工具的欄位；把唯讀任務關在唯讀權限裡 |
| subagent | — | 子代理 | 在獨立上下文裡辦事、只回報結論的助手；保護你的主上下文 |
| MCP | Model Context Protocol | 模型上下文協定 | 讓代理連接外部工具與資料源的開放協定；六家主流工具皆支援 |
| symbolic link | — | 符號連結 | 讓兩個檔名指向同一份內容；用來橋接各家不同的指示檔檔名 |

## 跨篇・專案與產品

| 術語 | 全名 | 中文 | 一句話解釋 |
|---|---|---|---|
| SRS | Spaced Repetition System | 間隔重複系統 | 按遺忘曲線安排複習時間的排程演算法（第三篇實作） |
| MVP | Minimum Viable Product | 最小可行產品 | 能驗證核心價值的最小版本，先能用再變好 |
| RAG | Retrieval-Augmented Generation | 檢索增強生成 | 先檢索相關資料塞進 prompt，再讓模型回答（第三篇） |
| PWA | Progressive Web App | 漸進式網頁應用 | 可安裝到主畫面、可離線的網頁應用（第四篇） |
| Sprint | — | 衝刺 | 一段短而完整的開發循環：目標→開發→交付 |
| CI | Continuous Integration | 持續整合 | 每次 push 自動執行測試／部署（第四篇） |

---

教材版本 v2.0（2026-09-08）・共 112 條・授權 CC BY-NC-SA 4.0
