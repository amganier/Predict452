
# coding: utf-8

# In[7]:


# Social Media Data Collection (Python)

# prepare for Python version 3x features and functions
from __future__ import division, print_function 

import twitter  # work with Twitter APIs
import json  # methods for working with JSON data

windows_system = False  # set to True if this is a Windows computer
if windows_system:
    line_termination = '\r\n' # Windows line termination
if (windows_system == False):
    line_termination = '\n' # Unix/Linus/Mac line termination
    
# name used for JSON file storage        
json_filename = 'my_tweet_file.json'  

# name for text file for review of results
full_text_filename = 'my_tweet_review_file.txt'  

# name for text from tweets
partial_text_filename = 'my_tweet_text_file.txt'  

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

    CONSUMER_KEY = 'void'
    CONSUMER_SECRET = 'void'
    OAUTH_TOKEN = 'void'
    OAUTH_TOKEN_SECRET = 'void'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api    
# -------------------------------------
# searching the REST API a la Russell (2014) section 9.4
def twitter_search(twitter_api, q, max_results=1000, **kw):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets and 
    # https://dev.twitter.com/docs/using-search for details on advanced 
    # search criteria that may be useful for keyword arguments  
    
    # See https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-search   
    search_results = twitter_api.users.search(q=q, count=10, **kw)
    
    statuses = search_results['statuses']
    type(statuses)
    
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
        except KeyError, e:
            break
            
        # Create a dictionary from next_results, which has the following form:
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.users.search(**kwargs)
        statuses += search_results['statuses']
        
        if len(statuses) > max_results: 
            break
            
    return statuses

# use the predefined functions from Russell to conduct the search

twitter_api = oauth_login()   
print(twitter_api)  # verify the connection

q = "official%20university"  # search string
results = twitter_search(twitter_api, q, max_results = 20)  # limit to 20 users

# examping the results object... should be list of dictionary objects
print('\n\ntype of results:', type(results)) 
print('\nnum type(statuses)ber of results:', len(results)) 
print('\ntype of results elements:', type(results[0]))

