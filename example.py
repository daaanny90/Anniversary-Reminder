stafrom reminder import *

big_date = 'd/mm/yyyy' #date when you first met each other, format is m/d/y
big_day = 00 #day of the month when you want to send the message, format is dd
email_sender = 'email@test.com' #your email address
email_receiver = 'email@test.com' #your partner email address
smtp_server = 'smtp.test.com:555' #server and port of your email provider. A full list can be found here: https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html
message_from = 'Your name' #name that your partner will read as sender of email
email_subject = 'subject' #subject of email
email_password = 'password' #your email password

#every day at 10:00 the program will check if is the right day to send the message
schedule.every().day.at("10:00").do(job_func, big_day, big_date, email_sender, email_receiver, smtp_server, message_from, email_subject, email_password)

while True:
    schedule.run_pending()
    time.sleep(1)

    #<div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>