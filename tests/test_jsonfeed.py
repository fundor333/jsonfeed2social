from unittest.case import TestCase

import requests
from requests.exceptions import MissingSchema

from jsonfeed2social.jsonfeed import ManagerFeed

NEEDED_FIELD = {
    "id",
    "content_text",
    "date_published",
    "image",
    "summary",
    "tags",
    "title",
    "url",
}

TEST_URL = "https://fundor333.com/index.json"
FEED_DATA = requests.get(TEST_URL).json()


class ManagerFeedTester(TestCase):
    def test_exception(self):
        self.assertRaises(MissingSchema, ManagerFeed, "")
        self.assertRaises(MissingSchema, ManagerFeed, None)

    def test_positive(self):
        c = ManagerFeed(TEST_URL)
        self.assertEqual(c.item_feed, FEED_DATA["items"])
        for e in NEEDED_FIELD:
            self.assertTrue(e in c.rss_sections)
        temp_data = c.elaborate_feed()
        lenth_data = len(temp_data.keys())
        not_data = list(temp_data.keys())[: int(lenth_data / 3)]
        self.assertTrue(
            len(c.get_to_publish(not_data)) == lenth_data - len(not_data)
        )
        for e in c.get_to_publish(not_data):
            self.assertTrue(e["id"] is not not_data)
