'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    gunnar = [int(a) for a in input().split()]
    emma = [int(a) for a in input().split()]
    g = sum(range(gunnar[0],gunnar[1]+1)) / float(gunnar[1]-gunnar[0]+1) + sum(range(gunnar[2],gunnar[3]+1)) / float(gunnar[3]-gunnar[2]+1) 
    e = sum(range(emma[0],emma[1]+1)) / float(emma[1]-emma[0]+1) + sum(range(emma[2],emma[3]+1)) / float(emma[3]-emma[2]+1)
    if e > g: print('Emma')
    elif g > e: print('Gunnar')
    else: print('Tie')
    