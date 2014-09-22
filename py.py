#!/usr/bin/python

import sys

def sayHello():
     print 'Hello World'

def printMax(a, b):
     if a > b:
         print a, 'is max'
     else:
         print b, 'is max'
         
def say(message,time=1):
    print message*time

def maxValue(x,y):
    '''
    this is the max value function doc
    '''
    if x>y:
        return x
    else :
        return y
version='1.0.0'
print '__name__', __name__
if __name__ == '__main__':
    print 'run it self'
    print 'max value is :', maxValue(4, 8)
    print sys.argv  
    print maxValue.__doc__
    say('hello', 5)
    say('test')
    sayHello()
    printMax(3, 4)
else :
     print 'run by others'

