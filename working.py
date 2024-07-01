def process_location(location):
    try:
        p_tag = location.find('p', class_="ui-pdp-color--BLACK ui-pdp-size--SMALL ui-pdp-family--REGULAR ui-pdp-media__title")
        address_list = [part.strip() for part in p_tag.text.split(',')]
        try:
            return {
                "Calle": address_list[0],
                "Barrio": address_list[1],
                "Comuna": address_list[2],
                "Ciudad": address_list[3],
                "Dirección": ", ".join(address_list)
            }
        except IndexError as ie:
            print(f"Error al acceder a los elementos de la dirección: {ie}")
            return {
                "Calle": None,
                "Barrio": None,
                "Comuna": None,
                "Ciudad": None,
                "Dirección": ", ".join(address_list) if address_list else None
            }
    except Exception as e:
        print(f"Error al procesar la ubicación: {e}")
        return {
            "Calle": None,
            "Barrio": None,
            "Comuna": None,
            "Ciudad": None,
            "Dirección": None
        }
