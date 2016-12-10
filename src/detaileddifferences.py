'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        line1 = input()
        line2 = input()
        print(line1)
        print(line2)
        
        differences = ""
        for i in range(len(line1)):
            if line1[i] == line2[i]:
                differences += "."
            else:
                differences += "*"
        print(differences)