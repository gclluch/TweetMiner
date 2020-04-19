import re
import pandas
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


class Processor():

    def __init__(self):
        self._stopwords = set(
            stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL']
            )

    def process_tweets(
        self,
        tweets,
        normalize=False,
        remove_hashtags=False,
        remove_punctuation=False,
        remove_stopwords=False,
        to_lowercase=False
    ):

        options = {
            'normalize': normalize,
            'remove_hashtags': remove_hashtags,
            'remove_punctuation': remove_punctuation,
            'remove_stopwords': remove_stopwords,
            'to_lowercase': to_lowercase
        }

        tweets = tweets.apply(
            lambda row: self._process(row, options),
            axis=1)

        return tweets

    def _process(self, row, options):
        normalize = options.get('normalize')
        remove_hashtags = options.get('remove_hashtags')
        remove_punctuation = options.get('remove_punctuation')
        remove_stopwords = options.get('remove_stopwords')
        to_lowercase = options.get('to_lowercase')

        row['processed_text'] = self._remove_URL(row['text'])
        row['processed_text'] = self._remove_hash(row['processed_text'])
        row['processed_text'] = self._remove_usernames(row['processed_text'])

        if to_lowercase:
            row['processed_text'] = row['processed_text'].lower()

        if remove_punctuation:
            row['processed_text'] = self._remove_punctuation(
                row['processed_text']
                )

        row['processed_text'] = self._remove_stopwords(row['processed_text'])

        return row

    def _remove_hash(self, text):
        return re.sub(r'#([^\s]+)', r'\1', text)

    def _remove_punctuation(self, text):
        nopunc = [char for char in text if char not in punctuation]
        return ''.join(nopunc)

    def _remove_stopwords(self, text):
        return  ' '.join([word for word in text.split() if word not in self._stopwords])


    def _remove_URL(self, text):
        return re.sub('((www\.[^r\s]+)|(https?://[^\rs]+))', 'URL', text)

    def _remove_usernames(self, text):
        return re.sub('@[^\s]+', 'AT_USER', text)