import imapclient
import pyzmail
from datetime import date

##################
select_UID = 11111
##################

conn = imapclient.IMAPClient(host='outlook.office365.com')  # Connection to the email client
conn.login(username='email@email.com', password='password')  # Login to the client

conn.select_folder('INBOX', readonly=True)  # Select the inbox to be read by imapclient

UIDs = conn.search(['SINCE', date(2022, 12, 6)])  # Find the UIDs of the emails back to a certain date
print(UIDs, end='\n\n')

rawMessage = conn.fetch([select_UID], ['BODY[]', 'FLAGS'])  # Fetch a specific message and turn it into a bytes object
# print(rawMessage, end='\n\n')

message = pyzmail.PyzMessage.factory(rawMessage[select_UID][b'BODY[]'])  # Pulls the info from the dictionary

print(message.text_part)
print(message.html_part, end='\n\n')  # Shows if the message includes plaintext and/or html

print(message.get_subject(), end='\n\n')
if message.text_part:
    print(message.text_part.get_payload().decode('UTF-8'))  # Decodes the message in UTF-8 (Universal Text Format)
