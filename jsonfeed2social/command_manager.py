import click

from jsonfeed2social.config import init_config
from jsonfeed2social.jsonfeed import ManagerFeed
from jsonfeed2social.social.manager import sender


@click.group()
def cli():
    pass


@cli.command()
@click.option("--config", default="config.ini", help="Path to the config file")
@click.option("--populatecache", default=False, help="Populate the cache")
def run(config, populatecache):
    config = init_config(config)
    sections = config.sections()
    if all(["twitter" not in sections, "mastodon" not in sections]):
        click.echo(
            "You need to set the twitter config or the mastodon config for working"
        )
    sender(config, populatecache)


@cli.command()
@click.option("--config", default="config.ini", help="Path to the config file")
@click.option(
    "--consumer_key",
    prompt="Yout twitter consumer key",
    help="Yout twitter consumer key",
)
@click.option(
    "--consumer_secret",
    prompt="Your twitter consumer secret",
    help="Your twitter consumer secret",
)
@click.option(
    "--access_token",
    prompt="Your twitter access token",
    help="Your twitter access token",
)
@click.option(
    "--access_token_secret",
    prompt="Your twitter token secret",
    help="Your twitter token secret",
)
def twitter(
    config, consumer_key, consumer_secret, access_token, access_token_secret
):
    config_path = config
    config = init_config(config_path)
    config["twitter"] = {
        "twitter_consumer_key": consumer_key,
        "twitter_consumer_secret": consumer_secret,
        "twitter_access_token": access_token,
        "twitter_access_token_secret": access_token_secret,
    }
    with open(config_path, "w") as configfile:
        config.write(configfile)


@cli.command("feed-sections")
@click.option("--config", default="config.ini", help="Path to the config file")
def feed_sections(config):
    config_path = config
    config = init_config(config_path)
    feed = ManagerFeed(config["feed"]["uri"])
    data = feed.feed_sections
    click.echo(f"The following sections are available in this feed {data}")
