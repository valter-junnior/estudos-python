from models.task import Task
from views.task_view import TaskView

class TaskController:
    def __init__(self):
        self.view = TaskView(self)

    def index(self):
        tasks = Task.all()

        self.view.index(tasks)

    def create(self, title, description, status, finished_at):
        Task.create(title, description, status, finished_at)

        return True