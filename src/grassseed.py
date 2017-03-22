'''
Created on 22 March 2017

@author: Sam
'''

# Python 3.5

from decimal import *

if __name__ == '__main__':
    C, L, total = Decimal(input()), int(input()), Decimal(0.0)
    for _ in range(L):
        wi, li = [Decimal(d) for d in input().split()]
        total += wi * li * C
    print (total)