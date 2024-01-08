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

print("\nDeleting Mailbox : Myntra")

resp_code, response = imapVar.delete(mailbox="ELITMUS_2")

print("Response Code : {}".format(resp_code))
print("Response      : {}".format(response[0].decode()))