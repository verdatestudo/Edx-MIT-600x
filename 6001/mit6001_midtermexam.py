'''
MIT6001 edX - mid-term exam problem set.

Misc mid-term exam problems.

Last Updated: 2016-Nov-02
First Created: 2016-Nov-02
Python 3.5
Chris
'''

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    distance = float('inf')

    while abs((base ** exponent)) - num < distance:
        distance =  abs((base ** exponent) - num)
        exponent += 1

    return exponent - 1

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    return sum([listA[x] * listB[x] for x in range(len(listA))])

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    for lst in L[::-1]:
        lst.reverse()
    L.reverse()

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers.
    Returns a tuple of dictionaries according to the instructions above.

    Assume you are given two dictionaries d1 and d2, each with integer keys and integer values
     You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

    Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
    The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

    intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2.
    To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values --
    the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function.
    Do not implement f inside your dict_interdiff code -- assume it is defined outside.

    difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears
    only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.

    '''
    # http://stackoverflow.com/questions/18554012/intersecting-two-dictionaries-in-python

    intersect_keys = {x:d1[x] for x in d1 if x in d2} # get keys that intersect both dictionaries.
    dif_result = {}

    intersect_result = {key: inter_f(d1[key], d2[key]) for key in intersect_keys} # get intersect result by applying the mystery function f() to keys which are in both dicts.

    #d = {key: value for (key, value) in iterable}
    dif_result.update({key: d1[key] for key in d1 if key not in intersect_keys}) # for all d1 keys not in d2, apply function f().
    dif_result.update({key: d2[key] for key in d2 if key not in intersect_keys}) # for all d2 keys not in d2, apply function f().

    return (intersect_result, dif_result)

def inter_f(a, b):
    '''
    Example mystery function f() for function dict_interdiff()
    '''
    return a + b

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
    L[:] = [item for item in L if fil_g(app_f(item))]
    try:
        return max(L)
    except:
        return -1

def app_f(i):
    '''
    Test function for applyF_filterG
    '''
    return i + 2

def fil_g(i):
    '''
    Test function for applyF_filterG
    '''
    return i > 5

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''

    # base case = non-list - simply return the values (as a list).
    if type(aList) != list:
        return [aList]
    else:
        if len(aList) == 0:
            return []
        elif len(aList) == 1:
            return flatten(aList[0])
        else:
            return flatten(aList[0]) + flatten(aList[1:])

def testing():
    print (closest_power(3,12), end=' ')
    print (closest_power(3,12) == 2)
    print (closest_power(4,12), end=' ')
    print (closest_power(4,12) == 2)
    print (closest_power(4,1), end=' ')
    print (closest_power(4,1) == 0)

    print (dotProduct([1, 2, 3], listB = [4, 5, 6]), end=' ')
    print (dotProduct([1, 2, 3], listB = [4, 5, 6]) == 32)

    deep_reverse([[1, 2], [3, 4], [5, 6, 7]])

    # intersect diff test
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    print(dict_interdiff(d1, d2), end=' ')
    print(dict_interdiff(d1, d2) == ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}))

    apply_list = [0, -10, 5, 6, -4]
    print(applyF_filterG(apply_list, app_f, fil_g))
    print(apply_list)

    print(flatten(['a']))
    print(flatten(['b', 2]))
    print(flatten(['b', [2, 'c']]))
    print(flatten(['a', ['b', 3], ['c', 'd', [2, 4]]]))
    print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

testing()
