import streamlit as st

st.set_page_config(page_title="Embrapa Dashboard", layout="wide")

st.title("🚀 FIAP Tech Challenge - Bem-vindo ao Dashboard da Embrapa")

logo_fiap = "https://www.fiap.com.br/wp-content/uploads/2023/01/logo-fiap.png"
st.image(logo_fiap, width=200)
logo_embrapa = "https://www.embrapa.br/portal/embrapa/img/logo-embrapa.png"
st.image(logo_embrapa, width=200)   

st.markdown("""
# Sobre o Projeto
Este projeto tem como objetivo desenvolver um dashboard para visualização de dados da Embrapa, utilizando a biblioteca Streamlit.
""")
st.markdown("""
# Funcionalidades
- Visualização de dados de produção agrícola
- Análise de tendências ao longo dos anos
- Comparação entre diferentes culturas
""")    

st.markdown("""
# Tecnologias Utilizadas
- Python
- Streamlit
- Pandas
- Matplotlib
""")    
st.markdown("""
# Como Contribuir
Para contribuir com este projeto, siga as etapas abaixo:
1. Faça um fork deste repositório.
2. Crie uma nova branch para sua feature: `git checkout -b minha-feature`
3. Faça suas alterações e commit: `git commit -m 'Adicionando nova feature'`
4. Envie sua branch: `git push origin minha-feature`
5. Abra um Pull Request

Agradecemos suas contribuições! 
""")
st.markdown("""
# Contato
Para mais informações, entre em contato conosco:
- Email: contato@embrapa.br
- Telefone: (61) 1234-5678
""")    
st.markdown("""
# Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
""")
st.markdown("""
# Agradecimentos
""")  
st.markdown("""
Agradecemos a todos os colaboradores e à equipe da Embrapa por tornarem este projeto possível.
""")
st.markdown("""
# Contribuidores
- [Seu Nome](https://github.com/seu-nome)       
- [Colaborador 1](https://github.com/colaborador-1)
- [Colaborador 2](https://github.com/colaborador-2)
""")
