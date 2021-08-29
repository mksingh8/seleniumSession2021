import time

from seleniumBasics.browser_invoking import invoke_browser

url = "https://mail.rediff.com/cgi-bin/login.cgi"
driver = invoke_browser()
driver.get(url)
driver.maximize_window()
driver.find_element_by_name("proceed").click()
time.sleep(1)
alert = driver.switch_to.alert

print(alert.text)
alert.accept()
time.sleep(1)
driver.close()



