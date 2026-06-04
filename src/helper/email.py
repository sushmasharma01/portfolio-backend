import os
import smtplib
from email.message import EmailMessage


from dotenv import load_dotenv
import socket


load_dotenv()


OWNER_EMAIL = os.getenv("CONTACT_OWNER_EMAIL", "sushmasharma0116@gmail.com")


def send_contact_email(name: str, email: str, message: str) -> None:
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    sender_email = os.getenv("SMTP_FROM_EMAIL", smtp_user)

    if not smtp_host or not smtp_user or not smtp_password or not sender_email:
        raise RuntimeError("SMTP configuration is missing")

    mail = EmailMessage()
    mail["Subject"] = f"New contact request from {name}"
    mail["From"] = sender_email
    mail["To"] = OWNER_EMAIL
    mail["Reply-To"] = email

    mail.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    mail.add_alternative(
        f"""
        <html>
          <body>
            <h2>New Contact Request</h2>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <div>{message}</div>
          </body>
        </html>
        """,
        subtype="html",
    )

    print("DNS check:", socket.gethostbyname("smtp.sendgrid.net"))

    with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as smtp:
        smtp.set_debuglevel(1)
        smtp.starttls()
        smtp.login(smtp_user, smtp_password)
        smtp.send_message(mail)
