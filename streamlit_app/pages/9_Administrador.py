import streamlit as st
import requests

st.set_page_config(page_title="Administrador", layout="centered")
st.title("🔐 Área Administrativa")

# Campo de senha opcional
senha = st.text_input("Digite a senha de acesso", type="password")

# URL do endpoint (ajuste se necessário)
API_URL = "https://api-embrapa-fyl8.onrender.com/admin/load_all"

if senha == "admin123":
    if st.button("🔄 Carregar todos os dados"):
        with st.spinner("Carregando os dados da Embrapa..."):
            try:
                response = requests.post(API_URL)
                if response.status_code == 200:
                    st.success("✅ Dados carregados com sucesso!")
                    st.json(response.json())
                else:
                    st.error(f"Erro: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error("Erro ao conectar com a API.")
                st.exception(e)
else:
    st.warning("⚠️ Acesso restrito. Insira a senha para continuar.")
