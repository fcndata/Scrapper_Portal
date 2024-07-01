import requests
import csv

from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from random import choice
from module2 import process_header,process_content,process_description,process_location
from param import user_agents,fieldnames,raw_data_path

def get_article(url):
    max_attempts = 15
    data = {"url": url}
    header_obtained = False
    content_obtained = False
    location_obtained = False
    description_obtained = False
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
            if not description_obtained:
                description = article.find("div", id="description")
                if description:
                    description_content=process_description(description)
                    description_obtained = True
                else:
                    print(f"Description no encontrado con el header: {headers}")
            if header_obtained and content_obtained and location_obtained and description_obtained:
                return  {"url": url, **header_content, **article_content, **location_content, **description_content,"user_agent":headers,"intento":attempt }

            attempt += 1
            sleep(3)

        except (requests.RequestException, ValueError) as e:
            print(f"Error: {e}. Reintentando...")
            attempt += 1
            sleep(7)
            continue

    print("No se pudo obtener la información después de varios intentos.")
    return None

def get_local_path(processed_article):
    base_path = Path(raw_data_path)
    pub_date = datetime.fromisoformat(processed_article["Fecha_Publicacion"])
    year_folder = pub_date.strftime("%Y")
    file_name = f"{pub_date.strftime('%Y%m')}.csv"
    full_path = base_path / year_folder
    full_path.mkdir(parents=True, exist_ok=True)

    return full_path / file_name

def save_csv(processed_article, local_path):
    local_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = local_path.is_file()
    with local_path.open("a", newline='', encoding="utf8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({field: processed_article.get(field, "") for field in fieldnames})
