import configparser

import click


def init_config(path_config: str):
    config = configparser.ConfigParser()
    config["feed"] = {}
    config["cache"] = {
        "cachefile": "config/json2social.db",
        "cache_limit": "10000",
    }
    config.read(path_config)
    try:
        config["feed"]["uri"]
    except KeyError:
        config["feed"]["uri"] = input("The URI of the feed\n")
    with open(path_config, "w") as configfile:
        config.write(configfile)
    sections = config.sections()
    if all(["twitter" not in sections, "mastodon" not in sections]):
        click.echo(
            "You need to set the twitter config or the mastodon config for working"
        )
    return config
