import pandas as pd 
import numpy as np
from datetime import datetime

lojas = pd.read_csv("projeto03/data/lojas.csv")
produtos = pd.read_csv("projeto03/data/produtos.csv")
vendas = pd.read_csv("projeto03/data/vendas.csv")

lojas["data_abertura"] = pd.to_datetime(lojas["data_abertura"]) # feito com ajuda no pd.to_datetime
vendas["data_venda"] = pd.to_datetime(vendas["data_venda"])
vendas["valor_total"] = vendas["quantidade"] * vendas["valor_unitario"]

"""
print(lojas)
print(produtos)
print(vendas)
"""

df = pd.merge(lojas, vendas)
df = pd.merge(df, produtos)

print(df[["nome_loja", "cidade", "nome_produto", "categoria", "quantidade", "valor_total", "data_venda"]], "\n")

faturamento_mensal_por_loja = df.groupby(["nome_loja", df["data_venda"].dt.month])["valor_total"].sum() # feito com ajuda no df["data_venda"].dt.month
faturament_total_por_categoria_de_produto = df.groupby("categoria")["valor_total"].sum()

print(faturamento_mensal_por_loja, "\n")
print(faturament_total_por_categoria_de_produto, "\n")

df["mes"] = df["data_venda"].dt.month
df["ano"] = df["data_venda"].dt.year
print(df[["data_venda", "mes", "ano"]],  "\n")

df["margem_lucro"] = df["valor_unitario"] - df["preco_custo"]

opcoes = [
    df["margem_lucro"] > df["valor_unitario"] * 0.3,
    df["margem_lucro"] <= df["valor_unitario"] * 0.3
]
categorias = ["alto", "baixo"]
df["desempenho"] = np.select(opcoes, categorias, default="neutro") # feito com ajuda no default="neutro

"""
df["desempenho"] = np.where(
    df["margem_lucro"] > df["valor_unitario"] * 0.3,
    "alto",    # valor se for True
    "baixo"    # valor se for False
)
"""

print(df[["valor_unitario", "margem_lucro", "desempenho"]],  "\n")

lojas_maior_faturamento = df.groupby(["nome_loja"])["valor_total"].sum().sort_values(ascending=False)[:5] # usar reset_index e o  .head(5)  # feito com ajuda no sort_values(ascending=False)
produtos_mais_vendidos_quantidade = df.groupby("nome_produto")["quantidade"].sum().sort_values(ascending=False)[:3]
print(lojas_maior_faturamento, "\n")
print(produtos_mais_vendidos_quantidade, "\n")

# todo com ajuda
hoje = datetime.now()
lojas["dias_operacao"] = (hoje - lojas["data_abertura"]).dt.days
print(lojas[["nome_loja", "dias_operacao"]])

