from sqlalchemy.orm import sessionmaker
from typing import Dict, Generic, TypeVar, Union

T = TypeVar("T")

def general_insert_value(
    SessionLocal: sessionmaker,
    class_type: Generic[T],
    row: Dict[str, Union[float, str]],
):
    """

    Args:
        SessionLocal (sessionmaker): *.db.database의 SessionLocal 객체
        class_type (Generic[T]): 사용자 정의 sqlalchemy ORM 클래스, DB 테이블 이름과 동일
        row (Dict[str, Union[float, str]]): 테이블에 들어갈 값
    """
    row = class_type(**row)
    with SessionLocal() as session:
        session.begin()
        try:
            session.add(row)
        except:
            session.rollback()
        else:
            session.commit()