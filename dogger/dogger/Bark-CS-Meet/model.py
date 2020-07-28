from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
class Dog(Base):
	__tablename__ ="Dogs"
	id = Column(Integer,primary_key=True)
	fname = Column(String)
	lname = Column(String)
	email = Column(String)
	phone = Column(String)
	desc = Column(String)
	def __repr__(self):
		return("First Name: {}\n"
				"Last Name: {}\n"
				"Email : {}\n"
				"Phone Number : {}\n"
				"Description :").format(
				self.fname,
				self.lname,
				self.email,
				self.phone,
				self.desc)
			