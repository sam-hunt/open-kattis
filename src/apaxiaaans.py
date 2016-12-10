'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    name = input()
    compact = str(name[0])
    for i in range(1,len(name)):
        if name[i] != name[i-1]:
            compact += name[i]
    print(compact)