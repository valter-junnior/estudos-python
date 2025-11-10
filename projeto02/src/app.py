import streamlit as st
from controllers.task_controller import TaskController
from config.database import Base, engine
from models import *

Base.metadata.create_all(engine)

st.title("Task Manager")

task_controller = TaskController()
task_controller.index()