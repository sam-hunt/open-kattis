'''
Created on 14 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        #calculate the lowest table size
        message = input()
        L = len(message)
        K = 1
        while K*K < L:
            K += 1
            message += '*'*(K*K-L)
            
        #encode the message
        encoded = [['' for _ in range(K)] for _ in range(K)]  
        x = 0
        for i in range(K-1,-1,-1):
            for j in range(K):
                encoded[j][i] = message[x]
                x+=1
                
        #remove the asterisks
        print(''.join([''.join(a) for a in encoded]).replace('*', '')) 