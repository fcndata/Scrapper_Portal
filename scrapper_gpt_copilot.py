# -*- coding: utf-8 -*-
"""Scrapper GPT_Copilot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ciHcgGpz0dKNZ_wk0kyZNvdFeJYnBSfN
"""

import requests
import csv

from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep,time
from random import choice

fieldnames = [
    "url", "Name of the flat", "Value", "Currency", "General Expenses",
    "Size of the flat", "Bedrooms", "Bathrooms", "Seller",
    "metraje", "sup_terraza", "Superficie util","ambientes","dormitorios", "estacionamiento", "bodegas",
    "piso_unidad", "cant_pisos", "dept_piso", "antiguedad",
    "gastos_comunes", "orientacion",
    "Calle", "Barrio", "Comuna", "Ciudad", "Dirección", "Fecha_Publicacion"
]

file_path = Path("data/scraped_urls_copilot.txt")

def get_scraped_urls():
    scraped_urls = []
    if file_path.exists():
        try:
            with file_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    return scraped_urls

def append_scraped_urls(urls):
    try:
        with file_path.open("a") as url_file: # "a" append
            url_file.writelines(f"{url}\n" for url in urls)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def get_urls():
    final_url = [
        "https://www.portalinmobiliario.com/venta/departamento/las-condes-metropolitana/_OrderId_BEGINS*DESC",
        "https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana/_OrderId_BEGINS*DESC",
        "https://www.portalinmobiliario.com/venta/departamento/providencia-metropolitana/_OrderId_BEGINS*DESC"
    ]
    all_hrefs = set()

    for url in final_url:
        max_retries = len(final_url)
        retry_delay = 1  # segundos
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                results_lists = soup.find_all("div", {"class": "ui-search-layout ui-search-layout--grid"})

                for results_list in results_lists:
                    items = results_list.find_all("li", {"class": "ui-search-layout__item"})
                    for item in items:
                        anchor = item.select_one("div.ui-search-result__wrapper > div > a")
                        if anchor and anchor.get("href"):
                            all_hrefs.add(anchor['href'])
                break  # Salir del bucle de intentos después de un éxito
            except requests.RequestException as e:
                print(f"Error al obtener datos de {url} en el intento {attempt+1}: {e}")
                time.sleep(retry_delay)
                retry_delay *= 4  # Duplicar el tiempo de espera para el próximo reintento

    return list(all_hrefs)

def get_urls_to_scrape():
    existing_urls = set(get_scraped_urls())
    all_urls = get_urls()
    urls_to_scrape = [url for url in all_urls if url not in existing_urls]
    return urls_to_scrape

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
    metraje = dormitorio = banos = None
    try:
        values = header.find(id="highlighted_specs_res").find("div",class_="ui-pdp-highlighted-specs-res").find_all(class_="ui-pdp-highlighted-specs-res__icon-label")
        if len(values) > 0:
            metraje = values[0].find('span').text.split()[0] if values[0] else metraje
            dormitorio = values[1].find('span').text.split()[0] if values[1] else dormitorio
            banos = values[2].find('span').text.split()[0] if values[2] else banos
    except Exception as e:
        print(f"Error extracting features: {e}")
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

def convert_float(value):
    try:
        return float(value.replace(",", ".").split()[0])
    except ValueError:
        return None # 
def process_content(content):
    fields = {
        "Superficie total": ("metraje", convert_float),
        "Superficie de terraza": ("sup_terraza", convert_float),
        "Dormitorios": ("dormitorios", convert_float),
        "Ambientes": ("ambientes",convert_float),
        "Estacionamientos": ("estacionamiento", convert_float),
        "Bodegas": ("bodegas", convert_float),
        "Número de piso de la unidad": ("piso_unidad", convert_float),
        "Cantidad de pisos": ("cant_pisos", convert_float),
        "Departamentos por piso": ("dept_piso", convert_float),
        "Antigüedad": ("antiguedad", lambda x: convert_float(x.split()[0])),
        "Gastos comunes": ("gastos_comunes", lambda x: x.split()[0]),
        "Orientación": ("orientacion", lambda x: x)
    }

    article_content = {
        "Fecha_Publicacion": datetime.now().strftime('%Y-%m-%d')
    }

    if content:
        for table_work in content:
            result_table = table_work.find_all("tr")
            for row in result_table:
                header_text = row.find("th").get_text(strip=True) if row.find("th") else ""
                value_text = row.find("td").get_text(strip=True) if row.find("td") else ""

                if header_text in fields:
                    field_key, func = fields[header_text]
                    article_content[field_key] = func(value_text)

    # Calculate 'Superficie util' based on other fields
    article_content["Superficie util"] = article_content.get("metraje", 0) - article_content.get("sup_terraza", 0)

    return article_content

def process_location(location):
    now = datetime.now()

    try:
        p_tag = location.find('p', class_="ui-pdp-color--BLACK ui-pdp-size--SMALL ui-pdp-family--REGULAR ui-pdp-media__title")
        address_list = p_tag.text.split(',') if p_tag else []

        if len(address_list) < 4:
            return {
                "Calle": " - ",
                "Barrio": " - ",
                "Comuna": " - ",
                "Ciudad": " - ",
                "Dirección": ", ".join(address_list),
                "Fecha_Publicacion": now.strftime('%Y-%m-%d')
            }

        return {
            "Calle": address_list[0],
            "Barrio": address_list[1],
            "Comuna": address_list[2],
            "Ciudad": address_list[3],
            "Dirección": ", ".join(address_list),
            "Fecha_Publicacion": now.strftime('%Y-%m-%d')
        }
    except Exception as e:
        print(f"Error al procesar la ubicación: {e}")
        return

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Android 10; Mobile; LG-M255; rv:84.0) Gecko/84.0 Firefox/84.0"
]

def get_article(url):
    max_attempts = 15
    data = {"url": url}
    header_obtained = False
    content_obtained = False
    location_obtained = False
    attempt = 0
    while attempt < max_attempts:
        try:
            print(f"Intento {attempt + 1} de obtener el artículo.")
            headers = {'User-Agent': choice(user_agents)}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            article = soup.find(id="root-app")
            if not article:
                raise ValueError("El artículo base no fue encontrado en el DOM.")
            if not header_obtained:
                header = article.find("div", class_="ui-pdp-container__row ui-pdp-component-list")
                if header:
                    header_content=process_header(header)
                    header_obtained = True
                else:
                    print(f"Header no encontrado con el header: {headers}")

            if not content_obtained:
                content = article.find_all("tbody", class_="andes-table__body")
                if content:
                    article_content=process_content(content)
                    content_obtained = True
                else:
                    print(f"Content no encontrado con el header: {headers}")

            if not location_obtained:
                location = article.find("div", id="location")
                if location:
                    location_content=process_location(location)
                    location_obtained = True
                else:
                    print(f"Location no encontrado con el header: {headers}")

            # Si todos los componentes han sido obtenidos, retornar los datos
            if header_obtained and content_obtained and location_obtained:
                return  {"url": url, **header_content, **article_content, **location_content,"user_agent":headers,"intento":attempt }

            attempt += 1
            sleep(3)

        except (requests.RequestException, ValueError) as e:
            print(f"Error: {e}. Reintentando...")
            attempt += 1
            sleep(7)
            continue

    print("No se pudo obtener la información después de varios intentos.")
    return None

get_article("https://www.portalinmobiliario.com/MLC-2398365192-oportunidad-providencia-departamento-e-yanez-_JM#position=15&search_layout=grid&type=item&tracking_id=daf8047a-24d9-42d9-aba3-8d0a1cc368c9")

def get_local_path(processed_article):
    base_path = Path("data")
    pub_date = datetime.fromisoformat(processed_article["Fecha_Publicacion"])
    year_folder = pub_date.strftime("%Y")
    file_name = f"{pub_date.strftime('%Y%m')}.csv"
    full_path = base_path / year_folder
    full_path.mkdir(parents=True, exist_ok=True)

    return full_path / file_name

def save_csv(processed_article, local_path):
    """Saves the article as a CSV file, appending to it if it already exists."""
    local_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = local_path.is_file()
    with local_path.open("a", newline='', encoding="utf8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({field: processed_article.get(field, "") for field in fieldnames})

urls_to_scrape = get_urls()
for post_url in urls_to_scrape:
    processed = get_article(post_url)
    if processed is not None:
        local_path = get_local_path(processed)
        save_csv(processed, local_path)
append_scraped_urls(reversed(urls_to_scrape))
