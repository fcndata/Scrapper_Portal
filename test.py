def is_number(text):
    for value in text:
        try:
            # Intentar convertir el valor a entero
            return int(value.replace('.', ''))
        except (ValueError, AttributeError) as e:
            # Si no se puede convertir, continuar con el siguiente valor
            continue
    return None

# Ejemplo de uso
texto = "Gastos comunes aproximados $ 70.000"
valor = texto.split()

# Llamar a la función is_number con la lista de valores
numero = is_number(valor)
print(f"Número encontrado: {numero}")
