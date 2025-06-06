import streamlit as st
import pandas as pd
import requests

option = "processamento"
suboptions = [
    "viniferas",
    "americanas_e_hibridas",
    "uvas_de_mesa",
    "sem_classificacao"
]
title = "Processamento"

st.set_page_config(page_title=title, layout="wide")
st.title(f"📦 {option} - Histórico de Dados")

suboption = st.selectbox("Selecione uma subopção", suboptions, index=0).lower()

url = f"http://127.0.0.1:8000/embrapa/{option}/{suboption}/historico"
response = requests.get(url)
st.text(response.text)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    ano = st.multiselect("Filtrar por ano", df['ano'].unique(), placeholder="Selecione os ano")
    if ano:
        df = df[df['ano'].isin(ano)]    
    st.dataframe(data=df, height=500, use_container_width=True, hide_index=True)
else:
    st.error(f"Erro ao buscar dados: {response.status_code}")