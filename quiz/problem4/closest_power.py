import math

def get_closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    differences = []

    for i in range(0, math.ceil(num**(1/base)) + 1):
        differences.append(abs(num - base**i))

    return differences.index(min(differences))
