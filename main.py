from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
# 1. ヘッドレスモードでの使用
# options.add_argument("--headless")
# 2. シークレットモードでの使用
options.add_argument("--incognito")
# 3. User-Agentの使用
#options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
# STEP1 : driverを作成。
driver = webdriver.Chrome(
    executable_path="tools\chromedriver.exe",
    options=options)

# STEP2 : driver.get()でサイトにアクセスする。
driver.get("https://news.yahoo.co.jp")
sleep(3)

print(driver.title)
print(driver.current_url)

driver.get("https://google.com")
sleep(3)

print(driver.title)
print(driver.current_url)

driver.back()
sleep(3)

driver.forward()
sleep(3)

driver.refresh()
sleep(3)

driver.quit()
# --> ブラウザを終了する(command + q, alt + F4)
# driver.close()
# --> ページを閉じる(command + w, alt +w)
