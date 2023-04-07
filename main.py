import requests
import smtplib
from email.mime.text import MIMEText
import time

def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    return temperature, description

def send_email(from_addr, to_addr, password, message):
    msg = MIMEText(message)
    msg['Subject'] = 'Alerta de clima'
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

API_KEY = '910f5c6d40d3e338bc5a3d25a071d8f2'
CITY_NAME = 'Petrópolis'
FROM_ADDR = 'luizito.dev@gmail.com'
TO_ADDR = 'luiz.cnpoker@gmail.com'
PASSWORD = 'xlcauuddnunyxtcd'

while True:
    temperature, description = get_weather(API_KEY, CITY_NAME)
    print(f"Temperatura: {temperature} graus Celsius")
    print(f"Descrição: {description}")

    if temperature < 30:
        message = f"A temperatura está abaixo de 30 graus Celsius: {temperature} graus Celsius"
        send_email(FROM_ADDR, TO_ADDR, PASSWORD, message)

    time.sleep(600) # Espera 10 minutos