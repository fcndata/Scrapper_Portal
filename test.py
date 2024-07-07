import sys
from pathlib import Path
from random import choice
from bs4 import BeautifulSoup
import requests

sys.path.append(str(Path(__file__).resolve().parent / 'src/module'))
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from param import user_agents,scrapped_url_path
from module.module1 import get_urls,get_urls_to_scrape,get_scraped_urls
from utilities import is_number


