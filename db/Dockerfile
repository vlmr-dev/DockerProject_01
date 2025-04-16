# Baseado na imagem oficial do PostgreSQL
FROM postgres:14-alpine

# Define o diretório onde os scripts de inicialização podem ser adicionados
# Qualquer script .sql ou .sh colocado aqui será executado na criação do container
COPY . /docker-entrypoint-initdb.d/

# Porta padrão do PostgreSQL
EXPOSE 5432