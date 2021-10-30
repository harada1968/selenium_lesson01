# スクリーンショットをとる

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

driver.save_screenshot("test.png")


driver.quit()