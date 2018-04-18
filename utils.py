from main import app, mail, Message


def send_email(subject, message):
    """
    This function sends an email alert to the owner of the application when
    it breaks/is non functional
    @param[in] subject: subject line of email
    @param[in] message: message  of the email
    """
    msg = Message(subject, sender=app.config.get('SENDER'), recipients=app.config.get('RECIPIENT'))
    msg.body = message
    with app.app_context():
        mail.send(msg)
    return "mail sent"