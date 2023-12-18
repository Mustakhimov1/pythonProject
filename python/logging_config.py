import logging
from logging.handlers import RotatingFileHandler


def setup_logger(
    log_filename="app.log",
    max_log_size=5 * 1024 * 1024,
    backup_count=5
):
    # Удалить все существующие обработчики логгера
    logging.getLogger().handlers = []

    # Настройка логгера для вывода в файл
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Создание RotatingFileHandler
    file_handler = RotatingFileHandler(
        log_filename, maxBytes=max_log_size, backupCount=backup_count
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Добавление RotatingFileHandler в логгер
    logger.addHandler(file_handler)


# Это нужно, чтобы при импорте файла настройка логгера выполнялась автоматически
setup_logger()
