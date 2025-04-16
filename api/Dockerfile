FROM python:3.12-slim

WORKDIR /app

# Copiar e instalar dependências
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expor porta para a API
EXPOSE 8000

# Iniciar API com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]