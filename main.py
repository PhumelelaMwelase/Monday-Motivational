import random
import smtplib
import datetime as dt
import os

from_email = os.environ.get("FROM_MAIL")
password = os.environ.get("TOKEN")
to_email = os.environ.get("TO_MAIL")


now = dt.datetime.now()
today = now.weekday()
used_quotes = []

if now.weekday() == 1:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        send_quote = random.choice(quotes)
        if send_quote in used_quotes:
            send_quote = random.choice(quotes)
        elif len(quotes) == 0:
            quotes = used_quotes
            used_quotes = []
            send_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Monday Motivational Quote\n\n{send_quote}"
        )
