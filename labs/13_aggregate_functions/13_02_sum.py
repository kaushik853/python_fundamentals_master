'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
def aggregate_sum(aggregate_list):
    """ We are not to use the SUM() name because of
        built-in function with same name
    """
    num = 0
    for item in aggregate_list:
        try:
            num += float(item)
        except ValueError as e:
            print(e)
            continue
    return num
x_num = [1, 2, 3, 'linux']
x_sum = aggregate_sum(x_num)
print(x_sum)
