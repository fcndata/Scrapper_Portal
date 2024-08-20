from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app import structure as models, schemas, crud, database
from .schemas import TrainedSchema

# Crear las tablas de la base de datos
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Montar los archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Ruta para leer los datos procesados
@app.get("/")
def read_processed(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    processed = crud.get_processed(db, skip=skip, limit=limit)
    print("Datos obtenidos:", processed)  # Verifica los datos
    return templates.TemplateResponse("index.html", {"request": request, "processed": processed})


# Ruta para etiquetar los datos
@app.post("/label")
def label_item(request: Request, item_id: str = Form(...), gusto: int = Form(...), db: Session = Depends(database.get_db)):
    # Paso 1: Obtener el dato original desde la tabla `processed`
    db_item = crud.get_item_by_id(db, item_id=item_id)

    # Paso 2: Si encontramos el dato en `processed`, lo procesamos automáticamente
    if db_item:
        # Automatizamos el mapeo del contenido del item procesado a `TrainedSQL`
        trained_data = {
    "id_name": db_item.id_name,
    "valor": db_item.valor,
    "gastos_comunes": db_item.gastos_comunes,
    "sup_total": db_item.sup_total,
    "sup_terraza": db_item.sup_terraza,
    "banos": db_item.banos,
    "orientacion": db_item.orientacion,
    "gusto": gusto,  # Solo tomamos gusto desde el formulario
    "url": db_item.url,
    "moneda": db_item.moneda,
    "sup_util": db_item.sup_util,
    "dormitorios": db_item.dormitorios,
    "estacionamiento": db_item.estacionamiento,
    "bodega": db_item.bodega,
    "ambientes": db_item.ambientes,
    "piso_unidad": db_item.piso_unidad,
    "tot_pisos": db_item.tot_pisos,
    "dept_x_piso": db_item.dept_x_piso,
    "antiguedad": db_item.antiguedad,
    "tipo_depa": db_item.tipo_depa,
    "vendedor": db_item.vendedor,
    "calle": db_item.calle,
    "barrio": db_item.barrio,
    "comuna": db_item.comuna,
    "ciudad": db_item.ciudad,
    "direccion": db_item.direccion,
    "fecha_scrap": db_item.fecha_scrap,
    "descripcion": db_item.descripcion,
    "id_publicacion": db_item.id_publicacion,
    "quality_scrap": db_item.quality_scrap,
}
       # Usamos `create_trained_with_gusto` para insertar el dato en `TrainedSQL`
        trained_data_schema = TrainedSchema(**trained_data)
        db_trained_item = crud.create_trained_with_gusto(db, trained_data_schema)
    
    # Paso 3: Recargar los datos procesados
    processed = crud.get_processed(db, skip=0, limit=10)
    
    return templates.TemplateResponse("index.html", {"request": request, "processed": processed, "updated_item": db_trained_item})


