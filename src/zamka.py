'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

#Wrong answer :(

import sys

if __name__ == '__main__':
    
    L, D, X = int(input()), int(input()), int(input())
    
    if L == D:
        print(L)
        print(D) 
        sys.exit(0)
    
    for N in range(L, D):
        A = [int(a) for a in str(N)]
        #print (A)
        if sum(A) == X:
            break
    print(N)
    for M in range(D, L-1, -1):
        B = [int(b) for b in str(M)] 
        #print(B)
        if sum(B) == X:
            break
    print(M)