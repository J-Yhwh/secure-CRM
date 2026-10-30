# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

import sys
import os

import SQLAlchemy

from pathlib import datetime, 


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key= True)
    user_name = Column(String, unique = True)
  
