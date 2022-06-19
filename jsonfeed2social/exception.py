class JsonFeed2SocialEcxception(Exception):
    pass


class FildNotInData(JsonFeed2SocialEcxception):
    pass


class MastodonException(JsonFeed2SocialEcxception):
    pass
