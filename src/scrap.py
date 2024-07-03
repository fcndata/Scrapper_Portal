import requests
import csv
from module.module1 import get_urls,append_scraped_urls
from module.module3 import get_article,get_local_path,save_csv
from param import new_url_path,scrapped_url_path
urls_to_scrape = get_urls(new_url_path)
for post_url in urls_to_scrape:
    processed = get_article(post_url)
    if processed is not None:
        local_path = get_local_path(processed)
        save_csv(processed, local_path)
append_scraped_urls(reversed(urls_to_scrape))

