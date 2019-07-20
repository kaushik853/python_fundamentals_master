'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import requests
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://root:'xxxyyxx'@localhost/employees')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
'''
User_Table = sqlalchemy.Table('users', metadata,
                       sqlalchemy.Column('userId', sqlalchemy.Integer()),
                       sqlalchemy.Column('first_name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('last_name', sqlalchemy.String(255), nullable=True)
              )
Task_Table = sqlalchemy.Table('tasks', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       sqlalchemy.Column('userId', sqlalchemy.Integer()),
                       sqlalchemy.Column('task_name', sqlalchemy.String(255), nullable=False)
              )
metadata.create_all(engine)'''

newTable1 = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
newTable2 = sqlalchemy.Table('tasks', metadata, autoload=True, autoload_with=engine)

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
for item in response.json()['data']:
    query = sqlalchemy.insert(newTable1).values(userId=item['id'], first_name=item['first_name'], last_name=item['last_name'])
    result_proxy = connection.execute(query)

base_url2 = "http://demo.codingnomads.co:8080/tasks_api/tasks"
response2 = requests.get(base_url2)

for item in response2.json()['data']:
    query = sqlalchemy.insert(newTable2).values(Id=item['id'], userId=item['userId'], task_name=item['name'])
    result_proxy = connection.execute(query)
