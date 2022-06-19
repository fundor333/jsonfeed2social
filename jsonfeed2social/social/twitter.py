from configparser import ConfigParser

import tweepy

from jsonfeed2social.utility import get_message


def send_tweet(
    status: str,
    api_key: str,
    api_secrets: str,
    access_token: str,
    access_secret: str,
):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(status=status)


def twitter_sender(config: ConfigParser, news: list):
    for e in news:
        send_tweet(
            get_message(e, config["feed"]["tweet"]),
            config["twitter"]["twitter_consumer_key"],
            config["twitter"]["twitter_consumer_secret"],
            config["twitter"]["twitter_access_token"],
            config["twitter"]["twitter_access_token_secret"],
        )
