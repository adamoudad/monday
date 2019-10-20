from tweepy import Stream, OAuthHandler, API
from tweepy.streaming import StreamListener

# from creds import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY

class Tweet:
    def __init__(self, text):
        self.stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER','URL'])
        self.text = text
    def __str__(self):
        return self.text
    def process(self):
        '''
        Text processing
        '''
        processed = self.text.lower()
        processed = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', processed) # remove URLs
        processed = re.sub('@[^\s]+', 'AT_USER', processed) # remove usernames
        processed = re.sub(r'#([^\s]+)', r'\1', processed) # remove the # in #hashtag
        return processed

    def tokenize(self):
        tokens = word_tokenize(self.process()) # remove repeated characters (helloooooooo into hello)
        return [word for word in tokens if word not in self.stopwords]

class Listener(StreamListener):
    def __init__(self, output_file):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        tweet = Tweet(status.text)
        print(tweet.text + "-"*30 + tweet.process() + "-"*30, file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return False

if __name__ == "__main__":
    # auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = API(auth)
    # listener = Listener(sys.stdout)
    # stream = Stream(auth=api.auth, listener=listener)
    # stream.filter(track=['barcelona', 'sevilla'])
