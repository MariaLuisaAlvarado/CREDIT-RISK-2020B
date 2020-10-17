from fintools.settings import get_logger

logger = get_logger(name="__main__")


class Main:

    @staticmethod
    def show(file: str) -> str:
        logger.info("Calling the show method.")
        with open(file, 'w') as f:
            f.read()
