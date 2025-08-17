# MQTT → RabbitMQ → MongoDB Simulation
Este projeto simula um pipeline de processamento de dados composto por múltiplos serviços integrados.
Um dispositivo simulador publica mensagens via MQTT, que são recebidas por um cliente responsável pela validação e processamento. Após o tratamento, os dados são encaminhados para uma fila no RabbitMQ, onde um consumidor dedicado os processa e realiza a persistência no MongoDB.


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

### Acessando o painel do EMQX
Para utilizar o **EMQX** via navegador, acesse:
http://localhost:18083

Credenciais padrão de acesso:
- **Usuário:** `admin`  
- **Senha:** `public` 

Após o login, clique em **Skip** para pular a configuração de novo usuário e senha.

### Acessando o Mongo Express

Para utilizar o **Mongo Express** via navegador, acesse:
http://localhost:8075

Credenciais padrão de acesso:
- **Usuário:** `admin`  
- **Senha:** `1234`

Após o login, você terá acesso à interface web para explorar os bancos de dados e coleções.

### Acessando o RabbitMQ

Para utilizar o **RabbitMQ** via navegador, acesse:
http://localhost:15672

Credenciais padrão de acesso:
- **Usuário:** `guest`  
- **Senha:** `guest`

Após o login, você poderá gerenciar filas, exchanges e monitorar as mensagens do RabbitMQ.

### 9 -feito isso em um dos terminais rode o comando

``python mqtt_consumer.py``

Podemos observar no **EMQX**, acessando a interface web em `http://localhost:18083`, que há uma conexão ativa.  
Em **All Connections**, é possível verificar que uma conexão foi registrada com sucesso.


### 10 - depois em um dos terminais e com o container anterior ainda rodando rode o comando

``python publisher_message.py``

Após a publicação da mensagem pelo dispositivo simulador, ela é encaminhada para o **broker MQTT** e recebida pelo **consumidor MQTT** que está rodando em nosso container.  
O consumidor **valida e processa os dados**, encaminhando-os para a fila no **RabbitMQ**.  

Na interface web do RabbitMQ (acessível em `http://localhost:15672`), em **Queues and Streams**, é possível observar que a fila `"fila_teste"` foi criada.  
Além disso, como o publisher está programado para enviar **três mensagens, uma a cada dez segundos**, é possível ver que três mensagens já foram adicionadas à fila.


### 11 - agora no ultimo terminal restante rode o seguinte comando:

``python amqp_consumer.py``

Este comando inicia o serviço que consome mensagens da fila do **RabbitMQ** e realiza a **persistência dos dados no MongoDB**.  

Na interface web do RabbitMQ, é possível observar que a fila `fila_teste` **não contém mais mensagens**, indicando que o consumidor processou todas elas.  

Em seguida, acessando o **Mongo Express** (`http://localhost:8075`), podemos verificar que o **banco `banco_teste`** foi criado.  
Clicando em **View** e depois em **View Collections**, é possível visualizar os hashes das mensagens salvas.  
Dando dois cliques em cada registro, confirmamos que as mensagens foram **persistidas com sucesso**.
