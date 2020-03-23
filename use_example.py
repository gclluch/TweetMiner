import GetOldTweets3 as got
from scraper import TweetMiner

import pandas as pd

# Initialize Miner
tm = TweetMiner()

tm.set_criteria(query_text='#TRUMP', limit=10)

tweets = tm.get_tweets(to_file='test.csv')

# df = pd.read_csv('test.csv')
