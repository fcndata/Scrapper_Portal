from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import structure as models, schemas, crud, database

# Crear las tablas de la base de datos
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Ruta para leer los datos procesados
@app.get("/")
def read_processed(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    processed = crud.get_processed(db, skip=skip, limit=limit)
    return templates.TemplateResponse("index.html", {"request": request, "processed": processed})

# Ruta para etiquetar los datos
@app.post("/label")
def label_item(request: Request, item_id: int = Form(...), gusto: int = Form(...), db: Session = Depends(database.get_db)):
    db_item = crud.update_gusto(db, item_id=item_id, gusto=gusto)
    return templates.TemplateResponse("index.html", {"request": request, "processed": [db_item]})
