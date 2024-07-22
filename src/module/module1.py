import requests
from bs4 import BeautifulSoup
from time import time, sleep
from random import choice
from param import new_url_path, user_agents
from data import collect_urls_db
from data_extraction import process_header,process_content,process_description,process_highlights,process_location

def request_url(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    results_lists = soup.find_all("ol", {"class": "ui-search-layout ui-search-layout--grid"})
    return results_lists

def get_urls():
    url_path=new_url_path
    all_hrefs = set()
    for url in url_path:
        max_retries = len(url_path)
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
    existing_urls = collect_urls_db()
    all_urls = get_urls()
    urls_to_scrape = [url for url in all_urls if url not in existing_urls]
    return urls_to_scrape

def get_article(url):
    max_attempts = 15
    data = {"url": url}
    header_obtained = False
    highlights_obtained = False
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
                    print(f"process_header not found: {headers}")
            if not highlights_obtained:
                highlights=article.find("div", id="highlighted_specs_res")
                if highlights:
                    highlights_content=process_highlights(highlights)
                    highlights_obtained=True
                else:
                    print(f"process_highlights not found: {highlights}")    

            if not content_obtained:
                content = article.find_all("tbody", class_="andes-table__body")
                if content:
                    article_content=process_content(content)
                    content_obtained = True
                else:
                    print(f"process_content not found: {headers}")
            if not location_obtained:
                location = article.find("div", id="location")
                if location:
                    location_content=process_location(location)
                    location_obtained = True
                else:
                    print(f"location_content not found: {headers}")
            if not description_obtained:
                description = article.find("div", id="description")
                if description:
                    description_content=process_description(description)
                    description_obtained = True
                else:
                    print(f"description_content not found: {headers}")
            if header_obtained and highlights_obtained and content_obtained and location_obtained and description_obtained:
                return  {"url": url, **header_content,**highlights_content, **article_content, **location_content, **description_content,"user_agent":headers,"intento":attempt }

            attempt += 1
            sleep(3)

        except (requests.RequestException, ValueError) as e:
            print(f"Error: {e}. Reintentando...")
            attempt += 1
            sleep(7)
            continue

    print("No se pudo obtener la información después de varios intentos.")
    return None

