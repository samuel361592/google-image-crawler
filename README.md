# Google Image Crawler

一個使用 Google Custom Search API 撰寫的 Python 圖片爬蟲工具，根據使用者定義的關鍵字，自動搜尋並下載圖片，儲存在對應的資料夾中。

---

## 專案動機

在實際工作中，我們需要針對特定主題（如食物、動作、物品等）蒐集大量圖片作為 **大型語言模型（LLM）訓練資料**。手動蒐集圖片耗時費力。

因此，我寫了這套 **自動化圖片爬蟲工具**，能夠：

- 快速從 Google 搜尋特定主題的圖片
- 自動分類儲存、排除非圖片檔
- 動補足指定張數，保證訓練資料品質

這個工具成功應用於 LLM 訓練資料前處理流程，並大幅減少人工蒐集時間 

---

## 功能特色

- 支援多關鍵字圖片搜尋
- 自動濾除非圖片格式（避免損壞檔案）
- 自動建立關鍵字資料夾儲存圖片
- 若圖片無效或下載失敗，自動補抓直到達成指定張數
---

## 安裝與執行

### 安裝相依套件
```bash
pip install requests python-dotenv
```

### 設定 API 金鑰與 CSE ID
建立 .env 檔案（可參考 .env.example）：

API_KEY=你的 Google API 金鑰
SEARCH_ENGINE_ID=你的 Google Custom Search Engine ID
你可以到 Google Cloud Console 取得金鑰，並在 Programmable Search Engine 建立搜尋引擎。

###  執行主程式
```bash
python picture.py
```

關鍵字設定
你可以在 picture.py 中修改 keywords 清單：

```bash
keywords = ['貓', '狗', '風景']
```

每個關鍵字會儲存在對應的資料夾中，例如：

```bash
google_images/
├── 貓/
├── 狗/
└── 兔子/
```
注意事項
每個 API 金鑰每日免費查詢限制為 100 次

遇到 SSL 憑證錯誤的圖片會自動忽略

專案結構
```bash
google-image-crawler/
├── .env.example      # API 設定範本
├── .gitignore        # 忽略圖片與敏感檔
├── picture.py        # 主程式
├── google_images/    # 爬下來的圖片（自動產生）
└── README.md         # 專案說明文件
```

## 作者

本專案由samuel開發
