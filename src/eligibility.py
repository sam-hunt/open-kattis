'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        line = input().split()
        if int(line[1].split('/')[0]) >= 2010:
            eligibility = 'eligible'
        elif int(line[2].split('/')[0]) >= 1991:
            eligibility = 'eligible'
        elif int(line[3]) >= 41:
            eligibility = 'ineligible'
        else:
            eligibility = 'coach petitions'
        print(line[0], eligibility)