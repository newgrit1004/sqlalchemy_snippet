from sqlalchemy.engine.row import Row
from db.table import Base
from typing import Union, List, Dict, Any

def remove_sa_state(query_result:dict):
    return {
        key: value for key, value in query_result.items() if key != "_sa_instance_state"
    }

def query_results_to_dict(
    query_results: Union[List[Row], List[Base]]
) -> List[Dict[str, Dict[str, Any]]]:
    """Convert query_results such as Rows in a list or sqlalchemy ORM class object defined by user to a list of dictionaries.
    Args:
        query_results (Union[List[Row], List[Base]):
            List[Row] : the result of session.query(ORM_CLASS.attr, ...).all()
            List[Base] : the result of session.query(ORM_CLASS).all()
    Returns:
        List[Dict[str, Dict[str, Any]]]
    """

    # query_results 타입이 List[Row]인 경우
    if isinstance(query_results[0], Row):
        object_dict_list: List[Dict[str, List[Base]]] = list(
            map(lambda x: x._asdict(), query_results),
        )

        return [
            {
                key: remove_sa_state(value.__dict__)
                if hasattr(value, "__dict__")
                else value
                for key, value in object_dict.items()
            }
            for object_dict in object_dict_list
        ]

    # Row 타입이 아닌 경우(List[Base])
    else:

        return [
            remove_sa_state(query_result.__dict__) for query_result in query_results
        ]
