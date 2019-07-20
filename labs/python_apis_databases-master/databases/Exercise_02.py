'''
Using sqlalchemy which the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of you choice comedy

- Select all the comedic films and that and sort them by rental rate

- Using one of the statements above, add a GROUP BY

- Using on of the statements above, add a ORDER BY

'''
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://root:'xxxyyxx'@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
join_statement1 = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
join_statement2 = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film_category, film_category.columns.film_id == film_actor.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
join_statement3 = film.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
query1 = sqlalchemy.select([actor]).where(actor.columns.first_name == 'JOHN')
query2 = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, film.columns.title]).select_from(join_statement1)
query3 = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, category.columns.name]).select_from(join_statement2).where(category.columns.name == 'Comedy')
query4 = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).select_from(join_statement3).where(category.columns.name == 'Comedy').group_by(film.columns.film_id).order_by(sqlalchemy.asc(film.columns.rental_rate))
result_proxy = connection.execute(query4)
result_final = result_proxy.fetchall()
pprint(result_final)
