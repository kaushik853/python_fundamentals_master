'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''
import functools
def strong(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return'<strong>'+func(*args, **kwargs)+'</strong>'
    return wrapper

def emphasis(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return'<em>'+func(*args, **kwargs)+'</em>'
    return wrapper


y = input('please specify which tag to use strong or emphasis: ')
if y == 'strong':
    @strong
    def greet():
        return "Hello!"
elif y == 'emphasis':
    @emphasis
    def greet():
        return "Hello!"

x = greet()
print(x)
