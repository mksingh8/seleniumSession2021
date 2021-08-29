import time

from selenium.webdriver.common.keys import Keys

from seleniumBasics.browser_invoking import invoke_browser

url = "https://www.google.com/"
driver = invoke_browser()
driver.get(url)
driver.find_element_by_name("q").send_keys("browser navigation", Keys.RETURN)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.quit()


