'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
numbers = input("Please enter 10 numbers seperated by comma: ")
num_list = numbers.split(',')
largest_num = max(num_list)
print(largest_num)
t = 1
for i in num_list:
    t = t * int(i)
print(t)
