'''
MIT6002 edX - week 5 - Cancer Clusters

Last Updated: 2016-Dec-12
First Created: 2016-Dec-12
Python 3.5
Chris

Hypothetical Example

Massachusetts is about 10,000 miles**2
About 36,000 new cancer cases each year
The state is divided into sections 10 miles ** 2 (so 1,000 sections)
It was discovered that one region (section 111) had 143 new cancer cases over a 3 year period.
More than 32% greater than expected.

How worried should residents be?

'''

import random

STATE_SIZE = 10000
SUBSTATE_SIZE = 10
CANCER_CASES = 36000
YEARS = 3
SIMS = 100 # number of simulations to run

def cancer_monte_carlo(sims, state_size, substate_size, cancer_cases, years):
    '''
    Takes various int args and randomly assigns new cancer cases to substates.
    Performs this sims number of times.
    '''
    for sim in range(sims):
        print('Completing sim {} ...'.format(sim))
        substates = [0 for x in range(state_size // substate_size)]
        for case in range(cancer_cases * years):
            substates[random.randint(0, len(substates) - 1)] += 1
        yield substates

def show_results():
    '''
    Results of cancer_monte_carlo.

    In our first example we just look at section 111, and how likely it is to randomly reach 143 new cases in 3 years.
    The probability tends to be 0-1%, suggesting that this is not down to chance and has a specific cause that we should be concerned about.

    However, this is known as the "Texas sharpshooter fallacy" - we are looking at the data in retrospect and then drawing conclusions.
    Instead we should calculate the probability of any section reaching this level of new cases to determine how likely it is that any specific section
    (in this case section 111) reaches 143 new cases. This probability works out to be 50-60% - much less concerning.

    '''
    print ('Results for {} simulations'.format(SIMS))
    results = list(cancer_monte_carlo(SIMS, STATE_SIZE, SUBSTATE_SIZE, CANCER_CASES, YEARS))

    # results for section 111
    section111 = [x[110] for x in results]
    print ('Mean of section 111: {}'.format(sum(section111) / len(section111)))
    print ('Prob of section 111 >= 143 cases in 3 years: {}'.format(len([x for x in section111 if x >= 143]) / len(section111)))

    # results for max section from each sim.
    section_max = [max(x) for x in results]
    print ('Mean of max section: {}'.format(sum(section_max) / len(section_max)))
    print ('Prob of the max section >= 143 cases in 3 years: {}'.format(len([x for x in section_max if x >= 143]) / len(section_max)))

show_results()
