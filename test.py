import sys
from pathlib import Path
from random import choice
from bs4 import BeautifulSoup
import requests

sys.path.append(str(Path(__file__).resolve().parent / 'src/module'))
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from param import user_agents
from utilities import is_number

from module2 import extract_features,extract_general_expenses
from module3 import fetch_and_extract_features
url="https://www.portalinmobiliario.com/MLC-1497944635-oportunidad-av-el-bosque-tobalaba-metro-_JM#position=14&search_layout=grid&type=item&tracking_id=159d886a-2af4-4aef-971d-368ec2dfcaab"


headers = {'User-Agent': choice(user_agents)}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#article = soup.find(id="root-app")
header = soup.find("div", class_="ui-pdp-container__row ui-pdp-component-list")

gc=extract_general_expenses(header)
print(gc)
metros,dorm,bano=fetch_and_extract_features(header)

print(f"El depa tiene {metros} metros, {dorm} dormitorios y {bano} baños con gastos comunes de {gc}")