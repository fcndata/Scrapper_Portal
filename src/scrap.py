import requests
import csv
from module.module1 import get_urls,append_scraped_urls
from module.module2 import get_article
from module.module3 import get_local_path,save_csv
from param import final_url

urls_to_scrape = get_urls(final_url)
#for post_url in urls_to_scrape:
#    processed = get_article(post_url)
#    if processed is not None:
#        local_path = get_local_path(processed)
#        save_csv(processed, local_path)
#append_scraped_urls(reversed(urls_to_scrape))
