import sys
import os
from data import fill_raw_db
from module import get_urls_to_scrape,append_scraped_urls
from module import get_article,get_local_path,save_csv 
from module import fieldnames

urls_to_scrape = get_urls_to_scrape()
for post_url in urls_to_scrape:
    processed = get_article(post_url)
    if processed is not None:
        print(f"The type of 'processed' is: {type(processed)}") 
        fill_raw_db(processed) # SQL
        local_path = get_local_path(processed) #CSV
        save_csv(processed, local_path,fieldnames)#CSV
append_scraped_urls(reversed(urls_to_scrape))