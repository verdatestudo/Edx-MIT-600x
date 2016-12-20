'''

MIT6002 edX - final exam - rabbits.py

Classic foxes and Rabbits simulation

Last Updated: 2016-Dec-20
First Created: 2016-Dec-19
Python 3.5
Chris

'''

import random
import pylab
import matplotlib.pyplot as plt
import numpy as np

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    prob = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)

    for rabbit in range(CURRENTRABBITPOP):
        if random.random() < prob and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    prob = CURRENTRABBITPOP / MAXRABBITPOP

    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > MIN_RABBIT_POP and random.random() < prob:
            CURRENTRABBITPOP -= 1
            if random.random() < FOX_BIRTH_RATE:
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > MIN_FOX_POP and random.random() < FOX_DEATH_RATE:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

def plot_populations(rabbit_populations, fox_populations, numSteps):
    '''
    Plot foxes and rabbits over time based on numSteps steps.
    '''
    plt.plot(range(numSteps), rabbit_populations)
    plt.plot(range(numSteps), fox_populations)
    plt.xlabel('Time (no. of steps)')
    plt.ylabel('Population')
    plt.title('Fox and Rabbit Population Over Time')
    plt.legend(['Rabbits', 'Foxes'])
    plt.show()
    #plt.savefig('FoxRabbit.png')

def plot_polyfit(rabbit_populations, fox_populations, numSteps, k):
    '''
    Plot a polyfit with k features.
    '''
    rab_coeff = np.polyfit(range(numSteps), rabbit_populations, 2)
    fox_coeff = np.polyfit(range(numSteps), fox_populations, 2)
    plt.plot(np.polyval(rab_coeff, range(numSteps)))
    plt.plot(np.polyval(fox_coeff, range(numSteps)))
    plt.xlabel('Time (no. of steps)')
    plt.ylabel('Population')
    plt.title('Fox and Rabbit population with polyfit (k = 2)')
    plt.legend(['Rabbit pop', 'Fox pop', 'Rabbit polyfit', 'Fox polyfit'])
    plt.show()
    #plt.savefig('FoxRabbit_polyfit.png')


# Global Variables
MAXRABBITPOP = 1000 # default = 1000
CURRENTRABBITPOP = 500 # default = 500
CURRENTFOXPOP = 30 # default = 30

# custom global variables
MIN_RABBIT_POP = 10
MIN_FOX_POP = 10
FOX_BIRTH_RATE = (1/3)
FOX_DEATH_RATE = 0.1

numSteps = 200

rabbit_populations, fox_populations = runSimulation(numSteps)
plot_populations(rabbit_populations, fox_populations, numSteps)
plot_polyfit(rabbit_populations, fox_populations, numSteps, 2)
