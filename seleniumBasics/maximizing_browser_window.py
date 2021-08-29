import time
from seleniumBasics.browser_invoking import invoke_browser


driver = invoke_browser()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.quit()
