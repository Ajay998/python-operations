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
# Mailbox folder where emails are present
imapVar.select('Inbox')
# Searching data through the mail
tmp, data = imapVar.search(None, 'ALL')
# Using for loop to print data
for n in data[0].split():
    tmp, data = imapVar.fetch(n, '(RFC822)')
    print('Message: {0}\n'.format(n))
    pp.pprint(data[0][1])
    
imapVar.close()