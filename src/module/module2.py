from datetime import datetime

def extract_name(header):
    return header.find(id="header").h1.text

def extract_seller(header):
    return header.find(id="header").find("div",class_="ui-pdp-seller-validated").a.text if header.find(id="header").find("div",class_="ui-pdp-seller-validated") else "Sin información"

def extract_value_and_currency(header):
    value, currency = None, None
    try:
        price_container = header.find(id="price")
        if price_container:
            value_container = price_container.find("span", class_="andes-money-amount__fraction")
            value = int(value_container.text.replace('.', '')) if value_container else None
            uf_symbol = price_container.find("span", itemprop="priceCurrency", string="UF")
            clp_symbol = price_container.find("span", itemprop="priceCurrency", string="$")
            currency = "UF" if uf_symbol else ("CLP" if clp_symbol else None)
            return value, currency
        else:
            return None, None
    except (IndexError, ValueError, AttributeError) as e:
        print(f"Error al extraer los gastos comunes: {e}")
        return None

def extract_general_expenses(header):
    try:
        maintenance_fee_element = header.find(id="maintenance_fee_vis")
        if maintenance_fee_element:
            fee_text = maintenance_fee_element.text.split('Gastos comunes aproximados $\xa0')[1]
            return int(fee_text.replace('.', ''))
        else:
            return None
    except (IndexError, ValueError, AttributeError) as e:
        print(f"Error al extraer los gastos comunes: {e}")
        return None

def extract_features(header):
    values = header.find_all("div",class_="ui-pdp-highlighted-specs-res__icon-label")
    metraje = dormitorio = banos = None
    try:
        metraje = values[0].find('span').text.split()[0] if values[0] else metraje
        dormitorio = values[1].find('span').text.split()[0] if values[1] else dormitorio
        banos = values[2].find('span').text.split()[0] if values[2] else banos
    except Exception as e:
        print(f"Error extracting features: {e}")
    return metraje, dormitorio, banos

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None 


def process_content(content):
    fields = {
        "Superficie total": ("metraje", convert_float),
        "Superficie de terraza": ("sup_terraza", convert_float),
        "Superficie útil": ("sup_util",convert_float),
        "Dormitorios": ("dormitorios", convert_float),
        "Baños":("banos",convert_float),
        "Ambientes": ("ambientes",convert_float),
        "Estacionamientos": ("estacionamiento", convert_float),
        "Bodegas": ("bodegas", convert_float),
        "Número de piso de la unidad": ("piso_unidad", convert_float),
        "Cantidad de pisos": ("cant_pisos", convert_float),
        "Departamentos por piso": ("dept_piso", convert_float),
        "Antigüedad": ("antiguedad", lambda x: convert_float(x.split()[0])),
        "Tipo de departamento": ("tipo_depa", lambda x: x),
        "Orientación": ("orientacion", lambda x: x)
    }

    article_content = {      
    }

    for table_work in content:
        result_table = table_work.find_all("tr")
        for row in result_table:
            header_text = row.find("th").get_text(strip=True) if row.find("th") else "-"
            value_text = row.find("td").get_text(strip=True) if row.find("td") else "-"

            if header_text in fields:
                field_key, func = fields[header_text]
                article_content[field_key] = func(value_text)

    
    return article_content

def process_location(location):
    try:
        p_tag = location.find('p', class_="ui-pdp-color--BLACK ui-pdp-size--SMALL ui-pdp-family--REGULAR ui-pdp-media__title")
        address_list = p_tag.text.split(',') if p_tag else []
        if len(address_list) < 4:
            return {
                "Calle": " - ",
                "Barrio": " - ",
                "Comuna": " - ",
                "Ciudad": " - ",
                "Dirección": ", ".join(address_list)}
        return {
            "Calle": address_list[0],
            "Barrio": address_list[1],
            "Comuna": address_list[2],
            "Ciudad": address_list[3],
            "Dirección": ", ".join(address_list)}
    except Exception as e:
        print(f"Error al procesar la ubicación: {e}")
        return

def process_description(description):
    now = datetime.now()
    return {"Description": description.p.text,
            "Fecha_Publicacion": now.strftime('%Y-%m-%d')}