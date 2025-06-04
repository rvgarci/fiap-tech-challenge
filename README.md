# FIAP Tech Challenge - API Embrapa

API RESTful desenvolvida com **FastAPI** para realizar scraping dos dados públicos de vitivinicultura da **Embrapa**, estruturá-los e disponibilizá-los por meio de endpoints REST. Os dados são armazenados em um banco de dados local SQLite com potencial para futura integração com modelos de Machine Learning.

## 📌 Funcionalidades

- Consulta de dados da Embrapa por ano (1970–2024)
- Endpoints separados por categoria: Produção, Processamento, Comercialização, Importação e Exportação
- Histórico de dados salvos no banco
- Documentação automática via Swagger
- Banco de dados SQLite usando SQLAlchemy
- Modularização com `routers`, `services`, `models`, `schema` e `utils`

## 🧪 Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **BeautifulSoup**
- **Pydantic**
- **Poetry** (gerenciador de dependências)

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/fiap-tech-challenge.git 
cd fiap-tech-challenge
```

### 2. Instale as dependências
```bash
poetry install
```

### 3. Execute a aplicação
```bash
poetry run uvicorn src.main:app --reload
```

Acesse a documentação interativa em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📚 Endpoints

Todos os endpoints estão sob o prefixo `/embrapa`.

### 🔹 Produção
- `GET /embrapa/producao?year=2023`
- `GET /embrapa/producao/historico`

### 🔹 Processamento
- `GET /embrapa/processamento/viniferas?year=2023`
- `GET /embrapa/processamento/americanas_e_hibridas?year=2023`
- `...`
- `GET /embrapa/processamento/viniferas/historico`

### 🔹 Comercialização
- `GET /embrapa/comercializacao?year=2023`
- `GET /embrapa/comercializacao/historico`

### 🔹 Importação e Exportação
- `GET /embrapa/importacao/uvas_frescas?year=2023`
- `GET /embrapa/exportacao/sucos_de_uva?year=2023`
- `...`
- `GET /embrapa/importacao/uvas_frescas/historico`

## 🗃️ Estrutura do Projeto

```
src/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── database/
```

## ⚠️ Observações

- 🟡 Autenticação JWT **não implementada** (opcional para este desafio)
- 📄 `.env` configurado para uso local com SQLite
- ✅ Banco de dados pré-populado: `embrapa.db`

## 📌 Autor

**Rafael Garcia**  
rm364717 – FIAP Pós-Tech Machine Learning Engineering  
[rvgarci@gmail.com](mailto:rvgarci@gmail.com)