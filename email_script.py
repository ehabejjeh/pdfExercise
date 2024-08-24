import smtplib
from email.message import EmailMessage


def send_email():
    msg = EmailMessage()
    sender = 'ihab.alajeh@gmail.com'
    msg['From'] = "Ihab Alajeh"
    msg['To'] = 'ehabejjeh@gmail.com'
    msg['Subject'] = 'Greetings'

    msg.set_content('Dear Sir,\n my name is Ihab, and this is a test email.')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        server.login(sender, 'czynkbtfbsfceydr')
        server.send_message(msg)
        server.quit()


if __name__ == '__main__':
    send_email()
