import sys

from tweepy import Stream, OAuthHandler, API
from tweepy.streaming import StreamListener

from creds import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_SECRET, CONSUMER_KEY

def processing(text):
    '''
    Text processing
    '''
    return text

class Listener(StreamListener):
    def __init__(self, output_file):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        print(processing(status.text), file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return False

if __name__ == "__main__":
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(auth)
    listener = Listener(sys.stdout)
    stream = Stream(auth=api.auth, listener=listener)
    stream.filter(track=['barcelona', 'sevilla'])
