import imaplib as imp
import pprint as pp

user = 'krishnaajay998@gmail.com'
app_password = 'hydnwajsllubdybt'
host = 'imap.gmail.com'

imapHostServer = host
imapUserEmail = user
imapPassword = app_password
imapVar = imp.IMAP4_SSL(imapHostServer)
imapVar.login(imapUserEmail, imapPassword)
resp_code, directories = imapVar.list(pattern="*Coursera*")
for directory in directories:
    print(directory.decode())