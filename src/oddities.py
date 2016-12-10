'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x = int(input()) 
        if x % 2:
            print(x, 'is odd')
        else:
            print(x, 'is even')