'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''
lower_bound = input("Please enter the first number: ")
upper_bound = input("Please enter the last number: ")
sum_num = 0
for i in range(int(lower_bound), int(upper_bound)+1):
	sum_num = sum_num+i

print(f"The sum is: {sum_num}")
