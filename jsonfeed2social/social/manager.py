from configparser import ConfigParser

from jsonfeed2social.jsonfeed import ManagerFeed
from jsonfeed2social.social.mastodon import mastodon_sender


def sender(config: ConfigParser, populatecache: bool):
    feed = ManagerFeed(config["feed"]["uri"])
    try:
        with open(config["cache"]["cachefile"]) as file:
            raw_lines = file.readlines()
    except FileNotFoundError:
        raw_lines = []
    lines = []
    for e in raw_lines:
        lines.append(e.strip())
    news, id_list = feed.get_to_publish(lines)
    print(id_list)
    if len(news) > 0:
        with open(config["cache"]["cachefile"], "a+") as file:
            file.write(id_list)
        if not populatecache:
            # We can send the message
            # twitter_sender(config, news)
            mastodon_sender(config, news)
