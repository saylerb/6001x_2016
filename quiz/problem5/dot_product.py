def calculate_dot_product(a, b):
    '''
    a: a list of numbers
    b: a list of numbers of the same length as a
    '''
    if len(a) == 1:
        return a[0] * b[0]
    else:
        return a[0] * b[0] + calculate_dot_product(a[1:], b[1:])



