import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'pcraqadmin@paictasa.africa'
receiver_email = 'simamkelembu5@gmail.com'
subject = 'Example Subject'
message = 'This is the body of the email.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration
smtp_server = 'smtp.paictasa.africa'
smtp_port = 587
smtp_username = 'pcraqadmin@paictasa.africa'
smtp_password = '#Prbh455$3@!*Jhk'

# Create an SMTP client and establish a connection
smtp_client = smtplib.SMTP(smtp_server, smtp_port)
smtp_client.starttls
