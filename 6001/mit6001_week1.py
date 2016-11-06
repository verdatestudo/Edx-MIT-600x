'''
MIT6001 edX - week1 problem set.

Hangman game.

Last Updated: 2016-Oct-24
First Created: 2016-Oct-24
Python 3.5
Chris
'''

def q1():
    # Paste your code into this box
    vowels = ['a', 'e', 'i', 'o', 'u']
    #s = 'azcbobobegghakl'
    count = len([letter for letter in s if letter in vowels])
    print('Number of vowels: %d' % (count))

def q2():
    s = 'azcbobobegghakl'
    count = len([x for x in range(len(s)) if s[x:x+3] == 'bob'])
    print('Number of times bob occurs is: %d' % (count))

def q3():
    s = 'azcbobobegghakl'
    #s = 'abcbcd'

    best_string = ''

    for x_let in range(len(s) - 1):
        new_string = s[x_let]
        while (x_let < len(s) - 1) and s[x_let] <= s[x_let + 1]:
            new_string += s[x_let + 1]
            x_let += 1
        if len(new_string) > len(best_string):
            best_string = new_string

    print ('Longest substring in alphabetical order is: %s' % (best_string))
