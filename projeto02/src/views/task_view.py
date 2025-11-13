import streamlit as st
from datetime import datetime
import pandas as pd

class TaskView():
    def __init__(self, controller):
        self.controller = controller

    def index(self, tasks):
        if "show_form" not in st.session_state:
            st.session_state.show_form = False

        if st.button("Novo"):
            st.session_state.show_form = not st.session_state.show_form
        
        if st.session_state.show_form:
            self.form()
        else:
            df = pd.DataFrame(t.__dict__ for t in tasks)
            df.drop("_sa_instance_state", axis=1, inplace=True)

            col1, col2, col3 = st.columns(3)
            col1.metric("Total", len(df))
            col2.metric("Pendentes", df[df["status"] == 1].shape[0])
            col3.metric("Concluidos", df[df["status"] == 3].shape[0])

            status_map = {
                1: "Pendente",
                2: "Em andamento",
                3: "Concluído"
            }

            df["status"] = df["status"].map(status_map)

            df = df.reindex(columns=["id", "title", "status", "created_at", "finished_at"])

            df = df.rename(columns={
                "id": "#",
                "title": "Titulo",
                "status": "Status",
                "created_at": "Criado em",
                "finished_at": "Finaliza(do) em"
            })

            st.dataframe(df)

    # def charts(self)

    def form(self):
        statuses = {
            "Pendente" : 1,
            "Em andamento": 2,
            "Concluido": 3
        }

        st.subheader("New")
        with st.form("form_task"):
            title = st.text_input("Titulo:")
            description = st.text_area("Descrição:")
            status = st.selectbox(
                "Status",
                list(statuses.keys())
            )
            finished_at = st.date_input("Data de conclusão: ", datetime.today())

            submitted = st.form_submit_button("Salvar")

            if submitted:
                if self.controller.create(title, description, statuses[status], finished_at): 
                    st.session_state.show_form = False
                    st.rerun()
                    
