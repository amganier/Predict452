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

# Creating a list with the hope of successfully looping through it later 
public_emails_list = [
 "http://www.alumni.northwestern.edu/s/1479/02-naa/16/interior.aspx?sid=1479&gid=2&pgid=25626&cid=42868&ecid=42868&crid=0&calpgid=25618&calcid=42867", 
 "http://www.alumni.northwestern.edu/s/1479/02-naa/16/interior.aspx?sid=1479&gid=2&pgid=25916&cid=43308&ecid=43308&crid=0&calpgid=25618&calcid=42867"
 ]
 

# Learning How to Build a loop
# Citation: Core Python Programming, Second Edition 
#for eachName in public_emails_list: print(eachName)

    
# Learning how to make a dictionary
# Citation: Automate the Boring Stuff with Python
# my_emails = {'PurpleLine_20092017':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25916&cid=43308&ecid=43308&crid=0&calpgid=25618&calcid=42867','PurpleLine_28082017':'http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25626&cid=42868&ecid=42868&crid=0&calpgid=25618&calcid=42867'}

#u = lambda
#r = map (requests.get(), public_emails_list)

# attempting to get the transformation to apply to a single URL
email_url = [http://www.alumni.northwestern.edu/?sid=1479&gid=2&pgid=25916&cid=43308&ecid=43308&crid=0&calpgid=25618&calcid=42867]
email_name = [PurpleLine_20092017]
>>> t = ['n'.text]
>>> h = [html.fromstring('t')]
>>> map(lambda x,y:x+y, public_emails_list,b)
[18, 14, 14, 14]
>>> map(lambda x,y,z:x+y+z, public_emails_list,b,c)
[17, 10, 19, 23]
>>> map(lambda x,y,z:x+y-z, public_emails_list,b,c)
[19, 18, 9, 5]

PurpleLine_20092017 = 
map(lambda n,u: n = (requests.get('u'), email_name,email_url)
map(lambda t,n: t = 


# Insight from conversation with CJG
# write lambdas that transform data set called on
# put those into an array in the order I need to call them
# map once on that array and give it the argument of the data set
# argument is the data set I want to do it on


r = lambda u: requests.get('u')
t = lambda r: 'r'.text
h = lambda t: html.fromstring('t')
b = lambda h: ''.join('h'.xpath('//div[@id="ContentMiddle"]//text()'))

process = array ([r,t,h,b])

web_page_text = web_page.text
web_page_html = html.fromstring(web_page_text)
''.join(web_page_html.xpath('//div[@id="ContentMiddle"]//text()'))


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
