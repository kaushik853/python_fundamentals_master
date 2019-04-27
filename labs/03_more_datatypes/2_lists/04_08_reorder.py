'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
user_input = input("Please enter 10 integers with comma: ")
#user_input2 =
user_rawlist = user_input.split(',')
user_list = []
for i in user_rawlist:
    x = int(i)
    user_list.append(x)
print(user_list)
output_list1 = []
output_list2 = []
for i in range(len(user_list)):
    if i%2 is not 0:
        output_list1.append(user_list[i])
    else:
        output_list2.append(user_list[i])

output_list = output_list1 + list(reversed(output_list2))
print(output_list)
