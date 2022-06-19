from configparser import ConfigParser

from jsonfeed2social.jsonfeed import ManagerFeed
from jsonfeed2social.social.mastodon import mastodon_sender
from jsonfeed2social.social.twitter import twitter_sender


def sender(config: ConfigParser, populatecache: bool):
    feed = ManagerFeed(config["feed"]["uri"])
    try:
        with open(config["cache"]["cachefile"]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    news, id_list = feed.get_to_publish(lines)
    if len(news) > 0:
        with open(config["cache"]["cachefile"], "a+") as file:
            file.write(id_list)
        if not populatecache:
            # We can send the message
            news, id_list = feed.get_to_publish(lines)
            try:
                config["feed"]["tweet"]
                twitter_sender(config, news)
            except KeyError:
                pass
            news, id_list = feed.get_to_publish(lines)
            try:
                config["feed"]["toot"]
                mastodon_sender(config, news)
            except KeyError:
                pass
