'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    cipher = input()
    newstr = "PER"
    days = 0
    for eachchar in enumerate(cipher):
        if eachchar[1] != newstr[eachchar[0] % 3]:
            days += 1
            
    print(days)