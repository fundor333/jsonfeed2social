import tweepy


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
