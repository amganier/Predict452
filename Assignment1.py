# -*- coding: utf-8 -*-
# Extracting and Parsing Web Site Data (Python)

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# import packages for web scraping/parsing
import requests  # functions for interacting with web pages
from lxml import html  # functions for parsing HTML
from bs4 import BeautifulSoup  # DOM html manipulation

# -----------------------------------------------
# demo using the requests and lxml packages
# -----------------------------------------------
# Requests package on an email sent 23Aug17 archived on the Northwestern Alumni site 
web_page = requests.get('http://www.alumni.northwestern.edu/s/1479/02-naa/16/interior.aspx?sid=1479&gid=2&pgid=25626&cid=42868&ecid=42868&crid=0&calpgid=25618&calcid=42867', auth=('user', 'pass'))
# obtain the entire HTML text for the page of interest

# show the status of the page... should be 200 (no error)
web_page.status_code
# show the encoding of the page... should be utf8
web_page.encoding

# show the text including all of the HTML tags... lots of tags
web_page_text = web_page.text
print(web_page_text)

# parse the web text using html functions from lxml package
# store the text with HTML tree structure
web_page_html = html.fromstring(web_page_text)

# ------- Attempt Three = Success
# extract the text within paragraph tags using an lxml XPath query
# Assignment 1 Added Value: Isolate content within div tag with id of "ContentMiddle"
# Citation: Achieved with help from https://stackoverflow.com/questions/35163864/extract-text-from-html-div-using-python-and-lxml
email_body = ''.join(web_page_html.xpath('//div[@id="ContentMiddle"]//text()'))

# show the resulting text string object
print(email_body)
print(len(email_body)) # has a few all-blank strings
print(len(email_body))   # a list of character strings

# -----------------------------------------------------------
# demo of parsing HTML with beautiful soup instead of lxml
# -----------------------------------------------------------

# Assignment 1 Added Value: Added explicitly specified parser to avoid issues in running script on other systems / virtual environments. Read following before making choice:https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser"
my_soup = BeautifulSoup(web_page_text, "lxml")
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# Assignment 1 Added Value: gather all the text from within div tag with id of "ContentMiddle"
# Citation: Achieved with help from https://stackoverflow.com/questions/25614702/get-contents-of-div-by-id-with-beautifulsoup
# using another list comprehension 
email_content = [x.text for x in my_soup.find_all('div', id='ContentMiddle')]

# show the resulting text string object
print(email_content)  # note absense of all-blank strings
print(len(email_content))  
print(type(email_content))  # a list of character strings

# there are carriage return, line feed characters, and spaces
# to delete from the text... but we have extracted the essential 
# content of the page for further analysis
