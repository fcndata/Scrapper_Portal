import sys
import os
from data import fill_raw_db,fill_urls_db
from module import get_urls_to_scrape,append_scraped_urls
from module import get_article,get_local_path,save_csv 
from module import fieldnames

def scrap_to_db():
    urls_to_scrape = get_urls_to_scrape()
    for post_url in urls_to_scrape:
        processed = get_article(post_url)
        if processed is not None:
            fill_raw_db(processed) 
    fill_urls_db(reversed(urls_to_scrape))


def scrap_to_csv():
    urls_to_scrape = get_urls_to_scrape()
    for post_url in urls_to_scrape:
        processed = get_article(post_url)
        if processed is not None:    
            local_path = get_local_path(processed) 
            save_csv(processed, local_path,fieldnames)
    append_scraped_urls(reversed(urls_to_scrape))


if __name__ == "__main__":
    scrap_to_db()