from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random, time, os

CHROME_DRIVER_PATH = r"C:\chromedriver\chromedriver.exe"  # 👈 apna path daalna

def take_screenshots(folder="static/screenshots", count=5):
    os.makedirs(folder, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

    try:
        driver.get("http://127.0.0.1:5000/madlibs")
        time.sleep(1)
        driver.save_screenshot(os.path.join(folder, "homepage.png"))
        print("Saved homepage.png")

        # baki story screenshots code ...
    finally:
        driver.quit()
