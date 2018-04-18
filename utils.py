from main import app, mail, Message


def send_email(subject, message):
    """
    This function sends an email alert to the owner of the application when
    it breaks/is non functional
    @param[in] subject: subject line of email
    @param[in] message: message  of the email
    """
    msg = Message(subject, sender='0505invincible@gmail.com', recipients=['0505invincible@gmail.com'])
    msg.body = message
    try:
        with app.app_context():
            mail.send(msg)
            print("email sent")
        return "mail sent"
    except Exception as ex:
        print(ex)