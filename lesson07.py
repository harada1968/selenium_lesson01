# JavaScriptを使ってページをスクロールする。

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe",
    options=options)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3) 

height = driver.execute_script("return document.body.scrollHeight")
sleep(3)
driver.execute_script(f"window.scrollTo(0,{height})")
    
sleep(3)


driver.quit()