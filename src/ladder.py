'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

import math

if __name__ == '__main__':
    line = input().split()
    h, v = int(line[0]), int(line[1])
    print(math.ceil(h/(math.sin(math.radians(v)))))
    