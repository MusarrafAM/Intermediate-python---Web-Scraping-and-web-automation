from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
WEBSITE = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service=Service(PATH))

driver.get(WEBSITE)
cookie_button = driver.find_element(By.ID, "cookie")   # (By.XPATH, '//*[@id="cookie"]') This works fine too.
money = driver.find_element(By.ID, "money")

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
items_id = [item.get_attribute("id") for item in items]
items_id.pop()  # Popped the last element because last element not show in the game.(Website's problem)

timeout = time.time() + 5
total_click_time = time.time() + 60*5   # 5min

while time.time() < total_click_time:
    cookie_button.click()

    # Every 5 seconds
    if time.time() > timeout:
        # Check current money
        user_money = int(money.text.replace(",", ""))

        # Get the list of item prices everytime price increase each time we buy it.
        item_prices_list = []
        for each_id in items_id:
            item_prices_list.append(int(driver.find_element(By.ID, each_id).text.split("\n")[0].split("-")[1].replace(",", "")))
        # item_prices = [int(driver.find_element(By.ID, each_id).text.split("\n")[0].split("-")[1].replace(",", "")) for each_id in items_id]
        # above is just the list comprehension of above code

        # Compare our price in hand vs the highest priced item we can afford.
        affordable_item_index = 0
        for (each_price) in item_prices_list:
            if user_money > each_price:
                affordable_item_index = item_prices_list.index(each_price)

        # Buy affordable item
        affordable_item = driver.find_element(By.ID, items_id[affordable_item_index])
        affordable_item.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

# Print speed before close
print(driver.find_element(By.ID, "cps").text)

driver.quit()









