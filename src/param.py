from pathlib import Path
fieldnames = [
    "url", "Name of the flat", "Value", "Currency", "General Expenses",
    "Size of the flat", "Bedrooms", "Bathrooms", "Seller",
    "metraje", "sup_terraza", "sup_util","ambientes","dormitorios","banos", "estacionamiento",
    "bodegas","piso_unidad", "cant_pisos", "dept_piso", "antiguedad",
    "tipo_depa", "orientacion","Calle", "Barrio", "Comuna", "Ciudad", "Dirección", "Fecha_Publicacion","Description"]

raw_data_path="../data/raw"

scrapped_url_path = Path("/data/raw/2024/scraped_urls.txt")

new_url_path = [
        "https://www.portalinmobiliario.com/venta/departamento/las-condes-metropolitana/_OrderId_BEGINS*DESC"
        #"https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana/_OrderId_BEGINS*DESC",
        #"https://www.portalinmobiliario.com/venta/departamento/providencia-metropolitana/_OrderId_BEGINS*DESC"
        ]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Android 10; Mobile; LG-M255; rv:84.0) Gecko/84.0 Firefox/84.0"]
