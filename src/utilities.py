def is_number(text):
    for value in text:
        if value and isinstance(value, str):  # Asegurarse de que el valor no sea None y sea una cadena
            try:
                return int(value.replace('.', ''))
            except ValueError:
                None
    return None

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None 
