import requests
import smtplib
from bs4 import BeautifulSoup
from twilio.rest import Client


my_email = "musapython1@gmail.com"
my_password = "ENTERYOUR GENERATED PASSWORD HERE"   # this password get evjmuhullfguaohg from mail  generated
sender_email = "musapython1@yahoo.com "
my_expected_price = 17.5


# whatsapp
Account_SID = "ACc3b4dd6888464ce6dcf3ef0edb2c4d64"  # like username
Auth_Token = "2e02b3cc185c550dec890a8fd05d7db6"  # os.environ.get("AUTH_TOKEN")   # like password

client = Client(Account_SID, Auth_Token)

from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = f"whatsapp:{+PUTYOURPHONENUMBERHERE}"    # +94779------




URL = "https://www.amazon.com/Razer-DeathAdder-Essential-Gaming-Mouse/dp/B094PS5RZQ/ref=sr_1_3?crid=" \
      "1NIQ5LKRH4UOH&keywords=razer+mouse&qid=1676581456&sprefix=razor+mo%2Caps%2C518&sr=8-3"

amazon_headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/109.0.0.0 Safari/537.36",
}

response = requests.get(URL, headers=amazon_headers).text

soup = BeautifulSoup(response, "html.parser")

current_price = float(soup.select_one(".a-offscreen").text.strip("$"))  # just many lines of code in 1 so much easy.

final_message_for_amazon = ""
if current_price <= my_expected_price:
    final_message_for_amazon = f"WoW \nOffer alert The razor mouse is now less than ${my_expected_price}\nHere is the link:-\n{URL}"
elif current_price <= 18:
    final_message_for_amazon = f"The price of razor mouse is slightly reduced \nHere is the link:-\n{URL}"
else:
    final_message_for_amazon = "The price hasn't changed."

client.messages.create(
    body=f"Subject:Amazon price update \n{final_message_for_amazon}",
    from_=from_whatsapp_number,
    to=to_whatsapp_number)

# mail
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=sender_email,
                        msg=f"Subject:Amazon price update \n{final_message_for_amazon}")
