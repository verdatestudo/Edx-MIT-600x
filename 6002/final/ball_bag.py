'''
MIT6002 edX - final exam - ball_bag.py

Last Updated: 2016-Dec-20
First Created: 2016-Dec-19
Python 3.5
Chris

'''

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    count = 0
    for trial in range(numTrials):
        ball_bag = [1, 1, 1, 1, 0, 0, 0, 0]
        # shuffle bag and pop x number of balls.
        # alternatively can choose random idx and pop using that.
        random.shuffle(ball_bag)
        chosen_balls = [ball_bag.pop() for _ in range(3)]
        count += int(len(set(chosen_balls)) == 1) # if all the same then len of set is 1, if true then int(true) adds 1 to count

    return count / numTrials


print('Test: ', drawing_without_replacement_sim(10000), 'Expected (rough): ', (1/7))
