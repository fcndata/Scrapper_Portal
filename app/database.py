from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ruta a la base de datos SQLite existente
SQLALCHEMY_DATABASE_URL = "sqlite:///../data/db.db"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear una clase de sesión configurada con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para nuestras clases de modelos de SQLAlchemy
Base = declarative_base()

# Dependencia para obtener una sesión de base de datos para cada solicitud
def get_db():
    db = SessionLocal()
    try:
        yield db #En lugar de retornar db, yield se utiliza para "ceder" la sesión de base de datos al código que consume esta función. Esto convierte get_db() en un generador, que puede pausar su ejecución y reanudarla más tarde.
    finally:
        db.close()
