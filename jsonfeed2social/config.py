import configparser


def init_config(path_config: None):
    config = configparser.ConfigParser()
    if path_config is not None:
        config.read("config.ini")
    return config
