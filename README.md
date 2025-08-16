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

docker run -it --rm --name projeto_teste --network mqtt-to-rabbit_rede -v "$PWD":/server -w /server python:3.13 bash


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


emqx:
localhost:18083
user:admin senha: public


mongo-express:
localhost:8075
user:admin senha:1234

rabbitmq:
localhost:15672
user:guest senha:guest 

--feito isso em um dos terminais rode o comando

python mqtt_consumer.py

podemos observar no emqx na web que está rodando no localhost:18083
em all conections que uma conexão foi inserida

--depois em um dos terminais e com o container anterior ainda rodando rode o comando

python publisher_message.py

nisso podemos observar que ele publicou a mensagem e ja encaminhou ao broker
que envou pro nosso container que esta rodando o consumidor mqtt
com isso o consumidor valida os dados trata eles e encaminha pra fila do rabbitmq.

na web no serviço do rabbitmq que está rodando no localhost:8075
podemos observar no tópico Queues and Streams que ja foi criado a "fila_teste"
e foi acoplado 3 mensagens nels, pois o publisher está programado para enviar 3 mensagens 
1 a cada 10 segundos

--agora no ultimo terminal restante rodaremos o comando para subir o serviço
que vai consumir da fila e persistir os dados no banco

python amqp_consumer.py

nisso podemos observar ainda na web no rabbitmq que não existe mais mensagens na fila_teste.
com isso iremos ainda na web para o mongo-express que está rodando no localhost:8075

ao carregarmos a página podemos observar que o banco teste foi inserido
clicando em view, e depois em view collections, podemos observar o hash das mensagens salvas
dando 2 cliques em cada uma podemos observar que a mensagens foi salva com sucesso!