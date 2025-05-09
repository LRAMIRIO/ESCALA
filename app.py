
import streamlit as st
from processador import processar_arquivo

st.set_page_config(page_title="Gerador de Escalas", layout="wide")
st.title("📅 Gerador de Escalas com Feriados e Férias")

uploaded_file = st.file_uploader("📥 Envie a planilha modelo (.xlsx)", type=["xlsx"])
if uploaded_file:
    st.success("Arquivo carregado com sucesso!")

    if st.button("🚀 Gerar arquivos"):
        zip_path = processar_arquivo(uploaded_file)
        with open(zip_path, "rb") as f:
            st.download_button("📦 Baixar escalas (.zip)", f, file_name="escalas_geradas.zip")
