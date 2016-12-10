'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        left = set('abcdefghijklmnopqrstuvwxyz')
        for eachchar in input().lower():
            if eachchar in left:
                left.remove(eachchar)
        if not len(left): print('pangram')
        else: print('missing', ''.join(sorted(left)))
