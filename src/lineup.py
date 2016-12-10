'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    I, D = 0, 0
    prev = input()
    for i in range(N-1):
        current = input()
        if current > prev:
            I += 1
        else:
            D += 1
        prev = current
    if I == N-1: print('INCREASING')
    elif D == N-1: print('DECREASING')
    else: print('NEITHER')
        