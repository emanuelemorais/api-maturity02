# Api Maturity 02

## Emanuele Lacerda Morais Martins
API contruída durante avaliação 1 do módulo 10 de Engenharia da Computação.

## Como rodar a API
> Importante: É necessário ter Git e Docker configurado na máquina

1. Clone esse repositorio executando o comando abaixo:

```
git clone https://github.com/emanuelemorais/api-maturity02.git
```
2. Entre no diretório `api-maturity02` e execute o comando abaixo:

 ```
docker compose up
```

## Teste da API

Existe um aequivo chamado `Insomnia.json` que possui uma collection para testar a API. É possível importa-lá no Insomnia para realizar o teste dos endpoints.

## Endpoints construidos

`POST http://127.0.0.1:8000/novo`: Salva nova informação
`GET http://127.0.0.1:8000/pedidos`: Retorna todos os pedidos registrados
`GET http://127.0.0.1:8000/pedidos/<id>`: Retorna pedido por ID de salvamento
`PUT http://127.0.0.1:8000/pedidos/<id>`: Edita pedido por ID de salvamento
`DELETE http://127.0.0.1:8000/pedidos/<id>`: Deleta pedido por ID de salvamento

### Modelo JSON

```
{
	"name": <nome>,
  "email": <email>,
  "description": <descrição>"
}
```

## Diretório / Arquivos

```
api-manurity02
├── database
│   └── migration.json
├── compose.yaml
├── Dockerfile
├── Insomnia.json
├── main.py
├── README.md
├── requirements.txt
```

- migration.json: Aquivo que contem as migrações do banco de dados
- compose.yaml: Arquivo que orquestra os containers.
- Dockerfile:  Arquivo que contém as instruções que definem como construir uma imagem Docker.
- Insomnia.json: Coleção de Insomnia para testar a API.
- main.py: Arquivo principal para execução da API.
- README.md: Este arquivo.
- requirements.txt: Bibliotecas necessárias para funcionamento do sistema.
