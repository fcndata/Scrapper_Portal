def is_number(text):
    try:
        text = text.replace('.', '')
        for value in text.split():
            try:
                return int(value)
                break
            except Exception as e:
                print(f'No encuentra enteros en el texto {e}')    
    except Exception as e:
        print(f"Error al procesar el texto: {e}")
    return None

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None 
