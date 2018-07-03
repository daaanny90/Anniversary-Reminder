import requests
import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import email.message
import schedule
import time
import datetime

def sendEmail(body,email_sender,email_receiver,smpt_server,message_from,email_subject,email_password):
    emailSender=email_sender
    emailReceiver=email_receiver
    password=email_password
    smtpServer=smtplib.SMTP_SSL(smpt_server)

    msg = email.message.Message()
    msg['From'] = message_from
    msg['To'] = emailReceiver
    msg['Subject'] = email_subject

    email_content = """<html>
                        <head>
                                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                                <title>Tutsplus Email Newsletter</title>
                                        <style type="text/css">
                                        </style>
                                </head>
                        <body>
                                <img src="https://www.publicdomainpictures.net/pictures/90000/velka/red-scribble-heart.jpg#.WzpAPCDkbpQ.link" style="display: block; margin: 0 auto; width: 25%;">
                                <p style="font-style: italic;">""" + body + """</p>
                        </body>
                </html>"""

    msg.add_header('Content-Type','text/html')
    msg.set_payload(email_content)
    server = smtpServer
    server.login(emailSender, password)

    text = msg.as_string()
    server.sendmail(emailSender, emailReceiver, text)
    server.quit()

def job_func(bigDay,anniversaryDate,email_sender,email_receiver,smpt_server,message_from,email_subject,email_password):
    today = datetime.date.today()
    monthDay = int(today.strftime('%d'))

    if (monthDay == bigDay):

        day = str(monthDay)

        print('today is the ' + day)

        response = requests.get('http://quotes.rest/qod.json?category=love')
        data = response.json()

        quote = data['contents']['quotes'][0]['quote']
        author = data['contents']['quotes'][0]['author']

        start = datetime.datetime.strptime(anniversaryDate,'%m/%d/%Y')
        today = datetime.datetime.now()
        type(today-start)

        years = str((today-start).days/365)
        month = str(int((((today-start).days/365.0)-(today-start).days/365)*12))

        if (month == '0' or month == '12' ):
                message = quote + "\n (" + author + ") \n \n I love you since " + years + " years <3"
        else:
                message = quote + "\n (" + author + ") \n \n I love you since " + years + " years and " + month + " month <3"

        print(message)
        sendEmail(message,email_sender,email_receiver,smpt_server,message_from,email_subject,email_password)
        print('message sent!')

    else:
        today = str(today)
        print('not the right day! ' + today)