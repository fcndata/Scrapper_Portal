import requests
import csv
from data import fill_raw_db
from module.module1 import get_urls_to_scrape,append_scraped_urls
from module.module3 import get_article,get_local_path,save_csv
from param import fieldnames

urls_to_scrape = get_urls_to_scrape()
for post_url in urls_to_scrape:
    processed = get_article(post_url)
    if processed is not None:
        fill_raw_db(processed) # SQL
        local_path = get_local_path(processed) #CSV
        save_csv(processed, local_path,fieldnames)#CSV
append_scraped_urls(reversed(urls_to_scrape))