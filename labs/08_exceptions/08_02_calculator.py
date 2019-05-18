'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    user_inpu1 = int(input("please enter a dividend: "))
    user_input2 = int(input("please enter a divisor: "))
    quotient = user_inpu1 // user_input2
    print(quotient)
except ValueError as VE:
    print(f"Integer is needed as input but error as {VE}")
except ZeroDivisionError as ZDE:
    print(f"incorrect divisor entered as {ZDE}")
