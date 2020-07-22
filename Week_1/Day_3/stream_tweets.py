#!/usr/bin/env python
# coding: utf-8

# In[2]:


import twitter
import os
import requests
import json


# **Task:** Load the values of access tokens and keys from environmental variables to python variables



consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_KEY_SECRET']
access_token =  os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']



api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)





# Checking the type of api object
print(type(api))


# In[36]:


## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
FILTER = [':)']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']


def main(location='C:/Users/jcoch/Data',name='output'):
    save_path = os.path.join(location,name+'.txt')
    with open(save_path, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')


# In[37]:


# Execute function
main()


# **Task:** Edit function `main` so it can store tweets anywhere (location specified as parameter). The FILTER and LANGUAGES should be parameters as well. Test it with different values and languages.

# **Task:** Create File `stream_tweets.py` that can be executed from the Terminal

# **Task:** Start storing tweets with either happy smiley (`:)`) or sad smiley (`:(`). We will use this dataset during the NLP section.

# In[31]:




