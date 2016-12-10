'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    
    total = 0
    
    for _ in range(N):
        P = input().strip()
        total += int(P[:-1]) ** int(P[-1:])
    print(total)