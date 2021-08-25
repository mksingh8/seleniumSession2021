import os

from selenium import webdriver

chromedriver = os.path.dirname(os.path.realpath(__file__)) + "/chromedriver"
print(chromedriver)
# geckodriver
drv = webdriver.Chrome(chromedriver)
