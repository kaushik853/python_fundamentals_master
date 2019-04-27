'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
words = input("Please enter a string of input : ")
symbol = input("Enter a symbol : ")
print(words.replace(words[0], symbol))
