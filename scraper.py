import sys
import codecs
import pandas as pd
import GetOldTweets3 as got


class TweetMiner():

    def __init__(self):
        self.criteria = got.manager.TweetCriteria()

    def set_criteria(
        self,
        query_text=None,
        limit=None,
        since=None,
        until=None,
        username=None,
    ):
        """Pass tweet criteria to got"""
        if query_text is not None:
            self.criteria = self.criteria.setQuerySearch(query_text)

        if limit is not None:
            self.criteria = self.criteria.setMaxTweets(limit)

        if since is not None:
            self.criteria = self.criteria.setSince(since)

        if until is not None:
            self.criteria = self.criteria.setUntil(until)

        if username is not None:
            self.criteria = self.criteria.setUsername(username)

        if list(self.criteria.__dict__.keys()) == [
            'maxTweets',
            'topTweets',
            'within',
            'emoji'
                ]:
            print('No criteria options supplied.')
            print('Available Criteria:')
            print('\tquery_text(str)')
            print('\tlimit(int)')
            print('\tsince(str)')
            print('\tuntil(str)')
            print('\tusername(str)')
            sys.exit()

        return self

    def get_tweets(self, to_file=None):
        tweets = got.manager.TweetManager.getTweets(self.criteria)

        tweet_df = pd.DataFrame(
            list(map(lambda tweet: tweet.__dict__, tweets))
            )

        if to_file is not None:
            tweet_df.to_csv(to_file, index=False)

        return tweet_df
