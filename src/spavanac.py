'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input().split()
    H, M = int(line[0]), int(line[1])
    H_carry = 0
    if M < 45:
        H_carry = -1
    M = (M+15)%60
    H = (H + 24 + H_carry) % 24
    
    print(H,M)