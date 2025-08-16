# MQTT → RabbitMQ → MongoDB Simulation
Este projeto simula um fluxo de dados em que um dispositivo publica mensagens via MQTT, um cliente valida e processa essas mensagens e, em seguida, envia para uma fila RabbitMQ. Por fim, outro serviço consome a fila e persiste os dados no MongoDB.


## Como testar o projeto

### 1 - Inicie os serviços com o seguinte comando:

``docker compose up -d``

### 2 - depois inicie um container python usando o seguinte comando

``docker run -it --rm --name projeto_teste --network mqtt-to-rabbit_rede -v "$PWD":/server -w /server python:3.13 bash``


### 3 - nesse container crie um ambiente virtual com o comando

``python -m venv venv``

### 4 - ative o ambiente:

``source venv/bin/activate``


### 5 - instale as dependencias

``pip install -r requirements.txt``

### 6 - depois abra mais 2 terminais e rode esse comando em cada um

``docker exec -it projeto_teste bash``

### 7 - ative o ambiente nos containers usando o comando abaixo em cada um

``source venv/bin/activate``

### 8 - primero no seu navegador abra os serviços

**emqx** pra utilizar na web digite a segunte URL: ``localhost:18083``
passe o usuário e senha padrão: ``user:admin senha: public`` e depois clique em skip para não precisar reinserir um novo user e senha


**mongo-express** seguindo a mesma ideia do serviço anterior na web 
digite a URL: ``localhost:8075`` e usurio e senha ``user:admin senha:1234``

rabbitmq: como nos dois anteriores na web passe a URL: localhost:15672 e o usuario e senha ``user:guest senha:guest`` 

### 9 -feito isso em um dos terminais rode o comando

``python mqtt_consumer.py``

podemos observar no **emqx** na web que está rodando no **localhost:18083**
em **all conections** que uma conexão foi inserida


### 10 - depois em um dos terminais e com o container anterior ainda rodando rode o comando

``python publisher_message.py``

nisso podemos observar que ele publicou a mensagem e ja encaminhou ao broker
que enviou pro nosso container que esta rodando o consumidor mqtt
com isso o consumidor valida os dados trata eles e encaminha pra fila do **rabbitmq**.

na web no serviço do rabbitmq que está rodando no ``localhost:8075``
podemos observar no tópico ``Queues and Streams`` que ja foi criado a ``"fila_teste"``
e foi acoplado 3 mensagens nela, pois o publisher está programado para enviar três mensagens,
uma a cada dez segundos.


### 11 - agora no ultimo terminal restante rode o seguinte comando:

``python amqp_consumer.py``

esse comando irá subir o serviço que consumirá da fila do **rabbitmq** e persistirá os dados no banco **MongoDB**
nisso podemos observar ainda na web no rabbitmq que não existe mais mensagens na ``fila_teste``.
com isso iremos ainda na web para o **mongo-express** que está rodando no ``localhost:8075``

ao carregarmos a página podemos observar que o ``banco_teste`` foi inserido
clicando em view, e depois em view collections, podemos observar o hash das mensagens salvas
dando 2 cliques em cada uma podemos observar que a mensagens foi salva com sucesso!