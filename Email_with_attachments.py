#email with attachments like .pdf, .docx, .csv

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# setting smtp server
smtp_port = 587 
smtp_server = "smtp.gmail.com" 

# set up email list
email_from = "abc@gmail.com"
email_list = ["abc1@gmail.com","abc2@gmail.com"]

# Define the password (better to reference externally)
psd = " "  #add the password of google account here

# name the email subject
subject = "New email with attachments!!"

# Define the email function (dont call it email!)
def send_emails(email_list):
    for person in email_list:
        
        # Make the body of the email
        body = f"""
        Hey, Buddy!
        This is the email with attachments.
        I have included my code, which is used to implement this email sending, in this word document.
        """

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['from'] = email_from
        msg['To'] = person
        msg['subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "filename.docx"  #here u can add the file which u want to send it to someone

        # Open the file in python as a binary
        attachment = open(filename,'rb') 

        # Encode as base64
        attachment_package = MIMEBase('application','octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('content-Disposition',"attachment; filename=" + filename)
        msg.attach(attachment_package)

        #cast as string
        text = msg.as_string()

        #connect with Server
        print("connecting to server")
        Connection_server = smtplib.SMTP(smtp_server,smtp_port)
        Connection_server.starttls()
        Connection_server.login(email_from,psd)
        print("successfully connected to server")
        print()

        #send emails to person as list iterated
        print(f"sending email to: {person}...")
        Connection_server.sendmail(email_from,person,text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    Connection_server.close()

# Run the function
send_emails(email_list)



#       THANKS ME LETTER!