'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []
for initial_list in starting_list:
    nested_list = initial_list
    for i in nested_list:
        flattened_list.append(i)
print(flattened_list)
