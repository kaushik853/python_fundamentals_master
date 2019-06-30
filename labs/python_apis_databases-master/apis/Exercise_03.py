'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "kaushik pal",#add first name inside quotes
    "last_name": "pal",#add last name inside quotes
    "email": "kaushik853@gmail.com"#add email inside quotes
}

response1 = requests.post(base_url, json=body)
print(f" response1 status is {response1.status_code}")

response2 = requests.get(base_url)
print(response2.content)
