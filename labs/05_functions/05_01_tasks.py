'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results
my_num = input("Please enter a number between 1 and 1000000000: ")
def div_1(num):
    if num % 4 == 0 and num % 7 == 0:
        print(f"the number {num} is divisible by both 4 and 7")
    else:
        print(f"the number {num} is not divisible by both 4 and 7")
def div_2(num):
    if (num % 4 == 0) or (num % 7 == 0):
        print(f"the number {num} is divisible by either 4 or 7")
    else:
        print(f"the number {num} is not divisible by either 4 or 7")
def div_3(num):
    if (num % 4 == 0) and (num % 7 != 0):
        print(f"the number {num} is divisible exclusively by 4" )
    elif (num % 7 == 0) and (num % 4 != 0):
        print(f"the number {num} is divisible exclusively by 7" )
    else:
        print(f"The number {num} is not divisible by 4 0r 7 exclusively")
div_1(int(my_num))
div_2(int(my_num))
div_3(int(my_num))        
