# Cookie Clicker automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os, time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

price0 = 15
count = 0
for i in range(5000):
    actions = ActionChains(driver) # sequence of actions in queue
    actions.click(cookie)
    if count > price0:
        item = driver.find_element(By.ID, "productPrice0")
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(item)
        upgrade_actions.click()
        upgrade_actions.perform()
        price0 = int(item.text)
    if i > 1:
        count = cookie_count.text.split(" ")[0]
        count.strip()
        count = int(count)
        print(count)
    actions.perform() # perform queued actions
