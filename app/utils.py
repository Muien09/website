from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app, jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models import User

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

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or not user.is_admin:
            return jsonify({'message': 'Admins only!'}), 403
        return fn(*args, **kwargs)
    return wrapper
