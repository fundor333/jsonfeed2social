import configparser


def init_config(path_config: str):
    config = configparser.ConfigParser()
    config["cache"] = {
        "cachefile": "/json2social/json2social.db",
        "cache_limit": "10000",
    }
    config.read(path_config)
    with open(path_config, "w") as configfile:
        config.write(configfile)
    return config
