'''birthday wisher program by Hamza Kyamanywa 2021/01/27'''
import pandas as pd
import datetime as dt
import smtplib
import random

my_mail = 'hamzamycode@gmail.com'
my_password = 'nokiaham'
gmail_server = 'smtp.gmail.com'

letters = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']


def send_message(email, name):
    letter_doc = random.choice(letters)
    with open(letter_doc, 'r') as letter:
        message = letter.read()
        message = message.replace('[NAME]', name)
    with smtplib.SMTP(gmail_server) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(from_addr=my_mail, to_addrs=email, msg=f'Subject: Happy Birthday\n\n' + message)


today = dt.datetime.now()
current_month = today.month
current_day = today.day
birthdays_df = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays_df.to_dict('records')

for person in birthdays_dict:
    print(person)
    if person['month'] == current_month and person['day'] == current_day:
        send_message(person['email'], person['name'])
        print(f'finished sending email to {person["name"]}')
