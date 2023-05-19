from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
WEBSITE_LINK = "https://www.linkedin.com/jobs/search/?currentJobId=3446653219&f_AL=true&geoId=103456484&keyword" \
               "s=Python%20developer&location=Colombo%20District%2C%20Western%20Province%2C%20Sri%20Lanka&refresh=true"
Linkedin_username = "Your Username "   # musapython1@gmail.com
Linkedin_fake_password = "Your password"  # python6699

EACH_CLICK_DELAY = 5

driver = webdriver.Chrome(service=Service(PATH))
driver.get(WEBSITE_LINK)

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()

driver.find_element(By.ID, "username").send_keys(Linkedin_username)
password_form = driver.find_element(By.ID, "password")
password_form.send_keys(Linkedin_fake_password)
password_form.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click() # This works fine too
time.sleep(40)

print("going to click in 3 sec")
time.sleep(3)

# new
jon_names_list = driver.find_elements(By.CSS_SELECTOR, "li .job-card-container--clickable")
print(len(jon_names_list))

for each_job in jon_names_list:
    # click each jobs
    each_job.click()
    time.sleep(EACH_CLICK_DELAY)

    # save those jobs if not already saved.
    save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_text = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/'
                                              'div[1]/div[1]/div[3]/div/button/span[1]').text
    if save_text == "Save":
        save.click()
    time.sleep(2)

    # Scroll to bottom of that job
    scroll = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div')  # find that section[2] is what I need.
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
    time.sleep(EACH_CLICK_DELAY)

    # Follow that company if not already following.
    follow = driver.find_element(By.CSS_SELECTOR, ".follow")
    follow_text = follow.get_attribute("aria-label")
    if follow_text == "Follow":
        follow.click()
    time.sleep(EACH_CLICK_DELAY)

print("Done")
time.sleep(5)
driver.quit()
