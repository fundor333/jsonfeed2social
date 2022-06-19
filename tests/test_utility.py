from unittest import TestCase

from jsonfeed2social.exception import FildNotInData
from jsonfeed2social.utility import get_message


class UtilityTester(TestCase):
    def test(self):
        message = get_message(
            {
                "titolo": "Titolo",
                "corpo": "Corpo",
                "link": "Link",
                "tags": ["tag1", "tag2", "tag3"],
            },
            "{{titolo}} - {{corpo}} - {{link}} {{tags}}",
        )
        self.assertEqual(message, "Titolo - Corpo - Link #tag1 #tag2 #tag3")

        message = get_message(
            {
                "titolo": "Titolo",
                "corpo": "Corpo",
                "link": "Link",
                "tags": ["tag1", "tag2", "tag3"],
            },
            "{{titolo}} - {{corpo[:4]}} - {{link}} {{tags}}",
        )
        self.assertEqual(message, "Titolo - Corp - Link #tag1 #tag2 #tag3")
        with self.assertRaises(FildNotInData):
            get_message(
                {
                    "titolo": "Titolo",
                    "link": "Link",
                    "tags": ["tag1", "tag2", "tag3"],
                },
                "{{titolo}} - {{corpo}} - {{link}} {{tags}}",
            )
