# TP - Intefçage des SGBD avec Python

## SGBD utilisées
- Neo4j 
- Cassandra
- MongoDB 
- Redis 

## Requirements 
- Docker runtime 
- Docker-container 


## Comment l'executé ? 
1. Creer un Environnement virtuelle et installer les dependances 
```zsh

virtualenv <nom-de-votre-environnement-virtuelle>  # creation du virtual environnement 

source /env-name/bin/activate   # activation de l'environnement virtuell 

pip install -r requirements.txt  # installation des dependences 
```

2. Executer avec docker-compose 
```zsh
docker-compose up -d 
```