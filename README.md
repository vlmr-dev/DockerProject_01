# Analytics Stack com Docker-compose

Este projeto utiliza **Docker-compose** para orquestrar três serviços principais:  
um banco de dados PostgreSQL, uma API para acesso aos dados e um dashboard interativo para visualização.

---

## Estrutura dos Serviços

### 1. **PostgreSQL (db)**

Banco de dados responsável por armazenar os dados utilizados pela aplicação.

- **Imagem:** `v1mr/postgres:1.0.0`  
- **Porta:** `5432`  
- **Variáveis de Ambiente:** Carregadas do arquivo `.env`  
- **Volume:** Persistência dos dados em `postgres_data`  
- **Healthcheck:** Verifica a disponibilidade com `pg_isready`

---

### 2. **API de Dados (api)**

Camada intermediária entre o banco e o dashboard, responsável por expor os dados via HTTP.

- **Imagem:** `v1mr/api:1.0.0`  
- **Porta:** `8000`  
- **Variáveis de Ambiente:** Usa `DATABASE_URL` para conectar-se ao banco  
- **Dependência:** Aguarda o banco estar saudável antes de iniciar

---

### 3. **Dashboard (dashboard)**

Interface visual da aplicação, acessível via navegador.

- **Imagem:** `v1mr/dashboard:1.0.0`  
- **Porta:** `8501`  
- **Variável de Ambiente:** Define o endereço da API (`API_URL`)

---