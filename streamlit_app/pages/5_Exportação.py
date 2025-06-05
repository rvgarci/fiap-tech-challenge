import datetime
import pandas as pd
import streamlit as st


st.title("📊 Dashboard de Produção")

year = st.number_input("Ano:", min_value=1970, max_value=2023, value=datetime.date.today().year-2)
submit = st.button("Enviar")

df = pd.DataFrame({
    "Ano": [2021, 2022, 2023, 2024, 2025],
    "Produção": [100, 150, 130, 170, 200]
})

st.line_chart(df.set_index("Ano"))
