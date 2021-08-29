import pytest as pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        option = Options()
        option.add_argument("--no-sandbox")
        option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument("--disable-web-security")
        # option.add_argument("--allow-running-insecure-content")
        # option.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)

    elif browser == 'firefox':
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
        driver = webdriver.Ie()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")  # This will get the value from Command line


@pytest.fixture
def browser(request):  # This will return the value of browser to the setup method
    return request.config.getoption("--browser")

# To run the test case run the below command in terminal
# pytest <test_case_path> -s -v --browser chrome
# pytest <test_case_path> -s -v --browser firefox
# pytest <test_case_path> -s -v
