# Simulador de Juros Compostos

Um simulador web moderno de juros compostos com projeção gráfica em tempo real. O projeto calcula a evolução patrimonial mês a mês ou ano a ano, discriminando o montante total investido e o acúmulo de juros compostos (o famoso efeito "bola de neve").

Este projeto foi desenvolvido com uma arquitetura desacoplada (Decoupled/SPA), utilizando **FastAPI** no ecossistema Python para o motor de cálculo financeiro e **Angular** com **Chart.js** para uma experiência de usuário fluida e visual.

---

## Funcionalidades

* **Cálculo Preciso:** Simulação exata de juros compostos com aportes mensais recorrentes.
* **Flexibilidade de Taxas:** Suporte para taxas informadas em períodos mensais ou anuais (com conversão automática por taxa equivalente).
* **Gráfico Interativo:** Visualização da linha do tempo da evolução do patrimônio dividido entre Capital Investido e Juros Acumulados através do `Chart.js`.
* **Interface Sob Demanda:** O gráfico e os resultados só aparecem após o primeiro cálculo, mantendo a tela limpa.
* **Dockerizado:** Ambiente totalmente configurado com Docker e Docker Compose para rodar com um único comando.

---

## Tecnologias Utilizadas

### **Back-end**
* [Python 3.11](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) (Framework de alta performance para APIs)
* [Uvicorn](https://www.uvicorn.org/) (Servidor ASGI)
* [Pydantic](https://docs.pydantic.dev/) (Validação de dados e Schemas)

### **Front-end**
* [Angular (Standalone Components)](https://angular.dev/)
* [Chart.js](https://www.chartjs.org/) (Renderização de gráficos interativos)
* TypeScript & HTML5/CSS3 (Flexbox/Grid para centralização de tela)

### **DevOps / Infraestrutura**
* [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

---

## Como Executar o Projeto

A forma mais rápida de rodar a aplicação completa na sua máquina é utilizando o **Docker**.

### **Pré-requisitos**
* Docker instalado
* Docker Compose instalado

### **Passo a Passo**

1. Clone o repositório para a sua máquina:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO

2. Execute o comando do Docker Compose para construir as imagens e iniciar os contêineres:
```
docker compose up --build
````