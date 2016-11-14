'''
Created on 17 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input()
    L = len(line)
    
    whitespace, low, high, symbols = 0,0,0,0
    lowchars = set('abcdefghijklmnopqrstuvwxyz')
    highchars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    for eachchar in line:
        if eachchar in ('_',):
            whitespace += 1
        elif eachchar in lowchars:
            low += 1
        elif eachchar in highchars:
            high += 1
        else:
            symbols += 1
            
    print(whitespace/L)
    print(low/L)
    print(high/L)
    print(symbols/L)