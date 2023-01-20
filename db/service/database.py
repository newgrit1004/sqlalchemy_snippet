from util.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    setting.testdb_uri,
    pool_pre_ping=True,
    connect_args={"options": "-c timezone={}".format(setting.timezone)},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
