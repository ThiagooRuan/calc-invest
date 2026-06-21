# Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do back-end para o contêiner
COPY . .

# Expõe a porta que o FastAPI usa
EXPOSE 8000

# Comando para rodar a API (usando 0.0.0.0 para aceitar conexões externas ao contêiner)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]