#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullabe=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False)
    max_guest = Column(Integer, nullable=False)
    price_by_night = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
