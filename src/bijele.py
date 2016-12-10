'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    need = [1,1,2,2,2,8]
    have = [int(a) for a in input().split()]
    want = []
    for eachpiece in range(6):
        want.append(str(need[eachpiece] - have[eachpiece]))
    print(' '.join(want))