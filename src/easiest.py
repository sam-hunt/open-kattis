'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    while N != 0:
        N_sum = sum([int(a) for a in str(N)])
        p=11
        while sum([int(a) for a in str(p*N)]) != N_sum:
            p+=1
        print(p)
        N = int(input())