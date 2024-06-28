from datetime import datetime

def extract_name(header):
    return header.find(id="header").h1.text

def extract_seller(header):
    return header.find(id="header").find("div",class_="ui-pdp-seller-validated").a.text if header.find(id="header").find("div",class_="ui-pdp-seller-validated") else "Sin información"

def extract_value_and_currency(header):
    price_container = header.find(id="price")
    value, currency = None, None
    if price_container:
        value_container = price_container.find("span", class_="andes-money-amount__fraction")
        value = int(value_container.text.replace('.', '')) if value_container else None
        uf_symbol = price_container.find("span", itemprop="priceCurrency", string="UF")
        clp_symbol = price_container.find("span", itemprop="priceCurrency", string="$")
        currency = "UF" if uf_symbol else ("CLP" if clp_symbol else None)
    return value, currency

def extract_general_expenses(header):
    return int(header.find(id="maintenance_fee_vis").text.split('Gastos comunes aproximados $\xa0')[1].replace('.', '')) if header.find(id="maintenance_fee_vis") else "Sin información"

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
    
def process_description(description):
    now = datetime.now()
    return {"Description": description.p.text,
            "Fecha_Publicacion": now.strftime('%Y-%m-%d')}