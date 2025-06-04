# 🌐 Deploy no Render – API Embrapa

Este guia descreve como fazer o deploy da API FastAPI no Render, uma plataforma de hospedagem gratuita e simples para aplicações web.

---

## ✅ Pré-requisitos

- Conta gratuita no [Render](https://render.com/)
- Repositório da aplicação no GitHub (público ou privado)

---

## 🗂️ Estrutura esperada do projeto

```
📁 fiap-tech-challenge/
├── src/
│   └── app/
│       ├── main.py
│       ├── routers/
│       ├── services/
│       ├── models/
│       ├── utils/
│       └── database/
├── poetry.lock
├── pyproject.toml
├── README.md
└── .env (não subir para o GitHub) 
```

---

## 🛠️ 1. Crie um arquivo `start.sh` na raiz do projeto

```bash
#!/bin/bash
poetry install
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
```

Dê permissão de execução (localmente):
```bash
chmod +x start.sh
```

---

## ⚙️ 2. Crie um arquivo `render.yaml` (Infra as Code - opcional)

```yaml
services:
  - type: web
    name: api-embrapa
    env: python
    plan: free
    buildCommand: "poetry install"
    startCommand: "./start.sh"
    envVars:
      - key: PYTHON_VERSION
        value: "3.12"
      - key: PYTHONPATH
        value: "src"
```

---

## 🚀 3. Publicar no Render

1. Vá para [https://dashboard.render.com](https://dashboard.render.com)
2. Clique em **"New Web Service"**
3. Conecte ao seu repositório GitHub
4. Configure:
   - **Environment**: Python 3
   - **Start command**: `./start.sh`
   - **Build command**: `poetry install`
   - **Branch**: `main` ou `master`
5. Clique em "Create Web Service"

---

## 🧪 4. Testar
- Acesse `https://<nome-do-serviço>.onrender.com/docs` para visualizar a documentação Swagger.
- Os dados serão carregados por scraping conforme os endpoints.

---

## 📦 Extras

- Render reinicia apps gratuitos após 15 minutos de inatividade.
- Certifique-se de manter a pasta `src` bem configurada e o `PYTHONPATH=src`.

---

Em caso de dúvidas ou erros, revise os logs disponíveis no dashboard do Render.