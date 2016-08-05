"""
    Functional Programming and Recursion
    7/26/16
"""

def recurse(x):
    """
        Calls recurse() method

    :param x: takes in x
    :return: None
    """
    if (x == 10):
        pass
    else:
        recurse(x+1)

recurse(1)

for i in range(1,10):
    print(i)

x = 1
while(x < 10):
    print(x)
    x+=1


def fibonnaci (x):
    if (x==0):
        return 0
    elif (x==1):
        return 1
    else:
        return fibonnaci(x-1) + fibonnaci(x-2)

fibonnaci(10)

nums_comprehension = [i for i in range(10)]
print(nums_comprehension)