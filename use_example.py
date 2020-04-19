import GetOldTweets3 as got
from scraper import TweetMiner
from processor import Processor

import pandas as pd

# Initialize Miner
tm = TweetMiner()

tm.set_criteria(query_text='#trump', limit=5)

# tweets = tm.get_tweets()

i = 1
tweets = pd.read_csv('data/test2.csv')
print(tweets.iloc[i]['text'])

pr = Processor()
processed_tweets = pr.process_tweets(
  tweets,
  to_lowercase=True,
  # remove_punctuation=True,
  # normalize=True,
  # tokenize=True
  )
print(processed_tweets.iloc[i]['processed_text'])
