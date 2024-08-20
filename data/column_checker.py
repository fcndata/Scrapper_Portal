import sqlite3
from param_db import db_file_path

def check_table_columns():
    # Conectar a la base de datos
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Consulta para obtener información de las columnas de la tabla 
    cursor.execute("PRAGMA table_info(processed)")
    
    # Obtener los resultados de la información de las columnas
    columns = cursor.fetchall()
    
    # Imprimir los nombres de las columnas
    print("Columnas de la tabla 'processed':")
    for column in columns:
        print(column)

    # Consulta para obtener las primeras 5 filas de la tabla processed
    cursor.execute("SELECT * FROM trained LIMIT 5;")
    
    # Obtener los resultados
    rows = cursor.fetchall()
    
    # Imprimir las primeras 5 filas
    print("\nPrimeras 5 filas de la tabla 'processed':")
    for row in rows:
        print(row)
    
    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    check_table_columns()
