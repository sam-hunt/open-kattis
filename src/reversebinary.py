'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    bits = []
    while(N):
        if N % 2 == 1:
            bits.append(1)
            N -= 1
            N /= 2
        else:
            bits.append(0)
            N /= 2
    newN, factor = 0, 1
    for eachbit in bits[::-1]:
        newN += eachbit*factor
        factor*=2
    print(newN)