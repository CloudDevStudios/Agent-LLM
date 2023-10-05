import tweepy
from Config import Config
from Commands import Commands

CFG = Config()


class twitter(Commands):
    def __init__(self):
        self.commands = {"Send Tweet": self.send_tweet}

    def send_tweet(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(CFG.TW_CONSUMER_KEY, CFG.TW_CONSUMER_SECRET)
        auth.set_access_token(CFG.TW_ACCESS_TOKEN, CFG.TW_ACCESS_TOKEN_SECRET)

        # Create API object
        api = tweepy.API(auth)

        # Send tweet
        try:
            api.update_status(self)
            print("Tweet sent successfully!")
        except tweepy.TweepyException as e:
            print(f"Error sending tweet: {e.reason}")
