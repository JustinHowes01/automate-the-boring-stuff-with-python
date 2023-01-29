import smtplib

conn = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)  # Creation of the variable that will make the connection

print(conn.ehlo())  # Returns a tuple. If it starts with a code beginning with "200", the connection was successful
print(conn.starttls(), end='\n\n')  # Starts encryption so a password can be sent safely when logging in

conn.login(user='email@email.com', password='password')  # Login (obviously)

conn.sendmail(
    from_addr='email@email.com',
    to_addrs='email@email.com',
    msg='Subject: So long...\n\n'
        'Dear Justin,\n'
        'So long, and thanks for all the fish\n\n'
        '-Justin'
)
print('Email Sent Successfully', end='\n\n')

print(conn.quit())
