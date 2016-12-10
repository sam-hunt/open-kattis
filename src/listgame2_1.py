'''
Created on 25 May 2016

@author: Sam
'''

# Python 2.7

import sys
from math import sqrt, ceil

#fails on 2*3*4*6*8*12*16*24*32 (169869312)
#incorrectly selects factors with minimal prime factors first

def get_pfactors(X):
    '''
    get the prime factors of X via trial division
    halve search space by removing evens first
    also stops early if root of X is reached 
    before the first prime factor is found 
    '''
    pfactors, divisor, Xsqrt = {}, 3, ceil(sqrt(X)) 
    if X%2==0: pfactors[2]=0
    while X%2==0:
        X/=2
        pfactors[2]+=1
    while X>1 and not(len(pfactors)==0 and divisor>Xsqrt):
        while not(X%divisor):
            X/=divisor
            if divisor not in pfactors: 
                pfactors[divisor]=1
            else: 
                pfactors[divisor]+=1 
        divisor+=2
    return pfactors

def fork(plist):
    '''fork each pattern in the list with 1 added to every position'''
    forkedlist = [plist[:] for _ in plist]
    for i in xrange(len(plist)):
        forkedlist[i][i] += 1
    return forkedlist
        
def remove_used(remaining, patterns):
    '''
    remove used prime factors from the list
    also remove patterns which use that prime
    this reduces the complexity of what is left
    '''
    while 1:
        emptyfound = False
        for i in xrange(len(remaining)):
            if remaining[i] == 0:
                emptyfound, j = True, 0
                while j < len(patterns):
                    if patterns[j][i] > 0:
                        del patterns[j]
                    else:
                        j+=1
                for j in xrange(len(patterns)):
                    del patterns[j][i]
                del remaining[i] 
                break
        if emptyfound == False: break
    

if __name__ == '__main__':
    #execute the prime decomposition
    pf = get_pfactors(int(sys.stdin.readline()))
    
    #only 1 possible value for Y if X is prime
    if not pf: print(1); sys.exit(0)
    
    #discard the prime factor bases, only need the powers
    bases = [k for k,v in pf.items()]
    pfpowers = [v for k,v in pf.items()]
    
    print pf
    print bases
    print pfpowers
    print
    
    #generate the initial pattern base
    patts = [[0 for _ in pf]]
    factors, factorlist = 0, []
    
    while len(pfpowers):
        #generate the next tier of factor patterns with n+1 prime factors 
        newpatts = []
        for eachpatt in patts:
            newpatts.extend(fork(eachpatt))
            
        #make sure they are unique
        patts = [list(a) for a in list(set(tuple(b) for b in newpatts))]
        print patts
        
        #check the factor patterns against the remaining prime factors 
        allfails = 0
        for eachpatt in patts:
            fail = False
            print pfpowers, eachpatt
            #check each part of the pattern
            for i in xrange(len(eachpatt)):
                if eachpatt[i] > pfpowers[i]:
                    fail = True
            if fail: 
                allfails+=1
                continue
            #factorise out a valid facto
            factorlist.append(1)
            for i in xrange(len(eachpatt)):
                if eachpatt[i]:
                    factorlist[-1] *= (bases[i]**eachpatt[i])
                pfpowers[i] -= eachpatt[i]
            factors += 1
            
        #clean up the remaining prime factor count and factor patterns
        remove_used(pfpowers, patts)
        
        #break if there are no more possible additional factors 
        if allfails==len(patts):
            break
    print sorted(factorlist)
    print factors 