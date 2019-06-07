'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''
import requests
response = requests.get('https://api.github.com')
response.content
response.text
response.json()
response.headers
requests.post('https://httpbin.org/post', data={'key':'value'})
 requests.put('https://httpbin.org/put', data={'key':'value'})
 requests.delete('https://httpbin.org/delete')
 requests.head('https://httpbin.org/get')
 requests.patch('https://httpbin.org/patch', data={'key':'value'})
 requests.options('https://httpbin.org/get')
requests.post('https://httpbin.org/post', data={'key':'value'})
data takes a dictionary, a list of tuples, bytes, or a file-like object.
You’ll want to adapt the data you send in the body of your request to the specific needs of the service
you’re interacting with.
from getpass import getpass
requests.get('https://api.github.com/user', auth=('username', getpass()))
requests.get('https://api.github.com', timeout=3.05)
mport requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

import requests
from getpass import getpass

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
print(response.headers)
print(response.json())

-----------------------------------------------------------------------------------------------

import scapy
