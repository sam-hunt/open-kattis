'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

import math

if __name__ == '__main__':
    line = input().split()
    R, C = int(line[0]), int(line[1])
    cheese = math.pi * ((R-C) ** 2)
    crust = (math.pi * (R ** 2)) - cheese
    print((cheese/(cheese+crust))*100)
    