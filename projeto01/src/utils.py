import pandas as pd
import numpy as np

def carregar_csv(caminho_csv: str):
    df = pd.read_csv(caminho_csv, parse_dates=["data_venda"])
    df["faturamento"] = df["quantidade"] * df["preco_unitario"]
    return df

def calcular_metricas(df: pd.DataFrame):
    total_vendas = len(df)
    faturamento_total = df["faturamento"].sum()
    ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0
    return total_vendas, faturamento_total, ticket_medio
