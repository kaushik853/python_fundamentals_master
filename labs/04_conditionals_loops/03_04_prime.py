'''
Print out every prime number between 1 and 100.

'''
for prime_num in range(1, 101):
    if prime_num > 1:
        for i in range(2, prime_num):
            if (prime_num % i) == 0:
                break
        else:
            print(prime_num)
