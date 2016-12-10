'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = sorted([int(a) for a in input().split()])
    print(line[0]*line[2])
    