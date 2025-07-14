import os
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context

# Carrega .env antes de qualquer importação que use as variáveis
load_dotenv()

# Agora sim importa config e Base
from app.utils.config import SQLALCHEMY_DATABASE_URI
from app.utils.database_helper import Base

# Alembic config
config = context.config
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URI)

# Log de depuração
print("DEBUG: SQLALCHEMY_DATABASE_URI =", SQLALCHEMY_DATABASE_URI)

# Setup de log
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata para autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# Modo offline vs online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# Importa os modelos para autogenerate
from app.models.models import (
    CommercialItemModel,
    ExportItemModel,
    ImportItemModel,
    ProcessingItemModel,
    ProductionItemModel,
)
