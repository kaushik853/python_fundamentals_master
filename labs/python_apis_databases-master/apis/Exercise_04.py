'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 22,
    "first_name": "tara",
    "last_name": "schwechenko",
    "email": "tara.s@email.com"
}

response1 = requests.put(base_url, json=body)
print(f"response status: {response1.status_code}")

response2 = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response2.content}")
