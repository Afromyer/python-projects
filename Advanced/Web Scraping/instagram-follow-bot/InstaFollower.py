from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")

        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self, username):
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Search"]'))
        )

        self.driver.get(f"https://www.instagram.com/{username}")

        followers = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@href, "/followers/")]'))
        )

        followers.click()

    def follow(self):
        time.sleep(3)

        dialog = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div['
                                                    '2]/div/div/div/div/div[2]/div/div/div[3]')

        can_scroll = True
        follower_list = []
        profile_count = 0
        follow_count = 0
        while can_scroll:
            # time.sleep(3)

            follower_list.clear()
            profile_count += 1
            try:
                profile = self.driver.find_element(By.XPATH, f'/html/body/div[6]/div[2]/div/div/div[1]/div/div['
                                                             f'2]/div/div/div/div/div[2]/div/div/div[2]/div['
                                                             f'2]/div/div[{profile_count}]')
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    profile = self.driver.find_element(By.XPATH,
                                                       f'/html/body/div[6]/div[2]/div/div/div[1]/div/div['
                                                       f'2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div['
                                                       f'{profile_count}]')
                except selenium.common.exceptions.NoSuchElementException:
                    print("Everyone followed")
                    exit()

            follow_button = profile.find_element(By.TAG_NAME, "button")
            button_text = follow_button.find_element(By.CSS_SELECTOR, "div > div").text
            if button_text == "Follow":
                follow_count += 1
                time.sleep(1)
                follow_button.click()

            if follow_count == 5:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
                follow_count = 0
