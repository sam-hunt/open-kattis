'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    K = int(input())
    A, B = 1, 0
    newA, newB = 0, 0
    while K > 0:
        newA = B
        newB = A + B 
        A, B = newA, newB
        K -= 1
    print(A, B)