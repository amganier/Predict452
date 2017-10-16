
# coding: utf-8

# In[1]:


# Social Media Data Collection (Python)

# prepare for Python version 3x features and functions
from __future__ import division, print_function 

import twitter  # work with Twitter APIs
import json  # methods for working with JSON data
import twitter_text #Extracting Tweet Entities from Arbitrary Text

windows_system = False  # set to True if this is a Windows computer
if windows_system:
    line_termination = '\r\n' # Windows line termination
if (windows_system == False):
    line_termination = '\n' # Unix/Linus/Mac line termination
    
# name used for JSON file storage of competitor Tweets        
json_filename_t = 'technolutions_tweet_file.json'  

# name for text file for review of competitor tweet results
full_text_filename_t = 'technolutions_tweet_review_file.txt'  

# name for text from competitor tweets
partial_text_filename_t = 'technolutions_tweet_file.txt'  


# See Russell (2014) and Twitter site for documentation
# https://dev.twitter.com/rest/public
# Go to http://twitter.com/apps/new to provide an application name
# to Twitter and to obtain OAuth credentials to obtain API data

# -------------------------------------
# Twitter authorization a la Russell (2014) section 9.1
# Insert credentials in place of the "blah blah blah" strings 
# Sample usage of oauth() function
# twitter_api = oauth_login()    
def oauth_login():

    CONSUMER_KEY = 'blank'
    CONSUMER_SECRET = 'blank'
    OAUTH_TOKEN = 'blank'
    OAUTH_TOKEN_SECRET = 'blank'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api    
# -------------------------------------
# searching the REST API a la Russell (2014) section 9.4
    
def twitter_search(twitter_api, q, max_results=200, **kw):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets and 
    # https://dev.twitter.com/docs/using-search for details on advanced 
    # search criteria that may be useful for keyword arguments
    
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets    
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    
    statuses = search_results['statuses']
    
    # Iterate through batches of results by following the cursor until we
    # reach the desired number of results, keeping in mind that OAuth users
    # can "only" make 180 search queries per 15-minute interval. See
    # https://dev.twitter.com/docs/rate-limiting/1.1/limits
    # for details. A reasonable number of results is ~1000, although
    # that number of results may not exist for all queries.
    
    # Enforce a reasonable limit
    max_results = min(1000, max_results)
    
    for _ in range(10): # 10*100 = 1000
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more results when next_results doesn't exist
            break
            
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        
        if len(statuses) > max_results: 
            break
            
    return statuses
    
    # use the predefined functions from Russell to conduct the search
twitter_api = oauth_login()   
print(twitter_api)  # verify the connection

q = "@Technolutions"  # search string
results_twt = twitter_search(twitter_api, q, max_results = 200)  # limit to 200 users

# examping the results object... should be list of dictionary objects for competitor tweets call

print('\n\ntype of results:', type(results_twt)) 
print('\nnum type(statuses)ber of results:', len(results_twt)) 
print('\ntype of results elements:', type(results_twt[0]))  

# -------------------------------------
# working with JSON files composed of multiple JSON objects
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as a JSON object on a separate line
item_count = 0  # initialize count of objects dumped to file
with open(json_filename_t, 'w') as outfile:
    for dict_item in results_twt:
        json.dump(dict_item, outfile, encoding = 'utf-8')
        item_count = item_count + 1
        if item_count < len(results_twt):
             outfile.write(line_termination)  # new line between items
                     
# -------------------------------------
# working with text file for reviewing multiple JSON objects
# this text file will show the full contents of each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as group of lines printed with indentation
item_count = 0  # initialize count of objects dumped to file
with open(full_text_filename_t, 'w') as outfile:
    for dict_item in results_twt:
        outfile.write('Item index: ' + str(item_count) +             ' -----------------------------------------' + line_termination)
        # indent for pretty printing
        outfile.write(json.dumps(dict_item, indent = 4))  
        item_count = item_count + 1
        if item_count < len(results_twt):
             outfile.write(line_termination)  # new line between items  
        
# -------------------------------------
# working with text file for reviewing text from multiple JSON objects
# this text file will show only the text from each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that the text of each tweet 
# is written to a separate line in the output text file
item_count = 0  # initialize count of objects dumped to file
with open(partial_text_filename_t, 'w') as outfile:
    for dict_item in results_twt:
        outfile.write(json.dumps(dict_item['text']))
        item_count = item_count + 1
        if item_count < len(results_twt):
             outfile.write(line_termination)  # new line between text items 


# In[2]:


# name used for JSON file storage of clients or prospects twitter users      
json_filename_u = 'university_users_file.json'  

# name for text file for review of clients or prospects twitter users results
full_text_filename_u = 'university_users_review_file.txt'   

# name for text from client or prospect users
partial_text_filename_u = 'university_users_text_file.txt'  

# See Russell (2014) and Twitter site for documentation
# https://dev.twitter.com/rest/public
# Go to http://twitter.com/apps/new to provide an application name
# to Twitter and to obtain OAuth credentials to obtain API data

# -------------------------------------
# Changing api a la Russell (2014) section 9.4 with get/users/search
def twitter_user_search(twitter_api, q, max_results=200, **kw):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets and 
    # https://dev.twitter.com/docs/using-search for details on advanced 
    # search criteria that may be useful for keyword arguments  
    
    user_search_results = twitter_api.users.search(q=q, count=1000, **kw)
    return user_search_results

# use the predefined functions from Russell to conduct the search
twitter_api = oauth_login()   
print(twitter_api)  # verify the connection

q = "official%20university"  # search string
results_u = twitter_user_search(twitter_api, q, max_results = 200)  # limit to 200 users

# examping the results object... should be list of dictionary objects for client/prospect users call
print('\n\ntype of results:', type(results_u)) 
print('\nnum type(user_search_results)ber of results:', len(results_u)) 
print('\ntype of results elements:', type(results_u[0]))  

# -------------------------------------
# working with JSON files composed of multiple JSON objects
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as a JSON object on a separate line
item_count = 0  # initialize count of objects dumped to file
with open(json_filename_u, 'w') as outfile:
    for dict_item in results_u:
        json.dump(dict_item, outfile, encoding = 'utf-8')
        item_count = item_count + 1
        if item_count < len(results_u):
             outfile.write(line_termination)  # new line between items
                     
# -------------------------------------
# working with text file for reviewing multiple JSON objects
# this text file will show the full contents of each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as group of lines printed with indentation
item_count = 0  # initialize count of objects dumped to file
with open(full_text_filename_u, 'w') as outfile:
    for dict_item in results_u:
        outfile.write('Item index: ' + str(item_count) +             ' -----------------------------------------' + line_termination)
        # indent for pretty printing
        outfile.write(json.dumps(dict_item, indent = 4))  
        item_count = item_count + 1
        if item_count < len(results_u):
             outfile.write(line_termination)  # new line between items  
        
# -------------------------------------
# working with text file for reviewing text from multiple JSON objects
# this text file will show only the text from each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that the text of each tweet 
# is written to a separate line in the output text file
#item_count = 0  # initialize count of objects dumped to file
#with open(partial_text_filename_u, 'w') as outfile:
    #for dict_item in results_u:
        #outfile.write(json.dumps(item['text']))
        #item_count = item_count + 1
        #if item_count < len(results_u):
             #outfile.write(line_termination)  # new line between text items


# In[11]:


#Using extract 
# Citation: Mining the Social Web, 2nd Edition 9.2 Tweet Entities from Arbitrary Text
users_extract = twitter_text.Extractor(results_u)
ue= ("Screen Names:", users_extract.extract_mentioned_screen_names())
ue_list = list(ue)
type(ue_list)

competition_extract = twitter_text.Extractor(results_twt)

ce = ("Screen Names:", competition_extract.extract_mentioned_screen_names())
ce_list = list(ce)
type(ce_list)

# FAIL: Looking to identify common values between lists
# Citation: https://stackoverflow.com/questions/28061223/python-how-to-find-common-values-in-three-lists
# set(ce_list).intersection(ue_list)

print(ue_list)
print(ce_list)

