from db.table import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)


class Student(Base):
    """학생 테이블.
    id: id
    name: 이름
    age: 나이
    """

    __tablename__ = "Student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)