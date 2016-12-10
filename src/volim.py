'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    K = int(input()) - 1
    N = int(input())
    
    elapsed = 0
    
    for _ in range(N):
        line = input().split()
        elapsed += int(line[0])
        if elapsed >= 210:
            print(K+1)
            break
        if line[1] == 'T':
            K+=1
            K%=8