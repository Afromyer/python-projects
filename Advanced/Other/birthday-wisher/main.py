import pandas as pd
import smtplib
import random
import os
import datetime as dt

MY_EMAIL = "jpjoubert2006@gmail.com"
MY_PASSWORD = os.getenv("GMAIL_APP_PASSW")

# Retrieve the current date
current_date = dt.datetime.now()
# Load the birthday data from "birthdays.csv"
birthday_data = pd.read_csv("birthdays.csv")
# Store all the data of current birthdays
current_birthdays = birthday_data[(birthday_data.month == current_date.month) & (birthday_data.day == current_date.day)]

letter_files = os.listdir("./letter_templates/")

# Check if there are people who have a birthday on the current date
if len(current_birthdays) > 0:
    # Loop through all the people who have a birthday
    for index, row in current_birthdays.iterrows():
        # Get a random letter from the array of letters stored in "letter_templates"
        random_letter = random.choice(letter_files)

        # Load the randomly picked letter and save it to a variable
        with open(f'./letter_templates/{random_letter}') as letter_file:
            letter_content = letter_file.read()
            custom_letter = letter_content.replace("[NAME]", row["name"])

        # Send the letter to the relevant email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject:Happy Birthday!\n\n{custom_letter}")
else:
    print("No birthdays today")
