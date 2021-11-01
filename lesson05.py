# 検索ボックスの取り扱い（入力・検索・削除）

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe",
    options=options)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3) 

search_box = driver.find_element_by_css_selector("input.sc-kgoBCf")
search_box.send_keys("Python")
sleep(3)

# search_box.clear()
text = search_box.get_attribute('value')
search_box.send_keys(Keys.BACKSPACE * len(text))
sleep(5)

search_box.send_keys("機械学習")
sleep(3)
search_box.submit()
sleep(5)

driver.quit()