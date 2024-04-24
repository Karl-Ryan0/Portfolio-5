import smtplib
from email.mime.text import MIMEText

def test_smtp_connection():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('info.karls.cooking@gmail.com', 'TestPassword')
        server.quit()
        print("SMTP connection test successful")
    except Exception as e:
        print("SMTP connection test failed:", e)

# Test SMTP connection
test_smtp_connection()