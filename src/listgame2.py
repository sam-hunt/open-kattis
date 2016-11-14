'''
Created on 27 May 2016

@author: Sam
'''

# Python 2.7

import sys
from math import sqrt, ceil

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

def cleanup(remaining_pfs):
    i=0
    while i < len(remaining_pfs):
        if remaining_pfs[i][1] == 0:
            del remaining_pfs[i]
        else:
            i+=1
        
def possiblef(pflist):
    '''
    generate the list of possible factor patterns for a list of prime factors
    '''
    patts = fork([0 for _ in pflist])
    patts = [list(a) for a in list(set(tuple(b) for b in patts))]
    newpatts = []
    print(pflist)
    for _ in xrange(sum(pflist)):
        for eachpatt in patts:
            newpatts.extend(fork(eachpatt))
        patts.extend([list(a) for a in list(set(tuple(b) for b in newpatts))])
    print patts
    

def factorise(pf_remaining, factors):
    
    possf = possiblef(pf_remaining)
    pf_remaining_new, factors_new = [], []
    results = [0 for _ in xrange(len(possf))]
    
    for _ in xrange(len(possf)):
        pf_remaining_new.append(pf_remaining[:])
        factors_new.append(factors.copy())
    
    allfails = 0
    for i in xrange(len(possf)):
        fail = False
        for j in xrange(len(possf[i])):
            if possf[i][j] > pf[j][1]:
                fail = True
                allfails += 1
                break
        if fail: continue
        factor = 1
        for j in xrange(len(possf[i])):
            if possf[i][j]:
                factor *= (pf_remaining[i][1]**possf[i])
            if factor in factors:
                fail = True
                allfails += 1
                break
            else:
                factors_new[i].add(factor)
                pf_remaining_new[i][j][1] -= possf[i][j]
                results[i] = 1 #recurse flag
        if fail: continue
    
    if allfails == len(possf):
        return len(factors)
    
    for i in xrange(len(possf)):
        if results[i]: #recurse flag is set
            cleanup(pf_remaining_new[i])
            results[i] = factorise(pf_remaining_new[i], factors_new[i])
    return len(factors) + max(results)
        
    
    

if __name__ == '__main__':
    #decompose to prime factors
    pf = get_pfactors(int(sys.stdin.readline()))
    
    #only 1 possible value for Y if X is prime
    if not pf: print(1); sys.exit(0)
    
    pf, factorset = list(pf.items()), set()
    print pf
    
    optimal_k = factorise(pf, factorset) 
    print optimal_k