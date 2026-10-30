import sqlalchemy

from .db.base import Base
from .db session import engine

#  directs SQLalchemy to create tables in MariaDB if they don't exist
Base.metadata.create_all(bind=engine)

