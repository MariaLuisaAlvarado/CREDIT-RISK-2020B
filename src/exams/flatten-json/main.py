import json
from fintools.settings import get_logger
from .utils import flatten_dict
logger = get_logger(name="__main__")


class Main:

    @staticmethod
    def show(file: str) -> str:
        logger.info("Calling the show method.")
        with open(file, 'r') as f:
            return json.loads(f.read())

    @staticmethod
    def flatten(file):
        return flatten_dict(file)
