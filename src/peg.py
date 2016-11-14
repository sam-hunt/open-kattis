'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    
    #set up the board
    board, moves = [], 0
    board.append("         ")
    for _ in range(7):
        board.append(" "+input()+" ")
    board.append("         ")
    
    #look for legal moves
    for i in range(1,8):
        for j in range(1,8):
            if board[i][j] == 'o':
                vertical = set([board[i][j-1], board[i][j+1]])
                horizontal = set([board[i-1][j], board[i+1][j]])
                if 'o' in vertical and '.' in vertical:
                    moves += 1 
                if 'o' in horizontal and '.' in horizontal:
                    moves += 1
    print(moves)