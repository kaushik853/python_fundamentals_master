'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://root:'xxxyyxx'@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
Ticket_Table = input('Please give a name to first table > ')
Employee_Table = input('Please give a name to 2nd table > ')
Food_Table = input('Please give a name to 3rd table > ')
newTable1 = sqlalchemy.Table(Ticket_Table, metadata, autoload=True, autoload_with=engine)
newTable2 = sqlalchemy.Table(Employee_Table, metadata, autoload=True, autoload_with=engine)
newTable3 = sqlalchemy.Table(Food_Table, metadata, autoload=True, autoload_with=engine)
ticketTable = sqlalchemy.Table(Ticket_Table, metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('rate', sqlalchemy.Float(), default=100.0),
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
              )
employeeTable = sqlalchemy.Table(Employee_Table, metadata,
                       sqlalchemy.Column('employee_id', sqlalchemy.Integer()),
                       sqlalchemy.Column('first_name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('last_name', sqlalchemy.String(255), nullable=False)
              )
foodTable = sqlalchemy.Table(Food_Table, metadata,
                       sqlalchemy.Column('food_id', sqlalchemy.Integer()),
                       sqlalchemy.Column('food_name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('food_rate', sqlalchemy.Float(), default=100.0),
                       sqlalchemy.Column('availability', sqlalchemy.Boolean(), default=True)
              )

metadata.create_all(engine)
print(f"Now you need to provide data for {Ticket_Table}")
def parse(string):
    d = {'True': True, 'False': False, 'TRUE': True, 'FALSE': False, 'true': True, 'false': False}
    return d.get(string, string)
ticket_name = input(f"provide name in {Ticket_Table} > ")
ticket_rate = input(f"provide floating rate value in {Ticket_Table} > ")
ticket_activity = input("whether the show is available or not, answer in true or false> ")
availability = parse(ticket_activity)

query1 = sqlalchemy.insert(newTable1).values(Id=1, name=ticket_name, rate=float(ticket_rate), active=availability)
query2 = sqlalchemy.insert(newTable2).values(employee_id=1, first_name='Software', last_name='Ninja')
query3 = sqlalchemy.insert(newTable3).values(food_id=1, food_name='Software Kheer', food_rate=800.00, availability=True)

query4 = sqlalchemy.update(newTable1).values(rate=75.00).where(newTable1.columns.Id==1)
query5 = sqlalchemy.update(newTable2).values(last_name='topgun').where(newTable2.columns.employee_id==1)
query6 = sqlalchemy.update(newTable3).values(food_rate=1000.00).where(newTable1.columns.Id==1)

query7 = sqlalchemy.select([newTable1])
query8 = sqlalchemy.select([newTable2])
query9 = sqlalchemy.select([newTable3])

result_proxy1 = connection.execute(query7)
result_proxy2 = connection.execute(query8)
result_proxy3 = connection.execute(query9)

result_final1 = result_proxy1.fetchall()
result_final2 = result_proxy2.fetchall()
result_final3 = result_proxy3.fetchall()
pprint(result_final1)
pprint(result_final2)
pprint(result_final3)

query10 = sqlalchemy.delete(newTable1)
#query11 = sqlalchemy.delete(newTable2)
#query12 = sqlalchemy.delete(newTable3)
result = connection.execute(query10)
