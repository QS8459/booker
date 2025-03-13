from src.db.models.account import Account
from sqlalchemy import select, and_


if __name__ == "__main__":
    filters = {
        'email': 'string',
        'password': 'string'
    }
    a = Account
    filter_conditions = []

    for field, value in filters.items():
        if value is not None:
            filter_conditions.append(getattr(a, field) == value)
    print(select(a).filter(*filter_conditions))