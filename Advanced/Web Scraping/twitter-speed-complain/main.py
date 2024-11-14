from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

DOWN_SPEED = 85
UP_SPEED = 85
SERVICE_PROVIDER = "megasurf"
X_USERNAME = "jubermire"
X_PASSWORD = "f-VY@,inNg8,9"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net/")

start_test_button = driver.find_element(By.CLASS_NAME, "start-text")

start_test_button.click()


def value_is_not_nan(element_class, tag_name):
    global driver
    element = driver.find_element(By.CLASS_NAME, element_class)
    return element.get_attribute(tag_name) != "NaN"


WebDriverWait(driver, 60).until(
    lambda d: value_is_not_nan("download-speed", "data-download-status-value")
)

download_speed = float(driver.find_element(By.CLASS_NAME, "download-speed").text)

WebDriverWait(driver, 60).until(
    lambda d: value_is_not_nan("upload-speed", "data-upload-status-value")
)

upload_speed = float(driver.find_element(By.CLASS_NAME, "upload-speed").text)

if download_speed < DOWN_SPEED or upload_speed < UP_SPEED:
    driver.get("https://x.com/i/flow/login")

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, "text"))
    )

    user_input = driver.find_element(By.NAME, "text")
    user_input.send_keys(X_USERNAME)
    user_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(X_PASSWORD)
    password_input.send_keys(Keys.ENTER)

    message = (f"Hey {SERVICE_PROVIDER}, why is my internet speed {download_speed}down/{upload_speed}up "
               f"when I pay for {DOWN_SPEED}down/{UP_SPEED}up?")

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "public-DraftEditor-content"))
    )

    tweet_input = driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
    tweet_input.send_keys(message)
else:
    print("Your internet speed is as advertised")
