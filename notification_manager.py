import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:
    def __init__(self):
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
    def send_notification(self,price,dep_code,arrival_code,out_date,in_date):
        message = f"Subject: CHEAP FLIGHT ALERT\n\n ONLY ${price} to fly from {dep_code} to {arrival_code}, on {out_date} to {in_date}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject: Good Morning :) \n\n{message}"
            )