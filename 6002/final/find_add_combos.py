'''

MIT6002 edX - final exam - find_add_combos.py

Last Updated: 2016-Dec-20
First Created: 2016-Dec-19
Python 3.5
Chris

'''
import numpy as np

def subsets_with_sum(lst, target, with_replacement=False):
    '''
    Copied solution (after exam) for best practice.
    http://stackoverflow.com/questions/20193555/finding-combinations-to-the-provided-sum-value
    '''
    x = 0 if with_replacement else 1
    def _a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(lst)):
            _a(u + x, l + [lst[u]], r, t)
        return r
    return _a(0, [], [], target)

def find_combo_greedy(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """

    # quick but does not always return the right result.

    result = np.zeros(len(choices))
    copy_choices = np.array(choices)
    sorted_choices_idx = np.argsort(copy_choices)[::-1]

    idx_results = []
    my_choices = []
    score = 0
    for idx, item in enumerate(sorted_choices_idx):
        if copy_choices[item] + score <= total:
            my_choices.append(copy_choices[item])
            score += copy_choices[item]
            idx_results.append(item)
        if score == total:
            for idx in idx_results:
                result[idx] = 1

            return result

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    import itertools

    result = [seq for i in range(len(choices), 0, -1) for seq in itertools.combinations(choices, i) if sum(seq) == total]
    result2 = []

    if result:
        result2 = list(min(result, key=len))
    else:
        for new_total in range(total, 0, -1):
            result = [seq for i in range(len(choices), 0, -1) for seq in itertools.combinations(choices, i) if sum(seq) == new_total]
            if result:
                result2 = list(min(result, key=len))
                break

    final_result = []
    for idx, item in enumerate(choices):
        if item in result2:
            final_result.append(1)
            result2.pop(result2.index(item))
        else:
            final_result.append(0)

    return np.array(final_result)

def testing():
    '''
    Testing.
    '''
    print(find_combination([1,2,2,3], 4))
    print(find_combination([1,1,3,5,3], 5))
    print(find_combination([1,1,1,9], 4))
    print(find_combination([4, 10, 3, 5, 8], 1))
    print(find_combination([2,2,2,5], 6)) # added

def testing_sub():
    '''
    Testing.
    '''
    print(subsets_with_sum([1,2,2,3], 4))
    print(subsets_with_sum([1,1,3,5,3], 5))
    print(subsets_with_sum([1,1,1,9], 4))
    print(subsets_with_sum([4, 10, 3, 5, 8], 1))
    print(subsets_with_sum([2,2,2,5], 6))

testing_sub()
