'''
Created on 14 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = int(input())
    setn = 1
    while n != 0:
        print("SET", setn)
        stack = []
        for _ in range(int(n/2)):
            print(input())
            stack.append(input())
        if n % 2:
            print(input())
        for _ in range(int(n/2)):
            print(stack.pop())
        n = int(input())
        setn += 1