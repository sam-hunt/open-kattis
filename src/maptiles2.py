'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    s = input()
    z, x, y = len(s), 0, 0
    xkey = {'0':0, '1':1, '2':0, '3':1}
    ykey = {'0':0, '1':0, '2':1, '3':1}
    
    for zoom in range(z-1,0-1,-1):
        x += xkey[s[zoom]]*(2**(z-zoom-1))
        y += ykey[s[zoom]]*(2**(z-zoom-1))
    print(z, x, y)