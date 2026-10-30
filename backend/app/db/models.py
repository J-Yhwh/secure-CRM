# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

import sys
import os
import pathlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.net import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key= True, autoincrement=True)
    user_name = Column(String(50), unique= True, null=False )
  
