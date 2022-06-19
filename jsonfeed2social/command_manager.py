import click

from jsonfeed2social.config import init_config


@click.command()
@click.option("--config", default="config.ini", help="Path to the config file")
def runner(config):
    click.echo(config)
    config = init_config(config)
