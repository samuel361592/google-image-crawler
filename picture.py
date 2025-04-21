import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"
keywords = ['KW1', 'KW2', 'Kw3']
images_per_keyword = 5

def download_google_images(query, num=5):
    folder = os.path.join("google_images", query)
    os.makedirs(folder, exist_ok=True)

    saved = 0  # 已成功儲存的張數
    start = 1  # Google API 的起始 index，從1開始
    attempt = 0  # 限制最多查幾次，避免死循環

    while saved < num and attempt < 5:
        attempt += 1
        params = {
            "q": query,
            "cx": SEARCH_ENGINE_ID,
            "key": API_KEY,
            "searchType": "image",
            "num": 10,  # 每次抓最多 10 張來挑
            "start": start
        }

        res = requests.get(SEARCH_URL, params=params)
        if res.status_code == 200 and 'application/json' in res.headers.get('Content-Type', ''):
            data = res.json()
            items = data.get("items", [])
            if not items:
                print(f"沒有更多圖片了：{query}")
                break

            for item in items:
                if saved >= num:
                    break
                img_url = item['link']
                try:
                    img_res = requests.get(img_url, timeout=10, verify=False, stream=True)
                    content_type = img_res.headers.get("Content-Type", "")
                    if not content_type.startswith("image"):
                        print(f"不是圖片，跳過：{img_url}")
                        continue

                    ext = content_type.split("/")[-1].split(";")[0]
                    filename = f"{query}_{saved + 1}.{ext}"
                    filepath = os.path.join(folder, filename)

                    with open(filepath, 'wb') as f:
                        for chunk in img_res.iter_content(1024):
                            f.write(chunk)
                    saved += 1
                    print(f"儲存 {filename}")
                except Exception as e:
                    print(f"錯誤：{e}")
        else:
            print("API 回傳錯誤，可能金鑰無效或流量用完")
            break

        start += 10  # 下一頁繼續搜尋

    print(f"{query} 完成，共儲存 {saved}/{num} 張圖片")

# 主流程
for kw in keywords:
    download_google_images(kw, images_per_keyword)
