# Configuração e Execução

Este arquivo contém instruções para configurar e executar o aplicativo, incluindo a inicialização do banco de dados no Docker, a execução dos testes e a execução do arquivo principal (`main.py`).

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes pré-requisitos instalados em sua máquina:

- Docker: [Instruções de instalação do Docker](https://docs.docker.com/get-docker/)

## Configuração e Instalação

1. **Clone este repositório em sua máquina local:**

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Build do projeto e execução do aplicativo:**

   Para buildar o projeto e executar o aplicativo, siga as etapas abaixo:

   Execute o seguinte comando para buildar o projeto:

   ```bash
   make build
   ```

   Em seguida, execute o comando a seguir para iniciar o aplicativo:

   ```bash
   make run
   ```

## Execução dos Testes

Para executar os testes, utilize o seguinte comando:

```bash
make test
```

## Remoção do Container e Volume

Caso deseje remover o container e volume do Docker, execute o seguinte comando:

```bash
make remove
```

## Estrutura do Banco de Dados

foi utilizado um banco de dados NoSQL MongoDB. O scraping realizado é armazenado em coleções dentro do banco de dados.

## Fluxo do Sistema

O sistema segue os seguintes passos para processar os dados:

1. Iniciar o serviço: Para começar, é necessário executar o comando para iniciar o aplicativo.

2. Scraping inicial: Na primeira execução, o aplicativo realiza um scraping para popular o banco de dados com os dados necessários para as APIs.

3. Agendador de tarefas: O aplicativo utiliza um agendador de tarefas para executar o scraping a cada 24 horas. O scraping é realizado para inserir os dados no banco de dados.

4. APIs disponíveis:
   - **API 1**: Retorna todos os dados com paginação. Você pode acessar a API através do endpoint `/foods/` e especificar a página desejada usando o parâmetro `page`.
   - **API 2**: Retorna os dados correspondentes a um código de barras. Você pode acessar a API através do endpoint `/foods/{barcode}`, substituindo `{barcode}` pelo código de barras desejado.

A aplicação pode ser acessada em `http://localhost:8000/docs`, onde você encontrará informações detalhadas sobre os endpoints e como utilizá-los.