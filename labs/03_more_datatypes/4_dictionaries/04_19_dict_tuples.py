'''
Write a script that sorts a dictionary into a list of tuples based on values. For einput_dictample:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = sorted(input_dict.items(), key=lambda kv: kv[1])
print(result_list)
