O projeto tem como objetivo simular um publisher que envia mensagens via MQTT para um cliente responsável por validar e processar os dados recebidos.
Após o tratamento, essas informações são encaminhadas para uma fila no RabbitMQ, onde outro serviço atua como consumidor dessa fila.
Esse consumidor, por sua vez, é responsável por persistir os dados no banco de dados MongoDB

Publisher MQTT: Simula o comportamento de um dispositivo publicando mensagens em um broker MQTT, enviando pacotes para um tópico específico previamente definido.

Cliente MQTT: Se conecta ao broker e inscrever-se no tópico, recebe a mensagem do dispositivo, valida o pacote recebido, se conecta como um publisher do rabbit encaminhando o pacote validado para fila do rabbitmq


Consumidor RabbitMQ: Consome o pacote ja tratado da fila do rabbitmq e persiste os dados no banco de dados MongoDB


# Como testar o projeto

--primeiro rode o comando:

docker compose up -d


--depois inicie um container python usando o seguinte comando

docker run -it --rm --name projeto_teste --network projeto_mqtt_v2_rede -v "$PWD":/server -w /server python:3.13 bash


--nesse container crie um ambiente virtual com o comando

python -m venv venv

--ative o ambiente:

source venv/bin/activate


--instale as dependencias

pip install -r requirements.txt

--depois abra mais 2 terminais e rode esse comando em cada um

docker exec -it projeto_teste bash

--ative o ambiente nos dois container

source venv/bin/activate


--primero no seu navegador abra os serviços

mongo-express:
localhost:8075

rabbitmq:
15672
