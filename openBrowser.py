from login import login
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
#开启网站完成登陆
def openBrowser(keyinfo,urlEntry):
    user_agent = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f'User-Agent={user_agent}')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser=webdriver.Chrome(chrome_options=chrome_options)

    browser.get(urlEntry)
    #r = requests.get(urlEntry)
    #print(r.status_code)
    print("open browser and start login")

    browser = login(keyinfo[0],keyinfo[1],browser)

    return browser



