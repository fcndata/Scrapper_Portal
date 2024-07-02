from datetime import datetime
from utilities import is_number,is_number_array,convert_float


def extract_name(header):
    return header.find(id="header").h1.text

def extract_seller(header):
    return header.find(id="header").find("div",class_="ui-pdp-seller-validated").a.text if header.find(id="header").find("div",class_="ui-pdp-seller-validated") else "Sin información"

def extract_value_and_currency(header):
    value, currency = None, None
    try:
        price_container = header.find(id="price")
        value_container = price_container.find("span", class_="andes-money-amount__fraction")
        uf_symbol = price_container.find("span", itemprop="priceCurrency", string="UF")
        clp_symbol = price_container.find("span", itemprop="priceCurrency", string="$")
    except (IndexError, ValueError, AttributeError) as e:
        print(f"Error al extraer el header: {e}")
        return None, None
    else:
        value = int(value_container.text.replace('.', ''))
        currency = "UF" if uf_symbol else ("CLP" if clp_symbol else None)
        return value, currency

def extract_general_expenses(header):
    try:
        gastos_comunes=header.find("div",id="maintenance_fee_vis").text
    except (IndexError, ValueError, AttributeError) as e:
        print(f"Error al extraer los gastos comunes: {e}")
    else:
        return is_number_array(gastos_comunes)
    
def extract_features(header):
    metraje = dormitorio = banos = None
    try:
        all_features=header.find("div", id="highlighted_specs_res")
        values = all_features.find_all("div",class_="ui-pdp-highlighted-specs-res__icon-label")
    except Exception as e:
        print(f"Error extracting features: {e}")
    else:
        for value in values:
            text = value.find('span').text.split()
            if any(word in text for word in ['total', 'totales']):
                metraje = is_number(text)
                
            elif any(word in text for word in ['dormitorio', 'dormitorios']):
                dormitorio = is_number(text)
                
            elif any(word in text for word in ['bano', 'banos', 'baño', 'baños']):
                banos =is_number(text)

    return metraje, dormitorio, banos

def process_header(header):
    name = extract_name(header)
    seller = extract_seller(header)
    value, currency = extract_value_and_currency(header)
    general_expenses = extract_general_expenses(header)
    metraje, dormitorio, banos = extract_features(header)

    return {
        "Name of the flat": name,
        "Value": value,
        "Currency": currency,
        "General Expenses": general_expenses,
        "Size of the flat": metraje,
        "Bedrooms": dormitorio,
        "Bathrooms": banos,
        "Seller": seller
    }

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
        address_list = [part.strip() for part in p_tag.text.split(',')]
        try:
            return {
                "Calle": address_list[0],
                "Barrio": address_list[1],
                "Comuna": address_list[2],
                "Ciudad": address_list[3],
                "Dirección": ", ".join(address_list)}
        except IndexError as ie:
            print(f"Error al acceder a los elementos de la dirección: {ie}")
            return {
                "Calle": None,
                "Barrio": None,
                "Comuna": None,
                "Ciudad": None,
                "Dirección": ", ".join(address_list) if address_list else None}
    except Exception as e:
        print(f"Error al procesar la ubicación: {e}")
        return {
            "Calle": None,
            "Barrio": None,
            "Comuna": None,
            "Ciudad": None,
            "Dirección": None}

def process_description(description):
    now = datetime.now()
    return {"Description": description.p.text,
            "Fecha_Publicacion": now.strftime('%Y-%m-%d')}