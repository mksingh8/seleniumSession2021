from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from seleniumBasics.browser_invoking import invoke_browser


def explicit_wait():
    TIMEOUT = 10
    url = "https://www.google.com/"
    driver = invoke_browser()
    driver.get(url)
    wait = WebDriverWait(driver, TIMEOUT)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    search_box.send_keys("explicit wait", Keys.RETURN)
    driver.close()


if __name__ == '__main__':
    explicit_wait()

