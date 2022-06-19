import requests as requests

url = "https://fundor333.com/index.json"


class ManagerFeed:
    def __init__(self, feed_url: str):
        self._feed = requests.get(feed_url).json()
        self._item_feed = []
        self._feed_sections = []

    @property
    def item_feed(self):
        self._item_feed = self._feed["items"]
        return self._item_feed

    @property
    def feed_sections(self) -> set:
        self._feed_sections = set().union(*(d.keys() for d in self.item_feed))
        return self._feed_sections

    def elaborate_feed(self) -> dict:
        out = {}
        for e in self.item_feed:
            dict_you_want = {
                your_key: e.get(your_key, None)
                for your_key in self.feed_sections
            }
            out[dict_you_want["id"]] = dict_you_want
        return out

    def get_to_publish(
        self,
        list_done: list,
    ) -> (list, str):
        full_list = self.elaborate_feed()
        out = []
        other = ""
        for e in full_list.keys():
            if e not in list_done and f"{e}\n" not in list_done:
                out.append(full_list.get(e))
                other += f"\n{e}"
        return out, other.strip()
