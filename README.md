# Integração API Meteorológica
Este é um projeto em Python 3 que tem como objetivo puxar dados da API do OpenWeatherMap para verificar se a temperatura de uma cidade está abaixo de 30 graus Celsius. Caso a temperatura seja inferior a 30 graus Celsius, o script envia um e-mail de alerta.

## Tecnologias utilizadas
As principais tecnologias utilizadas neste projeto foram:

- Python 3
- Biblioteca requests
- Biblioteca smtplib
- Biblioteca email
- API OpenWeatherMap

### Funcionalidades
As principais funcionalidades deste projeto são:

- Obter informações meteorológicas de uma cidade usando a API do OpenWeatherMap.
- Verificar se a temperatura está abaixo de 30 graus Celsius.
- Enviar um e-mail de alerta caso a temperatura seja inferior a 30 graus Celsius.
- Executar o script continuamente, verificando a temperatura a cada 10 minutos.

## Como utilizar
Para utilizar este projeto, você precisa seguir os seguintes passos:

Faça o download ou clone deste repositório em sua máquina local.
Instale as bibliotecas necessárias listadas no arquivo requirements.txt.
Abra o arquivo config.py e configure as variáveis API_KEY, CITY_NAME, FROM_EMAIL, FROM_PASSWORD, TO_EMAIL de acordo com suas credenciais e preferências.
Execute o arquivo main.py usando o comando python3 main.py.
O script será executado continuamente, verificando a temperatura da cidade a cada 10 minutos. Caso a temperatura esteja abaixo de 30 graus Celsius, um e-mail de alerta será enviado.



### Demonstração da aplicação




![codigo2](https://user-images.githubusercontent.com/127349318/230668236-57c99546-2cd8-4a49-b5d9-97fc22aebecf.JPG)


![rodando](https://user-images.githubusercontent.com/127349318/230668208-654b976f-f8e2-4116-a39b-77ce18cfbdc1.JPG)

![Email_enviado](https://user-images.githubusercontent.com/127349318/230668192-f44da87d-6830-4e9d-8e21-f388048f2f1d.JPG)



### Autor

Luiz Otávio Nunes Cidade
