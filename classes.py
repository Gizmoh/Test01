import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class user(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String)

	Character = relationship("player", backref="user", cascade="all, delete, delete-orphan")

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<User('%s','%s','%s')>" %(self.name)

class player(Base):
	__tablename__='Character'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	level = Column(Integer)
	id_user = Column(Integer, ForeignKey('users.id'))

	def __init__(self, name, user):
		self.name = name
		self.level = 0
		self.id_user = user