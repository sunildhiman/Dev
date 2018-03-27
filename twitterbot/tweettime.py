
# coding: utf-8

# In[1]:


import tweepy


# In[2]:


#import pandas as pd
#import numpy as np


# In[8]:


#import requests
#import os
import datetime
#import time


# In[9]:



def tweetHelloWorld():
    api = get_twitter_client()
    res=api.update_status(str(datetime.datetime.now()))
    return res


# In[10]:


# twitter client
def get_twitter_client():
    consumer_key = '*******'
    consumer_secret = '***************8'
    
    access_token = '*****************-***************8'
    access_token_secret = '******************8'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


# In[11]:


#tweetHelloWorld(get_twitter_client())

