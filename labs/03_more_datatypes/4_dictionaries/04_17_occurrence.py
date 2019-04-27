'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = input("please enter a text: ")
user_tuple = tuple(user_input)
user_dictionary = dict()
for i in user_tuple:
    user_dictionary[i] = user_tuple.count(i)
print(user_dictionary)
