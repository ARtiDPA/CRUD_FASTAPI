"""Модели бд."""
from sqlalchemy import Integer, MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import data_base_settings


class Base(DeclarativeBase):
    """Базовый класс.

    Args:
        DeclarativeBase (class): Декларативный класс.
    """

    metadata = MetaData(schema=data_base_settings.db_schema)


class Task(Base):
    """Модель задачи.

    Args:
        Base (class): Базовый класс
    """

    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
