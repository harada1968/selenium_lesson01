from selenium import webdriver
from time import sleep

# STEP1 : driverを作成
driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe")

# STEP2 : driver.get()でサイトにアクセスする
driver.get("https://www.google.co.jp")
sleep(3)

# STEP3 : 要素を取得して、何らかの処理をかける
search_bar = driver.find_element_by_name("q")
sleep(3)

search_bar.send_keys("python")
sleep(3)

search_bar.submit()
sleep(5)

driver.quit()