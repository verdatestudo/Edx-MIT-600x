'''
MIT6001 edX - week2 problem set.

Hangman game.

Last Updated: 2016-Oct-25
First Created: 2016-Oct-25
Python 3.5
Chris
'''

import math

def polysum(n, s):
    '''
    A regular polygon has n number of sides. Each side has length s.
        The area of a regular polygon is: (0.25 * n * s**2) / tan (pi / n).
        The perimeter of a polygon is: length of the boundary of the polygon.

    Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
    '''
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    peri = n * s
    print(round(area + peri, 4))

def cc_balance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

    A summary of the required math is found below:

    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    '''

    for month in range(1, 13):
        balance *= (annualInterestRate / 12.0) + 1 # calculate new balance based on monthly interest rate
        balance -= monthlyPaymentRate * balance # calculate min monthly payment and remove from balance
        print('Month %d remaining balance: %g' % (month, round(balance, 2))) # test print by month
    print('Remaining balance: %g' % (round(balance, 2)))
    return balance

def fixed_monthly(balance, annualInterestRate):
    '''
    Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
    By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

    Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
    The monthly payment must be a multiple of $10 and is the same for all months.
    Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    '''
    low_pay = round(balance / 12, -1)

    while fixed_monthly_helper(balance, annualInterestRate, low_pay) > 0:
        low_pay += 10

    print('Lowest Payment %d' %(low_pay))

def fixed_monthly_helper(balance, annualInterestRate, low_pay):
    '''
    Helper function
    '''
    for month in range(1, 13):
        balance -= low_pay
        balance *= (annualInterestRate / 12.0) + 1 # calculate new balance based on monthly interest rate
    return balance

def q2_fixed():
    '''
    This was used in their system as could not call functions.
    '''
    low_pay = round(balance / 12, -1)
    new_balance = balance

    while new_balance > 0:
        for month in range(1, 13):
            new_balance -= low_pay
            new_balance *= (annualInterestRate / 12.0) + 1 # calculate new balance based on monthly interest rate
        if new_balance > 0:
            new_balance = balance
            low_pay += 10
    print('Lowest Payment %d' %(low_pay))

def q3_binary_search(balance, annualInterestRate):
    '''
    Solve the fixed monthly payment problem from q2 using binary/bisection search.

    In short:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
    '''
    lower_bound = balance / 12
    upper_bound = balance * (1 + annualInterestRate / 12) ** 12 / 12.0
    mid_pay = (upper_bound + lower_bound) / 2

    while lower_bound < upper_bound - 0.01: # due to rounding making it equal leads to overflow.
        new_balance = balance
        mid_pay = (upper_bound + lower_bound) / 2
        for month in range(1, 13):
            new_balance -= mid_pay
            new_balance *= (annualInterestRate / 12.0) + 1 # calculate new balance based on monthly interest rate
            new_balance = new_balance
        if new_balance > 0:
            lower_bound = mid_pay
        else:
            upper_bound = mid_pay
        #print(lower_bound, upper_bound, mid_pay)

    print('Lowest Payment %0.2f' %(round(mid_pay, 2)))


def run():
    polysum(10, 5)
    cc_balance(42, 0.2, 0.04)
    cc_balance(484, 0.2, 0.04)
    fixed_monthly(3329, 0.2)
    fixed_monthly(4773, 0.2)
    fixed_monthly(3926, 0.2)
    q3_binary_search(320000, 0.2)
    q3_binary_search(999999, 0.18)
