'''
Write a script that takes a list and turns it into a tuple.

'''
user_string = input("enter a sentence: ")
user_list = user_string.split()
user_tuple = tuple(user_list)
print(user_tuple)
