# Usa uma imagem oficial estável do Node.js
FROM node:20

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de pacotes primeiro para aproveitar o cache de camadas
COPY package*.json .

# Instala as dependências do Angular
RUN npm install

# Copia o resto do código do front-end
COPY . .

# Expõe a porta padrão do Angular
EXPOSE 4200

# Comando para rodar o servidor de desenvolvimento do Angular público
CMD ["npm", "run", "start", "--", "--host", "0.0.0.0", "--poll", "2000"]