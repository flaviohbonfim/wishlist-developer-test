# Wishlist Developer Test

Este repositório contém dois projetos:

1. **mock_api** – API de mock de produtos.
2. **wishlist_developer_test** – API que irá consumir a **mock_api** para criar uma wishlist de produtos.

## 📺 Estrutura do Repositório

```
wishlist-repo/
│── docker/                        # Configuração do Docker
│   └── docker-compose.yml
│── mock_api/                      # API de mock
│   ├── Dockerfile
│   └── src/
│       └── app/                   # Código-fonte da API de mock
│           ├── __init__.py
│           ├── database.py
│           ├── main.py
│           ├── models.py
│           ├── routes.py
│           └── services.py
│   └── pyproject.toml
└── wishlist_developer_test/       # API cliente
    ├── .env.docker
    ├── Dockerfile
    └── src/
        ├── alembic.ini
        ├── app/                   # Código-fonte da API cliente
        │   ├── __init__.py
        │   ├── crud.py
        │   ├── database.py
        │   ├── main.py
        │   ├── models.py
        │   ├── routes.py
        │   ├── schemas.py
        │   └── security.py
        ├── migrations/            # Migrations do banco de dados
        │   ├── README
        │   ├── env.py
        │   ├── script.py.mako
        │   └── versions/
        │       └── 1ba2e89909b0_initial_migration.py
        └── pyproject.toml
```

## 🚀 Como Rodar o Projeto

### 1️⃣ Pré-requisitos

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)
- Docker (opcional, se preferir rodar em container)

### 2️⃣ Rodar o **mock_api** localmente

#### 2.1 Instalar dependências com Poetry

```sh
cd mock_api/src
poetry install
```

#### 2.2 Rodar a API com o FastAPI

Ative o ambiente virtual do Poetry e execute o FastAPI:

```sh
poetry shell
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

A API estará acessível em: [http://localhost:5000](http://localhost:5000)

#### 2.3 Rodar o **mock_api** com Docker

Se preferir rodar a API como um container Docker:

```sh
cd mock_api/src
docker build -t mock_api .
docker run -p 5000:5000 mock_api
```

---

## 📌 Endpoints da API **mock_api**

### ✅ Listagem de Produtos
```http
GET /api/product/?page=<PAGINA>
```

### ✅ Detalhe de um Produto
```http
GET /api/product/<ID>/
```

### 📚 Acesso ao Swagger UI

A API possui documentação interativa via Swagger:

[http://localhost:5000/docs](http://localhost:5000/docs)

---

### 3️⃣ Rodar a **wishlist_developer_test** localmente

#### 3.1 Instalar dependências com Poetry

```sh
cd wishlist_developer_test/src
poetry install
```

#### 3.2 Rodar a API com o FastAPI

Ative o ambiente virtual do Poetry e execute o FastAPI:

```sh
poetry shell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

A API estará acessível em: [http://localhost:8000](http://localhost:8000)

#### 3.3 Rodar a **wishlist_developer_test** com Docker

Se preferir rodar a API como um container Docker:

```sh
cd wishlist_developer_test/src
docker build -t wishlist_developer_test .
docker run -p 8000:8000 wishlist_developer_test
```

#### 3.4 Rodar as Migrations do Alembic

Após configurar a API, você precisará rodar as migrations do Alembic para configurar o banco de dados. Execute o seguinte comando:

```sh
cd wishlist_developer_test/src
poetry run alembic upgrade head
```

Isso vai aplicar as migrations mais recentes no banco de dados.

---

## 🛠️ Próximos Passos

- Melhorar a documentação
- Adicionar testes automatizados
- Finalizar integração entre **mock_api** e **wishlist_developer_test**
- Acompanhar a implementação de autenticação e segurança