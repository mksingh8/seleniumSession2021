# below locators are present
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--no-sandbox")
# option.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/index.html")

# locators
# driver.find_element_by_id("")
# user name field
driver.find_element_by_name("username").send_keys("manish1")
driver.find_element_by_xpath("//input[@name='username']").clear()
driver.find_element_by_xpath("//input[@name='username']").send_keys("manish2")
driver.find_element_by_class_name("form-control").clear()
driver.find_element_by_class_name("form-control").send_keys("manish3")
driver.find_element_by_css_selector(".form-control").clear()
driver.find_element_by_css_selector(".form-control").send_keys("manish4")
#
# anchor = driver.find_element_by_tag_name("a")
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text("")
# driver.find_element(By.ID, "")

time.sleep(5)
driver.close()