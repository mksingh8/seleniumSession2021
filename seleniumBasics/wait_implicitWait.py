from seleniumBasics.browser_invoking import invoke_browser


def implicit_wait():
    TIMEOUT = 10
    url = "https://www.google.com/"
    driver = invoke_browser()
    # this wait let the webdriver wait for TIMEOUT second for the DOM to load in case intended element is not loaded
    # and then throws "No Such Element Exception" error
    driver.implicitly_wait(TIMEOUT)
    driver.get(url)
    driver.close()


if __name__ == '__main__':
    implicit_wait()


