'''
Created on 26 May 2016

@author: Sam
'''

# Python 2.7

import sys

if __name__ == '__main__':
    
    #store board and check rows
    board, queens = [], []
    try:
        for i in xrange(8):
            row = raw_input()
            queens.append((row.index('*'), i))
            board.append(row)
    except ValueError:
        print('invalid')
        sys.exit()
    
    #print queens
    
    #check diagonals/columns
    for eachqueen in queens:
        for eachdirection in [(1,-1), (-1,1), (1,1), (-1,-1), (0,-1), (0,1)]:
            pos = list(eachqueen[:])
            #print 'q', pos, eachdirection
            while 1:
                pos[0] += eachdirection[0]
                pos[1] += eachdirection[1]
                if pos[0]<0 or pos[1]<0 or pos[0]>7 or pos[1]>7:
                    break
                #print 'checking', pos
                if board[pos[1]][pos[0]] == '*':
                    print('invalid')
                    sys.exit() 
            #print
    print('valid')
        