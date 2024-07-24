from sqlalchemy.orm import Session
from . import structure as models, schemas

def get_processed(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Processed).offset(skip).limit(limit).all()

def update_gusto(db: Session, item_id: int, gusto: int):
    db_item = db.query(models.Trained).filter(models.Trained.id == item_id).first()
    db_item.gusto = gusto
    db.commit()
    db.refresh(db_item)
    return db_item
