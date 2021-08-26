
# css selector
from selenium import webdriver

driver = webdriver.Chrome("")

# find element with id
driver.find_element_by_css_selector("#id")
driver.find_element_by_xpath("//tagName[@id='id']")

# find element with class
# css: .className; xpath: //tagName[@class='class_name']
driver.find_element_by_css_selector(".class")
driver.find_element_by_xpath("//input[@class='class_name']")

# regular expression: find all a tags with word mail
# css: tagName[Attribute*='value')]; xpath: //tagName[contains(@attribute,'attribute_fixed_value')]
driver.find_element_by_css_selector("a[href*='mail']")
driver.find_element_by_xpath("//input[contains(@id,'staticPartOf_id')]")
driver.find_element_by_xpath("//input[contains(text(),'static_testOfWebelement')]")

# find all elements with tag a
# css: tagName; xpath: //tagNmae
driver.find_elements_by_css_selector("a")
driver.find_elements_by_xpath("//a")

# find all child elements of tag a
# css: a>*; xpath: //a/*
driver.find_elements_by_css_selector("a>*")
driver.find_elements_by_xpath("//a/*")

# first child of all a
driver.find_elements_by_css_selector("a>*:first-child")
driver.find_elements_by_xpath("//a/*[0]")

# next element of a (sibling)
driver.find_element_by_css_selector("a+*")
driver.find_element_by_xpath("//a/following-sibling::*[0]")

# previous element of a
# not possible through css_selector
driver.find_element_by_xpath("//a/preceding-sibling::*[0]")


"//input[@name='email' or @type='text']"
"//input[@value='Login' and @type='submit']"
"//a[text()='Login']"
"//input[contains(@name,'name') and contains(@type,'text')]"
"//htmltag[contains(text(),'value')]"

# contains() with text() and attribute:
"//htmltag[contains(text(),'value') and contains(@attr,'value')]"

"(//input[@ type='text'])[position() = 1]"
"(//input[@class ='form-control'])[position()=1]"
"(//input[@ class ='form-control'])[1]"
"(//ul[@ class ='footer-nav'])[1] // a"

"(//input[@ class ='form-control'])[last()]"

# parent to child:'
"//div[ @class ='private-form__input-wrapper']/input"
"// div[@ class ='private-form__input-wrapper']/child::input[ @ id = 'username']"

# parent to ancestor:'
"// input[ @ id = 'username']/ancestor::div"
