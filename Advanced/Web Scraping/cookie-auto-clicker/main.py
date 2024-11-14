import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random

# Add service
service = Service(executable_path="C:/Users/jpjou/bin/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker")
time.sleep(6)
lang_selection = driver.find_element(By.ID, "langSelect-EN")
lang_selection.click()

time.sleep(5)


def get_product_details() -> list:
    products = [
        product for product in driver.find_elements(By.CLASS_NAME, "product")
        if ((product.get_attribute("class")).split(" "))[1] == "unlocked"
    ]
    all_product_details = []
    for i in range(len(products)):
        product_details = (products[i].get_attribute("class")).split(" ")
        product_content = products[i].find_element(By.CLASS_NAME, "content")
        name = product_content.find_element(By.CLASS_NAME, "productName")
        price = product_content.find_element(By.CLASS_NAME, "price")
        price = price.text.replace(",", "")

        amount_owned = product_content.find_element(By.CLASS_NAME, "owned")
        all_product_details.append({
            "product": products[i],
            "is_enabled": product_details[2] == "enabled",
            "price": int(price),
            "name": name.text,
            "own_amount": amount_owned.text
        })

    return all_product_details


def get_upgrade_details():
    upgrades = [
        upgrade for upgrade in driver.find_elements(By.CLASS_NAME, "upgrade")
        if ((upgrade.get_attribute("class")).split(" "))[-1] == "enabled"
    ]

    return upgrades


def click_cookie():
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()


def click_highest_product():
    try:
        products = get_product_details()
    except ValueError:
        print("Error Found")
        pass
    else:
        enabled_products = [product for product in products if product["is_enabled"] == True]
        if len(enabled_products) > 0:
            highest_value = enabled_products[-1]
            highest_value["product"].click()


def click_highest_upgrade():
    current_upgrades = get_upgrade_details()
    try:
        current_upgrades[-1].click()
    except IndexError:
        pass


def get_cookies_per_second():
    cookies_per_second = float(driver.find_element(By.ID, "cookiesPerSecond").text.split(" ")[2])
    cookies_per_second = float(str(cookies_per_second).replace(",", ""))

    return cookies_per_second


TIME_INTERVAL = 0.01
time_passed = 0
cookies_second = 0
while True:
    time_passed += TIME_INTERVAL
    time.sleep(TIME_INTERVAL)
    click_cookie()
    upgrade_delay = 50 + cookies_second
    # Check for upgrades and products every second
    if time_passed >= TIME_INTERVAL * upgrade_delay:
        time_passed = 0
        click_highest_upgrade()
        click_highest_product()
        try:
            cookies_second = get_cookies_per_second()
            print(f"Current upgrade delay: {upgrade_delay}")
        except selenium.common.exceptions.StaleElementReferenceException:
            pass
