def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    pairs = list(map(lambda num: (num, f(num)), L))
    pairs = list(filter(lambda pair: g(pair[1]), pairs))
    final = list(map(lambda pair: pair[0], pairs))
    L[:] = final # this will mutate L in the outer scope

    if len(L) > 0:
        result = max(L)
    else:
        result = -1
    return result
