# ----------------------------
# spider class defined by 
# script one_site_crawler.py
# ----------------------------
# location in directory structure:
# sads_exhibit_11_1/scrapy_application/spiders/one_site_crawler.py

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# each spider class gives code for crawing and scraping

import scrapy  # object-oriented framework for crawling and scraping
from scrapy_application.items import MyItem  # item class 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector


# spider subclass inherits from BaseSpider
# this spider is designed to crawl just one website
class MySpider(CrawlSpider):
    name = "WIKIPEDIA"  # unique identifier for the spider
    allowed_domains = ['wikipedia.org']  # limits the crawl to this domain list
    start_urls = ['https://en.wikipedia.org/wiki/Northwestern_University']  # first url to crawl in domain
       
    # define the parsing method for the spider
    def parse(self, response):
        sel = Selector(response)
        divs = sel.xpath('//div')  # identify all <div> nodes
        # XPath syntax to grab all the text in paragraphs in the <div> nodes
        results = []  # initialize list
        this_item = MyItem()  # use this item class
        this_item['paragraph'] = divs.xpath('.//p').extract()  
        results.append(this_item)  # add to the results list
        return results 
        

   