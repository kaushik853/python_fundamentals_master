'''

Write a script that removes all duplicates from a list.

'''
x = ['a', 'b', 'r', 'a', 'c', 'a', 'd']
result = []
for i in x:
    if i not in result:
        result.append(i)
print(result)
