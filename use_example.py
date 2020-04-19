import GetOldTweets3 as got
from scraper import TweetMiner
from processor import Processor

import pandas as pd

# Initialize Miner
tm = TweetMiner()

tm.set_criteria(query_text='#trump', limit=5)

# tweets = tm.get_tweets()

tweets = pd.read_csv('test2.csv')
print(tweets.iloc[1]['text'])

pr = Processor()
processed_tweets = pr.process_tweets(
  tweets,
  to_lowercase=True)
print(processed_tweets.iloc[1]['processed_text'])
