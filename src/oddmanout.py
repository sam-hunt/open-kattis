'''
Created on 15 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    N = int(input())
    for casenumber in range(N):
        input()
        C = set([])
        for eachguest in input().split():
            if eachguest not in C:
                C.add(eachguest)
            else:
                C.remove(eachguest)
        print("Case #" + str(casenumber+1) + ":", list(C)[0])