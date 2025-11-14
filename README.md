# 📚 Guia de Sintaxe - Python, Pandas, Streamlit e SQLAlchemy

Este README contém a sintaxe e comandos mais utilizados nos projetos, para facilitar a consulta rápida.

# não esquecer

```python
df = pd.DataFrame(t.__dict__ for t in tasks)
```
## 📊 Pandas

### Leitura e Manipulação de Dados

```python
import pandas as pd

# Ler CSV
df = pd.read_csv("arquivo.csv")
df = pd.read_csv("arquivo.csv", parse_dates=["coluna_data"])  # Com parsing de datas

# Criar novas colunas
df["nova_coluna"] = df["col1"] * df["col2"]

# Acessar atributos de datetime
df["mes"] = df["data_venda"].dt.month
df["ano"] = df["data_venda"].dt.year
df["dias"] = (hoje - df["data_abertura"]).dt.days
```

### Agrupamentos e Agregações

```python
# Agrupamento simples
df.groupby("categoria")["valor_total"].sum()

# Agrupamento múltiplo
df.groupby(["nome_loja", df["data_venda"].dt.month])["valor_total"].sum()

# Top N registros
df.groupby("nome_loja")["valor_total"].sum().sort_values(ascending=False)[:5]
df.groupby("nome_produto")["quantidade"].sum().sort_values(ascending=False).head(3)
```

### Merge e Joins

```python
# Merge de DataFrames
df = pd.merge(df1, df2)  # Inner join por padrão
df = pd.merge(df1, df2, on="coluna_comum")
```

### Manipulação de Colunas

```python
# Remover colunas
df.drop("coluna_indesejada", axis=1, inplace=True)

# Reordenar colunas
df = df.reindex(columns=["col1", "col2", "col3"])

# Renomear colunas
df = df.rename(columns={"old_name": "new_name"})

# Mapear valores
status_map = {1: "Pendente", 2: "Em andamento", 3: "Concluído"}
df["status"] = df["status"].map(status_map)
```

## 🔢 NumPy

### Condicionais e Seleção

```python
import numpy as np

# Condicionais com np.where
df["categoria"] = np.where(
    df["valor"] > 100,
    "alto",     # se True
    "baixo"     # se False
)

# Múltiplas condições com np.select
opcoes = [
    df["margem_lucro"] > df["valor_unitario"] * 0.3,
    df["margem_lucro"] <= df["valor_unitario"] * 0.3
]
categorias = ["alto", "baixo"]
df["desempenho"] = np.select(opcoes, categorias, default="neutro")
```

## 🌐 Streamlit

### Configuração e Layout

```python
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Título", layout="wide")

# Títulos e subtítulos
st.title("📊 Título Principal")
st.subheader("Subtítulo")
st.header("Cabeçalho")

# Layout em colunas
col1, col2, col3 = st.columns(3)
col1.metric("Métrica 1", valor1)
col2.metric("Métrica 2", f"R$ {valor2:,.2f}")
col3.metric("Métrica 3", f"R$ {valor3:,.2f}")
```

### Widgets de Input

```python
# Upload de arquivo
arquivo = st.file_uploader("Carregar CSV", type=["csv"])

# Inputs básicos
texto = st.text_input("Campo de texto")
numero = st.number_input("Número", min_value=1)
preco = st.number_input("Preço", min_value=0.0, step=0.01)
data = st.date_input("Data", datetime.today())
opcao = st.selectbox("Opções", ["opção1", "opção2"])
descricao = st.text_area("Descrição")

# Botões
if st.button("Clique aqui"):
    # ação
    
# Formulários
with st.form("meu_form"):
    campo1 = st.text_input("Campo 1")
    campo2 = st.number_input("Campo 2")
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        # processar dados
```

### Exibição de Dados

```python
# Exibir DataFrame
st.dataframe(df)

# Gráficos
st.line_chart(df.groupby("data")["valor"].sum())

# Métricas
st.metric("Total de Vendas", total_vendas)

# Mensagens
st.success("Sucesso!")
st.error("Erro!")
st.info("Informação")
st.warning("Aviso")
```

### Sidebar

```python
# Sidebar
st.sidebar.header("📂 Configurações")
arquivo = st.sidebar.file_uploader("Upload", type=["csv"])
```

### Session State

```python
# Gerenciar estado
if "dados_csv" not in st.session_state:
    st.session_state["dados_csv"] = None
    
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Atualizar estado
st.session_state.show_form = not st.session_state.show_form

# Recarregar página
st.rerun()
```

## 🗃️ SQLAlchemy

### Configuração do Banco

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/database"

# Engine e sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Obter sessão
def get_session():
    return SessionLocal()
```

### Definição de Modelos

```python
from datetime import date
from enum import Enum

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Venda(Base):
    __tablename__ = "vendas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    data_venda = Column(Date, default=date.today)
    
    def __repr__(self):
        return f"<Venda(id={self.id}, produto='{self.produto}')>"
```

### Operações CRUD

```python
# CREATE - Criar registro
def criar_venda(session, produto, quantidade, preco_unitario, data_venda):
    nova_venda = Venda(
        produto=produto,
        quantidade=quantidade,
        preco_unitario=preco_unitario,
        data_venda=data_venda
    )
    session.add(nova_venda)
    session.commit()

# READ - Listar registros
def listar_vendas(session):
    return session.query(Venda).all()

# UPDATE - Atualizar registro
def atualizar_venda(session, venda_id, **kwargs):
    venda = session.query(Venda).get(venda_id)
    if venda:
        for key, value in kwargs.items():
            setattr(venda, key, value)
        session.commit()

# DELETE - Excluir registro
def excluir_venda(session, venda_id):
    venda = session.query(Venda).get(venda_id)
    if venda:
        session.delete(venda)
        session.commit()
```

### Métodos de Classe (Static Methods)

```python
class Task(Base):
    # ... definição da tabela ...
    
    @staticmethod
    def all():
        return session.query(Task).all()
    
    @staticmethod
    def create(title, description, status, finished_at):
        task = Task(
            title=title,
            description=description,
            status=status,
            created_at=date.today(),
            finished_at=finished_at
        )
        session.add(task)
        session.commit()
    
    def update(id, **kwargs):
        task = session.query(Task).get(id)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)
            session.commit()
    
    def delete(id):
        task = session.query(Task).get(id)
        if task:
            session.delete(task)
            session.commit()
```

## 📅 DateTime

```python
from datetime import datetime, date

# Data atual
hoje = datetime.now()
data_hoje = date.today()

# Converter strings para datetime
pd.to_datetime("2025-11-01")
pd.to_datetime(df["coluna_data"])

# Calcular diferença de dias
dias_diferenca = (hoje - data_anterior).days
```

## 🛠️ Funções Utilitárias

### Manipulação de CSV

```python
def carregar_csv(caminho_csv: str):
    df = pd.read_csv(caminho_csv, parse_dates=["data_venda"])
    df["faturamento"] = df["quantidade"] * df["preco_unitario"]
    return df
```

### Cálculos de Métricas

```python
def calcular_metricas(df: pd.DataFrame):
    total_vendas = len(df)
    faturamento_total = df["faturamento"].sum()
    ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0
    return total_vendas, faturamento_total, ticket_medio
```

## 🏗️ Padrão MVC com Streamlit

### Controller
```python
class TaskController:
    def __init__(self):
        self.view = TaskView(self)
    
    def index(self):
        tasks = Task.all()
        self.view.index(tasks)
    
    def create(self, title, description, status, finished_at):
        Task.create(title, description, status, finished_at)
        return True
```

### View
```python
class TaskView:
    def __init__(self, controller):
        self.controller = controller
    
    def index(self, tasks):
        # Lógica da interface
        pass
    
    def form(self):
        # Formulário de criação
        pass
```

## 📝 Conversão de Dados para DataFrame

```python
# Converter objetos SQLAlchemy para DataFrame
df_vendas = pd.DataFrame([v.__dict__ for v in vendas])
df_vendas.drop("_sa_instance_state", axis=1, inplace=True)

# Converter lista de objetos
df = pd.DataFrame(t.__dict__ for t in tasks)
```

---

> 💡 **Dica**: Este guia contém os comandos mais utilizados nos projetos. Para funcionalidades específicas, consulte a documentação oficial de cada biblioteca.