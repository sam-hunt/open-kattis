'''
Created on 16 May 2016

@author: Sam
'''

# Python 2.7

import sys

if __name__ == '__main__':
    while 1:
        line = sys.stdin.readline().split()
        N, M = int(line[0]), int(line[1])
        if N == 0 and M == 0: break
        jack_collection, both = set(), 0
        for _ in range(N):
            jack_cd = int(input())
            jack_collection.add(jack_cd)
        for i in range(M):
            jill_cd = int(input())
            if jill_cd in jack_collection:
                both += 1
        print(both)


