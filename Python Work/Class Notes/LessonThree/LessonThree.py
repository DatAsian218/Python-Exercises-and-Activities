"""
6/27/16
Learning about import, modules, functions
"""

import math

print(math.pow(2,3)) #prints a float
print(math.ceil(5.4)) #rounds the integer

def exampleFunction(x, y):
    print(x**y)

exampleFunction(100, 2)

def moreFunc(name, age):
    return (name,age)

print(moreFunc("Alex",18))

def default(name="",age=0):
    return name,age
print(default())