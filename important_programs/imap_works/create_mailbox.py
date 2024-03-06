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
resp_code, response = imapVar.create(mailbox="ELITMUS_2")
resp_code, directories = imapVar.list()

print("\nResponse Code : {}".format(resp_code))

print("========= List of Directories =================\n")
for directory in directories:
    print(directory.decode())
