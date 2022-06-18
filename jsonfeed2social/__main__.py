import requests

url = "https://fundor333.com/index.json"


class JsonFeed2SocialEcxception(Exception):
    pass


def elaborate_feed(feed: str, element: dict) -> list:
    r = requests.get(feed).json()
    for e in r.json().keys():
        for a in e:
            print(a)
