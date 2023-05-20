from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = "C:\Program Files (x86)\chromedriver.exe"
EMAIL_OF_FB = "musapython1@gmail.com"
FB_PASSWORD = "jamesfb123"
TINDER_URL = "https://tinder.com/"


driver = webdriver.Chrome(service=Service(PATH))
driver.get(TINDER_URL)
sleep(1)

driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()
sleep(1)

sleep(1)

facebook_login_link = driver.find_element(By.XPATH, '//*[@id="c-1129896341"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login_link.click()
sleep(8)


# Window management and change to window 2
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)
# sleep(5)
# driver.switch_to.window(base_window)
# print(driver.title)


driver.switch_to.window(fb_login_window)

email_form = driver.find_element(By.XPATH, '//*[@id="email"]')
email_form.send_keys(EMAIL_OF_FB)
password_form = driver.find_element(By.ID, "pass")
password_form.send_keys(FB_PASSWORD)
# before press enter wait few sec to not detect as a bot
sleep(5)
password_form.send_keys(Keys.ENTER)
sleep(5)
print("OK")

# Switch back to window 1
driver.switch_to.window(base_window)
print(driver.title)




sleep(5)


sleep(1000)
driver.quit()




