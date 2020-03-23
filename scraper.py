import codecs
import GetOldTweets3 as got
import pandas


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

        return self

    def get_tweets(self, to_file=None):
        tweets = got.manager.TweetManager.getTweets(self.criteria)
        if to_file is not None:
            self.write_csv(to_file, tweets)

        return tweets

    def write_csv(self, to_file, tweets):
        output_file = codecs.open(to_file, "w+", "utf-8")

        output_file.write('username,date,retweets,favorites,text,geo,mentions,hashtags,id,permalink')

        for t in tweets:
            output_file.write(
                ('\n%s,%s,%d,%d,"%s",%s,%s,%s,"%s",%s' %
                 (t.username,
                  t.date.strftime("%Y-%m-%d %H:%M"),
                  t.retweets,
                  t.favorites,
                  t.text,
                  t.geo,
                  t.mentions,
                  t.hashtags,
                  t.id,
                  t.permalink)))

        output_file.flush()
        print('%d raw tweets saved to file...\n' % len(tweets))
        output_file.close()