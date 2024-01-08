import imaplib
import email
import re
from email.message import Message
from time import time

user = 'krishnaajay998@gmail.com'
app_password = 'hydnwajsllubdybt'
host = 'imap.gmail.com'

key_word = "Split bills instantly on Freecharge!"

try:
    imap = imaplib.IMAP4_SSL(host)
    imap.login(user, app_password)
    imap.select('Inbox')
    typ, data = imap.search(None, 'ALL')
    total = len(data[0].split())
    email_ids = data[0].split()
    for uid in data[0].split():
        print("uid: "+str(uid))
        tmp, data = imap.fetch(uid, '(RFC822)')
        # print('Message %s\n%s\n' % (num, data[0][1]))
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        subject = email_message['Subject']
        print("Your subject: "+str(email_message['Subject']))
        if key_word in subject:
            print("Got key..")
            result = imap.copy(uid,'BusinessEmails')
            if result[0] == 'OK':
                print("Going to delete..")
                imap.store(uid, '+FLAGS', '\\Deleted')
                imap.expunge()
            else:
                print("Unable to copy the message")
    imap.logout()

except Exception as e:
    print("Something issue in sending the email: "+str(e))







