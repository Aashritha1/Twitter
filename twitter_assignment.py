from wordcloud import WordCloud,STOPWORDS
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as Pd

consumerkey = 'G72Xr0wwOdlbMsahqrOdFPQOi'
consumersecret = 'pRHJNI4dOkOZwKXaIUS7tJV2EWJRK02eFPhu4Tv2nSaxKJRpHJ'
accesstoken = '772434266974072833-LytKJlE6iXZWP6R3JnItPlExYDvwun7'
accesssecret = 'm6Df2P4p3vHbMnFAItzEGt7agkozCIma2H3GTfZTwJ1U2'
auth = OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesssecret)
api = tweepy.API(auth)
twit = Cursor(api.search, q='earth').items(300)
twit_data = []
for each in twit:
    twit_data.append(json.loads(json.dumps(each._json)))
tweets = Pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), twit_data)

twit_text=" ".join([each for each in tweets['text'] if each.startswith('@')==False and each.startswith("http")==False])

f=open("twit.txt","a")
f.write(twit_text)
f.close()

s=set(STOPWORDS)
s.add("is")
s.add("are")
s.add("might")
s.add("may")
s.add("be")
s.add("then")
s.add("past")
wc=WordCloud(background_color="black",prefer_horizontal=1,stopwords=s)
wc.generate(twit_text)
wc.to_file("monster.gif")
wc.to_image().show()