'''
MIT6001 edX - final exam

Last Updated: 2016-Nov-06
First Created: 2016-Nov-06
Python 3.5
Chris
'''


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
              '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    assert 0 < len(us_num) < 3

    if int(us_num) < 11:
        return trans[us_num]
    else:
        if us_num[0] == '1':
            return trans['10'] + ' ' + trans[us_num[1]]
        elif us_num[1] == '0':
            return trans[us_num[0]] + ' ' + trans['10']
        else:
            return trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # variables for start and end points of "runs"
    best_start = 0
    best_end = 0

    cur_start = 0
    cur_end = 0

    forward_run = 0 # store whether the current run is going higher or going lower
    zero_dif_list = [] # store where flat runs appear, as once a run comes to the end we need to start the new run at a zero (if there is one)

    #print(L)

    for idx in range(1, len(L)):
        prev_num = L[idx - 1]
        cur_num = L[idx]

        if cur_num == prev_num: # store the zero run starting point
            zero_dif_list.append(idx - 1)

        if forward_run == 0:
            if cur_num > prev_num:
                forward_run = 1 # a positive run
                zero_dif_list[:] = [] # remove all zeroes from list. consider list [3, 3, 3, 3, 10]. we no longer want to store indexes (0, 1, 2, 3) as we now know this has to be a positive run.
            elif cur_num < prev_num:
                forward_run = -1 # negative run
                zero_dif_list[:] = []
            else:
                forward_run = 0

        if (cur_num > prev_num and forward_run == -1) or (cur_num < prev_num and forward_run == 1): # check if run has come to an end.
            cur_end = idx - 1
            if (cur_end - cur_start) > (best_end - best_start):
                best_start = cur_start
                best_end = cur_end

            forward_run *= -1
            if zero_dif_list: # if we've had flat/zeroes without a change, then we should start our new run from the first zero.
            # consider [100, 0, 0, 0, 100]. we've had a negative run from (idx 0 to 3), but our new positive run should go from (1, 4).
            # the zeroes could be part of either run.
                cur_start = zero_dif_list.pop(0)
            else:
                cur_start = idx - 1
            zero_dif_list[:] = []

        #print ('idx:', idx, 'nums:', prev_num, cur_num, 'for run', forward_run, '(currun):', (cur_end - cur_start), 'cur idx:', cur_start, cur_end, zero_dif_list)

    if (idx - cur_start) > (best_end - best_start):
        best_start = cur_start
        best_end = idx

    #print ((best_end - best_start), best_start, best_end + 1)

    return sum(L[best_start:best_end + 1])

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name

class USResident(Person):
    """
    A Person who resides in the US.
    The question was to implement the methods below.
    """
    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        legal_status = ['citizen', 'legal_resident', 'illegal_resident']
        if status not in legal_status:
            raise ValueError
        else:
            self.status = status

    def getStatus(self):
        """
        Returns the status
        """
        return self.status


class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return Professor.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    # e.g [1,2,3,4] with x=10 is 1*10**3 + 2*10**2 + 3*10**1 + 4*10**0
    return lambda x: sum((item * x ** ((len(L) - 1) - idx)) for idx, item in enumerate(L))

def gp(L):
    '''
    Just a quick function to help understand lambda
    # good mental tip - replace the word lambda with the word function
    '''
    f = lambda x: x + 1
    return f

def testing():
    '''
    testing 123
    '''
    print(convert_to_mandarin('36') + ' ... ' + 'san shi liu')
    print(convert_to_mandarin('20') + ' ... ' + 'er shi')
    print(convert_to_mandarin('16') + ' ... ' + 'shi liu')

    print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]), ' ... ', 26)
    print(longest_run([5, 4, 10]), ' ... ', 9)
    print(longest_run([1, 2, 3, 2, -1, -10]), ' ... ' , -6)
    print(longest_run([1, 2, 1, 2, 1, 2, 1, 2, -1, -2, -1, -2, 10, 20, 10, 20, 100, 200, 100, 0, 100, 0, 100, 0, 0, 100, 0, 0, 0, 100, 1500000, -1500000, 1, -150001]), ' ... ', 1500100, '14:17 vs 26:30')
    print(longest_run([3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]), ' ... ', 11)
    print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), ' ... ', 65)

    a = USResident('Tim Beaver', 'citizen')
    print(a.getStatus())
    #b = USResident('Tim Horton', 'non-resident') #is supposed to raise ValueError

    e = Person('eric')
    le = Lecturer('eric')
    pe = Professor('eric')
    ae = ArrogantProfessor('eric')

    print(pe.say('the sky is blue'), pe.say('the sky is blue') == 'Prof. eric says: I believe that eric says: the sky is blue')
    print(ae.say('the sky is blue'), ae.say('the sky is blue') == 'Prof. eric says: It is obvious that I believe that eric says: the sky is blue')

    print(general_poly([1, 2, 3, 4])(10), ' ... ', 1234)

#testing()
