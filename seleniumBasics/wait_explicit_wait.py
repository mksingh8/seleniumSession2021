from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from seleniumBasics.browser_invoking import invoke_browser

TIMEOUT = 10
Polling_Duration = 5
url = "https://www.google.com/"
driver = invoke_browser()
driver.get(url)

def explicit_wait():

    wait = WebDriverWait(driver, TIMEOUT)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    search_box.send_keys("explicit wait", Keys.RETURN)
    driver.close()


def explicit_wait_2():
    wait = WebDriverWait(driver, TIMEOUT, Polling_Duration, ignored_exceptions=None)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    search_box.send_keys("explicit wait", Keys.RETURN)
    wait.until(EC.title_contains("Search"))
    driver.close()


if __name__ == '__main__':
    explicit_wait_2()

