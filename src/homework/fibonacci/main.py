from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit, method_caching

logger = get_logger(name=__name__)

class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @method_caching
    def element(self, position: int) -> int:
        if position <= 1:
            return position
        else:
            return self.element(position - 1) + self.element(position - 2)

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        for i in range(length):
            print(self.element(i))
