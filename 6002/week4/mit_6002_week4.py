'''
MIT6002 edX - week 4

Last Updated: 2016-Dec-02
First Created: 2016-Dec-02
Python 3.5
Chris
'''

import numpy as np
import matplotlib.pyplot as plt

spring_data_file = 'springData.txt'

def fitData1(filename):
    '''
    Takes spring data from filename (distance, mass) and converts into
    xVals (mass) and yVals (distance).
    '''
    xVals = []
    yVals = []
    with open(filename) as f:
        for line in f:
            line = line.split()
            if len(line) == 2:
                yVals.append(float(line[0]))
                xVals.append(float(line[1]))

    xVals = np.array(xVals)
    yVals = np.array(yVals)

    # acceleration ~= 9.81ms**2. So xVals becomes force due to F=ma.
    xVals *= 9.81

    # best fit poly and get estimated Y values based on it.
    model = np.polyfit(xVals, yVals, 2)
    estYVals = np.polyval(model, xVals)

    points = plt.plot(xVals, yVals, 'bo', label = 'Measured points')
    best_fit = plt.plot(xVals, estYVals, 'r', label = 'Model')

    plt.title('Measured displacement of string (boing boing)')
    plt.xlabel('Force (Newtons)')
    plt.ylabel('Distance (m)')
    plt.legend(loc='upper left')

    plt.show()

fitData1(spring_data_file)
