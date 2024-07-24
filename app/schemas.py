from pydantic import BaseModel
from typing import Optional
from data.param_db import process_col

class TrainedBase(BaseModel):
    for col_name, col_type in process_col.items():
        exec(f'{col_name}: Optional[{col_type.capitalize()}] = None')

class TrainedCreate(TrainedBase):
    pass

class TrainedUpdate(BaseModel):
    gusto: int

class Trained(TrainedBase):
    id: int
    gusto: int

    class Config:
        orm_mode = True
