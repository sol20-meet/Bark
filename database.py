from model import *
# import sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from IPython.core import get_ipython

# hist = get_ipython().history_manager
# hist.db = sqlite3.connect(hist.hist_file , check_same_thread = False)



engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
# session = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_dog(fname,lname,phone,email,desc):
	dog_obj = Dog(
		first_name = fname,
		last_name = lname,
		phone_number = phone,
		email = email,
		description = desc)
	session.add(dog_obj)
	session.commit()

def query_all():
	Dogs = session.query(Dog).all()
	return Dogs
