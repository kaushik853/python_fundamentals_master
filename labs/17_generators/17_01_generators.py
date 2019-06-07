'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
gen = (num**2 for num in range(20) if num%2 == 0)
print(gen)
for i in gen:
    print(i)
    #print(gen.send(i))
