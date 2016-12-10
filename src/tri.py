'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input().split()
    for eachsign in ['+','-','*','/']:
        ssum = line[0]+eachsign+line[1]
        if int(eval(ssum)) == int(line[2]):
            print(ssum+'='+line[2])
            break
        ssum = line[1]+eachsign+line[2]
        if int(eval(ssum)) == int(line[0]):
            print(line[0]+'='+ssum)
            break
        