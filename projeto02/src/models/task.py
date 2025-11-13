from sqlalchemy import Column, Integer, String, Date
from enum import Enum
from config.database import session, Base
from datetime import date

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(Integer, default=TaskStatus.PENDING.value)
    created_at = Column(Date, nullable=False)
    finished_at = Column(Date, nullable=True)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', status={self.status})>"

    @staticmethod
    def all():
        return session.query(Task).all()

    @staticmethod
    def create(title, description, status, finished_at):
        task = Task(title=title, description=description, status=status, created_at=date.today(), finished_at=finished_at)
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