# -*- coding: utf-8 -*-
# Extracting and Parsing Web Site Data (Python)

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# import packages for web scraping/parsing
import requests  # functions for interacting with web pages
from lxml import html  # functions for parsing HTML
from bs4 import BeautifulSoup  # DOM html manipulation
from array import array # Need ability to create array

# -----------------------------------------------
# demo using the requests and lxml packages
# -----------------------------------------------

# Learning how to make a dictionary
# Citation: Automate the Boring Stuff with Python
my_emails = {'PurpleLine_20170920':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25916&cid=43308&ecid=43308&crid=0&calpgid=25618&calcid=42867','PurpleLine_20170828':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25626&cid=42868&ecid=42868&crid=0&calpgid=25618&calcid=42867'}

# Insight from conversation with CJG
# write lambdas that transform data set called on
# put those into an array in the order I need to call them
# map once on that array and give it the argument of the data set
# argument is the data set on which I want the function array to run

PurpleLine_20170920 = requests.get(my_emails['PurpleLine_20170920'], auth=('user', 'pass'))
    
# show the status of the page... should be 200 (no error)
PurpleLine_20170920.status_code
# show the encoding of the page... should be utf8
PurpleLine_20170920.encoding

# sequence of lambdas
# Do I need to swap with sequence of functions instead of lambdas?
# Removed '' from lambda variables to avoid single character strings with help from KO
r = PurpleLine_20170920
t = lambda r: r.text
h = lambda t: html.fromstring(t)
b = lambda h: ''.join(h.xpath('//div[@id="ContentMiddle"]//text()'))

# reference: http://pythoncentral.io/the-difference-between-a-list-and-an-array/
# Removed '' and [] from lambda variables to avoid making strings with help from KO
process = array(t,h,b)#
name = map(process, PurpleLine_20170920)

print(name)


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
