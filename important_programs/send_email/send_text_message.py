from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib

def send_email(message, subject_message):
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(message))
        msg['Subject'] = subject_message
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.login('krishnaajay998@gmail.com', 'vjhjtzwvploqraew')
        recipients = ['ajay.krishna@quintetsolutions.com', 'krishnaajay998@gmail.com']
        msg["To"] = ",".join(recipients)
        bcc = ['krishnaajay998@gmail.com', 'ajay.krishna@quintetsolutions.com']
        to_address = recipients + bcc
        server.sendmail('krishnaajay998@gmail.com', to_address, msg.as_string())
        print("Alert mail sent successfully")
    except Exception as e:
        print("Unable to send email due to the loss of network: "+str(e))

message = "This is for testing"
subject_message = "Test Mail1"
send_email(message,subject_message)


