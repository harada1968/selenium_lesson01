# HTMLタグを指定して情報を抽出する。

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe",
    options=options)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3) 

h2_tags = driver.find_elements_by_tag_name("h2")

for h2_tag in h2_tags:
    print(h2_tag.text)
    print(h2_tag.get_attribute("outerHTML"))

driver.quit()