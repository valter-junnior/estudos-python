from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    data_venda = Column(Date, default=date.today)

Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()

# Funções CRUD
def criar_venda(session, produto, quantidade, preco_unitario, data_venda):
    nova_venda = Venda(
        produto=produto,
        quantidade=quantidade,
        preco_unitario=preco_unitario,
        data_venda=data_venda
    )
    session.add(nova_venda)
    session.commit()

def listar_vendas(session):
    return session.query(Venda).all()

def atualizar_venda(session, venda_id, **kwargs):
    venda = session.query(Venda).get(venda_id)
    if venda:
        for key, value in kwargs.items():
            setattr(venda, key, value)
        session.commit()

def excluir_venda(session, venda_id):
    venda = session.query(Venda).get(venda_id)
    if venda:
        session.delete(venda)
        session.commit()
