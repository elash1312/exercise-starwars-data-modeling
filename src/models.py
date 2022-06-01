import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(80), nullable=False)
    UserFavorites = relationship('user_favorites',)

class UserFavorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(80))
    character_name = Column(String(80))
    users_favorited = relationship(User, secondary='user_favorites', viewonly=True)

    def to_dict(self):
        return {
            "planet": self.planet_name,
            "character": self.character_name}

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(80))
    character_height = Column(String(80))
    character_hair_color = Column(String(80))
    character_eye_color = Column(String(80))
    User = relationship(User, secondary='user_favorites', viewonly=True)

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(80))
    planet_rotation_period = Column(String(80))
    planet_orbital_period = Column(String(80))
    planet_terrain = Column(String(80))
    User = relationship(User, secondary='user_favorites', viewonly=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')