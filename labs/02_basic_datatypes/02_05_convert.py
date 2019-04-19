'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
x = 4
print(float(x))
y = 3.14
print(int(y))
print(x // y)
user_input1 = input("Please enter a number to multiply : ")
user_input2 = input("Please enter the 2nd number : ")
if '.' in user_input1:
    user_input1 = float(user_input1)
else:
    user_input1 = int(user_input1)
if '.' in user_input2:
    user_input2 = float(user_input2)
else:
    user_input2 = int(user_input2)
multiplication = user_input1 * user_input2
print(multiplication)
