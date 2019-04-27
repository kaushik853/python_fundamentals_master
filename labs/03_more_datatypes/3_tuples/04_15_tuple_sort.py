'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = sorted(unsorted_list, key=lambda x : x[1])
print(sorted_list)
