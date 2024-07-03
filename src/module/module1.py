#module files
import requests
from bs4 import BeautifulSoup
from time import time
from param import scrapped_url_path,new_url_path
from typing import List
from pathlib import Path


def get_scraped_urls(url_path):
    scraped_urls = []
    if url_path.exists():
        try:
            with url_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    return scraped_urls

def append_scraped_urls(url):
    try:
        url_path=scrapped_url_path
        with url_path.open("a") as url_file: 
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


