import smtplib as sm, ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'krishtanwar458@gmail.com'
    password = os.getenv("PASSWORD")
    
    receiver = 'krishtanwar458@gmail.com'
    context = ssl.create_default_context()

    with sm.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)