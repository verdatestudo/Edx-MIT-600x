'''
MIT6001 edX - week5 misc problems

Last Updated: 2016-Nov-03
First Created: 2016-Nov-03
Python 3.5
Chris
'''

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return (self.x - other.x) == 0 and (self.y - other.y) == 0

    def __repr__(self):
        return 'Coordinate(%d, %d)' %(self.x, self.y)

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        new_set = intSet()
        for x in self.vals:
            if x in other.vals:
                new_set.insert(x)
        return new_set

    def __len__(self):
        return len(self.vals)

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

def genPrimes():
    primes = []
    x = 2
    while True:
        if all((x % p) != 0 for p in primes):
            yield x
            primes.append(x)
        x += 1

def genFib():
    fib1 = 1
    fib2 = 2
    count = 0
    while count < 10:
        next_fib = fib1 + fib2
        yield next_fib
        fib1 = fib2
        fib2 = next_fib
        count += 1

#for x in genPrimes():
#    print(x)

#for x in genFib():
#    print (x)

#spell = Accio()
#spell.execute()
#studySpell(spell)
#studySpell(Confundo())
