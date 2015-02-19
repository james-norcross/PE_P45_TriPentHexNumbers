## Author: James Norcross
## Date 2/19/15
## Finds the first Triangular of index greater than 285 which is also
## Pentagonal and Hexagonl

import math

def isPentagonal(num):
    n = (math.sqrt((24 * num) + 1) + 1)/6
    if(n == int(n)):
        return True
    else:
        return False

def getTriangleNumber(n):
    return (n*(n+1))/2

## note all odd number triangle numbers are hexagonal
## while all even number triangle numbers are not hexagonal

done = False
n = 287

while(not done):
    t = getTriangleNumber(n)
    if(isPentagonal(t)):
        done = True;
        print str(t) + " is T-" + str(n)
        print "and P-" + str(int((math.sqrt((24 * t) + 1) + 1)/6))
        print "and H-" + str((n+1)/2)
    n += 2
