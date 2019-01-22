from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_link(type,subject,link): ####creats the links I actually need
	link_object = Link(type=type, subject=subject,link=link)##### an object - instant of the class in the model.py
	session.add(link_object)### adds the instant above to the databases
    session.commit()##### ACTUALLY ADDS THE INSTANT 

def get_all_links_with_the_specific_type(type, subject):#all the links in the database with the specific type that I was looking for
	links = session.query(Link).all() ###filters ?????
	list_randomname=[] ############## empty list
	for link in links:#### takes one link fro the list of links that was returned
		if (link.type==type and link.subject==subject): ### if the type  of the link (visual....) is the same as the type thet I were liiking for AND the subject is the same as I was looking for ------ do somwthing 
				list_randomname.append(link) ####adds the good links (the ones that answers to the conditions above) to the list above that ill return in the end --- the links that i was looking for : visual,math:....few links


	return list_randomname
