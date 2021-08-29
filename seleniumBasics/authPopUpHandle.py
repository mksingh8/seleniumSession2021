import time

from seleniumBasics.browser_invoking import invoke_browser

driver = invoke_browser()
userName = "admin"
password = "admin"
# print("https://" + userName + ":" + password + "@" + "the-internet.herokuapp.com/basic_auth")
driver.get("https://" + userName + ":" + password + "@" + "the-internet.herokuapp.com/basic_auth")
time.sleep(1)
driver.quit()

