# Simple One-Site Web Crawler and Scraper (Python)  Rev. 001 January 12, 2017
#
# Crawls Wikipedia rather than the now defunct website toutbay.com
# in particular it begins at the entry for Northwestern University:
# https://en.wikipedia.org/wiki/Northwestern_University
#
# code by Thomas W. Miller, updates by Kelsey O'Neill
#
# prepare for Python version 3x features and functions
from __future__ import division, print_function

# scrapy documentation at http://doc.scrapy.org/

# workspace directory set to outer folder/directory wnds_chapter_3b
# the operating system commands in this example are Mac OS X

import scrapy  # object-oriented framework for crawling and scraping
import os  # operating system commands

# function for walking and printing directory structure
def list_all(current_directory):
    for root, dirs, files in os.walk(current_directory):
        level = root.replace(current_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


# initial directory should have this form (except for items beginning with .):
#    sads_exhibit_11_1
#        run_one_site_crawler.py
#        scrapy.cfg
#        scrapy_application/
#            __init__.py
#            items.py
#            pipelines.py
#            settings.py
#            spiders
#                __init__.py
#                one_site_crawler.py

# examine the directory structure
current_directory = os.getcwd()
list_all(current_directory)

# list the avaliable spiders, showing names to be used for crawling
os.system('scrapy list')

# decide upon the desired format for exporting output: csv, JSON, or XML

# run the scraper exporting results as a JSON text file items.jsonlines
# this file provides text information with linefeeds to provide
# text output that is easily readable in a plain text editor
os.system('scrapy crawl WIKIPEDIA -o items.jsonlines')

# output formats commented out (choose the one needed for further parsing work)
# run the scraper exporting results as a comma-delimited text file items.csv
# os.system('scrapy crawl TOUTBAY -o items.csv')

# run the scraper exporting results as a JSON text file items.json
# os.system('scrapy crawl TOUTBAY -o items.json')

# run the scraper exporting results as a dictionary XML text file items.xml
# os.system('scrapy crawl TOUTBAY -o items.xml')

