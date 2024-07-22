import sqlite3
from data import db_file_path

def check_raw_data():
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Ejecutar la consulta para obtener los datos de la tabla 'raw'
    cursor.execute("SELECT * FROM processed") #processed, raw,url
    rows = cursor.fetchall()
    
    conn.close()
    
    # Imprimir los datos obtenidos
    for row in rows:
        print(row)

if __name__ == "__main__":
    check_raw_data()
