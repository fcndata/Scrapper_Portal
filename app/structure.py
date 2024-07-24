from sqlalchemy import Column, Integer, String, Float
from .database import Base
from data.param_db import process_col

class Processed(Base):
    __tablename__ = 'processed'
    
    for col_name, col_type in process_col.items():
        col_type_mapping = {
            "TEXT": String,
            "INTEGER": Integer,
            "REAL": Float
        }
        col_type = col_type_mapping.get(col_type, String)
        vars()[col_name] = Column(col_type)

class Trained(Base):
    __tablename__ = 'trained'
    
    for col_name, col_type in process_col.items():
        col_type_mapping = {
            "TEXT": String,
            "INTEGER": Integer,
            "REAL": Float
        }
        col_type = col_type_mapping.get(col_type, String)
        vars()[col_name] = Column(col_type)
        
    gusto = Column(Integer)  # Campo adicional para almacenar la etiqueta de gusto
