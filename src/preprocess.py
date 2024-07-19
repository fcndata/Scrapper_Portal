import pandas as pd
import os
from pathlib import Path
from preprocess import map_orientation,map_housing,extract_flat_id,calculate_quality_rate
from preprocess import update_missing_pairs,update_surface_areas,update_antiguedad
def main_preprocess():
    base_path = Path(__file__).resolve().parent.parent
    input_file_path = os.path.join(base_path, 'data/raw/2024/202407.csv')
    output_dir = os.path.join(base_path, 'data/processed/2024')
    output_file_path = os.path.join(output_dir, 'cleaned_data.csv')
    
    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"No such file: '{input_file_path}'")
    
    # Cargar datos
    data = pd.read_csv(input_file_path)
    data = data.copy()
    
    # Aplicar funciones de preprocesamiento
    data['orientacion'] = data['orientacion'].map(map_orientation)
    data['map_depa'] = data['tipo_depa'].map(map_housing)
    data['flat_id'] = data['url'].map(extract_flat_id)
    data = update_missing_pairs(data)
    data = update_surface_areas(data)
    data['antiguedad'] = data.apply(update_antiguedad, axis=1)
    data['quality_rate'] = data.apply(calculate_quality_rate, axis=1)  # tal vez salte error porque no me traje a column
    
    # Seleccionar la fila con el máximo quality_rate por flat_id
    data = data.loc[data.groupby('flat_id')['quality_rate'].idxmax()]
    
    # Guardar datos procesados
    data.to_csv(output_file_path, index=False)
if __name__ == "__main__":
    main_preprocess()
