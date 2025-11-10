import streamlit as st
import pandas as pd
from datetime import datetime
from database import (
    get_session, criar_venda, listar_vendas, atualizar_venda, excluir_venda
)
from utils import carregar_csv, calcular_metricas

st.set_page_config(page_title="Painel de Vendas", layout="wide")

st.title("📊 Painel de Vendas")

session = get_session()

# Sidebar - upload CSV
st.sidebar.header("📂 Fonte de Dados")
arquivo_csv = st.sidebar.file_uploader("Carregar arquivo CSV", type=["csv"])

if arquivo_csv:
    df_csv = carregar_csv(arquivo_csv)
    st.session_state["dados_csv"] = df_csv

# Seção de métricas
st.subheader("Resumo de Vendas")
if "dados_csv" in st.session_state:
    df = st.session_state["dados_csv"]
    total_vendas, faturamento_total, ticket_medio = calcular_metricas(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Vendas", total_vendas)
    col2.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")
    col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

    st.line_chart(df.groupby("data_venda")["faturamento"].sum())

# CRUD básico
st.subheader("Gerenciar Vendas")
with st.form("form_venda"):
    produto = st.text_input("Produto")
    quantidade = st.number_input("Quantidade", min_value=1)
    preco = st.number_input("Preço Unitário", min_value=0.0, step=0.01)
    data_venda = st.date_input("Data da Venda", datetime.today())
    submitted = st.form_submit_button("Adicionar Venda")

    if submitted:
        criar_venda(session, produto, quantidade, preco, data_venda)
        st.success("Venda adicionada com sucesso!")

vendas = listar_vendas(session)
if vendas:
    df_vendas = pd.DataFrame([v.__dict__ for v in vendas])
    df_vendas.drop("_sa_instance_state", axis=1, inplace=True)
    st.dataframe(df_vendas)
else:
    st.info("Nenhuma venda cadastrada ainda.")
