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

def fill_raw_db(data):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    if isinstance(data, dict):
        # Reemplazar None con NULL (valor adecuado para SQL)
        sanitized_data = {key.replace(' ', '_'): (value if value is not None else None) for key, value in data.items()}
        
        # Obtener los nombres de las columnas y los valores
        columns = ', '.join([f'"{key}"' for key in sanitized_data.keys()])
        placeholders = ', '.join(['?' for _ in sanitized_data])
        sql = f'INSERT INTO raw ({columns}) VALUES ({placeholders})'
        cursor.execute(sql, list(sanitized_data.values()))
    
    conn.commit()
    conn.close()


def fill_process_db(data):
    conn = sqlite3.connect(db_file_path)
    
    data.to_sql('processed', conn, if_exists='append', index=False)
    
    conn.close()




if __name__ == "__main__":
    create_db()
