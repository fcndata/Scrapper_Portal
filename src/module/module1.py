#module files
import requests
from bs4 import BeautifulSoup
from time import time
from param import file_path

def get_scraped_urls(file_path):
    scraped_urls = []
    if file_path.exists():
        try:
            with file_path.open() as url_file:
                scraped_urls = [line.strip() for line in url_file]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    return scraped_urls

def append_scraped_urls(urls,file_path):
    try:
        with file_path.open("a") as url_file: # "a" append
            url_file.writelines(f"{url}\n" for url in urls)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")


def get_urls(final_url):

    all_hrefs = set()

    for url in final_url:
        max_retries = len(final_url)
        retry_delay = 1  # segundos
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                results_lists = soup.find_all("ol", {"class": "ui-search-layout ui-search-layout--grid"}) # cambio div por ol

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