import concurrent.futures
import requests

TARGET_URL = "https://consularprotection-travelsafety-exhibition.hk/360/zh?mode=&sid=scene_1"
TOTAL_VISITS = 50

# 模擬真實瀏覽器的 User-Agent，避免被伺服器阻擋
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def visit_once(index):
    try:
        # 發送 GET 請求模擬訪問
        response = requests.get(TARGET_URL, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            print(f"[成功] 第 {index + 1} 次訪問完成 (狀態碼: 200)")
        else:
            print(f"[警告] 第 {index + 1} 次訪問回應狀態碼: {response.status_code}")
    except Exception as e:
        print(f"[失敗] 第 {index + 1} 次訪問發生錯誤: {e}")

def main():
    print(f"開始執行共 {TOTAL_VISITS} 次訪問任務...")  # <-- 這裡加上了正確的引號與 f-string 格式
    # 使用多執行緒（ThreadPoolExecutor）同時發送請求，提升效率
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(visit_once, range(TOTAL_VISITS))
    print("所有訪問任務已執行完畢！")

if __name__ == "__main__":
    main()
