import json
import logging
from urllib.error import HTTPError
from urllib.request import urlopen

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG
)
settings_url = 'your url here'


def get(name: str) -> str:
    url = settings_url + name
    try:
        with urlopen(url) as r:
            resp = json.load(r)
    except HTTPError as e:
        logging.error(f'Could not load settings: {e=}, {url=}, {name=}')
        return None
    return resp[name.upper()]


print(get('TG_CHAT_ID'))
