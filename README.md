# Anniversary Reminder :couple_with_heart:

This is a simple reminder, written in Python, to send every month an email with a love quote to your partner, with the exact amount of time that you are toghether.

The reminder is written in order to run on a server (you can use the free tier of AWS for example)

# Installation :green_heart:

First of all you have to install some required modules:
```
pip install requests
pip install json
pip install smtplib
pip install schedule
pip install time
pip install datetime
```

After that you can change the settings in `example.py`:

```
big_date = 'd/m/yyyy' #date when you first met each other
big_day = dd #day of the month when you want to send the message
email_sender = 'test@email.com' #your email address
email_receiver = 'tes@email.com' #your partner email address
smtp_server = 'smtp.test.com:555' #server and port of your email provider. A full list can be found here: https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html
message_from = 'A nice name' #name that your partner will read as sender of email
email_subject = 'subj' #subject of email
email_password = 'password' #your email password
```

If everything is correct, just start your reminder with:
```
python example.py
```

The result will be something like this:

picture

# Customization :blue_heart:
If you want to change the content of the message, the picture or something else, just modifiy the file `reminder.py`.
