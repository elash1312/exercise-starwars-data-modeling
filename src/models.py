import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# class Parent(Base):
#     __tablename__ = "parent"
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")


# class Child(Base):
#     __tablename__ = "child"
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey("parent.id"))

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(80), nullable=False)
    favorites = relationship('Favorites')

class UserFavorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey("User.id"))

    def to_dict(self):
        return {
            "name": self.name,
            }

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
        return {
            "name": self.character_name,
            "height": self.character_height,
            "hair color": self.character_hair_color,
            "eye color": self.character_eye_color
        }

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
        return {
            "name": self.planet_name,
            "rotation period": self.planet_rotation_period,
            "orbital period": self.planet_orbital_period,
            "terrain": self.planet_terrain
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')