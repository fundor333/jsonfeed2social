import configparser


def init_config(path_config: str):
    config = configparser.ConfigParser()
    config["feed"] = {}
    config["cache"] = {
        "cachefile": "/json2social/json2social.db",
        "cache_limit": "10000",
    }
    config.read(path_config)
    try:
        config["feed"]["uri"]
    except KeyError:
        config["feed"]["uri"] = input("The URI of the feed\n")
    with open(path_config, "w") as configfile:
        config.write(configfile)
    return config
