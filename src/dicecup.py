'''
Created on 22 March 2017

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N, M = [int(i) for i in input().split()]
    p, most = {}, 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (i+j) not in p.keys():
                p[i+j] = 1 
            else :
                p[i+j] += 1
    most = max(p.values())
    [print(k) for k,v in p.items() if v == most]
