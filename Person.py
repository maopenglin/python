#!/usr/bin/python

class Person:
    '''
     this is Person doc string
    '''
    version = 1
    def __init__(self, name):
        '''
         init method 
        '''
        self.name = name
        print 'init finish'
        Person.version += 1
    def __del__(self):
        '''
             i an del method
        '''
        print '%s sys bye.' % self.name
        Person.version -= 1
        if Person.version == 0:
            print 'last one'
        else :
            print 'i am the %d people' % Person.version
           
    def howMany(self):
        '''Prints the current population.'''
        if Person.version == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.version         
    def sayHi(self):
         print 'hello ', self.name
    
p = Person('maopenglin')
p.sayHi()
p.howMany()
