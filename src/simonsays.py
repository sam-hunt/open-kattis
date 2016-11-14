'''
Created on 14 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        line = input()
        if len(line) <= 10:
            continue
        if "Simon says" in line[:10]:
            print(line[11:])