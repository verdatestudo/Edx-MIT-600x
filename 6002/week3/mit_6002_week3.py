'''
MIT6002 edX - week 3

Last Updated: 2016-Nov-22
First Created: 2016-Nov-17
Python 3.5
Chris
'''

import math
import random

def stdDevOfLenghts(L):
    '''
    Takes a list of strings.
    Returns float of the standard deviation of the length of the strings in the list.

    - calculate mean
    - calculate squared std mean (item - mean) ** 2
    - sum total, divide by total items, take square root
    '''
    if len(L) == 0:
        return float('NaN')
    else:
        # sqrt (each item in L - mean) ** 2 / len (L)
        return math.sqrt(sum([(len(item) - sum(len(item) for item in L) / float(len(L))) ** 2 for item in L]) / len(L))

def coeVar(L):
    '''
    Takes a list of numbers, returns the coefficient of variation - which is the standard deviation divided by the mean.
    Loosely, it's a measure of how variable the population is in relation to the mean.
    '''
    if len(L) == 0:
        return float('NaN')
    else:
        mean = sum(L) / len(L)
        std = math.sqrt(sum([(item - mean) ** 2 for item in L]) / len(L))
        return std / mean

def noReplacementSimulationRecursive(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    global noRS_trials

    if numTrials == 0:
        return 0
    else:
        # probability is 2/5 * 1/4 = 2/20 = 1/10. Divide by numTrials to get decimal probability.
        return noReplacementSimulation(numTrials - 1) + (int(random.randint(1, 10) == 1) / noRS_trials)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    score = 0
    for trial in range(numTrials):
        # probability is 2/5 * 1/4 = 2/20 = 1/10. Divide by numTrials to get decimal probability.
        score += (int(random.randint(1, 10) == 1))

    return (score / numTrials)

def july_temps_loadFile():
    inFile = open('week3_julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        print(fields, len(fields))
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

def testing():
    print(stdDevOfLenghts(['a', 'z', 'p']), 0)
    print(stdDevOfLenghts(['apples', 'oranges', 'kiwis', 'pineapples']), 1.8708)
    print(coeVar([10, 4, 12, 15, 20, 5]))
    print(noReplacementSimulation(100000))
    print(july_temps_loadFile())
