'''
Write a script with a function that demonstrates the use of *args.

'''
def print_everything(*args):
    for count, v in enumerate(args):
        print( f'{count}. {v}')

print_everything('tomato', 'potato', 'pizza', 'guitar')
