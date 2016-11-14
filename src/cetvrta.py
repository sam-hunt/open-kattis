'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    X, Y = set([]), set([])
    for _ in range(3):
        line = input().split()
        newX, newY = int(line[0]), int(line[1])
         
        if newX not in X: X.add(newX)
        else: X.remove(newX)
        
        if newY not in Y: Y.add(newY)
        else: Y.remove(newY)
        
    print(list(X)[0], list(Y)[0])