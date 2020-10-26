import os
import json
from typing import Dict

from fintools.settings import get_logger
from fintools.utils import StringWrapper, timeit

from .settings import (
    INDUSTRY_SEARCH_DEFAULT_FILENAME,
    INDUSTRY_SEARCH_DEFAULT_THRESHOLD
)

logger = get_logger(name=__name__)


class Main:
    threshold = INDUSTRY_SEARCH_DEFAULT_THRESHOLD

    @staticmethod
    def read_dict(file: str = INDUSTRY_SEARCH_DEFAULT_FILENAME) -> dict:
        with open(file, 'r') as f:
            jason = f.read()
        dictionary = json.loads(jason)
        return dictionary

    @staticmethod
    def keys(dictionary):
        result = []

        def iterador(obj):
            if type(obj) == dict:
                [iterador(i) for i in obj]
            elif type(obj) == list:
                [iterador(i) for i in obj]
            else:
                result.append(obj)

        iterador(dictionary)
        return result

    @staticmethod
    def items(dictionary):
        result = []

        def iterador(obj):
            if type(obj) == dict:
                [iterador(obj[i]) for i in obj]
            elif type(obj) == list:
                [iterador(i) for i in obj]
            else:
                result.append(obj)

        iterador(dictionary)
        return result

    @timeit(logger=logger)
    def search(self, title: str, exact: bool = False, file: str = INDUSTRY_SEARCH_DEFAULT_FILENAME):
        dictionary = self.read_dict(file)
        keys = str(self.keys(dictionary))
        items = str(self.items(dictionary))
        string_wrapper_keys = StringWrapper(keys, case_sensitive=False)
        string_wrapper_items = StringWrapper(items, case_sensitive=False)
        in_keys = string_wrapper_keys.boolean_search(pattern=title,
                                                     exact=exact,
                                                     threshold=INDUSTRY_SEARCH_DEFAULT_THRESHOLD)
        in_items = string_wrapper_items.boolean_search(pattern=title,
                                                       exact=exact,
                                                       threshold=INDUSTRY_SEARCH_DEFAULT_THRESHOLD)
        if in_keys or in_items is False:
            return print([])
        elif in_keys is True:
            raise Exception("Search title should be a dict item")
        elif in_items is True:
            return print()
