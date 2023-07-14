# how to send an email text 

import smtplib

my_mail = "abc@gmail.com"
pass_code = "your_password"  # Add the password of your Google account here

# Establish a connection to the SMTP server
connection = smtplib.SMTP("smtp.gmail.com", 587)

# Enable transport layer security (TLS)
connection.starttls()

# Login to your email account
connection.login(my_mail, pass_code)

# Compose the email
mail_content = """
Enter the content here
"""

sender = my_mail
receiver = "receiver@gmail.com"
subject = "Test Email"

# Construct the email message
message = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{mail_content}"

try:
    # Send the email
    connection.sendmail(from_addr=sender, to_addrs=[receiver], msg=message)
    print("Email sent successfully!")
except Exception as e:
    print("Something went wrong while sending the email:", e)

# Close the connection
connection.close()
