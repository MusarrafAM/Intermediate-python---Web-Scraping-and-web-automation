from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common import ElementClickInterceptedException


insta_user_name = "musainstapy"
insta_password = "Musapy6699"
similar_account_name = "chefsteps"

similal_account_url = f"https://www.instagram.com/{similar_account_name}/"  # No need to change this.
# similar_url = "https://www.instagram.com/chefsteps/"  # We can do this in one step


PATH = "C:\Program Files (x86)\chromedriver.exe"
INSTA_LOGIN_URL = "https://www.instagram.com/"

# Create driver and visit site
driver = webdriver.Chrome(service=Service(PATH))
driver.get(INSTA_LOGIN_URL)
sleep(5)

driver.find_element(By.NAME, "username").send_keys(insta_user_name)
sleep(1)
password_textbox = driver.find_element(By.NAME, "password")
password_textbox.send_keys(insta_password)
sleep(1)
password_textbox.send_keys(Keys.ENTER)
# driver.find_element(By.NAME, "password").send_keys(insta_password, Keys.ENTER)  # We can use like this as well
sleep(5)

# Go the relevant insta account
driver.get(similal_account_url)
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "followers").click()
sleep(5)


# # Scroll
f_body = driver.find_element(By.XPATH, "//div[@class='_aano']")  # I got line of code from q/a if u dont get by x path
#                                                                       No Problem.
for i in range(1):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)
    sleep(3)


# Follow and if already following or requested cansel and back to popup.
list_of_people = driver.find_elements(By.CSS_SELECTOR, '._aano button')  # _aano this is to select the popup window.
for each_people in list_of_people:
    try:
        each_people.click()
        sleep(2)
    except ElementClickInterceptedException:
        print("inside exeption")
        cancel_button = driver.find_element(By.CSS_SELECTOR, "._a9-v ._a9_1")
        #                         _a9-v is the class to select this popup. and _a9_1 is hte class to find cancel button.
        cancel_button.click()


print("finished")
sleep(10)
driver.quit()
