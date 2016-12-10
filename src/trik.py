'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    moves = input()
    Cup1, Cup2, Cup3 = 1, 0, 0
    for eachmove in moves:
        if eachmove == 'A':
            Cup1, Cup2 = Cup2, Cup1
        elif eachmove == 'B':
            Cup2, Cup3 = Cup3, Cup2
        else:
            Cup1, Cup3 = Cup3, Cup1
    if Cup1:
        print(1)
    elif Cup2:
        print(2)
    else:
        print(3)