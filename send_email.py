import smtplib as sm, ssl

host = 'smtp.gmail.com'
port = 465

username = 'krishtanwar458@gmail.com'
password = 'olxh pjfb sxmi jrvv'

receiver = 'krishtanwar458@gmail.com'
context = ssl.create_default_context()

message = '''\
Subject: Hi!
Hi!, how are you'''

with sm.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)