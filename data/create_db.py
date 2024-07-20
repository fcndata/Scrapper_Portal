import sqlite3
import os
from data.param_db import raw_col, process_col, db_file_path

def create_db():
    # Crear la declaración SQL para la creación de las tablas
    create_raw_table = f"CREATE TABLE IF NOT EXISTS raw ({', '.join([f'{col} {dtype}' for col, dtype in raw_col.items()])})"
    create_processed_table = f"CREATE TABLE IF NOT EXISTS processed ({', '.join([f'{col} {dtype}' for col, dtype in process_col.items()])})"
    
    # Conectar a la base de datos SQLite (o crearla)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Crear tablas
    cursor.execute(create_raw_table)
    cursor.execute(create_processed_table)
    
    # Confirmar cambios y cerrar la conexión
    conn.commit()
    conn.close()

def fill_process_db(data):
    conn = sqlite3.connect(db_file_path)
    
    # Guardar datos en la tabla 'processed'
    data.to_sql('processed', conn, if_exists='append', index=False)
    
    # Cerrar la conexión
    conn.close()

def fill_raw_db(data):
    conn = sqlite3.connect(db_file_path)
    
    # Guardar datos en la tabla 'raw'
    data.to_sql('raw', conn, if_exists='append', index=False)
    
    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    create_db()
