'''
Created on 26 May 2016

@author: Sam
'''

# Python 2.7

import sys

if __name__ == '__main__':
    digits = ['**** ** ** ****', 
              '  *  *  *  *  *',
              '***  *****  ***',
              '***  ****  ****',
              '* ** ****  *  *',
              '****  ***  ****',
              '****  **** ****',
              '***  *  *  *  *',
              '**** ***** ****',
              '**** ****  ****']
    
    code = []
    for _ in xrange(5):
        code.append(sys.stdin.readline())
        
    chars = []
    while len(code[0])>3:
        nextchar = ''
        for i in range(5):
            nextchar+=code[i][:3]
            code[i] = code[i][4:]
        chars.append(nextchar)
    
    try:
        for i in xrange(len(chars)):
            chars[i] = digits.index(chars[i])
    except ValueError:
        print 'BOOM!!'
        sys.exit()
    
    if int(''.join([str(a) for a in chars]))%6:
        print 'BOOM!!'
    else:
        print 'BEER!!'
        