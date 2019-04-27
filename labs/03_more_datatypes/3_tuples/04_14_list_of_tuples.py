'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
my_string = input("Please enter a sentence: ")
my_list = my_string.split()
result_list = []
for i in my_list:
    result_list.append(tuple(i))
print(result_list)
