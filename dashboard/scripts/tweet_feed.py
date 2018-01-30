import tweepy
import sqlite3

# TODO: NEED TO UNPULL TO REMOVE THE SECRET KEY............

CONSUMER_KEY = 'DIVFNO658PjKMozopS1oLMOwo'
CONSUMER_SECRET = 'f8f8waBmcifaoiz0ohfwDMG3YPq0qnKzOL4aSRGBUb3JR2wc6g'
ACCESS_TOKEN = '1536654752-A4oOpKBfNjz0hOlRd0vl7y8DHKN5RlUORpcT0CM'
ACCESS_SECRET = 'yw5HYPaqt7C87jw8lQ1AFH7u9kfYYZL1prRd52YREFvFD'


class UserTweets(object):

    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def get_user_tweets(self, user_id):
        tweet_info = []
        for status in self.api.user_timeline(user_id, count=50):
            urls = status.entities['urls']
            if len(urls) > 0:
                for y in urls:
                    tweet_info.append([status.text, y.get('url')])
            else:
                tweet_info.append([status.text])
        return tweet_info


conn = sqlite3.connect('/Users/Rahul/Desktop/Side_projects/personal/db.sqlite3', check_same_thread=False)
c = conn.cursor()


def execute_tweets():
    c.execute("SELECT MAX(id) FROM dashboard_tweet")
    recent_primary_key = c.fetchone()
    if recent_primary_key[0] is None:
        recent_primary_key = 1
    else:
        recent_primary_key = recent_primary_key[0]
    t = UserTweets()
    timeline = t.get_user_tweets('theduggal07')
    for tweet in timeline:
        recent_primary_key += 1
        c.execute('INSERT INTO dashboard_tweet (id, tweet) VALUES (?, ?)', (recent_primary_key, tweet[0]))
        conn.commit()
