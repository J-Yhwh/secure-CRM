# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

import sqlalchemy

from .db.base import Base
from .db session import engine

#  directs SQLalchemy to create tables in MariaDB if they don't exist
Base.metadata.create_all(bind=engine)

