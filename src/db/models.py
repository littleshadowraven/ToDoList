from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import datetime

Base = declarative_base()


class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(UUID, primary_key=True)
    title = Column(String(50), nullamle=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))


class TodoItem(Base):
    __tablename__ = "todo_item"

    id = Column(UUID, primary_key=True)
    title = Column(String(50), nullamle=False)
    list_id = Column(ForeignKey(TodoList.id), nullamle=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
