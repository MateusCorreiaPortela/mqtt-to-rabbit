#RABBITMQ
RABBIT:
docker run -d \
  --name rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  --network servico_rede \
  rabbitmq:3-management


# MongoDB
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  --network servico_rede \
  mongo:latest

# Mongo Express
docker run -d \
  --name mongo-express \
  -p 8081:8081 \
  --network servico_rede \
  mongo-express:latest

#EMQX
docker run -d --name emqx \
  -p 1883:1883 \    # MQTT TCP
  -p 8883:8883 \    # MQTT TLS
  -p 8083:8083 \    # MQTT WebSocket
  -p 8084:8084 \    # MQTT WebSocket TLS
  -p 18083:18083 \  # Painel de administração
  emqx/emqx:latest
