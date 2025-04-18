import os
from playwright.sync_api import sync_playwright
import time
import datetime

def is_time_in_range(start_hour, end_hour):
    now = datetime.datetime.now().time()
    if start_hour < end_hour:
        return start_hour <= now.hour < end_hour
    else:
        return now.hour >= start_hour or now.hour < end_hour

def run_bot():
    if not is_time_in_range(20, 3):  # من 8 مساءً إلى 3 صباحًا
        print("ليس الوقت المناسب لتشغيل البوت.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://kick.com/login')
        page.fill('input[name="username"]', os.environ['KICK_USERNAME'])
        page.fill('input[name="password"]', os.environ['KICK_PASSWORD'])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        page.goto('https://kick.com/atro')
        print("البوت يشاهد بث أترو الآن...")
        while is_time_in_range(20, 3):
            time.sleep(300)
        print("انتهى وقت البث، يتم إغلاق البوت.")
        browser.close()

run_bot()
