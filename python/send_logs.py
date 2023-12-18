import logging
from logging.handlers import SocketHandler


def setup_logger(
    log_filename="app.log",
    max_log_size=5 * 1024 * 1024,
    backup_count=5,
    use_socket_handler=False,
):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    if use_socket_handler:
        # Создание SocketHandler для отправки логов на локальный сокет
        handler = SocketHandler("localhost", 9000)
    else:
        # Создание RotatingFileHandler
        handler = logging.handlers.RotatingFileHandler(
            log_filename, maxBytes=max_log_size, backupCount=backup_count
        )

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)


if __name__ == "__main__":
    setup_logger(use_socket_handler=True)
    logger = logging.getLogger()
    logger.info("Hello, logging world!")
