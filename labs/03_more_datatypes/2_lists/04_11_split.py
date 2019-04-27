'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
user_string = input("Please enter some sentence: ")
user_list = user_string.split()
print(max(user_list, key=user_list.count))
