import csv
from datetime import datetime
from .module1 import get_urls
from param import raw_data_path,scrapped_url_path

def get_scraped_urls(): #CSV Data.
    
    url_path=scrapped_url_path
    scraped_urls = []  
    if url_path.exists():
        try:
            with url_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        try:
            url_path.touch()
            print(f"Archivo creado: {url_path}")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
    return scraped_urls

def get_local_path(processed_article): # CSV Data.
    base_path = raw_data_path
    pub_date = datetime.fromisoformat(processed_article["Fecha_Publicacion"])
    year_folder = pub_date.strftime("%Y")
    file_name = f"{pub_date.strftime('%Y%m')}.csv"
    full_path = base_path / year_folder
    full_path.mkdir(parents=True, exist_ok=True)
    return full_path / file_name

def save_csv(processed_article, local_path,saved_field): #CSV Data.
    try:
        local_path.parent.mkdir(parents=True, exist_ok=True)
        file_exists = local_path.is_file()
        with local_path.open("a", newline='', encoding="utf8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=saved_field)
            if not file_exists:
                writer.writeheader()
            writer.writerow({field: processed_article.get(field, "") for field in saved_field})
    except Exception as e:
        print(f'Error {e} en save_csv')

def get_urls_to_scrape_csv():
    existing_urls = set(get_scraped_urls()) 
    all_urls = get_urls()
    urls_to_scrape = [url for url in all_urls if url not in existing_urls]
    return urls_to_scrape

def get_scraped_urls(): #CSV Data.
    
    url_path=scrapped_url_path
    scraped_urls = []  
    if url_path.exists():
        try:
            with url_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    else:
        try:
            url_path.touch()
            print(f"Archivo creado: {url_path}")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
    return scraped_urls

def append_scraped_urls(urls): #CSV Data.
    url_path=scrapped_url_path
    try:
        with url_path.open("a") as url_file: 
            url_file.writelines(f"{url}\n" for url in urls)
    except FileNotFoundError as fnf_error:
        print(f"Error: el archivo no se encontró. Detalles: {fnf_error}")
    except IOError as io_error:
        print(f"Error de entrada/salida al escribir en el archivo. Detalles: {io_error}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")