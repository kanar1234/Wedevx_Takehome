import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Utility to send email to designated user
def send_email(to_email: str, subject: str, body: str):
    from_email = "first.last@example.com"
    password = "password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
