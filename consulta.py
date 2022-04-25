from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
assert "Python" in driver.title
elem = driver.find_element_by_id("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()