'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = int(input())
    while n > -1:
        oldelapsed, miles = 0, 0
        for i in range(n):
            line = input().split()
            elapsed = int(line[1]) 
            miles += int(line[0]) * (elapsed - oldelapsed)
            oldelapsed = elapsed
        print(miles, 'miles')
        n = int(input())