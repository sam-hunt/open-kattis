'''
Created on 19 May 2016

@author: Sam
'''

# Python 2.7

from math import sqrt, ceil

if __name__ == '__main__':
    X = int(raw_input())
    pfactors = 0
    divisor=3
    Xsqrt = ceil(sqrt(X))
    
    factors = []
    
    while not (X % 2):
        X/=2
        pfactors+=1
        factors.append(2)
        
    while X>1 and not(not(pfactors) and divisor>Xsqrt):
        while not(X%divisor):
            X/=divisor
            pfactors+=1 
            factors.append(divisor)
        divisor+=2
    if not pfactors:
        pfactors=1
    
    print (''.join(str(factors)))
    print (pfactors)
    
        