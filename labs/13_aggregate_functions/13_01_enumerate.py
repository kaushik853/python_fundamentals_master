'''
Demonstrate the use of the .enumerate() function.
'''
grocery = ['bread', 'milk', 'butter']
for count, item in enumerate(grocery, 100):
    print(count, item)
