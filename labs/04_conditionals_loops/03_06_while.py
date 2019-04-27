'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.


'''

num = 1
while num in range(1, 1001):
    if (num % 5) == 0:
        print(num)
    num += 1
