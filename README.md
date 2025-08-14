O projeto tem como objetivo simular um publisher que envia mensagens via MQTT para um cliente responsável por validar e processar os dados recebidos.
Após o tratamento, essas informações são encaminhadas para uma fila no RabbitMQ, onde outro serviço atua como consumidor dessa fila.
Esse consumidor, por sua vez, é responsável por persistir os dados no banco de dados MongoDB

[Publisher MQTT]
        │
        ▼

[Cliente MQTT]
 - Recebe mensagem
 - Valida dados
 - Trata/transforma informações
        │
        ▼

[Producer RabbitMQ]
 - Publica dados tratados na fila
        │
        ▼

[Consumer RabbitMQ]
 - Consome mensagens da fila
 - Persiste no MongoDB
        │
        ▼
  
[MongoDB]
 - Armazena os dados


# RabbitMQ
docker run -d -p 5672:5672 -p 15672:15672 --network servicos_rede rabbitmq:3-management

# MongoDB
docker run -d -p 27020:27017 --network servicos_rede mongo:latest

# Mongo Express
docker run -d -p 8075:8081 --network servicos_rede mongo-express:latest

#EMQX
docker run -d --name emqx \
  -p 1883:1883 \    # MQTT TCP
  -p 8883:8883 \    # MQTT TLS
  -p 8083:8083 \    # MQTT WebSocket
  -p 8084:8084 \    # MQTT WebSocket TLS
  -p 18083:18083 \  # Painel de administração
  emqx/emqx:latest
