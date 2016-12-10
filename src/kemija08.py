'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    code = input()
    decoded = ""
    skip=0
    for eachchar in code:
        if skip:
            skip-=1
            continue
        decoded += eachchar
        if eachchar in "aeiou":
            skip=2
    print(decoded)