import os


# Definir la ruta base
os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.db')

raw_col = {
    "flat_id": "TEXT",
    "quality_rate": "REAL",
    "orientacion": "TEXT",
    "map_depa": "TEXT",
    "antiguedad": "INTEGER",
    "source": "TEXT"
}

process_col = {
    "flat_id": "TEXT",
    "quality_rate": "REAL",
    "orientacion": "TEXT",
    "map_depa": "TEXT",
    "antiguedad": "INTEGER",
    "source": "TEXT"
}
