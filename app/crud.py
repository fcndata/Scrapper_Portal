from sqlalchemy.orm import Session
from app.structure import Processed, Trained
from app.schemas import  TrainedCreate

# Funciones CRUD para la tabla "processed"
def get_processed(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Processed).offset(skip).limit(limit).all()
    except Exception as e:
        raise Exception(f"Database error: {e}")

# Crear un nuevo registro en la tabla "trained"
def create_trained(db: Session, trained: TrainedCreate):
    if not trained.id_publicacion:
        raise ValueError("id_publicacion is required")
    db_trained = Trained(**trained.dict())
    db.add(db_trained)
    db.commit()
    db.refresh(db_trained)
    return db_trained

# Actualizar el campo "gusto" en la tabla "trained"
def update_trained(db: Session, item_id: str, gusto: int):
    db_item = db.query(Trained).filter(Trained.id_publicacion == item_id).first()
    if not db_item:
        raise Exception(f"Item with id {item_id} not found")
    db_item.gusto = gusto
    db.commit()
    db.refresh(db_item)
    return db_item
