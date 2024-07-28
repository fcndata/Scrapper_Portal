from pydantic import BaseModel, create_model
from typing import Optional, Dict, Any
from data.param_db import process_col
from param_app import sql_to_pydantics

def create_pydantic_model(name: str, fields: Dict[str, Any]) -> BaseModel:
    annotations = {key: sql_to_pydantics[key] for key in fields.keys()}
    return create_model(name, **annotations)

# Crear modelos base dinámicamente
ProcessedBase = create_pydantic_model('ProcessedBase', process_col)
TrainedBase = create_pydantic_model('TrainedBase', process_col)
TrainedBase.__annotations__['gusto'] = int  # Añadir campo 'gusto' 

# Crear clases para operaciones de creación basadas en los modelos base
ProcessedCreate = type('ProcessedCreate', (ProcessedBase,), {})
TrainedCreate = type('TrainedCreate', (TrainedBase,), {})

# Crear clases finales con configuración ORM
Processed = type('Processed', (ProcessedBase,), {'Config': type('Config', (), {'orm_mode': True})})
Trained = type('Trained', (TrainedBase,), {'Config': type('Config', (), {'orm_mode': True})})
