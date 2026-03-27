# 🚀 FastAPI do Zero

Repositório de estudos do curso sobre FastAPI documentado por **Gabriel Telles**.

Projeto desenvolvido construindo uma API REST completa com autenticação JWT, banco de dados PostgreSQL, testes automatizados, Docker e CI/CD.

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-linter-D7FF64?style=flat)

---

## 📁 Estrutura do Projeto

```
fastapi_zero/
├── fast_zero/
│   ├── __init__.py
│   ├── app.py          # FastAPI app + routers
│   ├── database.py     # Engine + get_session
│   ├── models.py       # SQLAlchemy ORM models
│   ├── schemas.py      # Pydantic schemas
│   ├── security.py     # JWT + hash + get_current_user
│   ├── settings.py     # pydantic-settings + .env
│   └── routers/
│       ├── auth.py     # /auth/token, /register, /refresh_token
│       ├── users.py    # /users/me
│       └── todos.py    # /todos CRUD
├── migrations/         # Alembic migrations
├── tests/
│   ├── conftest.py     # Fixtures + factories
│   ├── test_auth.py
│   ├── test_users.py
│   └── test_todos.py
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── Dockerfile
├── compose.yaml
├── pyproject.toml
└── .env.example
```

---

## ⚙️ Como Rodar Localmente

### Pré-requisitos

- Python 3.13+
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/) (opcional, para o banco)

### 1. Clonar o repositório

```bash
git clone https://github.com/telleswq/fastapi_zero.git
cd fastapi_zero
```

### 2. Instalar as dependências

```bash
poetry install
```

### 3. Configurar as variáveis de ambiente

```bash
cp .env.example .env
# Edite o .env com suas configurações
```

```env
DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
SECRET_KEY="sua-chave-secreta-aqui"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Subir o banco com Docker

```bash
docker run \
  --name fastapi_db \
  -e POSTGRES_USER=app_user \
  -e POSTGRES_DB=app_db \
  -e POSTGRES_PASSWORD=app_password \
  -p 5432:5432 \
  -d postgres
```

### 5. Executar as migrações

```bash
alembic upgrade head
```

### 6. Rodar a aplicação

```bash
task run
```

A API estará disponível em:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 🐳 Rodando com Docker Compose

Sobe tudo (banco + aplicação) com um único comando:

```bash
docker compose up --build
```

---

## 🧪 Testes

```bash
# Rodar todos os testes com cobertura
task test

# Ver o relatório de cobertura
open htmlcov/index.html
```

Os testes usam **TestContainers** para subir um PostgreSQL real e isolado durante a execução — sem precisar de banco externo.

---

## 📋 Comandos Disponíveis

| Comando | O que faz |
|---------|-----------|
| `task run` | Inicia o servidor de desenvolvimento |
| `task test` | Executa os testes com cobertura |
| `task lint` | Verifica o código com Ruff |
| `task format` | Formata o código com Ruff |

---

## 🔐 Endpoints Principais

### Auth
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/auth/register` | Cadastrar novo usuário |
| `POST` | `/auth/token` | Login → retorna JWT |
| `POST` | `/auth/refresh_token` | Renovar token |

### Users
| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/users/me` | Dados do usuário logado |
| `PUT` | `/users/me` | Atualizar perfil |
| `DELETE` | `/users/me` | Deletar conta |

### Todos
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/todos/` | Criar tarefa |
| `GET` | `/todos/` | Listar tarefas (com filtros) |
| `PATCH` | `/todos/{id}` | Atualizar tarefa |
| `DELETE` | `/todos/{id}` | Deletar tarefa |

---

## 🔄 CI/CD

O repositório conta com um pipeline de **Integração Contínua** via GitHub Actions que é executado a cada `push` ou `pull request`:

1. Checkout do código
2. Instalação do Python 3.13
3. Instalação das dependências via Poetry
4. Execução do lint com Ruff
5. Execução dos testes com cobertura

---

## 📖 Referências

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/)
- [Documentação Alembic](https://alembic.sqlalchemy.org/)
- [Documentação Pydantic v2](https://docs.pydantic.dev/)

---

## 👨‍💻 Autor

**Gabriel Telles**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gabriel_Telles-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/gdtelles)
[![GitHub](https://img.shields.io/badge/GitHub-telleswq-181717?style=flat&logo=github&logoColor=white)](https://github.com/telleswq)
[![Site](https://img.shields.io/badge/Site-tellesdev.com.br-F59E0B?style=flat&logo=google-chrome&logoColor=white)](https://tellesdev.com.br)
