from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfIAA1PA7lDM-jHITh7ewNw_856wKsWa3jN6Cm3rnULCrBAyQ/viewform?usp=sf_link"
PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapB" \
      "ounds%22%3A%7B%22west%22%3A-122.56825534228516%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.69560" \
      "22862589%2C%22north%22%3A37.85489581746633%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22re" \
      "gionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afa" \
      "lse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%" \
      "22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2" \
      "C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A300" \
      "0%7D%2C%22price%22%3A%7B%22max%22%3A583963%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%2" \
      "2%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

# -------------------------------------Webscraping using Beautifulsoup

website = requests.get(URL, headers=header).text

soup = BeautifulSoup(website, "html.parser")

results_container = soup.select(".list-card_for-rent a")

# To get all the address kinda hard not impossible it would take soo much time, so I did this.
# to visit all the pages in a loop need to create url and soup according to the page number in url.
top_9_address = []
top_9_links = []
top_9_prices = []

# Address
all_prop_address = []
for x in results_container:
    address = x.text
    if address == "":
        pass
    else:
        all_prop_address.append(address)

for i in range(9):
    top_9_address.append(all_prop_address[i])


# Links
all_links = []
for link in results_container:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

link_list_without_duplicate = []
[link_list_without_duplicate.append(x) for x in all_links if x not in link_list_without_duplicate] # Create a list without duplicate.

for i in range(9):
    top_9_links.append(link_list_without_duplicate[i])


# Price
all_prices = []
prices = soup.select(".property-card-data span")

final_price = ""
for each_price in prices:
    price = each_price.text
    if "+" in price:
        final_price = price.split("+")[0]
        all_prices.append(final_price)
    elif "/" in price:
        final_price = price.split("/")[0]
        all_prices.append(final_price)

for i in range(9):
    top_9_prices.append(all_prices[i])


print(top_9_address)
print(top_9_links)
print(top_9_prices)

# -------------------------------------form filling using Selenium

driver = webdriver.Chrome(service=Service(PATH))
for i in range(9):
    driver.get(GOOGLE_FORM_URL)
    sleep(1)
    # type in address
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    address_input.send_keys(top_9_address[i])
    sleep(0.5)

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(top_9_prices[i])
    sleep(0.5)


    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(top_9_links[i])
    sleep(0.5)

    submit = driver.find_element(By.CSS_SELECTOR, ".NPEfkd")
    submit.click()
    sleep(0.5)
print("job done")
sleep(5)
driver.quit()


