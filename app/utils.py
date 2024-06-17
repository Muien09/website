from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app

def send_email(to_email, subject, content):
    message = Mail(
        from_email='your-email@example.com',
        to_emails=to_email,
        subject=subject,
        html_content=content
    )
    try:
        sg = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
        sg.send(message)
    except Exception as e:
        print(str(e))
