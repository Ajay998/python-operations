import imaplib as imp
import pprint as pp
import email
from email.header import decode_header

user = 'krishnaajay998@gmail.com'
app_password = 'hydnwajsllubdybt'
host = 'imap.gmail.com'

imapHostServer = host
imapUserEmail = user
imapPassword = app_password
imapVar = imp.IMAP4_SSL(imapHostServer)

# Login to the email server with credentials
imapVar.login(imapUserEmail, imapPassword)
# Mailbox folder where emails are present
imapVar.select('Inbox')
# Searching data through the mail
tmp, data = imapVar.search(None, 'ALL')
# Using for loop to print data
message_id = "<CAKtO42EXjyprmH-QCaxwgfB+m0RoZD2peB8O6Puvdc9RNZandQ@mail.gmail.com>"
subject = "Test daily report data 2024"
search_criteria = f'HEADER Message-ID "{message_id}" SUBJECT "{subject}"'
result, data = imapVar.search(None, search_criteria)
if result == "OK":
    # Get the email ID(s) from the search result
    email_ids = data[0].split()
    print(email_ids)
    for ids in email_ids:
        result, message_data = imapVar.fetch(ids, "(RFC822)")
        if result == "OK":
            print(message_data)
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get("Content-Disposition") is not None:
                        filename = decode_header(part.get_filename())
                        attachment_filename = filename[0][0] if filename[0][1] is None else filename[0][0].decode(filename[0][1])
                        print(attachment_filename)