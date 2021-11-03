# 機械学習を検索し、全記事のタイトルとURLを取得する。

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

search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
search_box.send_keys("機械学習")
sleep(1)
search_box.submit()
sleep(5)

while True:
    #1 スクロールする
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    #2 ボタンのCSSセレクタを取得する
    button = driver.find_elements_by_css_selector('div.newsFeed > div > span > button')
    sleep(2)
    #3 ボタンを押す
    if button:
        button[0].click()
    else:
        break    
a_tags = driver.find_elements_by_css_selector("a.newsFeed_item_link")

for i, a_tag in enumerate(a_tags):
    print("=" * 30, i, "=" * 30)
    print(a_tag.find_element_by_css_selector(".newsFeed_item_title").text)
    print(a_tag.get_attribute("href"))


    
driver.quit()