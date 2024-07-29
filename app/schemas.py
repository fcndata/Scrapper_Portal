from pydantic import BaseModel, create_model
from typing import Dict, Any
from param_app import sql_to_pydantics

class Config:
    from_attributes = True  # Nueva configuración para Pydantic v2

def create_pydantic_model(name: str, fields: Dict[str, Any]) -> BaseModel:
    annotations = {key: sql_to_pydantics[key] for key in fields.keys()}
    return create_model(name, __config__=Config, __module__=__name__, **annotations)

# Crear modelos base dinámicamente
ProcessedSchemaBase = create_pydantic_model('ProcessedSchemaBase', sql_to_pydantics)
TrainedSchemaBase = create_pydantic_model('TrainedSchemaBase', sql_to_pydantics)

# Crear clases finales con configuración ORM
ProcessedSchema = type('ProcessedSchema', (ProcessedSchemaBase,), {'Config': Config})
TrainedSchema = type('TrainedSchema', (TrainedSchemaBase,), {'Config': Config})

# Crear clases para operaciones de creación basadas en los modelos base
ProcessedCreateSchema = type('ProcessedCreateSchema', (ProcessedSchemaBase,), {})
TrainedCreateSchema = type('TrainedCreateSchema', (TrainedSchemaBase,), {})
