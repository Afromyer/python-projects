from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+19472227091"

# Enter your verified Twilio number
TWILIO_VERIFIED_NUMBER = "+27680495232"

APP_PASSWORD = "rwpmavsbnefgxccw"

my_email = "jpjoubert2006@gmail.com"
my_password = APP_PASSWORD


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        self.client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
            body=message
        )
        print("Notification sent to Client")

    def send_email(self, to_address, message):
        with smtplib.SMTP("smtp.gmail.com") as host:
            host.starttls()
            host.login(user=my_email, password=my_password)
            host.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:Flight Deal Found\n\n{message}")
        print(f"Email sent to {to_address}")
