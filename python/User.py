import pymysql
from config import host, user, password, db_name
import logging

# Настройка логгера
logging.basicConfig(
    filename="../app.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class User:
    def __init__(self, nickname):
        self.nickname = nickname
        self.files = []

    def add_files(self, file_path):
        self.files.append(file_path)

    def get_files(self):
        return self.files


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            return None

    def write_file(self, content):
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")


try:
    connection = pymysql.Connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    logging.info("Connect for user success")

    try:
        with connection.cursor() as cursor:
            create_table_user = """
                CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                files TEXT
                );
                """
            cursor.execute(create_table_user)
            logging.info("Table for user created")
        connection.commit()
    except Exception as ex:
        logging.error(ex)
except Exception as ex:
    logging.error(ex)
# Создание пользователя
user = User("nickname_example")

# Добавление файла к пользователю
user.add_files("/path/to/file.txt")

# Работа с файлом
file_handler = File("/path/to/file.txt")
content = file_handler.read_file()
print(content)  # Вывод содержимого файла
file_handler.write_file("Новое содержимое")  # Запись в файл
