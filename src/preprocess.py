import pandas as pd
from preprocess import map_orientation, map_housing, calculate_quality_rate, rename
from preprocess import update_missing_pairs, update_surface_areas, update_antiguedad
from data import fill_process_db, collect_raw_db

def main_preprocess():
    data = collect_raw_db()

    # Imprimir nombres de las columnas para verificar
    print("Columnas iniciales del DataFrame:", data.columns)
    # Aplicar funciones de preprocesamiento
    data['orientacion'] = data['orientacion'].map(map_orientation)
    data['tipo_depa'] = data['tipo_depa'].map(map_housing)
    data = update_missing_pairs(data)
    data = update_surface_areas(data)
    data['antiguedad'] = data.apply(update_antiguedad, axis=1)
    data['quality_rate'] = data.apply(calculate_quality_rate, axis=1)
    data = rename(data)

    # Seleccionar la fila con el máximo quality_rate por flat_id
    data = data.loc[data.groupby('id_name')['quality_scrap'].idxmax()]

    fill_process_db(data)

if __name__ == "__main__":
    main_preprocess()
