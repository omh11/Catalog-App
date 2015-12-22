import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Define the Sport Category Table
# Sport Names are unique thus chosen as a primary key


class SportCategory(Base):

    __tablename__ = 'sport_category'
    name = Column(String(80), primary_key=True)
    id = Column(Integer)

# Define the Sport Item Table
# Timestamp added to identfy the latest items


class SportItem(Base):
    __tablename__ = 'sport_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    description = Column(String(1000))
    user_id = Column(String(80))
    time = Column(DateTime(False))
    sport_category_name = Column(Integer, ForeignKey('sport_category.name'))
    sport_category = relationship(SportCategory)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.create_all(engine)
