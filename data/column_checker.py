import sqlite3
from param_db import db_file_path

def check_table_columns():
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Consulta para obtener información de las columnas de la tabla 'raw'
    cursor.execute("PRAGMA table_info(raw)")
    columns = cursor.fetchall()
    
    conn.close()
    
    # Imprimir los nombres de las columnas
    for column in columns:
        print(column)

if __name__ == "__main__":
    check_table_columns()