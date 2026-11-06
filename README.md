# 🤖 LLM 新聞摘要小程式 (AI News Summarizer)

本專案為人工智慧應用實作作業，透過 Python 呼叫 Google Gemini API 實現自動化新聞重點摘要，並結合 **Streaming（串流輸出）** 技術即時呈現 AI 思考與生成過程。同時搭配 GitHub Actions 實現自動化部署，將專案成果展示於 GitHub Pages。

---

## 🛠️ 專案技術規格 (Tech Stack)
- **程式語言**：Python 3.10+
- **核心套件**：`google-genai` (Gemini API SDK)、`python-dotenv`
- **套件/專案管理**：`uv`
- **自動化部署**：GitHub Actions (Workflow)、GitHub Pages
- **使用模型**：`gemini-2.5-flash`

---

## 📂 專案檔案結構 (Project Structure)
```text
llm-homework/
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions 自動部署設定檔
├── .gitignore             # 排除 .env 等敏感機密檔案，避免外洩
├── main.py                # 呼叫 Gemini API 進行串流摘要的主程式
├── pyproject.toml         # 專案相依性與環境設定檔
└── index.html             # GitHub Pages 作業成果展示網頁
