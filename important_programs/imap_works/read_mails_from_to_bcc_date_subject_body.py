import imaplib as imp
import pprint as pp
import email
user = 'krishnaajay998@gmail.com'
app_password = 'hydnwajsllubdybt'
host = 'imap.gmail.com'

imapHostServer = host
imapUserEmail = user
imapPassword = app_password
imapVar = imp.IMAP4_SSL(imapHostServer)
imapVar.login(imapUserEmail, imapPassword)
resp_code, mail_count = imapVar.select(mailbox="BusinessEmails", readonly=True)
resp_code, mail_ids = imapVar.search(None, "ALL")
print("Mail IDs : {}\n".format(mail_ids[0].decode().split()))
# for mail_id in mail_ids[0].decode().split()[-2:]:
for mail_id in mail_ids[0].decode().split()[-2:]:
        print("================== Start of Mail [{}] ====================".format(mail_id))

        resp_code, mail_data = imapVar.fetch(mail_id, '(RFC822)') ## Fetch mail data.

        message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data
        print("From       : {}".format(message.get("From")))
        print("To         : {}".format(message.get("To")))
        print("Bcc        : {}".format(message.get("Bcc")))
        print("Date       : {}".format(message.get("Date")))
        print("Subject    : {}".format(message.get("Subject")))

        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    print("Body:")
                    print(body)
        else:
            body = message.get_payload(decode=True).decode()
            print("Body:")
            print(body)

        print("================== End of Mail [{}] ====================\n".format(mail_id))

    ############# Close Selected Mailbox #######################
imapVar.close()