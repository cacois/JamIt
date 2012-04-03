'''
Created on Mar 23, 2012

@author: cacois
'''

class Case:
    
    def populate(self):
        raise NotImplementedError("You should implement this")

    def isDone(self):
        raise NotImplementedError("You should implement this")

    def __str__(self):
        raise NotImplementedError("You should implement this")

class Solver:
    
    cases = None
    
    def __init__(self):
        raise NotImplementedError("You should implement this")
    
    def solve(self, case):
        raise NotImplementedError("You should implement this")
    
    def printCases(self):
        for case in self.cases:
            print(case)
