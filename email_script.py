import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

def send_email():

    html = Template(Path("index.html").read_text())
    substitute = html.substitute({"name": "Sally", "amount" : "500000$"})

    msg = EmailMessage()
    sender = 'ihab.alajeh@gmail.com'
    msg['From'] = "Ihab Alajeh"
    msg['To'] = 'ehabejjeh@gmail.com'
    msg['Subject'] = 'Greetings'

    msg.set_content(substitute, "html")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        server.login(sender, 'czynkbtfbsfceydr')
        server.send_message(msg)
        server.quit()


if __name__ == '__main__':
    send_email()
