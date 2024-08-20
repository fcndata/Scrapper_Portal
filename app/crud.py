from sqlalchemy.orm import Session
from app.structure import Processed, TrainedSQL
from app.schemas import  TrainedSchema

# Funciones CRUD para la tabla "processed" # Aquí se agrega la logica de filtro
def get_processed(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Processed).offset(skip).limit(limit).all()
    except Exception as e:
        raise Exception(f"Database error: {e}")

def create_trained_with_gusto(db: Session, trained_data: TrainedSchema):
    try:
        # Inserta todos los datos de una vez, incluyendo gusto
        db_trained = TrainedSQL(**trained_data.model_dump())
        db.add(db_trained)
        db.commit()
        db.refresh(db_trained)
        return db_trained
    except Exception as e:
        db.rollback()  # Deshacer la transacción en caso de error
        raise Exception(f"Error al crear el registro en trained: {e}")
