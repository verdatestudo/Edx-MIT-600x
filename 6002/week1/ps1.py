'''
MIT6002 edX - week 1 problem set

Last Updated: 2016-Nov-09
First Created: 2016-Nov-09
Python 3.5
Chris
'''


###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if len(cows) == 0:
        return []

    limit_copy = limit

    # turn cows into a sorted list
    try:
        sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    except:
        sorted_cows = cows

    # work the way through the sorted list, biggest cow first. if it fits it goes into trip list,
    # otherwise it's added to new_cows and will run greedy_cow_transport again recursively.

    trip = []
    new_cows = []

    for cow in sorted_cows:
        if cow[1] <= limit:
            trip.append(cow[0])
            limit -= cow[1]
        else:
            new_cows.append(cow)

        #print (limit, 'sc', sorted_cows, 'tr', trip, 'nc', new_cows)

    return [trip] + greedy_cow_transport(new_cows, limit_copy)


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # get all possible combos using generator in ps1_partition.py.
    # note: it is sorted so that we loop through the smaller possibilities first.
    # for each transport group inside the partition, if each group is equal or below the limit, then it is valid.
    # as soon as we find a valid partition we can return the names of the cows (because we sorted the partitions by length earlier).

    for partition in sorted(get_partitions(cows.items()), key = len):
        if all(sum(value[1] for value in group) <= limit for group in partition):
            return [[item[0] for item in group] for group in partition]

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")

    start = time.time()
    print(greedy_cow_transport(cows, limit=10))
    end = time.time()
    print('Greedy timing: ', end - start)

    start = time.time()
    print(brute_force_cow_transport(cows, limit=10))
    end = time.time()
    print('Brute force timing: ', end - start)


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

def testing():
    print(greedy_cow_transport(cows, limit))
    print(greedy_cow_transport(cows2, limit=10))
    print(greedy_cow_transport(cows3[0], cows3[1]))

    cows = load_cows("ps1_cow_data.txt")
    cows2 = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    cows3 = ({'Dottie': 85, 'Daisy': 50, 'Betsy': 65, 'Patches': 12, 'Coco': 10, 'Abby': 38, 'Rose': 50, 'Willow': 35, 'Lilly': 24, 'Buttercup': 72}, 100)
    limit=100
    print(cows)

    print(brute_force_cow_transport(cows, limit))
    print(brute_force_cow_transport(cows2, limit=10))
    print(brute_force_cow_transport(cows3[0], cows3[1]))
    print(brute_force_cow_transport({'Buttercup': 11, 'Betsy': 39, 'Starlight': 54, 'Luna': 41}, 145))
    print(brute_force_cow_transport({'Milkshake': 40, 'Miss Bella': 25, 'MooMoo': 50, 'Horns': 25, 'Boo': 20, 'Lotus': 40}, 100))
    print(brute_force_cow_transport({'Lotus': 40, 'Boo': 20, 'Horns': 25, 'MooMoo': 50, 'Milkshake': 40, 'Miss Bella': 25}, 100))

compare_cow_transport_algorithms()
