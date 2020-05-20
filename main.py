from handler import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    #tweets = api.user_timeline(screen_name = "wojespn", count=200)
    tweets = api.search(q = "coronavirus", result_type = "recent", count = 100);
    df = tweet_analyzer.tweets_to_data_frame(tweets)
     
    print(df.head(10))
    #df.plot(x = 'likes', y = 'RT', kind = 'scatter')
    #plt.show()


