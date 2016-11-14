'''
Created on 16 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    try:
        line = input().split()
        while len(line) == 2:
            print(abs(int(line[0])- int(line[1])))
            line = input().split()
    except:
        pass