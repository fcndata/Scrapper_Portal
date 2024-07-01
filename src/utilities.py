def is_number(text):
    for value in text:
        try:
            return int(value.replace('.', ''))
        except (ValueError, AttributeError) as e:
            continue
    return None

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None 
