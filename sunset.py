import requests
from datetime import datetime
import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_sunset():

    request_parameters = {
        'lat': 52.229675,
        'lng': 21.012230,
        'date': '2021-12-23',
        'formatted': 0
        }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=request_parameters)
    response.raise_for_status()
    data = response.json()
    sunset = data['results']['sunset'].split('T')[1]

    return sunset
    

def is_night():

    sunset = get_sunset()
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    
    if current_time >= sunset:
        return "It's dark."
    else:
        return str(current_time) + ' it\'s still a day.'


def send_mail(email_address):
    sender = 'nguyen.szymonn@gmail.com'
    password = getpass('Password: ')
    receiver = email_address

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Is it dark already?'
    message.attach(MIMEText(is_night(), 'plain'))
    text = message.as_string()

    session = smtplib.SMTP('smtp.gmail.com')
    session.starttls()
    session.login(sender, password=password)
    session.sendmail(sender, receiver, text)

    print('Mail sent')

send_mail('nguyentienanh341@gmail.com')
