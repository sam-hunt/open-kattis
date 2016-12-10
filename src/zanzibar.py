'''
Created on 14 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        imports = 0
        pop = [int(a) for a in input().split()]
        for i in range(1,len(pop)-1):
            pop2 = pop[i-1]*2
            if pop[i] > pop2:
                imports += (pop[i] - pop2)
        print(imports)