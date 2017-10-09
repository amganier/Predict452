# -*- coding: utf-8 -*-
# Extracting and Parsing Web Site Data (Python)

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# import packages for web scraping/parsing
import requests  # functions for interacting with web pages
from lxml import html  # functions for parsing HTML
from bs4 import BeautifulSoup  # DOM html manipulation
from functools import reduce # Need reduce to combine lambdas

# -----------------------------------------------
# built from demo using the requests and lxml packages
# -----------------------------------------------

# Building a dictionary 
# Citation: Automate the Boring Stuff with Python
my_emails = {'PurpleLine_20170920':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25916&cid=43308&ecid=43308&crid=0&calpgid=25618&calcid=42867','PurpleLine_20170828':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25626&cid=42868&ecid=42868&crid=0&calpgid=25618&calcid=42867'}

# Using first key from dictionary in sample request statement. I hope to automate this later.
PurpleLine_20170920_data = requests.get(my_emails['PurpleLine_20170920'], auth=('user', 'pass'))
 
# Writing sequence of lambdas that transform item from dictionary
# Citation: https://www.python-course.eu/lambda.php
r = PurpleLine_20170920_data
t = lambda r: r.text
h = lambda t: html.fromstring(t)
 # Isolating desired content from rest of web page using div tag with id of "ContentMiddle"
 # Citation: https://stackoverflow.com/questions/35163864/extract-text-from-html-div-using-python-and-lxml
b = lambda h: ''.join(h.xpath('//div[@id="ContentMiddle"]//text()'))

# Combining lambda functions into an array in the order I need to call them
process = [t,h,b]

# Help from CJG: map runs lambdas in succession but not using the output of previous to feed input of next. Instead try reduce 
# Citation: https://stackoverflow.com/questions/4021731/python-function-list-chained-executing
result = reduce(lambda x, y: y(x), process, PurpleLine_20170920_data)

# Affirming success
print(result)

# Printing successful data acquisition... String to text file
with open('/Users/amganier/Documents/Predict452/PurpleLine_20170920.txt', 'w', encoding='utf-8') as f:
    f.write(result)

# -----------------------------------------------------------
# demo of parsing HTML with beautiful soup instead of lxml
# -----------------------------------------------------------

beautiful_email = PurpleLine_20170920_data.text
my_soup = BeautifulSoup(beautiful_email, "lxml")
# note that my_soup is a BeautifulSoup object
print(type(my_soup))

# remove JavaScript code from Beautiful Soup page object
# using a comprehension approach
[x.extract() for x in my_soup.find_all('script')] 

# Gathers all the text from within div tag with id of "ContentMiddle"
# Citation: https://stackoverflow.com/questions/25614702/get-contents-of-div-by-id-with-beautifulsoup
# using another list comprehension 
email_content = [x.text for x in my_soup.find_all('div', id='ContentMiddle')]

# show the resulting text string object
print(email_content)  # note absense of all-blank strings
print(len(email_content))  
print(type(email_content))  # a list of character strings


# Printing successful data acquisition to text file Using writelines since type is list
with open('/Users/amganier/Documents/Predict452/PurpleLine_20170920_soup.txt', 'w', encoding='utf-8') as f:
    f.writelines(email_content)
