'''
MIT6002 edX - week 2

Last Updated: 2016-Nov-10
First Created: 2016-Nov-10
Python 3.5
Chris
'''

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice([x for x in range(0, 100, 2)])

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.choice([x for x in range(10, 21, 2)])


import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)
print('aaa')

# Code Sample B
mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print(mylist)
