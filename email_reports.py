import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configurations
    sender_email = "shashank.karigowda@gmail.com"
    receiver_email = "shashank.karigowda@gmail.com"
    password = "your_email_password"  # Enter your email password here
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Report"

    # Add message body
    body = "This is your daily report."
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

def main():
    # Schedule the email to be sent daily at 12:20 PM
    schedule.every().day.at("12:20").do(send_email)

    # Keep the script running indefinitely
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()

