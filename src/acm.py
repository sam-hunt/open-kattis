'''
Created on 16 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    line = input().split()
    score, time = 0, 0
    penalties = {}
    while line[0] != '-1':
        if line[2] == 'right':
            score += 1
            time += int(line[0])
            if line[1] in penalties:
                time += penalties[line[1]]
        else:
            if line[1] in penalties:
                penalties[line[1]] += 20
            else:
                penalties[line[1]] = 20 
        #print(line, score, time)
        line = input().split()
    print(score, time)