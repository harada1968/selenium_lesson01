# idやclsaa名を元に情報抽出する。

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

a_tags = driver.find_elements_by_class_name("sc-hmzhuo")
for a_tag in a_tags:
    print(a_tag)
    print(a_tag.text)
    print(a_tag.get_attribute("href"))
    

driver.quit()