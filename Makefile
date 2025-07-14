# -----------------------------------------
# Makefile para o projeto Embrapa
# -----------------------------------------
# Comandos principais:
# make install            → instala dependências
# make run                → inicia API local
# make migrate            → gera e aplica migração
# make reset-db           → recria o DB local e aplica migração
# make clean-migrations   → limpa as versões geradas
# make seed               → popula o banco via endpoint
# make help               → mostra esta ajuda
# -----------------------------------------

# Carrega variáveis do .env
include .env
export

# Variáveis padrão
ENV ?= local
DB_SQLITE=src/app/database/embrapa.db
DATABASE_URL ?= sqlite:///$(DB_SQLITE)

ifeq ($(ENV),production)
	DB_URL=$(DATABASE_URL)
else
	DB_URL=sqlite:///$(DB_SQLITE)
endif

# 🆘 Ajuda
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "🛠️  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Instala dependências com Poetry
	poetry install

run: ## Sobe a API FastAPI
ifeq ($(ENV),production)
	@echo "🌐 Rodando em PRODUÇÃO (porta 10000)"
	ENV=production poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
else
	@echo "🌐 Rodando LOCALMENTE (porta 8000)"
	poetry run uvicorn src.app.main:app --host 127.0.0.1 --port 8000 --reload
endif

migrate: ## Gera e aplica migração
	PYTHONPATH=. alembic revision --autogenerate -m "auto migration"
	PYTHONPATH=. alembic upgrade head

reset-db: ## ⚠️ Remove e recria o banco SQLite local com migração
ifeq ($(ENV),production)
	@echo "🚫 Não use reset-db em produção!"
else
	@echo "🗑️  Resetando banco local em $(DB_SQLITE)..."
	rm -f $(DB_SQLITE)
	touch $(DB_SQLITE)
	PYTHONPATH=. alembic upgrade head
endif

clean-migrations: ## Remove todos os arquivos de migração
	@echo "🧹 Limpando versões de migração..."
	@find alembic/versions -type f -name "*.py" -exec rm -f {} +

seed: ## Popula o banco chamando endpoint /admin/load_all
ifeq ($(ENV),production)
	curl -X POST https://seu-dominio.onrender.com/admin/load_all -H "Authorization: Bearer $(ADMIN_TOKEN)"
else
	curl -X POST http://127.0.0.1:8000/admin/load_all -H "Authorization: Bearer $(ADMIN_TOKEN)"
endif
