'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://root:'xxxyyxx'@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

pprint(f"Columns in film table: \n {film.columns.keys()}")
pprint(f"Columns in category table: \n {category.columns.keys()}")
