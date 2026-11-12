import asyncio
from playwright.async_api import async_playwright

TARGET_URL = "https://consularprotection-travelsafety-exhibition.hk/360/zh?mode=&sid=scene_1"
TOTAL_VISITS = 50

async def visit_page(browser, index):
    page = await browser.new_page()
    try:
        # 前往網址，設定 60 秒逾時
        await page.goto(TARGET_URL, timeout=60000)
        # 等待 5 秒讓 360 度環景資源完整載入
        await asyncio.sleep(5)
        print(f"[成功] 第 {index + 1} 次瀏覽完成")
    except Exception as e:
        print(f"[失敗] 第 {index + 1} 次瀏覽發生錯誤: {e}")
    finally:
        await page.close()

async def main():
    async with async_playwright() as p:
        # 啟動無頭瀏覽器 (在背景執行，不顯示視窗)
        browser = await p.chromium.launch(headless=True)
        
        # 為了平衡執行速度，每次同時跑 5 個分頁
        batch_size = 5
        for i in range(0, TOTAL_VISITS, batch_size):
            current_batch = range(i, min(i + batch_size, TOTAL_VISITS))
            tasks = [visit_page(browser, idx) for idx in current_batch]
            await asyncio.gather(*tasks)
            # 批次之間休息 2 秒
            await asyncio.sleep(2)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
