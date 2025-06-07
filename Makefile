# Makefile para o projeto Embrapa
# Comandos principais:
# make install            → instala dependências
# make reset-db           → recria DB local, gera e aplica migração
# make run                → sobe a API FastAPI
# make migrate            → gera nova migration (após mudar os modelos)
# ENV=production make run → executa com banco PostgreSQL (produção)
# ENV=local make seed
# 	ENV=production make seed


include .env
export


# Variáveis
ENV ?= local
DB_SQLITE=src/app/database/embrapa.db
DATABASE_URL ?= sqlite:///$(DB_SQLITE)

# Ativa URL do banco conforme ambiente
ifeq ($(ENV),production)
	DB_URL=$(DATABASE_URL)
else
	DB_URL=sqlite:///$(DB_SQLITE)
endif

# Instala dependências com Poetry
install:
	poetry install

# Gera e aplica migração
migrate:
	alembic revision --autogenerate -m "auto migration"
	alembic upgrade head

# Reseta banco local (SQLite)
reset-db:
ifeq ($(ENV),production)
	@echo "⚠️  Não use reset-db em produção!"
else
	rm -f $(DB_SQLITE)
	touch $(DB_SQLITE)
	alembic revision --autogenerate -m "reset local"
	alembic upgrade head
endif

# Sobe aplicação com Uvicorn
run:
ifeq ($(ENV),production)
	ENV=production poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
else
	poetry run uvicorn src.app.main:app --host 127.0.0.1 --port 8000 --reload
endif

# Limpa as migrations
clean-migrations:
	rm -rf alembic/versions/*.py

# Popula o banco com dados via rota de admin
seed:
ifeq ($(ENV),production)
	curl -X POST https://seu-dominio.onrender.com/admin/load_all -H "Authorization: Bearer $(ADMIN_TOKEN)"
else
	curl -X POST http://127.0.0.1:8000/admin/load_all -H "Authorization: Bearer $(ADMIN_TOKEN)"
endif
