'''
Created on 13 May 2016

@author: Sam
'''

# Python 3.5

if __name__ == '__main__':
    runningbest = (0, 0)
    for contestant in range(5):
        line = input().split()
        score = sum([int(line[a]) for a in range(4)])
        if score > runningbest[1]:
            runningbest = (contestant, score)
    print(runningbest[0]+1, runningbest[1])