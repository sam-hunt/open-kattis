'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input().split()
    while line[0] != '0' and line[1] != '0':
        N, D, W = int(line[0]), int(line[1]), 0
        if N >= D:
            W = int(N / D)
            N -= W*D 
            
        print(W, N, '/', D)
        line = input().split()
            