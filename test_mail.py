import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "andy19968579@gmail.com"
receiver = ["andy70582@yahoo.com.tw","happy220909@icloud.com"]
PW = "apgz tdoi gkbb phvz"

for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"]=i
    msg["Subject"] = Header("test send email","utf-8").encode()

    body = "Hello this is test email sent using Python\nHow are you?"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,PW)
        server.sendmail(sender,i,msg.as_string())
print("Email sent successfully!")
