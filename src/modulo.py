'''
Created on 12 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    distincts = set([])
    for _ in range(10):
        distincts.add(int(input()) % 42)
    print(len(distincts))