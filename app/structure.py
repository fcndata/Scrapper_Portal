from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from .database import Base
from data.param_db import process_col, col_type_mapping

primary_key = "id_publicacion"

ProcessedSQL = type('Processed', (Base,), {
    '__tablename__': 'processed',
    **{col_name: Column(col_type_mapping.get(col_type, String), primary_key=(col_name == primary_key)) for col_name, col_type in process_col.items()}
})

TrainedSQL = type('Trained', (Base,), {
    '__tablename__': 'trained',
    **{col_name: Column(col_type_mapping.get(col_type, String), primary_key=(col_name == primary_key)) for col_name, col_type in process_col.items()},
    'gusto': Column(Integer)
})
