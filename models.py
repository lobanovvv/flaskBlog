from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship
import re


engine = create_engine("sqlite:///sqlite.db", future=True)
session = sessionmaker(bind=engine, future=True)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


class Posts(Base):
    __tablename__ = "Posts"

    # @classmethod
    # def get_slug(cls):
    #     return re.sub(r"\W", "-", cls.title)

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    body = Column(Text)
    # slug = get_slug()

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f"id: {self.id} title: {self.title}"
