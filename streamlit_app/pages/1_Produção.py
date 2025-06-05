import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Produção", layout="wide")

st.title("📦 Produção - Histórico de Dados")

# Requisição para a API
st.write("🔄 Buscando dados da API...")
url = "http://127.0.0.1:8000/embrapa/producao/historico"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Filtros
    produtos = st.multiselect("Filtrar por produto", df['produto'].unique())
    if produtos:
        df = df[df['produto'].isin(produtos)]

    st.dataframe(df, use_container_width=True)

    # Gráfico
    st.bar_chart(df.groupby("produto")["quantidade_litros"].sum())
else:
    st.error(f"Erro ao buscar dados: {response.status_code}")
