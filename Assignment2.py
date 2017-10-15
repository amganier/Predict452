
# coding: utf-8

# In[4]:


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
    
# name used for JSON file storage of competitor Tweets        
json_filename_t = 'technolutions_tweet_file.json' 

# name used for JSON file storage of clients or prospects twitter users      
json_filename_u = 'university_users_file.json'  

# name for text file for review of competitor tweet results
full_text_filename_t = 'technolutions_tweet_file.txt'  

# name for text file for review of clients or prospects twitter users results
full_text_filename_u = 'university_users_review_file.txt' 

# name for text from competitor tweets
partial_text_filename_t = 'technolutions_tweet_file.txt'  

# name for text from client or prospect users
partial_text_filename_u = 'university_users_text_file.txt'  

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

    CONSUMER_KEY = 'OUeSQiDBOoiosaf7g9uECkr2F'
    CONSUMER_SECRET = 'WG6nIqPns9PnpMP8MVbKQ3uZRXwb48fMX6ywkmPqMn8cvZx9j2'
    OAUTH_TOKEN = '862669440990793728-uoZPYdduf5hhrpd47QFrzSLFyyEpSN2'
    OAUTH_TOKEN_SECRET = 'aCg8tZBXE9PIpUrTtyKmtNPM5ZdcU6NHZN0RYCnImpOuV'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api    
# -------------------------------------
# searching the REST API a la Russell (2014) section 9.4
def twitter_user_search(twitter_api, q, max_results=200, **kw):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets and 
    # https://dev.twitter.com/docs/using-search for details on advanced 
    # search criteria that may be useful for keyword arguments  
    
    # See https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-search   
    user_search_results = twitter_api.users.search(q=q, count=1000, **kw)
    return user_search_results
    
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

q = "official%20university"  # search string
results = twitter_user_search(twitter_api, q, max_results = 200)  # limit to 200 users

# examping the results object... should be list of dictionary objects for client/prospect users call
print('\n\ntype of results:', type(results)) 
print('\nnum type(user_search_results)ber of results:', len(results)) 
print('\ntype of results elements:', type(results[0]))  

# examping the results object... should be list of dictionary objects for competitor tweets call

print('\n\ntype of results:', type(results)) 
print('\nnum type(statuses)ber of results:', len(results)) 
print('\ntype of results elements:', type(results[0]))  


# In[5]:



# -------------------------------------
# working with JSON files composed of multiple JSON objects
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as a JSON object on a separate line
item_count = 0  # initialize count of objects dumped to file
with open(json_filename_t, 'w') as outfile:
    for dict_item in results:
        json.dump(dict_item, outfile, encoding = 'utf-8')
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between items
                     
# -------------------------------------
# working with text file for reviewing multiple JSON objects
# this text file will show the full contents of each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as group of lines printed with indentation
item_count = 0  # initialize count of objects dumped to file
with open(full_text_filename_t, 'w') as outfile:
    for dict_item in results:
        outfile.write('Item index: ' + str(item_count) +             ' -----------------------------------------' + line_termination)
        # indent for pretty printing
        outfile.write(json.dumps(dict_item, indent = 4))  
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between items  
        
# -------------------------------------
# working with text file for reviewing text from multiple JSON objects
# this text file will show only the text from each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that the text of each tweet 
# is written to a separate line in the output text file
item_count = 0  # initialize count of objects dumped to file
with open(partial_text_filename_t, 'w') as outfile:
    for dict_item in results:
        outfile.write(json.dumps(dict_item['text']))
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between text items  

# -------------------------------------
# working with JSON files composed of multiple JSON objects
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as a JSON object on a separate line
item_count = 0  # initialize count of objects dumped to file
with open(json_filename_u, 'w') as outfile:
    for dict_item in results:
        json.dump(dict_item, outfile, encoding = 'utf-8')
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between items
                     
# -------------------------------------
# working with text file for reviewing multiple JSON objects
# this text file will show the full contents of each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that each dictionary item
# is written as group of lines printed with indentation
item_count = 0  # initialize count of objects dumped to file
with open(full_text_filename_u, 'w') as outfile:
    for dict_item in results:
        outfile.write('Item index: ' + str(item_count) +             ' -----------------------------------------' + line_termination)
        # indent for pretty printing
        outfile.write(json.dumps(dict_item, indent = 4))  
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between items  
        
# -------------------------------------
# working with text file for reviewing text from multiple JSON objects
# this text file will show only the text from each tweet
# results is a list of dictionary items obtained from twitter
# these functions assume that the text of each tweet 
# is written to a separate line in the output text file
item_count = 0  # initialize count of objects dumped to file
with open(partial_text_filename_u, 'w') as outfile:
    for dict_item in results:
        outfile.write(json.dumps(dict_item['text']))
        item_count = item_count + 1
        if item_count < len(results):
             outfile.write(line_termination)  # new line between text items  

