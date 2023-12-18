import requests
import logging
from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from logging_config import setup_logger

from config import host, user, password, db_name

# Настройка логгера
setup_logger()

Base = declarative_base()


# Определение модели для таблицы новостей
class News(Base):
    __tablename__ = "news_table"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    genre = Column(String(50))
    continent = Column(String(50))
    event_date = Column(Date)
    content = Column(Text)


# api key NYT
api_key = "cAzgZfj16AqOdXcmXA5RQyk8kyfRyaAA"

# database connection
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{db_name}", echo=False
)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}"
    response = requests.get(url)

    # Проверка кода
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])

        for article in articles:
            title = article.get("title")
            genre = article.get("section")
            date = article.get("published_date")
            text = article.get("abstract")

            # Проверяем, существуют ли данные с таким же заголовком в базе данных
            existing_data = session.query(News).filter(News.title == title).first()

            if not existing_data:
                new_article = News(
                    title=title,
                    genre=genre,
                    continent="Unknown",
                    event_date=date,
                    content=text,
                )
                session.add(new_article)

        session.commit()
        logging.info("Data inserted successfully")

except Exception as ex:
    logging.error("Error during processing")
    logging.error(ex)

finally:
    session.close()
