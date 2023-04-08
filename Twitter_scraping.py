#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Importing necessary libraries
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating an empty list to store scraped tweets
TWEET_LIST1 = []

# Scraping tweets using snscrape TwitterSearchScraper
for tweet in (sntwitter.TwitterSearchScraper('Netflix india lang:en since:2022-09-01 until:2023-03-01').get_items()):
    if len (TWEET_LIST1)== 1000:
        break
    # Appending tweet information to the tweet list
    TWEET_LIST1.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source])

# Converting the tweet list into a pandas DataFrame
df = pd.DataFrame(TWEET_LIST1, columns=['DATE', 'ID', 'URL', 'CONTENT', 'USER', 'REPLY_COUNT', 'RETWEET_COUNT', 'LANGUAGE', 'SOURCE'])

# Saving the DataFrame to a CSV file
df.to_csv('twitter_scrapping_Netflixn.csv', index=False)


# In[ ]:




