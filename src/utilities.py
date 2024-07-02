def is_number_array(list):
    try:
        for value in list.split():
            try:
                return int(value.replace('.', ''))
                break
            except Exception as e:
                continue  
    except Exception as e:
        print(f"Error al procesar la lista: {e}")
    return None

def is_number(text):
    for value in text:
        try:
            return int(value.replace('.', ''))
        except ValueError:
            continue
    return None

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None 
