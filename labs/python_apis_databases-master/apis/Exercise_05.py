'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response1 = requests.delete(base_url + "/22")
print(f"response status: {response1.status_code}")

response2 = requests.get(base_url)
print(response2.content)
