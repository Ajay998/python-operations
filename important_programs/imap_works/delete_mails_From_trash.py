import imaplib as imp
import pprint as pp
import email
user = 'ajay.krishna@quintetsolutions.com'
app_password = 'bhkoadzorwyxebaj'

host = 'imap.gmail.com'

imapHostServer = host
imapUserEmail = user
imapPassword = app_password
imapVar = imp.IMAP4_SSL(imapHostServer)
imapVar.login(imapUserEmail, imapPassword)

# imapVar.store("1:*",'Invalid mail', '\\Trash')
imapVar.select(mailbox='"[Gmail]/Trash"', readonly=False)
imapVar.store("1:*", '+FLAGS', '\\Deleted')
imapVar.expunge()
imapVar.close()  # close and logout the connection
imapVar.logout()