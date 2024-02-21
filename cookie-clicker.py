from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

still_clicking = True
start = dt.now()
previous_time = start

while still_clicking:
    cookie.click()
    now = dt.now()
    if (now - start).total_seconds() >= (5*60):
        still_clicking = False
        cookies_second = driver.find_element(By.ID, value="cps").text
        print(cookies_second)
    elif (now - previous_time).total_seconds() >= 20:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
        previous_time = now
        if money >= 123456789:
            buy_time_machine = driver.find_element(By.ID, value="buyTime machine")
            buy_time_machine.click()
        elif money >= 1000000:
            buy_portal = driver.find_element(By.ID, value="buyPortal")
            buy_portal.click()
        elif money >= 50000:
            buy_alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
            buy_alchemy_lab.click()
        elif money >= 7000:
            buy_shipment = driver.find_element(By.ID, value="buyShipment")
            buy_shipment.click()
        elif money >= 2000:
            buy_mine = driver.find_element(By.ID, value="buyMine")
            buy_mine.click()
        elif money >= 550:
            buy_factory = driver.find_element(By.ID, value="buyFactory")
            buy_factory.click()
        elif money >= 123:
            buy_grandma = driver.find_element(By.ID, value="buyGrandma")
            buy_grandma.click()
        elif money >= 17:
            buy_cursor = driver.find_element(By.ID, value="buyCursor")
            buy_cursor.click()
