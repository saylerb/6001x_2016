def dict_interdiff(d1, d2, f):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    f: function applied to the intersection values
    '''

    intersect_keys = set(d1).intersection(d2)
    difference_keys = set(d1).symmetric_difference(d2)

    intersect_dict = {}
    for key in intersect_keys:
        intersect_dict[key] = f(d1[key], d2[key])

    diff_dict = {}
    for key in difference_keys:
        if key in d1:
            diff_dict[key] = d1[key]
        else:
            diff_dict[key] = d2[key]

    return intersect_dict, diff_dict
