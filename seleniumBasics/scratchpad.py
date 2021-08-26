# import os
#
# import webdrivermanager
# from selenium import webdriver
# from webdrivermanager import ChromeDriverManager
#
# chromedriver = os.path.dirname(os.path.realpath(__file__)) + "/chromedriver"
# print(chromedriver)
# # geckodriver
# # drv = webdriver.Chrome(chromedriver)
# # webdrivermanager.AVAILABLE_DRIVERS()
# driver = webdrivermanager.chrome
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com/")
# driver.close()
#
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
driver.get("https://www.google.com/")
driver.close()


# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("https://www.google.com/")
# driver.close()
