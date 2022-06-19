from configparser import ConfigParser

import requests

from jsonfeed2social.exception import MastodonException
from jsonfeed2social.utility import get_message


def send_toot(tweet: str, host_instance: str, token: str):
    headers = {}
    headers["Authorization"] = "Bearer " + token
    data = {}
    data["status"] = tweet
    data["visibility"] = "public"

    response = requests.post(
        url=host_instance + "/api/v1/statuses", data=data, headers=headers
    )
    if response.status_code == 200:
        return True
    else:
        raise MastodonException(
            f"Status return {response.status_code} - {response.json()}"
        )


def mastodon_sender(config: ConfigParser, news: list):
    for e in news:
        send_toot(
            get_message(e, config["feed"]["toot"]),
            config["mastodon"]["instance_url"],
            config["mastodon"]["mastodon_access_token"],
        )
