# 自動で要素をクリックする

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe",
    options=options)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3) 

a_tag = driver.find_element_by_css_selector("div.sc-kDgGX > div > ul > li:nth-of-type(2) > a")
sleep(3)

a_tag.click()
sleep(5)

driver.quit()
