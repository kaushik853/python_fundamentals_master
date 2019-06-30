'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
email_list = []
for item in response.json()['data']:
    email_list.append(item['email'])

print(email_list)
