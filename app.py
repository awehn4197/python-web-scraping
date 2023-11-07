import tweepy
from tweepy import OAuthHandler

# consumer_key = 'TelDbWqUd9d1XbJpNlyxblH6Q'
# consumer_secret = 'JXS6pQCy6PbGnsDNheLvl13TyZxQDDHpoFKWHnYeozk8oXuBY3'
# access_token = '1542282446607208449-V3n3cz69ejLOTcKIe9G8SUR3jsJLxq'
# access_secret = 'lmizTfF6ZO5Iiu4k514crIamnST7Q3RfA2Po8MXAul6oT'

dict_twitter_api = {
    "consumer_key": "TelDbWqUd9d1XbJpNlyxblH6Q",
    "consumer_secret": "JXS6pQCy6PbGnsDNheLvl13TyZxQDDHpoFKWHnYeozk8oXuBY3",
    "access_token": "1542282446607208449-V3n3cz69ejLOTcKIe9G8SUR3jsJLxq", 
    "access_token_secret": "lmizTfF6ZO5Iiu4k514crIamnST7Q3RfA2Po8MXAul6oT"
}

client = tweepy.Client(**dict_twitter_api)

print(client.get_me())
# print(client.get_home_timeline())

# bearer_token=None
# client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_secret)

# client.get_me()
# client.create_tweet(text="Hello Twitter! This tweet brought to you by Python + Tweepy")

# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)

object_methods = [method_name for method_name in dir(client.get_me())
                  if callable(getattr(client.get_me(), method_name))]

for mthd in object_methods:
  print(mthd)

# print(object_methods)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)