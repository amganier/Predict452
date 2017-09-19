# ----------------------------
# MyItem class defined by 
# items.py
# ----------------------------
# location in directory structure:
# sads_exhibit_11_1/scrapy_application/items.py

# establishes data fields for scraped items

import scrapy  # object-oriented framework for crawling and scraping

class MyItem(scrapy.item.Item):
    # define the data fields for the item (just one field used here)
    paragraph = scrapy.item.Field()  # paragraph content
