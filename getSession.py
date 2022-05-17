from requests import *
from pyuseragents import random as random_useragent


class Accounts:
    def __init__(self, current_cookie, current_proxy):
        self.current_cookie = current_cookie
        self.current_proxy = current_proxy
        self.session = Session()
        self.session.headers.update({
            'user-agent': random_useragent(),
            'Origin': 'https://mobile.twitter.com',
            'Referer': 'https://mobile.twitter.com/',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            'content-type': 'application/json'})
