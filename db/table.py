from sqlalchemy.ext.declarative import declarative_base, declared_attr

class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

Base = declarative_base(cls=Base)