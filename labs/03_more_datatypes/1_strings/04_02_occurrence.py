'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
string_of_words = input("Please enter enter some words: ")
letter = input("substring to find: ")
print(string_of_words.find(letter))
