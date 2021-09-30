"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendEmail(message, to, From, password, subject):
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(From, password)
    text = msg.as_string()
    server.sendmail(From, to, text)
    server.quit()

#Hello - the body, if its from a print, remove "".
#"to@gmail.com" - reciever
#"from@gmail.com" - sender
#"password" - pss of the sender (must have less secure app permissions ON, 2FA disabled)
#"Subject" - subject of the mail
SendEmail("Hello", "to@gmail.com", "from@gmail.com", "password", "Subject")

#if function returns a string
SendEmail(GetLatencyFunction(), "to@gmail.com", "from@gmail.com", "password", "Subject")

# Code Block, if using exceptions
EXAMPLE:
except Exception as e:
print(f"exception {e} occurred")
SendEmail(e, "to@gmail.com", "from@gmail.com", "password", "Subject")
quit() # Better to exit if you are using generalized Exceptions though.
"""