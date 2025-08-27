from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    _name = Column(String, nullable=False)
    email = Column(String)
    preferences = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    quests = relationship("Quest", back_populates="creator")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._name = value.strip()

    @validates("email")
    def validate_email(self, key, email):
        if email and '@' not in email:
            raise ValueError("Invalid email format")
        return email

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id"))
    _location = Column(String, nullable=False)
    _type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    creator = relationship("User", back_populates="quests")

    QUEST_TYPES = ("Adventure", "Mystery", "History")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value not in self.QUEST_TYPES:
            raise ValueError(f"Type must be one of {self.QUEST_TYPES}")
        self._type = value
   
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        from lib.utils import validate_location
        valid, _ = validate_location(value)
        if not valid:
            raise ValueError(f"Invalid location: {value}")
        self._location = value