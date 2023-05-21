from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
TWITTER_USERNAME = "PythonMusa"
TWITTER_PASSWORD = "PythonMusa6699"
CLICK_WAIT_TIME_IN_SPEED_CHECKER = 50
PROMISED_INTERNET_SPEED = 5.00  # MBPS
INTERNET_PROVIDERS_TWITTER = "@hutchsrilanka"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(PATH))
        self.message = ""
        self.report_need = False

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        sleep(2)

        # Click go button in speedtest
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        print(f"wait {CLICK_WAIT_TIME_IN_SPEED_CHECKER} sec to check your internet connection.")
        sleep(CLICK_WAIT_TIME_IN_SPEED_CHECKER)

        # download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[
        # 3]/div[3]/di' 'v/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.download-speed").text
        # Above xpath also worked just fine

        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-value.upload-speed").text

        self.report_need = False
        if float(download_speed) <= PROMISED_INTERNET_SPEED:
            self.message = f"{INTERNET_PROVIDERS_TWITTER}\nReport Issue\nThe internet very slow speed: " \
                           f"Download {download_speed}Mbps," \
                           f" Upload = {upload_speed}Mbps "
            self.report_need = True
        else:
            self.message = f"{INTERNET_PROVIDERS_TWITTER}\nSpeed is ok\nspeed : Download = {download_speed}" \
                           f"Mbps, Upload = {upload_speed}Mbps"
        # after 5 sec speed site will close automatically
        sleep(5)
        print(f"Your internet Speed is Download {download_speed}Mbps, Upload = {upload_speed}Mbps")

    def tweet(self):
        self.driver.get(TWITTER_URL)
        sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()
        sleep(3)

        # Enter username
        input_field_of_username = self.driver.find_element(By.NAME, "text")
        input_field_of_username.send_keys(TWITTER_USERNAME)
        sleep(1)
        input_field_of_username.send_keys(Keys.ENTER)
        sleep(2)

        # Enter password
        input_field_of_password = self.driver.find_element(By.NAME, "password")
        input_field_of_password.send_keys(TWITTER_PASSWORD)
        sleep(1)
        input_field_of_password.send_keys(Keys.ENTER)
        sleep(3)

        # Tweet the message
        tweet_textbot = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/'
                                                 'div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/d'
                                                 'iv/div/div/div/label/div[1]/div/div/div/div/div/div['
                                                 '2]/div/div/div/div')
        tweet_textbot.send_keys(self.message)
        sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/di'
                                                          'v/div/div/div[3]/div/div[2]/div[1]/div/div/div'
                                                          '/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

        print("Job done")
        sleep(100)
        self.driver.quit()
