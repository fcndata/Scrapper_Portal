import sqlite3
import pandas as pd
from .param_db import raw_col,raw_col_sql,process_col, db_file_path

def create_db():
    # Crear la declaración SQL para la creación de las tablas
    create_raw_table = f"CREATE TABLE IF NOT EXISTS raw ({', '.join([f'{col} {dtype}' for col, dtype in raw_col_sql.items()])})"
    create_processed_table = f"CREATE TABLE IF NOT EXISTS processed ({', '.join([f'{col} {dtype}' for col, dtype in process_col.items()])})"
    create_urls_scraped = "CREATE TABLE IF NOT EXISTS url (url TEXT)"

    # Conectar a la base de datos SQLite (o crearla)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Crear tablas
    cursor.execute(create_raw_table)
    cursor.execute(create_processed_table)
    cursor.execute(create_urls_scraped)
    # Confirmar cambios y cerrar la conexión
    conn.commit()
    conn.close()

def fill_raw_db(data):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    if isinstance(data, dict):
        # Reemplazar None con NULL y manejar nombres de columnas con espacios
        sanitized_data = {key.replace(' ', '_'): (value if value is not None else None) for key, value in data.items() if key in raw_col.keys()}
        
        # Obtener los nombres de las columnas y los valores
        columns = ', '.join(sanitized_data.keys())
        placeholders = ', '.join(['?' for _ in sanitized_data])
        sql = f'INSERT INTO raw ({columns}) VALUES ({placeholders})'
        cursor.execute(sql, list(sanitized_data.values()))
    
    conn.commit()
    conn.close()

def collect_raw_db():
    conn = sqlite3.connect(db_file_path)
    query = "SELECT * FROM raw"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def fill_process_db(data):
    conn = sqlite3.connect(db_file_path)
    if isinstance(data, pd.DataFrame):
    # Conectar a la base de datos SQLite
        # Reemplazar espacios en los nombres de las columnas
        data.columns = [col.replace(' ', '_') for col in data.columns]
        # Insertar DataFrame en la tabla 'processed'
        data.to_sql('processed', conn, if_exists='append', index=False)
    # Cerrar la conexión
    conn.commit()
    conn.close()

def collect_urls_db():
    conn = sqlite3.connect(db_file_path)
    query = "SELECT DISTINCT url FROM url"
    df = pd.read_sql_query(query, conn)
    conn.close()
    url_list = df['url'].tolist()
    return url_list

def fill_urls_db(data):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    if isinstance(data, list):
        for url in data:
            cursor.execute("INSERT INTO url (url) VALUES (?)", (url,))
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_db()
