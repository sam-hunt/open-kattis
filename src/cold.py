'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = input()
    coldcount = 0
    for eachtemp in input().split():
        if int(eachtemp) < 0:
            coldcount +=1
    print(coldcount)