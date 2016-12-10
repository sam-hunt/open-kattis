'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        cities = set([])
        for _ in range(n):
            cities.add(input())
        print(len(cities))
            