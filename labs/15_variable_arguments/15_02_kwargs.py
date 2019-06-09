'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def print_keyword_args(**kwargs):
       # kwargs is a dict of the keyword args passed to the function
    for key, value in kwargs.items():
        print (f"{key} = {value}")

print_keyword_args(first_name = 'foo', last_name = 'bar', place_of_birth = 'california')
