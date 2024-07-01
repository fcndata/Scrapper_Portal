#module files
import requests
from bs4 import BeautifulSoup
from time import time
from param import file_path
from typing import List
from pathlib import Path


def get_scraped_urls(file_path):
    scraped_urls = []
    if file_path.exists():
        try:
            with file_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except FileNotFoundError as fnf_error:
            print(f"Error: el archivo no se encontró. Detalles: {fnf_error}")
        except IOError as io_error:
            print(f"Error de entrada/salida al leer el archivo. Detalles: {io_error}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    else:
        print(f"El archivo {file_path} no existe.")
    return scraped_urls

def append_scraped_urls(urls,file_path):
    try:
        with file_path.open("a") as url_file:  # "a" para agregar
            url_file.writelines(f"{url}\n" for url in urls)
    except FileNotFoundError as fnf_error:
        print(f"Error: el archivo no se encontró. Detalles: {fnf_error}")
    except IOError as io_error:
        print(f"Error de entrada/salida al escribir en el archivo. Detalles: {io_error}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def request_url(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    results_lists = soup.find_all("ol", {"class": "ui-search-layout ui-search-layout--grid"})  # cambio div por ol
    return results_lists

def get_urls(final_url: List[str]):
    all_hrefs = set()

    for url in final_url:
        max_retries = len(final_url)
        retry_delay = 1  # segundos
        for attempt in range(max_retries):
            try:
                results_lists = request_url(url)
                for results_list in results_lists:
                    items = results_list.find_all("li", {"class": "ui-search-layout__item"})
                    for item in items:
                        anchor = item.select_one("div.ui-search-result__wrapper > div > a")
                        if anchor and anchor.get("href"):
                            all_hrefs.add(anchor['href'])
                break  
            except requests.HTTPError as http_err:
                print(f"HTTP error al obtener datos de {url} en el intento {attempt+1}: {http_err}")
            except requests.ConnectionError as conn_err:
                print(f"Error de conexión al obtener datos de {url} en el intento {attempt+1}: {conn_err}")
            except requests.Timeout as timeout_err:
                print(f"Timeout al obtener datos de {url} en el intento {attempt+1}: {timeout_err}")
            except requests.RequestException as req_err:
                print(f"Error de solicitud al obtener datos de {url} en el intento {attempt+1}: {req_err}")
            except Exception as e:
                print(f"Ocurrió un error inesperado al obtener datos de {url} en el intento {attempt+1}: {e}")
            time.sleep(retry_delay)
            retry_delay *= 2

    return list(all_hrefs)


def get_urls_to_scrape():
    existing_urls = set(get_scraped_urls())
    all_urls = get_urls()
    urls_to_scrape = [url for url in all_urls if url not in existing_urls]
    return urls_to_scrape