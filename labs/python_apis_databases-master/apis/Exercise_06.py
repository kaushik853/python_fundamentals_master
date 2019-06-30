'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import requests
from textwrap import dedent

print(dedent("""
        Welcome to the world of APIs.Please
        choose your options carefully and responsibily
        Please select from the following options (enter the number of the action you'd like to take):
        1) Create a new account (POST)
        2) View all your tasks (GET)
        3) View your completed tasks (GET)
        4) View only your incomplete tasks (GET)
        5) Create a new task (POST)
        6) Update an existing task (PATCH/PUT)
        7) Delete a task (DELETE)
        """))
action = input("enter> ")
if action == '1':
    print("we will create a new account")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
    body = {
        "first_name": input("enter user's first name: "),#add first name inside quotes
        "last_name": input("enter user's last name: "),#add last name inside quotes
        "email": input("enter email id: ")#add email inside quotes
    }
    response1 = requests.post(base_url, json=body)
    print(f" response1 status is {response1.status_code}")

    response2 = requests.get(base_url)
    print(response2.content)
elif action == '2':
    print("You want to see all your task")
    userid = input("please enter userid: ")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=" + userid
    response1 = requests.get(base_url)
    print(response1.status_code)
    print(response1.json())
elif action == '3':
    print("You want to see all your completed task")
    userid = input("please enter userid: ")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=" + userid + "&complete=true"
    response1 = requests.get(base_url)
    print(response1.status_code)
    print(response1.json())
elif action == '4':
    print("You want to see all your incompleted task")
    userid = input("please enter userid: ")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=" + userid + "&complete=false"
    response1 = requests.get(base_url)
    print(response1.status_code)
    print(response1.json())
elif action == '5':
    print("You want to create a new task")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    body = {
        "userId": int(input("enter user's id: ")),
        "name": input("enter task name: "),
        "description": input("enter task description: ")
    }
    response1 = requests.post(base_url, json=body)
    print(f" response status is {response1.status_code}")
elif action == '6':
    print("You want to update a old task")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    body = {
        "userId": int(input("enter an existing user's id: ")),
        "name": input("enter task name: "),
        "description": input("enter task description: ")
    }
    response1 = requests.put(base_url, json=body)
    print(f" response status is {response1.status_code}")
    print(response1.text)
elif action == '7':
    print("You want to remove an old task")
    base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    var = input("enter the id:")
    response1 = requests.delete(base_url + f"/{var}")
    print(f"response status: {response1.status_code}")
else:
    print("Please choose only mentioned options")
