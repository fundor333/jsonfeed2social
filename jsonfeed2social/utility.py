import re

from jinja2 import Template
from jinja2 import Environment, meta

from jsonfeed2social.exception import FildNotInData


def get_message(data_old: dict, message_format: str):
    data = data_old
    env = Environment()
    ast = env.parse(message_format)
    for e in meta.find_undeclared_variables(ast):
        if not data.get(e, False) and e != "tags":
            raise FildNotInData(f"You need {e} for the message")
    if "tags" in data:
        tags = ""
        for e in data["tags"]:
            tag = re.sub(r"[^a-zA-Z0-9]", "", e)
            tags += f"#{tag} "
        data["tags"] = tags.strip()
    rtemplate = Template(message_format)
    data = rtemplate.render(**data)
    return data
