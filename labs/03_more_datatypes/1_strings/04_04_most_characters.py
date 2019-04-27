'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
string_1 = input("please enter string 1: ")
string_2 = input('please enter string 2: ')
string_3 = input("please enter string 3: ")
# if (len(string_1) >= len(string_2)) and (len(string_1) >= len(string_3)):
#     print(f"Most character: {string_1}")
# elif (len(string_2) >= len(string_1)) and (len(string_2) >= len(string_3)):
#     print(f"Most character: {string_2}")
# else:
#     print(f"Most character: {string_3}")
list1 = [string_1, string_2, string_3]
result = max(list1, key=lambda x:len(x))
print(result)
