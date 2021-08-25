from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def invoke_browser(browser=None):
    if browser == 'chrome':
        option = Options()
        option.add_argument("--no-sandbox")
        option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument('--headless')
        # option.add_argument("--disable-xss-auditor")
        # option.add_argument("--disable-web-security")
        # option.add_argument("--allow-running-insecure-content")
        # option.add_argument("--no-sandbox")
        # option.add_argument("--disable-setuid-sandbox")
        # option.add_argument("--disable-webgl")
        # option.add_argument("--disable-popup-blocking")
        # option.add_argument("window-size=1500,1200")
        # option.add_argument("disable-dev-shm-usage")
        # option.add_argument("disable-gpu")
        # option.add_argument("log-level=3")
        driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
        # driver.get("https://www.google.com/")
        # driver.close()

    elif browser == 'firefox':
        # option = Options()
        option = webdriver.FirefoxOptions()
        # option.headless = False
        option.binary_location("/usr/bin/firefox")
        option.add_argument("-profile")
        option.add_argument("/home/manish/.mozilla/firefox/n1wvl68n.default")
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        # fp = webdriver.FirefoxProfile("/home/manish/.mozilla/firefox/n1wvl68n.default")

        driver = webdriver.Firefox(executable_path="/home/manish/Documents/browsers/geckodriver"
                                   , options=option, capabilities=firefox_capabilities)

    else:
        option = Options()
        option.add_argument("--no-sandbox")
        option.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
    return driver


if __name__ == '__main__':
    driver = invoke_browser()
    driver.get("https://www.google.com/")
    driver.close()
