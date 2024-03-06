from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib

body = '''
Hello All,
Please find attached file.
Regards,
CoderzColumn
'''
msg = MIMEMultipart()
msg.attach(MIMEText(body))
msg["Subject"] = "Mail with attachments"