from requests import *
from pyuseragents import random as random_useragent
from bs4 import BeautifulSoup
from getSession import Accounts


class Bot(Accounts):
    def __init__(self, SubscribeQueryId, RetweetQueryId, LikeQueryId,
                 CommentQueryId, FollowQueryId, TweetQueryId):
        self.SubscribeQueryId = SubscribeQueryId
        self.RetweetQueryId = RetweetQueryId
        self.LikeQueryId = LikeQueryId
        self.CommentQueryId = CommentQueryId
        self.FollowQueryId = FollowQueryId
        self.TweetQueryId = TweetQueryId

    def getvalues(self):
        for _ in range(15):
            r = self.session.get('https://twitter.com/home', verify=False)
            url_to_get_query_ids = BeautifulSoup(r.text, 'lxml') \
                .find_all('link',
                          {'rel': 'preload', 'as': 'script', 'crossorigin': 'anonymous'})[-1] \
                .get('href')

            r = self.session.get(url_to_get_query_ids, verify=False)
            self.SubscribeQueryId = r.text.split('",operationName:"TweetResultByRestId')[0] \
                .split('"')[-1]
            self.RetweetQueryId = r.text.split('",operationName:"CreateRetweet')[0] \
                .split('"')[-1]
            self.LikeQueryId = r.text.split('",operationName:"FavoriteTweet')[0] \
                .split('"')[-1]
            self.CommentQueryId = r.text.split('",operationName:"CreateTweet"')[0] \
                .split('"')[-1]
            self.FollowQueryId = r.text.split('",operationName:"Followers')[0] \
                .split('"')[-1]
            self.TweetQueryId = r.text.split('",operationName:"CreateTweet"')[0] \
                .split('"')[-1]