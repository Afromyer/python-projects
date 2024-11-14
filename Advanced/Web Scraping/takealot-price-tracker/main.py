from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from smtplib import SMTP
import os

MY_EMAIL = "jpjoubert2006@gmail.com"
MY_PASSWORD = os.getenv("GMAIL_APP_PASSW")

product_url = input("Enter the product url: ")
budget_price = input("Enter your budget price for the product: ")

try:
    budget_price = float(budget_price)
except ValueError:
    raise Exception("Invalid format")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(product_url)
    page.wait_for_load_state("networkidle")
    html_content = page.content()
    browser.close()


def send_email(recipient, message):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(MY_EMAIL, recipient, msg=f"Subject:Takealot Price Alert!!\n\n{message}")
    print("Email was sent successfully")


soup = BeautifulSoup(html_content, "html.parser")

prices = soup.select(selector=".buybox-offer-module_single-item_18a_g .currency-module_currency_29IIm")
product_title = (soup.select(selector=".product-title h1"))[0].getText()
print(product_title)

price = ""
if prices:
    price = prices[0].getText()
else:
    print("No price found")
    exit()

num_price = float((price.split(" ")[1]).replace(",", "."))

if num_price <= budget_price:
    send_email(recipient=MY_EMAIL, message=f"{product_title} now R{num_price}\n{product_url}")

