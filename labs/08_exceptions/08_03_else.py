'''
Write a script that demonstrates a try/except/else.

'''
try:
    age = int(input('Enter your age: '))
except Exception as e:
    print (f"You have entered an invalid value {e}")
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
