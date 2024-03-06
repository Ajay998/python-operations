import imaplib as imp
import pprint as pp

user = 'krishnaajay998@gmail.com'
app_password = 'hydnwajsllubdybt'
host = 'imap.gmail.com'

imapHostServer = host
imapUserEmail = user
imapPassword = app_password
imapVar = imp.IMAP4_SSL(imapHostServer)

# Login to the email server with credentials
imapVar.login(imapUserEmail, imapPassword)
resp_code, directories = imapVar.list()
for directory in directories:
        directory_name = directory.decode().split('"')[-2]
        directory_name = '"' + directory_name + '"'
        if directory_name == '"[Gmail]"':
            continue
        try:
            resp_code, mail_count = imapVar.select(mailbox=directory_name, readonly=True)
            print("{} - {}".format(directory_name, mail_count[0].decode()))
        except Exception as e:
            print("{} - ErrorType : {}, Error : {}".format(directory_name, type(e).__name__, e))
            resp_code, mail_count = None, None