def deep_reverse_list(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    result = []
    stack = L[:]

    while len(stack) > 0:
        element = stack.pop()

        if type(element) is list:
            element.reverse()
            result.append(element)

    L.reverse()
