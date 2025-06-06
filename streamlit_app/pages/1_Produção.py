import streamlit as st
import pandas as pd
import requests


option = "producao"
title = "Produção"

st.set_page_config(page_title=title, layout="wide")
st.title(f"📦 {option} - Histórico de Dados")

url = f"http://127.0.0.1:8000/embrapa/{option}/historico"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    ano = st.multiselect("Filtrar por ano", df['ano'].unique(), placeholder="Selecione os ano")
    if ano:
        df = df[df['ano'].isin(ano)]    
    st.dataframe(data=df, height=500, use_container_width=True, hide_index=True)
else:
    st.error(f"Erro ao buscar dados: {response.status_code}")