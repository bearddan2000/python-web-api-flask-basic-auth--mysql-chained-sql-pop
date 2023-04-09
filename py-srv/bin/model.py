from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DbModel(Base):
    __tablename__ = 'pop'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    color = Column(String())

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"<Pop {self.id}, {self.name}, {self.color}>"
