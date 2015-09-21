# -*- encoding: utf-8 -*-
from requests_oauthlib import OAuth1

from . import settings

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = settings.key
CONSUMER_SECRET = settings.secret
OAUTH_TOKEN = settings.token
OAUTH_TOKEN_SECRET = settings.token_secret


def get_oauth():
    oauth = OAuth1(
        CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=OAUTH_TOKEN,
        resource_owner_secret=OAUTH_TOKEN_SECRET,
    )
    return oauth
