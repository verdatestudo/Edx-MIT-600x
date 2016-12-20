'''

MIT6002 edX - final exam - die.py

Longest runs in a sequence.

Last Updated: 2016-Dec-20
First Created: 2016-Dec-19
Python 3.5
Chris

'''

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """

    longest_runs = []
    for trial in range(numTrials):
        rolls = [die.roll() for _ in range(numRolls)]
        max_count = 1
        max_count_idx = 0
        count_idx = 0
        start_run = rolls[0]
        for idx, roll in enumerate(rolls[1:], 1):
            if roll != start_run:
                if (idx - count_idx) > max_count:
                    max_count = (idx - count_idx)
                    max_count_idx = count_idx
                count_idx = idx
                start_run = roll
        if (len(rolls) - count_idx) > max_count:
            max_count = (idx - count_idx)
            max_count_idx = count_idx

        longest_runs.append(max_count)

    mean, std = getMeanAndStd(longest_runs)
    makeHistogram(longest_runs, 10, 'Longest runs', 'Quantity', title='Die: {}, numRolls: {}, numTrials: {}'.format(die.possibleVals, numRolls, numTrials))
    return mean


# One test case
print('Test: ', getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000), 'Expected (rough): {}'.format(5.312))

#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 20, 2))
#makeHistogram([1, 1, 2, 3, 2, 4, 5, 1, 1, 1], 6, 'im an xlabel', 'im a ylabel')
